# Assignment 04 Interpretation Memo

**Student Name:** Henry Simon
**Date:** February 13, 2026
**Assignment:** REIT Annual Returns and Predictors (Simple Linear Regression)

> **To fill this report:** Run `python assignment04_regression.py`, then copy the regression coefficients and statistics into the sections marked `[PASTE_HERE]`. See `FILL_REPORT_GUIDE.md` for exact mapping.

---

## 1. Regression Overview

You estimated **three** simple OLS regressions of REIT *annual* returns on different predictors:

| Model | Y Variable | X Variable | Interpretation Focus |
|-------|------------|------------|----------------------|
| 1 | ret (annual) | div12m_me | Dividend yield |
| 2 | ret (annual) | prime_rate | Interest rate sensitivity |
| 3 | ret (annual) | ffo_at_reit | FFO to assets (fundamental performance) |

For each model, summarize the key results in the sections below.

---

## 2. Coefficient Comparison (All Three Regressions)

**Model 1: ret ~ div12m_me**
- Intercept (β₀): 0.1082 (SE: 0.006, p-value: 0.000)
- Slope (β₁): -0.0687 (SE: 0.032, p-value: 0.035)
- R²: 0.002 | N: 2527

**Model 2: ret ~ prime_rate**
- Intercept (β₀): 0.1765 (SE: 0.015, p-value: 0.000)
- Slope (β₁): -0.0142 (SE: 0.003, p-value: 0.000)
- R²: 0.010 | N: 2527

**Model 3: ret ~ ffo_at_reit**
- Intercept (β₀): 0.0973 (SE: 0.009, p-value: 0.000)
- Slope (β₁): 0.5770 (SE: 0.567, p-value: 0.309)
- R²: 0.000 | N: 2518

*Note: Model 3 may have fewer observations if ffo_at_reit has missing values; statsmodels drops those rows.*

---

## 3. Slope Interpretation (Economic Units)

**Dividend Yield (div12m_me):**
- A 1 percentage point increase in dividend yield is associated with a **-0.0687** change in annual return.
- **Your interpretation:** Higher dividend yields are associated with lower returns. With a higher dividend, there is less growth, which can mean lower returns.
**Prime Loan Rate (prime_rate):**
- A 1 percentage point increase in the year-end prime rate is associated with a **-0.0142** change in annual return.
- **Your interpretation:** Yes, the prime rate is negative and statistically significant. The evidence suggests they are.

**FFO to Assets (ffo_at_reit):**
- A 1 unit increase in FFO/Assets is associated with a **0.5770** change in annual return.
- **Your interpretation:** The slope is positive but not statistically significant, so the evidence does not back it up.

---

## 4. Statistical Significance

For each slope, check if p-value < 0.05 (marked with *** in console output):

- **div12m_me (p-value 0.035):** Significant — Higher dividend yield is linked with lower returns in the sample.
- **prime_rate (p-value 0.000):** Significant — Higher interest rates are linked with lower returns.
- **ffo_at_reit (p-value 0.309):** Not significant — Profitability does not show a reliable relationship with returns here.

**Which predictor has the strongest statistical evidence?** The prime rate.

---

## 5. Model Fit (R-squared)

Compare the three R² values: 0.002, 0.010, 0.000

- **Which explains the most variation?** The prime rate.
- **Are these R² values high or low?** They are low.
- **What does this suggest about other factors driving REIT returns?** Other factors likely drive most REIT variation.

---

## 6. Omitted Variables

We're only using one predictor at a time. What important variables might we be missing?

- **Leverage:** Higher leverage can amplify returns and risk through greater financial exposure.
- **Market cap (size):** Size can affect risk, liquidity, and expected returns.
- **Sector/property type:** Different property sectors face different demand and economic sensitivities.

**Potential bias:** Omitted variables like leverage could be correlated with both the predictor and returns, so the slope may be biased.

---

## 7. Summary and Key Takeaway

**Main finding:**
Based on your three regressions, which predictor(s) matter most for explaining REIT annual returns?
- The prime rate has the strongest relationship with returns.
- It makes economic sense because the p-value and $R^2$ indicate it provides the most insight relative to the other variables.
- The relationships can vary by sector because each variable reflects different sector-specific fundamentals.

**What we would do next:**
- Extend to multiple regression (include two or more predictors simultaneously)
- Test for heteroskedasticity and other OLS assumption violations
- Examine whether relationships vary by time period or REIT sector


---

## Reproducibility Checklist
- [x] Script runs end-to-end without errors
- [x] Regression output saved to `Results/regression_div12m_me.txt`, `regression_prime_rate.txt`, `regression_ffo_at_reit.txt`
- [x] Scatter plots saved to `Results/scatter_div12m_me.png`, `scatter_prime_rate.png`, `scatter_ffo_at_reit.png`
- [x] Report accurately reflects regression results
- [x] All interpretations are in economic units (not just statistical jargon)
