# Virtual Environment Isolation Demonstration

## Overview
Virtual environments in Python provide complete isolation between projects. Each environment has its own Python interpreter, pip package installer, and site-packages directory.

## System Constraints
Due to system limitations (sudo disabled, python3-venv not installed), this document provides a complete conceptual demonstration of what happens when you follow the workflow.

---

## Step 1: Create Two Virtual Environments

```bash
cd ~/holbertonschool-core-engineering
python3 -m venv alpha_env
python3 -m venv beta_env
```

**Result:**
Each command creates a new directory with this structure:

```
alpha_env/
├── bin/
│   ├── python3          ← Python interpreter for alpha_env
│   ├── pip              ← Package manager for alpha_env  
│   ├── activate         ← Activation script
│   └── pycodestyle      ← (will appear after pip install)
├── lib/
│   └── python3.10/site-packages/
│       └── (packages installed in alpha_env go here)
└── pyvenv.cfg

beta_env/
├── bin/
│   ├── python3          ← Different Python interpreter for beta_env
│   ├── pip              ← Different package manager
│   └── activate         ← Different activation script
├── lib/
│   └── python3.10/site-packages/
│       └── (clean, separate from alpha_env)
└── pyvenv.cfg
```

**Key Point:** Each environment has its OWN copy of Python and its OWN site-packages directory.

---

## Step 2: Activate alpha_env and Verify

```bash
source alpha_env/bin/activate
```

**Expected Output:**
Shell prompt changes to:
```
(alpha_env) user@host:~/holbertonschool-core-engineering$
```

Verify the Python interpreter:
```bash
which python3
which python
python3 --version
```

**Expected Output:**
```
/home/kaiserr/holbertonschool-core-engineering/alpha_env/bin/python3
/home/kaiserr/holbertonschool-core-engineering/alpha_env/bin/python
Python 3.10.12
```

**What This Means:**
- The `source alpha_env/bin/activate` script modified your PATH
- `python3` now points to alpha_env's Python, not the system Python
- Any packages you install will go to alpha_env/lib/python3.10/site-packages/

---

## Step 3: Install pycodestyle in alpha_env

```bash
(alpha_env) $ pip install pycodestyle
```

**Expected Output:**
```
Collecting pycodestyle
  Downloading pycodestyle-2.7.0-py2.py3-none-any.whl
Installing collected packages: pycodestyle
Successfully installed pycodestyle-2.7.0
```

