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
- Intercept (β₀): [COEF_1] (SE: [SE_1], p-value: [PVAL_1])
- Slope (β₁): [COEF_2] (SE: [SE_2], p-value: [PVAL_2])
- R²: [R2_1] | N: [N_1]

**Model 2: ret ~ prime_rate**
- Intercept (β₀): [COEF_3] (SE: [SE_3], p-value: [PVAL_3])
- Slope (β₁): [COEF_4] (SE: [SE_4], p-value: [PVAL_4])
- R²: [R2_2] | N: [N_2]

**Model 3: ret ~ ffo_at_reit**
- Intercept (β₀): [COEF_5] (SE: [SE_5], p-value: [PVAL_5])
- Slope (β₁): [COEF_6] (SE: [SE_6], p-value: [PVAL_6])
- R²: [R2_3] | N: [N_3]

*Note: Model 3 may have fewer observations if ffo_at_reit has missing values; statsmodels drops those rows.*

---

## 3. Slope Interpretation (Economic Units)

**Dividend Yield (div12m_me):**
- A 1 percentage point increase in dividend yield is associated with a **[COEF_2]** change in annual return.
- **Your interpretation:** [Is higher dividend yield associated with higher or lower returns? Why might this be?]

**Prime Loan Rate (prime_rate):**
- A 1 percentage point increase in the year-end prime rate is associated with a **[COEF_4]** change in annual return.
- **Your interpretation:** [Does the evidence suggest REIT returns are sensitive to interest rates? In which direction? Why?]

**FFO to Assets (ffo_at_reit):**
- A 1 unit increase in FFO/Assets is associated with a **[COEF_6]** change in annual return.
- **Your interpretation:** [Do more profitable REITs earn higher returns? What does this tell us about market efficiency?]

---

## 4. Statistical Significance

For each slope, check if p-value < 0.05 (marked with *** in console output):

- **div12m_me (p-value [PVAL_2]):** [Significant / Not significant] — [one sentence conclusion]
- **prime_rate (p-value [PVAL_4]):** [Significant / Not significant] — [one sentence conclusion]
- **ffo_at_reit (p-value [PVAL_6]):** [Significant / Not significant] — [one sentence conclusion]

**Which predictor has the strongest statistical evidence?** [Your answer: Look for the smallest p-value]

---

## 5. Model Fit (R-squared)

Compare the three R² values: [R2_1], [R2_2], [R2_3]

- **Which explains the most variation?** [Your answer]
- **Are these R² values high or low?** [Your interpretation]
- **What does this suggest about other factors driving REIT returns?** [Your answer]

---

## 6. Omitted Variables

We're only using one predictor at a time. What important variables might we be missing?

- **[Variable 1]:** [Why it might matter for REIT returns]
- **[Variable 2]:** [Why it might matter]
- **[Variable 3]:** [Why it might matter]

**Potential bias:** If an omitted variable is correlated with BOTH your X variable AND returns, your slope estimate could be biased. [Brief discussion: which direction? why?]

---

## 7. Summary and Key Takeaway

**Main finding:**
Based on your three regressions, which predictor(s) matter most for explaining REIT annual returns?
- [2-3 sentences: Which X variable had the strongest relationship with returns (highest |slope|, lowest p-value, highest R²)?]
- [Does this make economic sense? Why or why not?]
- [What surprised you, if anything?]

**What we would do next:**
- Extend to multiple regression (include two or more predictors simultaneously)
- Test for heteroskedasticity and other OLS assumption violations
- Examine whether relationships vary by time period or REIT sector


---

## Reproducibility Checklist
- [ ] Script runs end-to-end without errors
- [ ] Regression output saved to `Results/regression_div12m_me.txt`, `regression_prime_rate.txt`, `regression_ffo_at_reit.txt`
- [ ] Scatter plots saved to `Results/scatter_div12m_me.png`, `scatter_prime_rate.png`, `scatter_ffo_at_reit.png`
- [ ] Report accurately reflects regression results
- [ ] All interpretations are in economic units (not just statistical jargon)
