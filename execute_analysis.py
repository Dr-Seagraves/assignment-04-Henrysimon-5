#!/usr/bin/env python3
"""
Direct execution wrapper to run assignment04_regression.py
This allows us to bypass terminal issues.
"""

import sys
import os

# Set working directory
os.chdir('/workspaces/assignment-04-Henrysimon-5')
sys.path.insert(0, '/workspaces/assignment-04-Henrysimon-5')

# Import and run
from assignment04_regression import main

if __name__ == "__main__":
    try:
        main()
        print("\n" + "="*60)
        print("SUCCESS: Script completed without errors!")
        print("="*60)
    except Exception as e:
        print(f"\nERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
