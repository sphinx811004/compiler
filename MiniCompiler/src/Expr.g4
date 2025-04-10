grammar Expr;

prog: expr+ EOF;

expr
    : ID '=' expr                             # assignExpr
    | 'MADD_SUB' '(' expr ',' expr ',' expr ')'  # maddExpr
    | expr '*' expr '+' expr                  # mathExpr
    | ID                                       # idExpr
    | INT                                      # intExpr
    ;

ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
