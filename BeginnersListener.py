# Generated from Beginners.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BeginnersParser import BeginnersParser
else:
    from BeginnersParser import BeginnersParser

# This class defines a complete listener for a parse tree produced by BeginnersParser.
class BeginnersListener(ParseTreeListener):

    # Enter a parse tree produced by BeginnersParser#programa.
    def enterPrograma(self, ctx:BeginnersParser.ProgramaContext):
        pass

    # Exit a parse tree produced by BeginnersParser#programa.
    def exitPrograma(self, ctx:BeginnersParser.ProgramaContext):
        pass


    # Enter a parse tree produced by BeginnersParser#bloque.
    def enterBloque(self, ctx:BeginnersParser.BloqueContext):
        pass

    # Exit a parse tree produced by BeginnersParser#bloque.
    def exitBloque(self, ctx:BeginnersParser.BloqueContext):
        pass


    # Enter a parse tree produced by BeginnersParser#instruccion.
    def enterInstruccion(self, ctx:BeginnersParser.InstruccionContext):
        pass

    # Exit a parse tree produced by BeginnersParser#instruccion.
    def exitInstruccion(self, ctx:BeginnersParser.InstruccionContext):
        pass


    # Enter a parse tree produced by BeginnersParser#mostrar.
    def enterMostrar(self, ctx:BeginnersParser.MostrarContext):
        pass

    # Exit a parse tree produced by BeginnersParser#mostrar.
    def exitMostrar(self, ctx:BeginnersParser.MostrarContext):
        pass


    # Enter a parse tree produced by BeginnersParser#asignar.
    def enterAsignar(self, ctx:BeginnersParser.AsignarContext):
        pass

    # Exit a parse tree produced by BeginnersParser#asignar.
    def exitAsignar(self, ctx:BeginnersParser.AsignarContext):
        pass


    # Enter a parse tree produced by BeginnersParser#tipo.
    def enterTipo(self, ctx:BeginnersParser.TipoContext):
        pass

    # Exit a parse tree produced by BeginnersParser#tipo.
    def exitTipo(self, ctx:BeginnersParser.TipoContext):
        pass


    # Enter a parse tree produced by BeginnersParser#si.
    def enterSi(self, ctx:BeginnersParser.SiContext):
        pass

    # Exit a parse tree produced by BeginnersParser#si.
    def exitSi(self, ctx:BeginnersParser.SiContext):
        pass


    # Enter a parse tree produced by BeginnersParser#darvueltas.
    def enterDarvueltas(self, ctx:BeginnersParser.DarvueltasContext):
        pass

    # Exit a parse tree produced by BeginnersParser#darvueltas.
    def exitDarvueltas(self, ctx:BeginnersParser.DarvueltasContext):
        pass


    # Enter a parse tree produced by BeginnersParser#hacerFuncion.
    def enterHacerFuncion(self, ctx:BeginnersParser.HacerFuncionContext):
        pass

    # Exit a parse tree produced by BeginnersParser#hacerFuncion.
    def exitHacerFuncion(self, ctx:BeginnersParser.HacerFuncionContext):
        pass


    # Enter a parse tree produced by BeginnersParser#parametros.
    def enterParametros(self, ctx:BeginnersParser.ParametrosContext):
        pass

    # Exit a parse tree produced by BeginnersParser#parametros.
    def exitParametros(self, ctx:BeginnersParser.ParametrosContext):
        pass


    # Enter a parse tree produced by BeginnersParser#expresion.
    def enterExpresion(self, ctx:BeginnersParser.ExpresionContext):
        pass

    # Exit a parse tree produced by BeginnersParser#expresion.
    def exitExpresion(self, ctx:BeginnersParser.ExpresionContext):
        pass


    # Enter a parse tree produced by BeginnersParser#termino.
    def enterTermino(self, ctx:BeginnersParser.TerminoContext):
        pass

    # Exit a parse tree produced by BeginnersParser#termino.
    def exitTermino(self, ctx:BeginnersParser.TerminoContext):
        pass


    # Enter a parse tree produced by BeginnersParser#factor.
    def enterFactor(self, ctx:BeginnersParser.FactorContext):
        pass

    # Exit a parse tree produced by BeginnersParser#factor.
    def exitFactor(self, ctx:BeginnersParser.FactorContext):
        pass


    # Enter a parse tree produced by BeginnersParser#condicion.
    def enterCondicion(self, ctx:BeginnersParser.CondicionContext):
        pass

    # Exit a parse tree produced by BeginnersParser#condicion.
    def exitCondicion(self, ctx:BeginnersParser.CondicionContext):
        pass


    # Enter a parse tree produced by BeginnersParser#texto.
    def enterTexto(self, ctx:BeginnersParser.TextoContext):
        pass

    # Exit a parse tree produced by BeginnersParser#texto.
    def exitTexto(self, ctx:BeginnersParser.TextoContext):
        pass



del BeginnersParser