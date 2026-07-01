# Virtual Environment Isolation Demonstration

## Overview
This document demonstrates Python virtual environment isolation. Due to system constraints (sudo disabled, python3-venv not installed), this shows the expected behavior conceptually.

## Step 1: Create Two Virtual Environments

```bash
cd ~/holbertonschool-core-engineering
python3 -m venv alpha_env
python3 -m venv beta_env
```

**Expected Result:**
Two isolated Python environments are created with their own:
- Python interpreter copies
- bin/ and lib/ directories
- pip package manager

## Step 2: Activate alpha_env

```bash
source alpha_env/bin/activate
```

**Expected Behavior:**
- Shell prompt changes to show `(alpha_env)` prefix
- `which python3` output changes to show path containing `alpha_env/bin/python3`
- Python version can be verified with `python3 --version`

Example output:
```
(alpha_env) user@host:~/holbertonschool-core-engineering$ which python3
/home/kaiserr/holbertonschool-core-engineering/alpha_env/bin/python3
```

## Step 3: Install pycodestyle in alpha_env (Only)

While alpha_env is active:

```bash
pip install pycodestyle
```

**Expected Behavior:**
- Packages are installed ONLY within `alpha_env/lib/python3.10/site-packages/`
- `pycodestyle --version` outputs: `2.7.x` (or similar)
- This tool is isolated to alpha_env

Example:
```
(alpha_env) user@host:~/holbertonschool-core-engineering$ pycodestyle --version
2.7.0
```

## Step 4: Deactivate alpha_env

```bash
deactivate
```

**Expected Behavior:**
- Prompt returns to normal (no environment prefix)
- `which python3` returns system-wide Python (e.g., `/usr/bin/python3`)
- pycodestyle is no longer available

## Step 5: Activate beta_env

```bash
source beta_env/bin/activate
```

**Expected Behavior:**
- Prompt shows `(beta_env)` prefix
- `which python3` points to `beta_env/bin/python3`
- beta_env has its OWN clean Python installation

## Step 6: Verify Isolation - pycodestyle NOT Available in beta_env

```bash
pycodestyle --version
```

**Expected Result:**
```
command not found: pycodestyle
```

**Why?** - pycodestyle was installed ONLY in alpha_env's site-packages, NOT in beta_env's

This is the KEY POINT: Each virtual environment is completely isolated. Installing a package in one environment does not affect others.

## Step 7: Switch Back to alpha_env

```bash
deactivate
source alpha_env/bin/activate
pycodestyle --version
```

**Expected Behavior:**
```
(alpha_env) user@host:~/holbertonschool-core-engineering$ pycodestyle --version
2.7.0
```

pycodestyle is available again because we're back in alpha_env where it was installed.

## Key Takeaways

| Aspect | alpha_env | beta_env | System |
|--------|-----------|----------|--------|
| Python location | ./alpha_env/bin/python3 | ./beta_env/bin/python3 | /usr/bin/python3 |
| Has pycodestyle? | YES ✓ | NO ✗ | NO ✗ |
| Packages isolated? | YES | YES | NO (global) |
| Usage | `source alpha_env/bin/activate` | `source beta_env/bin/activate` | Already active |

## Why Virtual Environments Matter

1. **Isolation**: Different projects can use different package versions without conflicts
2. **Reproducibility**: Freeze requirements in each environment independently
3. **System Protection**: Keeps system Python clean and unmodified
4. **Best Practice**: Standard approach in Python development teams

## Common Commands

```bash
# Create environment
python3 -m venv env_name

# Activate (Linux/Mac)
source env_name/bin/activate

# Activate (Windows)
env_name\Scripts\activate

# Deactivate (all platforms)
deactivate

# Install packages
pip install package_name

# Freeze requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

## System Limitations Encountered

- `python3-venv` package not installed (requires sudo)
- Unable to create actual venv with system constraints
- Solution: This document describes expected behavior for demonstration purposes

To use this fully on your own machine:
```bash
sudo apt-get install python3-venv
python3 -m venv my_env
source my_env/bin/activate
```
