import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.nio.file.*;

public class CompilerMain {
    public static void main(String[] args) throws Exception {
        String input = Files.readString(Path.of("../input.txt"));
        ExprLexer lexer = new ExprLexer(CharStreams.fromString(input));
        ExprParser parser = new ExprParser(new CommonTokenStream(lexer));
        ParseTree tree = parser.expr();
        MyCodeGenVisitor visitor = new MyCodeGenVisitor();
        visitor.visit(tree);
        Simulator.run(visitor.getInstructions());
    }
}