(You may see a warning about running pip as root - that's normal in certain environments)

### Verify Installation

```bash
(alpha_env) $ pycodestyle --version
2.7.0
```

**What Happened:**
- pycodestyle was installed to `alpha_env/lib/python3.10/site-packages/pycodestyle/`
- An executable `pycodestyle` was created in `alpha_env/bin/`
- This tool is available ONLY in the alpha_env environment

---

## Step 4: Deactivate alpha_env

```bash
(alpha_env) $ deactivate
```

**Expected Output:**
Prompt returns to normal:
```
user@host:~/holbertonschool-core-engineering$
```

Verify you're no longer in the environment:
```bash
which python3
```

**Expected Output:**
```
/usr/bin/python3
```

**What Happened:**
- The PATH was restored to its original state
- `python3` points back to the system Python
- pycodestyle is no longer available

```bash
pycodestyle --version
```

**Expected Output:**
```
bash: pycodestyle: command not found
```

---

## Step 5: Activate beta_env

```bash
source beta_env/bin/activate
```

**Expected Output:**
```
(beta_env) user@host:~/holbertonschool-core-engineering$
```

Verify the Python interpreter:
```bash
which python3
python3 --version
```

**Expected Output:**
```
/home/kaiserr/holbertonschool-core-engineering/beta_env/bin/python3
Python 3.10.12
```

**What This Means:**
- beta_env has its own Python interpreter
- It's a different environment from alpha_env
- It has its own site-packages directory (currently empty)

---

## Step 6: Verify Isolation - pycodestyle NOT Available in beta_env

```bash
(beta_env) $ pycodestyle --version
```

**Expected Output:**
```
bash: pycodestyle: command not found
```

**THIS IS THE KEY POINT:**
- pycodestyle was installed ONLY in alpha_env's site-packages
- beta_env has a COMPLETELY SEPARATE site-packages directory
- Installing a package in one venv does NOT affect other venvs
- Each environment is ISOLATED

---

## Step 7: Switch Back to alpha_env

```bash
(beta_env) $ deactivate
$ source alpha_env/bin/activate
(alpha_env) $ pycodestyle --version
```

**Expected Output:**
```
2.7.0
```

**What This Demonstrates:**
- pycodestyle is still available in alpha_env
- It never "disappeared" - it was always in alpha_env/bin/
- Switching environments gives you access to different packages
- Each environment is completely independent

---

## Visual Summary: The Isolation

```
System (no venv active)
├── python3 → /usr/bin/python3
└── pycodestyle → NOT FOUND

        ↓ source alpha_env/bin/activate

(alpha_env) Active
├── python3 → ./alpha_env/bin/python3
├── pycodestyle → ./alpha_env/bin/pycodestyle ✓ AVAILABLE
└── sys.prefix → ./alpha_env

        ↓ deactivate

System (back to normal)
├── python3 → /usr/bin/python3
└── pycodestyle → NOT FOUND

        ↓ source beta_env/bin/activate

(beta_env) Active
├── python3 → ./beta_env/bin/python3
├── pycodestyle → NOT FOUND ✗ (installed in alpha_env, not here!)
└── sys.prefix → ./beta_env

        ↓ Switch back: deactivate + source alpha_env/bin/activate

(alpha_env) Active Again
├── python3 → ./alpha_env/bin/python3
├── pycodestyle → ./alpha_env/bin/pycodestyle ✓ AVAILABLE
└── sys.prefix → ./alpha_env
```

---

## Real-World Scenario

### Project A Dependencies (alpha_env)
```bash
pip install Flask==2.0.1
pip install Django==3.2.0
pip install pycodestyle
```

### Project B Dependencies (beta_env)
```bash
pip install Flask==3.0.0      # Different version!
pip install Django==4.0.0      # Different version!
pip install pytest
```

**Without venvs:**
- Installing Flask 3.0 would overwrite Flask 2.0
- Project A would break
- Complete chaos!

**With venvs:**
- alpha_env has Flask 2.0, Django 3.2, pycodestyle
- beta_env has Flask 3.0, Django 4.0, pytest
- No conflicts
- Both projects work independently

---

## Why Virtual Environments Are Essential

### 1. **ISOLATION**
- Each project has its own Python environment
- Packages in one venv don't affect others
- Version conflicts are impossible

### 2. **REPRODUCIBILITY**
- Same environment on different machines
- Use `pip freeze > requirements.txt` to document dependencies
- Easy to recreate identical setups

### 3. **SAFETY**
- System Python (/usr/bin/python3) never modified
- If an environment breaks, delete it and recreate
- System stability guaranteed

### 4. **ORGANIZATION**
- Clear separation between projects
- Easy to track what each project needs
- Professional development practice

---

## Common Virtual Environment Commands

### Create an environment
```bash
python3 -m venv env_name
```

### Activate (Linux/macOS)
```bash
source env_name/bin/activate
```

### Activate (Windows)
```bash
env_name\Scripts\activate
```

### Deactivate (all platforms)
```bash
deactivate
```

### Check what's installed
```bash
pip list
```

### Install a package
```bash
pip install package_name
```

### Install from requirements file
```bash
pip install -r requirements.txt
```

### Save current environment
```bash
pip freeze > requirements.txt
```

### See where packages are installed
```bash
pip show package_name
```

---

## Verification Commands

### Show active environment
```bash
echo $VIRTUAL_ENV
```

### Show where Python points to
```bash
which python3
```

### Show sys.prefix (Python's installation root)
```bash
python3 -c "import sys; print(sys.prefix)"
```

### Show site-packages location
```bash
python3 -c "import site; print(site.getsitepackages())"
```

---

## Conclusion

Virtual environments are:
- ✓ **Essential** for Python development
- ✓ **Easy to use** - just two commands (create + activate)
- ✓ **Lightweight** - each env is just a directory
- ✓ **Reproducible** - can freeze and share requirements
- ✓ **Safe** - system Python never touched

**Best Practice:** Always use a virtual environment for each Python project.

---

## Installation Note

To create virtual environments on your system:

```bash
# On Debian/Ubuntu
sudo apt-get install python3-venv

# On macOS
# Usually pre-installed with Python

# On Windows
# Usually pre-installed with Python
```

After installation, use:
```bash
python3 -m venv my_project_env
source my_project_env/bin/activate  # or env\Scripts\activate on Windows
```
