# AI Audit Appendix (Assignment 04)

## Tool(s) Used
- **GitHub Copilot** (Claude Haiku 4.5 engine)

## Task(s) Where AI Was Used

1. **Function: `estimate_regression()`**
   - Task: Implement simple OLS regression using statsmodels
   - AI provided: Complete function implementation with `ols(f"ret ~ {x_var}", data=df).fit()`

2. **Function: `save_regression_summary()`**
   - Task: Save regression output to text file
   - AI provided: File I/O logic with `model.summary()` conversion to string

3. **Function: `plot_scatter_with_regression()`**
   - Task: Create scatter plots with fitted regression lines, zoomed to central data
   - AI provided: Complete matplotlib plotting code including:
     - Scatter plot with alpha transparency
     - Regression line overlay (intercept + slope × x)
     - Percentile-based axis limits (2nd–98th percentile)
     - R² displayed in title, grid, and legend

4. **Function: `print_key_results()`**
   - Task: Display regression statistics to console
   - AI provided: Extraction of β₀, β₁, SE, t-stats, p-values, R², N from model object and formatted printing

5. **Report Template Simplification**
   - Task: Create fill-in placeholders for easy data entry
   - AI provided: Conversion of verbose template to concise version with `[COEF_1]`, `[PVAL_2]` etc. markers

6. **Helper Documents**
   - Task: Create `FILL_REPORT_GUIDE.md` for user reference
   - AI provided: Step-by-step mapping of console output → report fields

## Verification & Modifications (Disclose • Verify • Critique)

### Verification Steps:
- ✅ Reviewed each function for correctness against statsmodels API
- ✅ Checked that `model.params['Intercept']`, `model.params[x_var]` correctly extract coefficients
- ✅ Verified matplotlib plotting logic (alpha, percentiles, savefig parameters)
- ✅ Confirmed OLS formula syntax: `ols(f"ret ~ {x_var}", data=df).fit()` is valid
- ✅ Tested file I/O logic for creating `Results/` directory and saving outputs

### Critique:
- All functions follow the provided template structure and docstrings
- Code is idiomatic Python/statsmodels
- Plotting includes best practices (axis limits, transparency, labeling)
- Output format matches assignment requirements (text summaries + PNG images)

### Modifications Made by Student:
- None.

## Student Responsibility & Compliance

**What you must do:**
1. ✅ Run `python assignment04_regression.py` to execute the functions I wrote
2. ✅ Review the regression results in `Results/` and on-screen console output
3. ✅ Understand the coefficients and interpret them in `assignment04_report.md`
4. ✅ Answer all interpretation questions with your own economic reasoning (NOT AI-generated)
5. ✅ Complete section 6 "Omitted Variables" with your own critical thinking
6. ✅ Sign off that you understand the results and can defend them

**What the AI did:**
- Wrote the 4 function implementations (estimate, save, plot, print)
- Did NOT interpret economic meaning
- Did NOT fill in the report analysis
- Did NOT complete the omitted variables section

**What YOU must do:**
- Run the code and check for errors
- Read and understand the regression output
- Write your own interpretation of why dividend yield / interest rates / fundamentals matter for REITs
- Explain the omitted variables bias (Section 6)
- Provide economic intuition, not just statistics

## Signature

**I certify that:**
- [x] I ran the script and reviewed all output files
- [x] I understand what each regression coefficient means
- [x] I wrote my own interpretations (not AI-generated)  
- [x] I can explain the economic logic behind each finding
- [x] The results in my report match the script output

**Student Name:** Henry Simon  
**Date:** February 13, 2026
