#!/usr/bin/env python3
"""
Manual execution of regression analysis.
This file can be run directly: python manual_analysis.py
"""

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from pathlib import Path

# Setup paths
DATA_DIR = Path(__file__).parent / "data"
RESULTS_DIR = Path(__file__).parent / "Results"
RESULTS_DIR.mkdir(exist_ok=True)

print("="*60)
print("REIT Regression Analysis - Manual Execution")
print("="*60)

# Load data
print("\nLoading data...")
df = pd.read_csv(DATA_DIR / "REIT_sample_annual_2004_2024.csv")

# Rename ret12 to ret
df = df.rename(columns={"ret12": "ret"})

# Load interest rates
rates = pd.read_csv(DATA_DIR / "interest_rates_monthly.csv")
rates["date"] = pd.to_datetime(rates["date"])
rates["year"] = rates["date"].dt.year
rates["month"] = rates["date"].dt.month
rates_dec = rates[rates["month"] == 12][["year", "mortgage_30y", "prime_rate"]].copy()

# Merge
df = df.merge(rates_dec, on="year", how="left")

# Drop missing values
df = df.dropna(subset=["ret", "div12m_me", "prime_rate"])

print(f"Loaded {len(df)} firm-year observations.")
print(f"Years: {df['year'].min():.0f}–{df['year'].max():.0f}")

# Define regressions
REGRESSIONS = [
    ("div12m_me", "Dividend Yield", "Dividend Yield (12m)"),
    ("prime_rate", "Prime Loan Rate", "Prime Loan Rate (%)"),
    ("ffo_at_reit", "FFO to Assets", "FFO / Assets"),
]

results_summary = {}

for x_var, title, xlabel in REGRESSIONS:
    print(f"\n{'='*60}")
    print(f"Estimating: ret (annual) ~ {x_var.upper()}")
    print(f"{'='*60}")
    
    # Fit model
    model = ols(f"ret ~ {x_var}", data=df).fit()
    
    # Extract stats
    intercept = model.params['Intercept']
    slope = model.params[x_var]
    intercept_se = model.bse['Intercept']
    slope_se = model.bse[x_var]
    intercept_tstat = model.tvalues['Intercept']
    slope_tstat = model.tvalues[x_var]
    intercept_pval = model.pvalues['Intercept']
    slope_pval = model.pvalues[x_var]
    r_squared = model.rsquared
    adj_r_squared = model.rsquared_adj
    nobs = model.nobs
    
    # Print summary
    print(f"Intercept (β₀):    {intercept:>10.6f}  (SE: {intercept_se:.6f}, t: {intercept_tstat:>8.4f}, p: {intercept_pval:.6f})")
    print(f"Slope (β₁):        {slope:>10.6f}  (SE: {slope_se:.6f}, t: {slope_tstat:>8.4f}, p: {slope_pval:.6f})")
    print(f"R² = {r_squared:.6f}  |  Adj R² = {adj_r_squared:.6f}  |  N = {nobs}")
    
    sig_marker = "***" if slope_pval < 0.05 else "   "
    direction = "positive" if slope > 0 else "negative"
    print(f"Slope is {direction} and {'SIGNIFICANT' if slope_pval < 0.05 else 'not significant'} at 5% {sig_marker}")
    
    # Save summary to file
    summary_path = RESULTS_DIR / f"regression_{x_var}.txt"
    with open(summary_path, "w") as f:
        f.write(str(model.summary()))
    print(f"✓ Saved: {summary_path}")
    
    # Create scatter plot
    plot_df = df[[x_var, 'ret']].dropna()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(plot_df[x_var], plot_df['ret'], alpha=0.5, s=30)
    
    # Regression line
    x_line = np.array([plot_df[x_var].min(), plot_df[x_var].max()])
    y_line = intercept + slope * x_line
    ax.plot(x_line, y_line, 'r-', linewidth=2, label=f'Fit line (slope={slope:.4f})')
    
    # Zoom to central data
    x_p2, x_p98 = np.percentile(plot_df[x_var], [2, 98])
    y_p2, y_p98 = np.percentile(plot_df['ret'], [2, 98])
    ax.set_xlim(x_p2, x_p98)
    ax.set_ylim(y_p2, y_p98)
    
    # Labels
    ax.set_title(f"{title}\nR² = {r_squared:.4f}", fontsize=12, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel('Annual Return', fontsize=11)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    
    # Save plot
    plot_path = RESULTS_DIR / f"scatter_{x_var}.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {plot_path}")
    
    # Store results
    results_summary[x_var] = {
        'intercept': intercept,
        'intercept_se': intercept_se,
        'intercept_pval': intercept_pval,
        'slope': slope,
        'slope_se': slope_se,
        'slope_pval': slope_pval,
        'r_squared': r_squared,
        'adj_r_squared': adj_r_squared,
        'nobs': nobs,
    }

print("\n" + "="*60)
print("✓ Assignment 04 Analysis Complete!")
print("="*60)
print("\nResults saved to Results/:")
print("  - regression_div12m_me.txt")
print("  - regression_prime_rate.txt")  
print("  - regression_ffo_at_reit.txt")
print("  - scatter_div12m_me.png")
print("  - scatter_prime_rate.png")
print("  - scatter_ffo_at_reit.png")
print("\nNext steps:")
print("  1. Review regression outputs in Results/")
print("  2. Compare coefficients across all three models")
print("  3. Complete assignment04_report.md with your interpretation")
print("  4. AI_AUDIT_APPENDIX.md is already complete")
print("\n" + "="*60)
