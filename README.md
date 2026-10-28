# Python DSA Class

Learn and practice Data Structures & Algorithms with Python.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Setup](#setup)
- [Usage](#usage)
- [How to Study](#how-to-study)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Overview

Python DSA Class is an educational repository for students, self-learners, and interview-preparation candidates. It collects practice problems, code examples, and learning notes to help build programming fundamentals and explore common data structures and algorithms.

The repository is a work in progress. Examples and topics are organized in folders and Jupyter notebooks, so you can study a concept, run an example, and adapt it for further practice.

## Features

- Python examples and practice questions covering topics such as arrays, strings, sorting, and problem solving.
- Jupyter notebooks for interactive exploration of arrays, hashing, pointers, strings, sorting, and matrices.
- Notes and algorithm examples, including search, sorting, and graph-related material.
- A beginner-friendly place to experiment with solutions and strengthen interview preparation.

## Repository Structure

```text
.
├── strings.py/
│   ├── arrays.py/
│   │   ├── arrays.ipynb
│   │   ├── hashing.ipynb
│   │   ├── pointers.ipynb
│   │   ├── possible.py
│   │   └── prefix_sum.ipynb
│   ├── python/
│   │   └── functions.py
│   ├── sortings/
│   │   ├── algorithms.txt
│   │   ├── matrix.ipynb
│   │   └── sorting.ipynb
│   ├── strpractice.ipynb
│   └── strings_dsa.ipynb
└── README.md
```

The repository also includes additional practice files and learning notes. File and folder names are kept as they currently appear in the project.

## Setup

### Requirements

- Git
- Python 3
- A terminal or command prompt

Most standalone examples use Python's built-in features. To work with notebooks, install Jupyter:

```bash
python -m pip install notebook
```

### Clone the repository

```bash
git clone https://github.com/kolkarnisha/python_dsa_class.git
cd python_dsa_class
```

### (Optional) Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Usage

Run a Python file from the repository root. For example:

```bash
python strings.py/python/functions.py
```

If your system uses `python3` as the Python command, replace `python` with `python3`. Some practice files may be works in progress.

Start Jupyter from the repository root:

```bash
python -m notebook
```

Then open a notebook such as `strings.py/arrays.py/arrays.ipynb` and run its cells.

## How to Study

1. Read a problem and try solving it on your own first.
2. Run your attempt and compare it with the provided example.
3. Review the approach and note the time and space complexity where applicable.
4. Re-solve it from memory a few days later.
5. Move to the next topic once you can solve problems without looking.

## Contributing

Contributions that make the examples clearer, more accurate, or easier to practice are welcome.

1. Fork the repository.
2. Create a branch for your change.
3. Add or improve an example, explanation, or practice problem.
4. Run your Python example and check that it behaves as described.
5. Open a pull request with a short summary of the change.

Prefer readable Python, include useful explanations for non-obvious solutions, and avoid submitting generated files such as `__pycache__` contents.

## License

There is currently no `LICENSE` file in this repository. Until one is added, the project should not be assumed to grant permission to reuse, modify, or distribute its contents. Contact the repository owner if you need permission.

## Author

**Nisha Kolkar**

- GitHub: [@kolkarnisha](https://github.com/kolkarnisha)
- Repository: [python_dsa_class](https://github.com/kolkarnisha/python_dsa_class)
