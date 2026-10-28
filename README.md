# 🐍 Python Practice Scripts

A collection of beginner-friendly Python scripts covering fundamental programming concepts — from basic arithmetic to string manipulation, user input handling, and command-line arguments.

---

## 📁 Project Structure

```
Python/
├── first python.py           # Variable swapping without a temp variable
├── second python.py          # Floating-point arithmetic & complex numbers
├── calculator.py             # Interactive calculator (add, sub, mul, div, avg)
├── split.py                  # Calculator using .split() for inline input
├── split method.py           # Demonstrating the str.split() method
├── user login.py             # Simple username/password login system
├── restart.py                # Loop with restart prompt (y/n)
├── range.py                  # Python range() function example
├── eval function.py          # Python eval() function demo
├── eval prof2.py             # Extended eval() practice
├── eval3.py                  # Further eval() exploration
├── command line arguments.py # Sum of even numbers via CLI arguments
└── README.md
```

---

## 📜 Script Descriptions

### 🔄 `first python.py`
Demonstrates swapping two variables **without a temporary variable** using arithmetic operations.
```
Before Swap A Value is  10  And B Value is  5
After Swap  A Value is  5   And B Value is  10
```

---

### ➕ `second python.py`
Performs basic floating-point addition and displays the result of two numbers being summed.

---

### 🧮 `calculator.py`
An interactive command-line calculator. Prompts the user for two integers, then asks for an operation:

| Command | Operation       |
|---------|-----------------|
| `add`   | Addition        |
| `sub`   | Subtraction     |
| `mul`   | Multiplication  |
| `div`   | Division        |
| `avg`   | Average         |

**Usage:**
```bash
python calculator.py
```

---

### 🔢 `split.py`
A compact calculator that accepts two numbers **and** an operation choice all in a single line of input using `.split()`.

**Usage:**
```bash
python split.py
# Input example: 10 5 1    (numbers: 10, 5 | operation: 1=add)
```

| Code | Operation |
|------|-----------|
| 1    | Add       |
| 2    | Subtract  |
| 3    | Multiply  |
| 4    | Divide    |
| 5    | Average   |
| 6    | Exit      |

---

### ✂️ `split method.py`
Shows how to use `str.split(",")` to parse comma-separated user input into multiple integer variables.

**Usage:**
```bash
python "split method.py"
# Input example: 10,20,30
```

---

### 🔐 `user login.py`
A simple login system that checks user credentials against the keyword `"admin"`.

**Usage:**
```bash
python "user login.py"
```

---

### 🔁 `restart.py`
Demonstrates a restart loop pattern — after the main program logic, it prompts the user with `Run again? (y/n)` and loops accordingly until the user exits.

**Usage:**
```bash
python restart.py
```

---

### 📊 `range.py`
Illustrates Python's built-in `range()` function with a start, stop, and step value.

```python
r = range(30, 500, 100)
# Output: 30, 130, 230, 330, 430
```

---

### 🔬 `eval function.py` / `eval prof2.py` / `eval3.py`
Explores Python's built-in `eval()` function, which parses and evaluates a string expression at runtime using the current variable context.

```python
a, b = 5, 10
result = eval("a+b-4")  # Output: 11
```

---

### 💻 `command line arguments.py`
Accepts numbers as **command-line arguments** and prints the cumulative **sum of even numbers** among them.

**Usage:**
```bash
python "command line arguments.py" 2 4 5 6 8 11
# Output: sum of even numbers = 2, 6, 12, 20
```

---

## 🚀 Getting Started

### Prerequisites
- Python **3.x** installed on your machine.
- Download from [python.org](https://www.python.org/downloads/)

### Running a Script
```bash
# Navigate to the project directory
cd "path/to/Python"

# Run any script
python calculator.py
python "command line arguments.py" 1 2 3 4 5
```

---

## 🧠 Concepts Covered

| Concept                    | Scripts                                    |
|----------------------------|--------------------------------------------|
| Variables & Arithmetic     | `first python.py`, `second python.py`      |
| User Input (`input()`)     | `calculator.py`, `user login.py`           |
| Conditional Statements     | `calculator.py`, `split.py`, `user login.py` |
| Loops (`while`, `for`)     | `restart.py`, `range.py`                  |
| String `.split()` method   | `split.py`, `split method.py`              |
| `eval()` built-in          | `eval function.py`, `eval prof2.py`, `eval3.py` |
| Command-line args (`sys`)  | `command line arguments.py`               |
| List comprehensions        | `split.py`, `split method.py`              |

---

## 👤 Author

**Altaf Malek**

---

## 📄 License

This project is open source and available for educational purposes.
