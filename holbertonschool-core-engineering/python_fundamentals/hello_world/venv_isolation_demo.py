#!/usr/bin/env python3
"""
Virtual Environment Isolation Demonstration Script

This script demonstrates how virtual environments work and shows
the directory structure and isolation between environments.
"""

import os
import sys
import subprocess


def show_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def create_venv_demo():
    """
    Demonstrate virtual environment isolation conceptually.
    """
    
    show_section("1. Current System Python")
    print(f"System Python: {sys.executable}")
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Prefix: {sys.prefix}")
    print(f"Site-packages: {os.path.join(sys.prefix, 'lib/python3.10/site-packages')}")
    
    show_section("2. Virtual Environment Structure")
    print("""
A virtual environment creates this structure:

alpha_env/
├── bin/
│   ├── python3          ← Python interpreter
│   ├── python           ← Symlink to python3
│   ├── pip              ← Package installer
│   ├── pip3             ← Pip v3
│   ├── activate         ← Activation script
│   └── pycodestyle      ← Installed tools
├── lib/
│   └── python3.10/site-packages/
│       ├── pycodestyle/ ← Only in alpha_env
│       └── ...other packages...
└── pyvenv.cfg          ← Config file

beta_env/
├── bin/
│   ├── python3          ← Different interpreter
│   ├── pip              ← Different pip
│   └── activate         ← Separate activation
├── lib/
│   └── python3.10/site-packages/
│       └── ...clean, empty for new env...
└── pyvenv.cfg
    """)
    
    show_section("3. Isolation Demonstration")
    print("""
Step-by-step isolation:

┌─────────────────────────────────────────────────────────┐
│ System (no virtual env active)                          │
│ python3 → /usr/bin/python3                              │
│ pycodestyle → /usr/bin/pycodestyle (if installed)       │
└─────────────────────────────────────────────────────────┘
             ↓ source alpha_env/bin/activate
┌─────────────────────────────────────────────────────────┐
│ (alpha_env) Active                                       │
│ python3 → ./alpha_env/bin/python3                       │
│ pip → ./alpha_env/bin/pip                               │
│ pycodestyle → ./alpha_env/bin/pycodestyle ✓ AVAILABLE   │
└─────────────────────────────────────────────────────────┘
             ↓ deactivate
┌─────────────────────────────────────────────────────────┐
│ System (no virtual env active)                          │
│ python3 → /usr/bin/python3                              │
│ pycodestyle → Not found ✗ (not installed in system)     │
└─────────────────────────────────────────────────────────┘
             ↓ source beta_env/bin/activate
┌─────────────────────────────────────────────────────────┐
│ (beta_env) Active                                        │
│ python3 → ./beta_env/bin/python3                        │
│ pip → ./beta_env/bin/pip                                │
│ pycodestyle → Not found ✗ (NOT installed in beta_env)   │
│              (only in alpha_env!)                        │
└─────────────────────────────────────────────────────────┘
    """)
    
    show_section("4. Why This Matters")
    print("""
Scenario: Two Python Projects

Project A (Uses alpha_env):
  • Flask 2.0.1
  • Django 3.2
  • pycodestyle 2.7.0
  
Project B (Uses beta_env):
  • Flask 3.0.0  ← Different version!
  • Django 4.0
  • No pycodestyle
  
Benefits:
✓ No version conflicts
✓ Projects don't interfere with each other
✓ Easy to reproduce environments
✓ Clean system Python
✓ Different Python versions per project (with different venvs)
    """)
    
    show_section("5. Complete Workflow Example")
    print("""
# Create environments
python3 -m venv alpha_env
python3 -m venv beta_env

# Work in alpha_env
source alpha_env/bin/activate
pip install pycodestyle
pycodestyle my_script.py
deactivate

# Work in beta_env (fresh environment)
source beta_env/bin/activate
pip install pytest
pytest tests/
# pycodestyle not available here!
deactivate

# Switch back to alpha_env
source alpha_env/bin/activate
pycodestyle my_script.py  # Still available!
    """)
    
    show_section("6. Package Installation Locations")
    
    packages_info = {
        "System (no venv)": "/usr/lib/python3.10/dist-packages",
        "alpha_env": "./alpha_env/lib/python3.10/site-packages",
        "beta_env": "./beta_env/lib/python3.10/site-packages",
    }
    
    for env, path in packages_info.items():
        print(f"{env:20} → {path}")
    
    print("\nKey insight: Packages go to DIFFERENT locations!")
    print("Installing in alpha_env doesn't affect beta_env.\n")
    
    show_section("7. Verify Isolation with 'pip list'")
    print("""
$ source alpha_env/bin/activate
(alpha_env) $ pip list
Package         Version
--------------- ---------
pip             22.0.2
setuptools      60.0.0
pycodestyle     2.7.0    ← Installed!

(alpha_env) $ deactivate
$ source beta_env/bin/activate
(beta_env) $ pip list
Package         Version
--------------- ---------
pip             22.0.2
setuptools      60.0.0
# pycodestyle NOT in the list!

(beta_env) $ pycodestyle --version
command not found
    """)
    
    show_section("Summary: Isolation Checklist")
    print("""
✓ Each venv has its own Python interpreter
✓ Each venv has its own site-packages directory
✓ pip installs only to the ACTIVE environment
✓ Packages in one venv don't appear in another
✓ System Python remains unchanged
✓ Easy to switch between projects
✓ Easy to freeze/share requirements

This is WHY you should ALWAYS use virtual environments
for development!
    """)


if __name__ == "__main__":
    create_venv_demo()
