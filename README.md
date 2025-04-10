# Mini Compiler with Custom Instruction (MADD_SUB)

This is a mini compiler project built using ANTLR4 in Java. It parses and evaluates arithmetic expressions, generates intermediate code with a custom instruction `MADD_SUB`, simulates execution, and prints the final values of variables.

## 🛠 Features

- Parses assignment expressions (e.g., `z = a * b + c`)
- Generates 3-address code
- Supports a custom instruction `MADD_SUB t3, t0, t1, t2` → `t3 = t0 * t1 + t2`
- Simulates instruction execution
- Displays final values of all variables
- Displays the AST (Abstract Syntax Tree)

## 🧠 Grammar (ANTLR4)

grammar Expr;

prog: expr+ EOF;

expr : ID '=' expr # assignExpr | expr '*' expr '+' expr # maddExpr | ID # idExpr | INT # intExpr ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ; INT : [0-9]+ ; WS : [ \t\r\n]+ -> skip ;

shell
Copy
Edit

## 📂 Folder Structure

MiniCompiler/ │ ├── src/ │ ├── CompilerMain.java │ ├── MyCodeGenVisitor.java │ ├── Simulator.java │ ├── Expr.g4 │ └── (generated ANTLR files) │ ├── lib/ │ └── antlr-4.13.1-complete.jar │ └── input.txt

bash
Copy
Edit

## 🚀 How to Run

1. **Generate ANTLR files:**
   ```bash
   java -cp "../lib/antlr-4.13.1-complete.jar" org.antlr.v4.Tool -visitor Expr.g4
Compile all Java files:

bash
Copy
Edit
javac -cp ".;../lib/antlr-4.13.1-complete.jar" *.java
Create an input.txt file with your expression:

ini
Copy
Edit
z = a * b + c
Run the compiler:

bash
Copy
Edit
java -cp ".;../lib/antlr-4.13.1-complete.jar" CompilerMain
Output Example:

pgsql
Copy
Edit
AST: (prog (expr z = a * b + c))
LOAD t0, a
LOAD t1, b
LOAD t2, c
MADD_SUB t3, t0, t1, t2
STORE t3, z
Final result: {t0=2, t1=3, t2=4}
🧾 Notes
MADD_SUB is a custom instruction implemented in the codegen.

Simulation assigns dummy values to variables (a=2, b=3, c=4) for demonstration.

AST is printed using the ANTLR tree structure.

📚 Dependencies
ANTLR 4.13.1

Java 11 or higher

Created with ❤️ for educational and compiler design practice.

vbnet
Copy
Edit

name-Pratyu Dehriya
roll-no-23115073







