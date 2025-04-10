import java.util.*;

public class MyCodeGenVisitor extends ExprBaseVisitor<Void> {
    private List<String> instructions = new ArrayList<>();
    private Map<String, Integer> memory = new HashMap<>();
    private int tempCount = 0;

    public List<String> getInstructions() {
        return instructions;
    }

    public Map<String, Integer> getMemory() {
        return memory;
    }

    private String getTemp() {
        return "t" + tempCount++;
    }

    @Override
    public Void visitAssignExpr(ExprParser.AssignExprContext ctx) {
        visit(ctx.expr());
        String resultTemp = getLastTemp();
        instructions.add("STORE " + resultTemp + ", " + ctx.ID().getText());
        memory.put(ctx.ID().getText(), null);
        return null;
    }

    @Override
    public Void visitMaddExpr(ExprParser.MaddExprContext ctx) {
        visit(ctx.expr(0));
        String t1 = getLastTemp();

        visit(ctx.expr(1));
        String t2 = getLastTemp();

        visit(ctx.expr(2));
        String t3 = getLastTemp();

        String t4 = getTemp();
        instructions.add("MADD_SUB " + t4 + ", " + t1 + ", " + t2 + ", " + t3);
        memory.put(t4, null);
        return null;
    }

    @Override
    public Void visitIdExpr(ExprParser.IdExprContext ctx) {
        String t = getTemp();
        instructions.add("LOAD " + t + ", " + ctx.ID().getText());
        memory.put(t, null);
        return null;
    }

    @Override
    public Void visitIntExpr(ExprParser.IntExprContext ctx) {
        String t = getTemp();
        instructions.add("LOAD " + t + ", " + ctx.INT().getText());
        memory.put(t, Integer.parseInt(ctx.INT().getText()));
        return null;
    }

    private String getLastTemp() {
        return "t" + (tempCount - 1);
    }
}
