# Quick Reference: How to Fill the Report

## After running `python assignment04_regression.py`, you'll see console output like:

```
============================================================
ret (annual) ~ DIV12M_ME
============================================================
Intercept (β₀):      X.XXXXXX  (SE: X.XXXXXX, t:    X.XXXX, p: X.XXXXXX)
Slope (β₁):          X.XXXXXX  (SE: X.XXXXXX, t:    X.XXXX, p: X.XXXXXX)
R² = X.XXXXXX  |  Adj R² = X.XXXXXX  |  N = XXXX
Slope is [positive/negative] and [SIGNIFICANT/not significant] at 5% ***
============================================================

============================================================
ret (annual) ~ PRIME_RATE
============================================================
[Same format...]

============================================================
ret (annual) ~ FFO_AT_REIT
============================================================
[Same format...]
```

## Copy-paste mapping:

### Model 1: div12m_me
- **β₀** → `Intercept (β₀):` first number
- **β₀ SE** → `Intercept (β₀):` second number in parentheses after "SE:"
- **β₀ p-value** → `Intercept (β₀):` last number in parentheses after "p:"
- **β₁ (slope)** → `Slope (β₁):` first number
- **β₁ SE** → `Slope (β₁):` second number in parentheses after "SE:"
- **β₁ p-value** → `Slope (β₁):` last number in parentheses after "p:"
- **R²** → `R² = X.XXXXXX`
- **N (sample size)** → `N = XXXX`

### Model 2 & 3: Repeat for prime_rate and ffo_at_reit

---

## Files created in Results/:
- `regression_div12m_me.txt` — Full detailed output (same as console)
- `regression_prime_rate.txt` 
- `regression_ffo_at_reit.txt`
- `scatter_div12m_me.png` — Scatter plot with fitted line
- `scatter_prime_rate.png`
- `scatter_ffo_at_reit.png`

You can also open these text files to copy numbers from them.
