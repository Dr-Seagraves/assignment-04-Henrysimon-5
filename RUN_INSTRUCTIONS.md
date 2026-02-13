# CRITICAL: How to Run the Assignment

Due to terminal connection issues in the environment, **you need to run the script manually**.

## Option 1: VS Code Built-in Terminal (RECOMMENDED)

1. Press **`Ctrl + ~`** (backtick) to open the integrated terminal in VS Code
2. Paste this command:
   ```bash
   cd /workspaces/assignment-04-Henrysimon-5 && python assignment04_regression.py
   ```
3. Press **Enter** and wait 10-20 seconds for results

## Option 2: External Terminal / Command Line

```bash
cd /workspaces/assignment-04-Henrysimon-5
python assignment04_regression.py
```

## Option 3: Python Directly

If `python` doesn't work, try `python3`:
```bash
cd /workspaces/assignment-04-Henrysimon-5
python3 assignment04_regression.py
```

---

## What You'll See

### Console Output (appears immediately):
```
Loading REIT annual data (REIT_sample_annual_*.csv)...
Loaded 2547 firm-year observations.
Years: 2004–2024

Estimating regression: ret (annual) ~ div12m_me

============================================================
ret (annual) ~ DIV12M_ME
============================================================
Intercept (β₀):      [NUMBER]  (SE: [NUMBER], t:    [NUMBER], p: [NUMBER])
Slope (β₁):          [NUMBER]  (SE: [NUMBER], t:    [NUMBER], p: [NUMBER])
R² = [NUMBER]  |  Adj R² = [NUMBER]  |  N = [NUMBER]
Slope is [positive/negative] and [SIGNIFICANT/not significant] at 5% ***
============================================================

[REPEATS FOR prime_rate AND ffo_at_reit]

✓ Assignment 04 complete!
Next steps:
  1. Review regression outputs in Results/
  2. Compare coefficients across dividend yield, prime rate, and FFO/Assets
  3. Complete assignment04_report.md with your interpretation
  4. Complete AI_AUDIT_APPENDIX.md
```

### Files Created (in `Results/` folder):
- `regression_div12m_me.txt` — Full statsmodels summary table
- `regression_prime_rate.txt` — Full statsmodels summary table
- `regression_ffo_at_reit.txt` — Full statsmodels summary table
- `scatter_div12m_me.png` — Beautiful scatter plot with fitted line
- `scatter_prime_rate.png` — Beautiful scatter plot with fitted line
- `scatter_ffo_at_reit.png` — Beautiful scatter plot with fitted line

---

## After the Script Runs

1. **Copy numbers** from console or `.txt` files in `Results/`
2. **Paste into** `assignment04_report.md` where you see `[COEF_1]`, `[PVAL_2]`, etc.
3. **Answer interpretations** with your own economic reasoning
4. **Review plots** in `Results/` to verify the relationships visually

See `FILL_REPORT_GUIDE.md` for exact field mapping.

---

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'pandas'"
- Run: `pip install pandas numpy statsmodels matplotlib`

### Error: "FileNotFoundError: interest_rates_monthly.csv"  
- File already exists in `/data/` — it shouldn't error. Check that you're in the right directory.

### Error: "NotImplementedError"
- This shouldn't happen — all functions are implemented. Make sure you have the latest version of `assignment04_regression.py`

### Error: "Permission denied"
- Try: `chmod +x assignment04_regression.py` then run again

---

## Questions?

- Check `FILL_REPORT_GUIDE.md` for how to map console output to the report
- Check `AI_AUDIT_APPENDIX.md` to understand what functions do what
- Review `assignment04_report.md` template for all required sections

**YOUR TO DO: Run the script and fill in the report!**
