@echo off
echo [1/6] Creating project folders...
mkdir MiniCompiler
cd MiniCompiler
mkdir src
mkdir lib

echo [2/6] Downloading ANTLR...
curl -L -o lib\antlr-4.13.1-complete.jar https://www.antlr.org/download/antlr-4.13.1-complete.jar

echo [3/6] Creating grammar file...
echo grammar Expr;

echo expr:
    expr '*' expr '+' expr     # MaddExpr
  | expr ('*'|'/') expr        # MulDivExpr
  | expr ('+'|'-') expr        # AddSubExpr
  | ID                         # IdExpr
  | INT                        # IntExpr
  | '(' expr ')'               # ParenExpr
  ;

tokens { MUL='*'; ADD='+'; }

ID  : [a-zA-Z]+ ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
> src\Expr.g4

echo [4/6] Creating Java files...
REM CompilerMain.java
(
echo import org.antlr.v4.runtime.*;
echo import org.antlr.v4.runtime.tree.*;
echo import java.nio.file.*;
echo public class CompilerMain {
echo     public static void main(String[] args) throws Exception {
echo         String input = Files.readString(Path.of("input.txt"));
echo         ExprLexer lexer = new ExprLexer(CharStreams.fromString(input));
echo         ExprParser parser = new ExprParser(new CommonTokenStream(lexer));
echo         ParseTree tree = parser.expr();
echo         MyCodeGenVisitor visitor = new MyCodeGenVisitor();
echo         visitor.visit(tree);
echo         Simulator.run(visitor.getInstructions());
echo     }
echo }
) > src\CompilerMain.java

REM MyCodeGenVisitor.java
(
echo import java.util.*;
echo public class MyCodeGenVisitor extends ExprBaseVisitor<Void> {
echo     private List<String> instructions = new ArrayList<>();
echo     private int tempCount = 0;
echo     private String newTemp() { return "t" + (tempCount++); }
echo     private Map<String, String> values = new HashMap<>();
echo     public List<String> getInstructions() { return instructions; }

echo     @Override
echo     public Void visitMaddExpr(ExprParser.MaddExprContext ctx) {
echo         visit(ctx.expr(0));
echo         visit(ctx.expr(1));
echo         visit(ctx.expr(2));
echo         String a = values.get(ctx.expr(0).getText());
echo         String b = values.get(ctx.expr(1).getText());
echo         String c = values.get(ctx.expr(2).getText());
echo         String t = newTemp();
echo         instructions.add("MADD " + t + ", " + a + ", " + b + ", " + c);
echo         values.put(ctx.getText(), t);
echo         return null;
echo     }

echo     @Override
echo     public Void visitIdExpr(ExprParser.IdExprContext ctx) {
echo         String id = ctx.getText();
echo         String t = newTemp();
echo         instructions.add("LOAD " + t + ", " + id);
echo         values.put(id, t);
echo         return null;
echo     }

echo     @Override
echo     public Void visitIntExpr(ExprParser.IntExprContext ctx) {
echo         String t = newTemp();
echo         instructions.add("LOADI " + t + ", " + ctx.getText());
echo         values.put(ctx.getText(), t);
echo         return null;
echo     }
echo }
) > src\MyCodeGenVisitor.java

REM Simulator.java
(
echo import java.util.*;
echo public class Simulator {
echo     static Map<String, Integer> vars = Map.of("a", 2, "b", 3, "c", 4);
echo     static Map<String, Integer> temps = new HashMap<>();

echo     public static void run(List<String> code) {
echo         for (String line : code) {
echo             String[] p = line.split("[ ,]+");
echo
