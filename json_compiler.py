import sys
from lexer import Lexer
from parser import Parser

class JsonCompiler:
    def __init__(self):
        lex = Lexer()
        self.lexer = lex.build()
        par = Parser()
        self.parser = par.build()
        self.input_data = ""

    def input_file(self, file_path):
        f = open(file_path)
        self.input_data = f.read()
        f.close()
        self.lexer.input(self.input_data)
        self.parser.parse(self.input_data, self.lexer)
        self.validate_input()

    def validate_input(self):
        try:
            self.parser.parse(self.input_data)
        except SyntaxError as e:
            print("Error: Input is not of JSON type")
            print(e)
            sys.exit(0)
        else:
            print("OK")

def main():
    json_compiler = JsonCompiler()
    file = input("File: ")
    json_compiler.input_file(file)

if __name__ == "__main__":
    main()
