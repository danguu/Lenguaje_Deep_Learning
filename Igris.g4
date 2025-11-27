grammar Igris;

program         : statement+ EOF ;

statement
    : ID '=>' expression                    #assignStmt
    | 'ver' printItem (',' printItem)*      #printStmt
    | 'si' '(' expression ')' bloque ('sino' bloque)? #ifStmt
    | 'mientras' '(' expression ')' bloque  #whileStmt
    | 'cargar' '(' STRING ')'               #loadStmt
    | 'col' '(' expression ',' expression ')' #colStmt
    | 'regresion' '(' expression ',' expression ')' #regresionStmt
    | 'predecir' '(' expression ',' expression ')'  #predecirStmt
    | 'perceptron' '(' expression ',' expression (',' expression)? ')' #perceptronStmt
    | 'kmeans' '(' expression ',' expression (',' expression)? ')' #kmeansStmt
    | 'mat_suma' '(' expression ',' expression ')' #matSumaStmt
    | 'mat_resta' '(' expression ',' expression ')' #matRestaStmt
    | 'mat_mult' '(' expression ',' expression ')' #matMultStmt
    | 'mat_trans' '(' expression ')'            #matTransStmt
    | 'mat_inv' '(' expression ')'              #matInvStmt
    | 'puntos' '(' expression ',' expression (',' STRING)? ')' #puntosStmt
    | 'linea' '(' expression ')'            #lineaStmt
    | 'graficar' '(' ')'                    #graficarStmt
    | expression                            #exprStmt
    ;

bloque          : '{' statement* '}' ;

printItem
    : STRING                                #stringItem
    | expression                            #exprItem
    ;

expression
    : atom                                  #atomExpr
    | 'raiz' '(' expression ')'             #sqrtExpr
    | 'seno' '(' expression ')'             #sinExpr
    | 'cargar' '(' STRING ')'               #loadExpr
    | 'col' '(' expression ',' expression ')' #colExpr
    | 'regresion' '(' expression ',' expression ')' #regresionExpr
    | 'predecir' '(' expression ',' expression ')'  #predecirExpr
    | 'perceptron' '(' expression ',' expression (',' expression)? ')' #perceptronExpr
    | 'kmeans' '(' expression ',' expression (',' expression)? ')' #kmeansExpr
    | 'mat_suma' '(' expression ',' expression ')' #matSumaExpr
    | 'mat_resta' '(' expression ',' expression ')' #matRestaExpr
    | 'mat_mult' '(' expression ',' expression ')' #matMultExpr
    | 'mat_trans' '(' expression ')'            #matTransExpr
    | 'mat_inv' '(' expression ')'              #matInvExpr
    | expression '^' expression             #powerExpr
    | expression op=('*'|'/'|'%') expression #mulDivExpr
    | expression op=('+'|'-') expression    #addSubExpr
    | expression op=('<'|'>'|'>='|'<='|'=='|'!=') expression #cmpExpr
    | expression op=('&&'|'||') expression    #boolExpr
    ;

atom
    : NUMBER                                #numberAtom
    | 'verdadero'                           #trueAtom
    | 'falso'                               #falseAtom
    | ID '[' expression ']'                 #indexAtom
    | ID                                    #varAtom
    | '[' exprList ']'                      #vectorAtom
    | '(' expression ')'                    #parenAtom
    ;

exprList        : expression (',' expression)* ;

ID              : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER          : [0-9]+ ('.' [0-9]+)? ;
STRING          : '"' (~["\\] | '\\' .)* '"' ;
WS              : [ \t\r\n]+ -> skip ;
COMMENT         : '#' ~[\r\n]* -> skip ;
