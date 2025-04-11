# 🧾 Mini Compiler: Custom Instruction `MADD_SUB`  
**👤 Name:** Pratyu Dehriya  
**🆔 Roll No:** 23115073

---

## 🛠️ Overview  
A mini compiler built using **ANTLR4** and **Java** that:
- Parses assignment expressions
- Generates 3-address code
- Uses a **custom instruction** `MADD_SUB`
- Simulates instruction execution
- Displays the AST and final variable values

---

## 🧠 Grammar (ANTLR4)
```antlr
grammar Expr;

prog: expr+ EOF;

expr
  : ID '=' expr             # assignExpr
  | expr '*' expr '+' expr  # maddExpr
  | ID                      # idExpr
  | INT                     # intExpr;

ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
```

---

## 🔧 Custom Instruction: `MADD_SUB`

```
MADD_SUB t3, t0, t1, t2  →  t3 = t0 * t1 + t2
```

A custom instruction that fuses multiplication and addition into one.

---

## 📂 Project Structure
```
MiniCompiler/
├── src/
│   ├── CompilerMain.java
│   ├── MyCodeGenVisitor.java
│   ├── Simulator.java
│   └── Expr.g4
├── lib/
│   └── antlr-4.13.1-complete.jar
└── input.txt
```

---

## 🖥️ Input Example  
`input.txt`:
```
z = a * b + c
```

---

## 🧬 AST Output  
```
(prog (expr z = a * b + c))
```

**AST Tree**  
```
       =
     /   \
    z     +
         / \
       *    c
      / \
     a   b
```

---

## ⚙️ Code Generation  
```
LOAD t0, a  
LOAD t1, b  
LOAD t2, c  
MADD_SUB t3, t0, t1, t2  
STORE t3, z
```

---

## 🧪 Simulation (Example Values)
```
a = 2, b = 3, c = 4  
→ t3 = 2 * 3 + 4 = 10  
→ z = 10
```

---

## 🧰 How to Run

### ✅ 1. Generate ANTLR files  
```bash
java -cp "lib/antlr-4.13.1-complete.jar" org.antlr.v4.Tool -visitor src/Expr.g4 -o src

```

### ✅ 2. Compile Java files  
```bash
javac -cp ".;lib/antlr-4.13.1-complete.jar" src/*.java

```

### ✅ 3. Run the compiler  
```bash
java -cp ".;lib/antlr-4.13.1-complete.jar;src" CompilerMain

```

---







