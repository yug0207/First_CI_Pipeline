# First_CI_Pipeline

Continuous Integration (CI) pipeline project using GitHub Actions, Python, and pytest. The repository contains Python solutions for Programs 21 through 30 along with automated unit test suites for each program. Every code push or pull request to the main branch triggers automated test runs through GitHub Actions.

## Prerequisites

- Python 3.12 or newer
- Git version control
- A GitHub account

## Installation and Virtual Environment Setup

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/YOUR-USERNAME/First_CI_Pipeline.git
cd First_CI_Pipeline
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

- On Windows (Command Prompt):
  ```cmd
  .venv\Scripts\activate
  ```
- On Windows (PowerShell):
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- On macOS / Linux:
  ```bash
  source .venv/bin/activate
  ```

## Dependency Installation

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

Verify that pytest is installed:

```bash
pytest --version
```

## Running Individual Programs

Any program can be executed directly from the project root using Python:

```bash
python codes/21_largest_word.py
python codes/22_anagram_strings.py
python codes/23_sort_without_sort.py
python codes/24_merge_sorted_lists.py
python codes/25_max_min_list.py
python codes/26_sum_of_list.py
python codes/27_rotate_list.py
python codes/28_set_intersection.py
python codes/29_armstrong_number.py
python codes/30_decimal_to_binary.py
```

## Running Automated Tests

Run the full test suite with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest test_cases/test_21_largest_word.py -v
```

Run tests for another specific program:

```bash
pytest test_cases/test_30_decimal_to_binary.py -v
```

## Project Folder Structure

```text
First_CI_Pipeline/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── codes/
│   ├── 21_largest_word.py
│   ├── 22_anagram_strings.py
│   ├── 23_sort_without_sort.py
│   ├── 24_merge_sorted_lists.py
│   ├── 25_max_min_list.py
│   ├── 26_sum_of_list.py
│   ├── 27_rotate_list.py
│   ├── 28_set_intersection.py
│   ├── 29_armstrong_number.py
│   └── 30_decimal_to_binary.py
├── test_cases/
│   ├── test_21_largest_word.py
│   ├── test_22_anagram_strings.py
│   ├── test_23_sort_without_sort.py
│   ├── test_24_merge_sorted_lists.py
│   ├── test_25_max_min_list.py
│   ├── test_26_sum_of_list.py
│   ├── test_27_rotate_list.py
│   ├── test_28_set_intersection.py
│   ├── test_29_armstrong_number.py
│   └── test_30_decimal_to_binary.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Explanation of GitHub Actions Workflow

The workflow file `.github/workflows/python-ci.yml` automates the testing process:

1. **Triggers:** Automatically runs on every push to the `main` branch as well as any pull request targeting the `main` branch.
2. **Runner:** Executes on a clean Ubuntu runner (`ubuntu-latest`).
3. **Check Out Code:** Uses `actions/checkout@v4` to download the repository code onto the runner.
4. **Set Up Python:** Uses `actions/setup-python@v5` to configure Python 3.12.
5. **Install Dependencies:** Upgrades `pip` and installs packages defined in `requirements.txt` (`pytest`).
6. **Run Tests:** Runs `pytest` across all test files in `test_cases/`. A green checkmark indicates that all tests passed successfully; any failed assertion produces a red cross in the GitHub Actions dashboard.

## Git Commands for Committing and Pushing Changes

Check the status of modified and untracked files:

```bash
git status
```

Stage files for commit:

```bash
git add .
```

Commit staged changes with a descriptive message:

```bash
git commit -m "Add programs and automated test cases"
```

Ensure the default branch is named `main`:

```bash
git branch -M main
```

Push commits to the remote repository:

```bash
git push origin main
```
