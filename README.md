# 🧠 Mini Compiler for Arithmetic Expressions

This project is a basic compiler written in Python. It **tokenizes**, **parses**, and **generates assembly-like instructions** for simple arithmetic expressions.

---

## 👤 Author

- **Name:** Pratyu Dehriya
- **Roll No:** 23115073

---

## 📁 Project Structure

| File               | Description                                     |
|--------------------|-------------------------------------------------|
| `main.py`          | Entry point of the compiler                     |
| `lexer.py`         | Tokenizes arithmetic expressions                |
| `parser.py`        | Builds an abstract syntax tree (AST) from tokens|
| `code_generator.py`| Converts AST into instruction-like output       |
| `test.py`          | Runs tests on the compiler pipeline             |
| `output.txt`       | Stores the output of test results               |
| `.gitignore`       | Ignores unnecessary files/folders               |

---

## ⚙️ Features

- Supports basic arithmetic: `+`, `-`, `*`, `/`
- Operator precedence handled correctly
- AST-based code generation
- Modular design (Lexer → Parser → CodeGen)
- Easy to extend (e.g., for new instructions or backends)

---

## 🚀 How to Run

1. **Clone the repo** or download the files.

2. **Run tests** from the terminal:
   ```bash
   python test.py
