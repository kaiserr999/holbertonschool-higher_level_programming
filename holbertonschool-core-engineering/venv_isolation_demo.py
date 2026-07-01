#!/usr/bin/env python3
"""
Virtual Environment Isolation Demonstration

This script shows what Python sees in different virtual environments.
"""

import sys
import os


def show_environment_info():
    """Display current Python environment information."""
    
    print("\n" + "="*70)
    print("  PYTHON ENVIRONMENT INFORMATION")
    print("="*70 + "\n")
    
    print(f"Python Executable: {sys.executable}")
    print(f"Python Version:    {sys.version.split()[0]}")
    print(f"Prefix (venv):     {sys.prefix}")
    print(f"Base Prefix:       {sys.base_prefix}")
    
    site_packages = os.path.join(sys.prefix, 'lib', f'python{sys.version_info.major}.{sys.version_info.minor}', 'site-packages')
    print(f"Site-packages:     {site_packages}")
    
    # Check if in venv
    in_venv = sys.prefix != sys.base_prefix
    print(f"In Virtual Env:    {'YES ✓' if in_venv else 'NO ✗'}")
    
    print("\n" + "="*70)


def show_isolation_example():
    """Display how isolation works."""
    
    print("\n" + "="*70)
    print("  VIRTUAL ENVIRONMENT ISOLATION EXAMPLE")
    print("="*70 + "\n")
    
    example = """
Scenario: Two Python Projects

Project A uses alpha_env:
  $ source alpha_env/bin/activate
  (alpha_env) $ pip install pycodestyle
  (alpha_env) $ pycodestyle --version
  2.7.0 ✓ AVAILABLE
  
  Environment contains:
  - alpha_env/bin/python3
  - alpha_env/lib/python3.10/site-packages/pycodestyle/
  - (isolation)

Project B uses beta_env:
  $ source beta_env/bin/activate
  (beta_env) $ pycodestyle --version
  bash: command not found ✗ NOT AVAILABLE
  
  Environment contains:
  - beta_env/bin/python3
  - beta_env/lib/python3.10/site-packages/ (no pycodestyle!)
  - (isolation)

WHY? Each environment has its OWN site-packages directory!
    """
    
    print(example)


def show_benefits():
    """Display benefits of virtual environments."""
    
    print("\n" + "="*70)
    print("  BENEFITS OF VIRTUAL ENVIRONMENTS")
    print("="*70 + "\n")
    
    benefits = """
1. ISOLATION
   ✓ Each project gets its own Python packages
   ✓ No version conflicts between projects
   ✓ Installing Package X in one project doesn't affect another project

2. REPRODUCIBILITY
   ✓ Use: pip freeze > requirements.txt
   ✓ Same environment on different machines
   ✓ New developer: pip install -r requirements.txt

3. SAFETY
   ✓ System Python (/usr/bin/python3) never modified
   ✓ If broken, just delete the venv directory and recreate
   ✓ System remains stable and clean

4. ORGANIZATION
   ✓ Each project is self-contained
   ✓ Easy to track dependencies
   ✓ Professional development practice

5. FLEXIBILITY
   ✓ Different Python versions per project (if available)
   ✓ Easy to switch between projects
   ✓ No global package pollution
    """
    
    print(benefits)


def show_directory_structure():
    """Show typical virtual environment structure."""
    
    print("\n" + "="*70)
    print("  VIRTUAL ENVIRONMENT DIRECTORY STRUCTURE")
    print("="*70 + "\n")
    
    structure = """
my_project/
├── alpha_env/                          ← First venv
│   ├── bin/
│   │   ├── python3                    ← Alpha's interpreter
│   │   ├── pip                        ← Alpha's pip
│   │   ├── activate                   ← Activation script
│   │   └── pycodestyle                ← After: pip install pycodestyle
│   ├── lib/
│   │   └── python3.10/site-packages/
│   │       └── pycodestyle/           ← ONLY in alpha_env
│   └── pyvenv.cfg
│
├── beta_env/                           ← Second venv
│   ├── bin/
│   │   ├── python3                    ← Beta's interpreter
│   │   ├── pip                        ← Beta's pip
│   │   └── activate                   ← Different activation
│   ├── lib/
│   │   └── python3.10/site-packages/
│   │       └── (empty or other packages)
│   └── pyvenv.cfg
│
└── src/
    └── main.py

KEY INSIGHT:
- alpha_env/bin/python3 and beta_env/bin/python3 are DIFFERENT
- alpha_env/lib/.../site-packages and beta_env/lib/.../site-packages are DIFFERENT
- Installing in alpha doesn't affect beta
- This is ISOLATION
    """
    
    print(structure)


def main():
    """Run all demonstrations."""
    
    show_environment_info()
    show_isolation_example()
    show_benefits()
    show_directory_structure()
    
    print("\n" + "="*70)
    print("  QUICK REFERENCE COMMANDS")
    print("="*70 + "\n")
    
    commands = """
# Create environments
python3 -m venv alpha_env
python3 -m venv beta_env

# Activate alpha_env (Linux/Mac)
source alpha_env/bin/activate

# Activate beta_env (Linux/Mac)
source beta_env/bin/activate

# Activate (Windows)
env_name\\Scripts\\activate

# Deactivate (all platforms)
deactivate

# Install packages
pip install pycodestyle

# Check version
pycodestyle --version

# List installed packages
pip list

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
    """
    
    print(commands)
    
    print("\n" + "="*70)
    print("  RUNNING THIS SCRIPT")
    print("="*70 + "\n")
    
    print("If this script is running in a virtual environment:")
    print("  → All the isolation concepts above apply to it")
    print("  → You can verify by checking 'In Virtual Env' status above\n")
    
    print("If this script is running in system Python:")
    print("  → You're seeing system-wide Python")
    print("  → To use a venv, run: source venv_name/bin/activate\n")
    
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
