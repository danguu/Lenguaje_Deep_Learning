import sys
from antlr4 import *  # noqa: F403
from IgrisLexer import IgrisLexer
from IgrisParser import IgrisParser
from IgrisVisitor import IgrisVisitor

from lib.algebra import *  # noqa: F403
from lib.archivos import cargar, col
from lib.modelos import regresion, predecir, perceptron, kmeans
from lib.graficos import puntos, linea, graficar


class IgrisInterpreter(IgrisVisitor):
    def __init__(self):
        self.mem = {}

    def visitAssignStmt(self, ctx):
        name = ctx.ID().getText()
        val = self.visit(ctx.expression())
        self.mem[name] = val

    def visitBloque(self, ctx):
        for st in ctx.statement():
            self.visit(st)

    def visitPrintStmt(self, ctx):
        for item in ctx.printItem():
            if isinstance(item, IgrisParser.StringItemContext):
                print(item.STRING().getText()[1:-1], end=" ")
            else:
                print(self.visit(item.expression()), end=" ")
        print()

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expression())
        if cond:
            self.visit(ctx.bloque(0))
        elif ctx.bloque(1):
            self.visit(ctx.bloque(1))

    def visitWhileStmt(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.bloque())

    def _load_data(self, string_ctx):
        ruta = string_ctx.getText()[1:-1]
        return cargar("datos/" + ruta)

    def visitLoadStmt(self, ctx):
        return self._load_data(ctx.STRING())

    def visitLoadExpr(self, ctx):
        return self._load_data(ctx.STRING())

    def visitColStmt(self, ctx):
        return self._col(ctx)

    def visitColExpr(self, ctx):
        return self._col(ctx)

    def _col(self, ctx):
        mat = self.visit(ctx.expression(0))
        idx = int(self.visit(ctx.expression(1)))
        return col(mat, idx)

    def visitRegresionStmt(self, ctx):
        return self._regresion(ctx)

    def visitRegresionExpr(self, ctx):
        return self._regresion(ctx)

    def _regresion(self, ctx):
        X = self.visit(ctx.expression(0))
        y = self.visit(ctx.expression(1))
        return regresion(X, y)

    def visitPredecirStmt(self, ctx):
        return self._predecir(ctx)

    def visitPredecirExpr(self, ctx):
        return self._predecir(ctx)

    def _predecir(self, ctx):
        mod = self.visit(ctx.expression(0))
        x = self.visit(ctx.expression(1))
        return predecir(mod, x)

    def visitPerceptronStmt(self, ctx):
        return self._perceptron(ctx)

    def visitPerceptronExpr(self, ctx):
        return self._perceptron(ctx)

    def _perceptron(self, ctx):
        X = self.visit(ctx.expression(0))
        y = self.visit(ctx.expression(1))
        capas = self.visit(ctx.expression(2)) if ctx.expression(2) else None
        return perceptron(X, y, capas)

    def visitKmeansStmt(self, ctx):
        return self._kmeans(ctx)

    def visitKmeansExpr(self, ctx):
        return self._kmeans(ctx)

    def _kmeans(self, ctx):
        X = self.visit(ctx.expression(0))
        k = int(self.visit(ctx.expression(1)))
        it = int(self.visit(ctx.expression(2))) if ctx.expression(2) else 20
        return kmeans(X, k, it)

    def visitMatSumaStmt(self, ctx):
        return self._mat_suma(ctx)

    def visitMatSumaExpr(self, ctx):
        return self._mat_suma(ctx)

    def _mat_suma(self, ctx):
        return mat_suma(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    def visitMatRestaStmt(self, ctx):
        return self._mat_resta(ctx)

    def visitMatRestaExpr(self, ctx):
        return self._mat_resta(ctx)

    def _mat_resta(self, ctx):
        return mat_resta(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    def visitMatMultStmt(self, ctx):
        return self._mat_mult(ctx)

    def visitMatMultExpr(self, ctx):
        return self._mat_mult(ctx)

    def _mat_mult(self, ctx):
        return mat_mult(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    def visitMatTransStmt(self, ctx):
        return self._mat_trans(ctx)

    def visitMatTransExpr(self, ctx):
        return self._mat_trans(ctx)

    def _mat_trans(self, ctx):
        return mat_trans(self.visit(ctx.expression()))

    def visitMatInvStmt(self, ctx):
        return self._mat_inv(ctx)

    def visitMatInvExpr(self, ctx):
        return self._mat_inv(ctx)

    def _mat_inv(self, ctx):
        return mat_inv(self.visit(ctx.expression()))

    def visitPuntosStmt(self, ctx):
        X = self.visit(ctx.expression(0))
        y = self.visit(ctx.expression(1))
        color = "rojo"
        if ctx.STRING():
            color = ctx.STRING().getText()[1:-1]
        puntos(X, y, color)

    def visitLineaStmt(self, ctx):
        mod = self.visit(ctx.expression())
        linea(mod)

    def visitGraficarStmt(self, ctx):
        graficar()

    # Expresiones
    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitSqrtExpr(self, ctx):
        return raiz(self.visit(ctx.expression()))

    def visitSinExpr(self, ctx):
        return seno(self.visit(ctx.expression()))

    def visitPowerExpr(self, ctx):
        return potencia(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    def visitMulDivExpr(self, ctx):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        op = ctx.op.text
        if op == "*":
            return multiplicar(a, b)
        if op == "/":
            return dividir(a, b)
        return a % b

    def visitAddSubExpr(self, ctx):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return sumar(a, b) if ctx.op.text == "+" else restar(a, b)

    def visitCmpExpr(self, ctx):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        op = ctx.op.text
        if op == "==":
            return a == b
        if op == "!=":
            return a != b
        if op == ">":
            return a > b
        if op == "<":
            return a < b
        if op == ">=":
            return a >= b
        return a <= b

    def visitBoolExpr(self, ctx):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        if ctx.op.text == "&&":
            return bool(a) and bool(b)
        return bool(a) or bool(b)

    # Átomos
    def visitNumberAtom(self, ctx):
        t = ctx.getText()
        return int(t) if "." not in t else float(t)

    def visitTrueAtom(self, ctx):
        return True

    def visitFalseAtom(self, ctx):
        return False

    def visitVarAtom(self, ctx):
        n = ctx.ID().getText()
        return self.mem.get(n, 0)

    def visitIndexAtom(self, ctx):
        nombre = ctx.ID().getText()
        seq = self.mem.get(nombre, [])
        idx = int(self.visit(ctx.expression()))
        return seq[idx]

    def visitVectorAtom(self, ctx):
        return [self.visit(e) for e in ctx.exprList().expression()]

    def visitParenAtom(self, ctx):
        return self.visit(ctx.expression())


def ejecutar(archivo):
    input_stream = FileStream(archivo, encoding="utf-8")
    lexer = IgrisLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = IgrisParser(stream)
    tree = parser.program()
    IgrisInterpreter().visit(tree)
    print(f"\nIGRIS → '{archivo}' ejecutado con éxito")


if len(sys.argv) == 2:
    ejecutar(sys.argv[1])
else:
    print("Uso: python3 igris.py ejemplos/02_regresion.igris")
