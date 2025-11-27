# Generated from Igris.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IgrisParser import IgrisParser
else:
    from IgrisParser import IgrisParser

# This class defines a complete generic visitor for a parse tree produced by IgrisParser.

class IgrisVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IgrisParser#program.
    def visitProgram(self, ctx:IgrisParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#assignStmt.
    def visitAssignStmt(self, ctx:IgrisParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#printStmt.
    def visitPrintStmt(self, ctx:IgrisParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#ifStmt.
    def visitIfStmt(self, ctx:IgrisParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#whileStmt.
    def visitWhileStmt(self, ctx:IgrisParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#loadStmt.
    def visitLoadStmt(self, ctx:IgrisParser.LoadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#colStmt.
    def visitColStmt(self, ctx:IgrisParser.ColStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#regresionStmt.
    def visitRegresionStmt(self, ctx:IgrisParser.RegresionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#predecirStmt.
    def visitPredecirStmt(self, ctx:IgrisParser.PredecirStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#perceptronStmt.
    def visitPerceptronStmt(self, ctx:IgrisParser.PerceptronStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#kmeansStmt.
    def visitKmeansStmt(self, ctx:IgrisParser.KmeansStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matSumaStmt.
    def visitMatSumaStmt(self, ctx:IgrisParser.MatSumaStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matRestaStmt.
    def visitMatRestaStmt(self, ctx:IgrisParser.MatRestaStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matMultStmt.
    def visitMatMultStmt(self, ctx:IgrisParser.MatMultStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matTransStmt.
    def visitMatTransStmt(self, ctx:IgrisParser.MatTransStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matInvStmt.
    def visitMatInvStmt(self, ctx:IgrisParser.MatInvStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#puntosStmt.
    def visitPuntosStmt(self, ctx:IgrisParser.PuntosStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#lineaStmt.
    def visitLineaStmt(self, ctx:IgrisParser.LineaStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#graficarStmt.
    def visitGraficarStmt(self, ctx:IgrisParser.GraficarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#exprStmt.
    def visitExprStmt(self, ctx:IgrisParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#bloque.
    def visitBloque(self, ctx:IgrisParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#stringItem.
    def visitStringItem(self, ctx:IgrisParser.StringItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#exprItem.
    def visitExprItem(self, ctx:IgrisParser.ExprItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#loadExpr.
    def visitLoadExpr(self, ctx:IgrisParser.LoadExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matSumaExpr.
    def visitMatSumaExpr(self, ctx:IgrisParser.MatSumaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#powerExpr.
    def visitPowerExpr(self, ctx:IgrisParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#addSubExpr.
    def visitAddSubExpr(self, ctx:IgrisParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#regresionExpr.
    def visitRegresionExpr(self, ctx:IgrisParser.RegresionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#predecirExpr.
    def visitPredecirExpr(self, ctx:IgrisParser.PredecirExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#sinExpr.
    def visitSinExpr(self, ctx:IgrisParser.SinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#sqrtExpr.
    def visitSqrtExpr(self, ctx:IgrisParser.SqrtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#atomExpr.
    def visitAtomExpr(self, ctx:IgrisParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matRestaExpr.
    def visitMatRestaExpr(self, ctx:IgrisParser.MatRestaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matTransExpr.
    def visitMatTransExpr(self, ctx:IgrisParser.MatTransExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#kmeansExpr.
    def visitKmeansExpr(self, ctx:IgrisParser.KmeansExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#cmpExpr.
    def visitCmpExpr(self, ctx:IgrisParser.CmpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#colExpr.
    def visitColExpr(self, ctx:IgrisParser.ColExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matInvExpr.
    def visitMatInvExpr(self, ctx:IgrisParser.MatInvExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#perceptronExpr.
    def visitPerceptronExpr(self, ctx:IgrisParser.PerceptronExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#matMultExpr.
    def visitMatMultExpr(self, ctx:IgrisParser.MatMultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#boolExpr.
    def visitBoolExpr(self, ctx:IgrisParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:IgrisParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#numberAtom.
    def visitNumberAtom(self, ctx:IgrisParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#trueAtom.
    def visitTrueAtom(self, ctx:IgrisParser.TrueAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#falseAtom.
    def visitFalseAtom(self, ctx:IgrisParser.FalseAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#indexAtom.
    def visitIndexAtom(self, ctx:IgrisParser.IndexAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#varAtom.
    def visitVarAtom(self, ctx:IgrisParser.VarAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#vectorAtom.
    def visitVectorAtom(self, ctx:IgrisParser.VectorAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#parenAtom.
    def visitParenAtom(self, ctx:IgrisParser.ParenAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IgrisParser#exprList.
    def visitExprList(self, ctx:IgrisParser.ExprListContext):
        return self.visitChildren(ctx)



del IgrisParser