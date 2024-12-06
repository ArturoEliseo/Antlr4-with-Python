# Generated from Beginners.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BeginnersParser import BeginnersParser
else:
    from BeginnersParser import BeginnersParser

# This class defines a complete generic visitor for a parse tree produced by BeginnersParser.

class BeginnersVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BeginnersParser#programa.
    def visitPrograma(self, ctx:BeginnersParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#bloque.
    def visitBloque(self, ctx:BeginnersParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#instruccion.
    def visitInstruccion(self, ctx:BeginnersParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#mostrar.
    def visitMostrar(self, ctx:BeginnersParser.MostrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#contenido.
    def visitContenido(self, ctx:BeginnersParser.ContenidoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#elemento.
    def visitElemento(self, ctx:BeginnersParser.ElementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#asignar.
    def visitAsignar(self, ctx:BeginnersParser.AsignarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#tipo.
    def visitTipo(self, ctx:BeginnersParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#si.
    def visitSi(self, ctx:BeginnersParser.SiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#darvueltas.
    def visitDarvueltas(self, ctx:BeginnersParser.DarvueltasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#mientras.
    def visitMientras(self, ctx:BeginnersParser.MientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#hacerFuncion.
    def visitHacerFuncion(self, ctx:BeginnersParser.HacerFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#parametros.
    def visitParametros(self, ctx:BeginnersParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#expresion.
    def visitExpresion(self, ctx:BeginnersParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#termino.
    def visitTermino(self, ctx:BeginnersParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#factor.
    def visitFactor(self, ctx:BeginnersParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#condicion.
    def visitCondicion(self, ctx:BeginnersParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeginnersParser#texto.
    def visitTexto(self, ctx:BeginnersParser.TextoContext):
        return self.visitChildren(ctx)



del BeginnersParser