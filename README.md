# python_dsa_class
# Python DSA Class

> Learn Data Structures & Algorithms in Python through practice problems, clean solutions, and clear explanations.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Topic](https://img.shields.io/badge/Topic-DSA-orange)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Intermediate-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Setup](#setup)
- [Usage](#usage)
- [How to Study with This Repo](#how-to-study-with-this-repo)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Overview

**Python DSA Class** is an educational repository for learning Data Structures and Algorithms (DSA) using Python. It collects practice problems, worked solutions, and explanations in one place, organised by topic so you can build skills step by step.

It is designed for:

- **Students** learning DSA for coursework
- **Self-learners** starting their programming journey
- **Interview candidates** preparing for technical coding rounds

---

## Features

- **Practice problems** organised by topic and difficulty
- **Worked solutions** written in readable, idiomatic Python
- **Explanations** of the approach behind each solution
- **Complexity notes** (time and space) for key problems
- **Runnable code**: every file can be executed directly with Python
- **Beginner-friendly progression** from fundamentals to interview-style problems

### Topics Covered

> Update this list to match the folders in your repository.

- Arrays and Strings
- Searching and Sorting
- Recursion and Backtracking
- Linked Lists
- Stacks and Queues
- Hash Tables
- Trees and Graphs
- Dynamic Programming

---

## Tech Stack

| Component | Details |
|-----------|---------|
| Language | Python 3.8+ |
| Dependencies | Python standard library only (no external packages required) |
| Tools | Git, any code editor (VS Code, PyCharm) or terminal |

---

## Repository Structure

> Update the tree below to match your repository layout.

```text
python_dsa_class/
├── arrays/
├── strings/
├── linked_lists/
├── stacks_queues/
├── trees/
├── graphs/
├── sorting_searching/
├── dynamic_programming/
├── LICENSE
└── README.md
```

---

## Setup

### Prerequisites

- [Python 3.8 or higher](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

Verify your installation:

```bash
python --version
git --version
```

### Clone the repository

```bash
git clone https://github.com/kolkarnisha/python_dsa_class.git
cd python_dsa_class
```

### (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

No `pip install` step is needed unless a file states otherwise.

---

## Usage

### Run a solution file

```bash
python arrays/two_sum.py
```

> Replace the path with any file in the repository.

### Run a file with a specific Python version

```bash
python3 arrays/two_sum.py
```

### Example solution format

Each solution follows a consistent structure:

```python
def two_sum(nums, target):
    """
    Return indices of the two numbers that add up to target.

    Approach: Use a hash map to store seen values.
    Time:  O(n)
    Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # Output: [0, 1]
```

### Run tests (if a file includes them)

```bash
python -m unittest discover
```

---

## How to Study with This Repo

1. **Read the problem** and try solving it on your own first.
2. **Run your attempt** and compare it with the provided solution.
3. **Read the explanation** and note the time and space complexity.
4. **Re-solve it from memory** a few days later.
5. **Move to the next topic** once you can solve problems without looking.

---

## Contributing

Contributions are welcome, including new problems, alternative solutions, and corrections.

1. **Fork** the repository.
2. **Create a branch**:
   ```bash
   git checkout -b add/problem-name
   ```
3. **Add your changes** to the correct topic folder.
4. **Test your code** by running it locally.
5. **Commit** with a clear message:
   ```bash
   git commit -m "Add binary search solution"
   ```
6. **Push** and open a **Pull Request**:
   ```bash
   git push origin add/problem-name
   ```

### Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) style.
- Use descriptive file and function names (for example, `two_sum.py`).
- Include a short docstring with the approach, time complexity, and space complexity.
- Add an `if __name__ == "__main__":` block with sample input and output.
- Keep one problem per file.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Author

**Nisha Kolkar**

- GitHub: [@kolkarnisha](https://github.com/kolkarnisha)
- Repository: [github.com/kolkarnisha/python_dsa_class](https://github.com/kolkarnisha/python_dsa_class)

If this repository helps you, consider giving it a ⭐.
