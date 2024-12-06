from antlr4 import *
from BeginnersLexer import BeginnersLexer
from BeginnersParser import BeginnersParser
from BeginnersVisitor import ParseTreeVisitor

class BeginnersExecutor(ParseTreeVisitor):
    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx):
        print("Visiting the main program block...")
        self.visit(ctx.bloque())

    def visitBloque(self, ctx):
        for instruccion in ctx.instruccion():
            self.visit(instruccion)
            
    def visitAsignar(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.variables[nombre] = valor  
        print(f"Assigned {nombre} = {valor}")


    def visitMostrar(self, ctx):
        
        result = ""
        for elemento_ctx in ctx.contenido().elemento():
            if elemento_ctx.texto():
                raw_text = elemento_ctx.texto().getText()
                clean_text = raw_text[1:-1]  
                result += clean_text
            elif elemento_ctx.expresion():
                result += str(self.visit(elemento_ctx.expresion()))
        
        print(f"Output: {result}")  

    def visitMientras(self, ctx):
        print("Entering 'mientras' loop...")
        iteration = 0 
        while self.visit(ctx.condicion()):
            print(f"Iteration {iteration}: Condition is True. Executing block...")
            self.visit(ctx.bloque())  
            iteration += 1

            
            print(f"Variables state after iteration {iteration}: {self.variables}")
            
            if iteration > 1000:  
                raise RuntimeError("Infinite loop detected!")
        
        print("Exiting 'mientras' loop. Condition is False.")

    def visitExpresion(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.termino(0))
        else:
            izquierda = self.visit(ctx.termino(0))
            derecha = self.visit(ctx.termino(1))
            operador = ctx.getChild(1).getText()

            
            if operador == '+':
                return float(izquierda) + float(derecha)
            elif operador == '-':
                return float(izquierda) - float(derecha)
            elif operador == '*':
                return float(izquierda) * float(derecha)
            elif operador == '/':
                return float(izquierda) / float(derecha)
            else:
                raise ValueError(f"Unsupported operator: {operador}")

    def visitTermino(self, ctx):
        
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor(0))
        else:
            izquierda = self.visit(ctx.factor(0))
            derecha = self.visit(ctx.factor(1))
            operador = ctx.getChild(1).getText()

            if operador == '*':
                return izquierda * derecha
            elif operador == '/':
                return izquierda / derecha
            else:
                raise ValueError(f"Unsupported operator: {operador}")

    def visitFactor(self, ctx):
        
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        elif ctx.ID():
            nombre = ctx.ID().getText()
            return self.variables.get(nombre, 0)
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.expresion())

    def visitDarvueltas(self, ctx):
        veces = int(self.visit(ctx.expresion()))
        print(f"Repeating {veces} times.")
        for _ in range(veces):
            self.visit(ctx.bloque())

    def visitSi(self, ctx):
        condicion = self.visit(ctx.condicion())
        print(f"Condition result: {condicion}")
        if condicion:
            print("Condition is true, executing the block.")
            self.visit(ctx.bloque(0))
        elif ctx.bloque(1):
            print("Condition is false, executing 'sino' block.")
            self.visit(ctx.bloque(1))

    def visitCondicion(self, ctx):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        operador = ctx.getChild(1).getText()

        result = False
        if operador == '==':
            result = izquierda == derecha
        elif operador == '!=':
            result = izquierda != derecha
        elif operador == '<':
            result = izquierda < derecha
        elif operador == '>':
            result = izquierda > derecha
        elif operador == '<=':
            result = izquierda <= derecha
        elif operador == '>=':
            result = izquierda >= derecha
        
        print(f"Evaluating condition: {izquierda} {operador} {derecha} -> {result}")
        return result


def main():
    try:
        lexer = BeginnersLexer(FileStream("programa.beginners"))
        tokens = CommonTokenStream(lexer)
        parser = BeginnersParser(tokens)

        tree = parser.programa()

        executor = BeginnersExecutor()
        executor.visit(tree)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting the interpreter...")
    main()
    print("Interpreter finished.")
