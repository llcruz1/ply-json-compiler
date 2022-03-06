import ply.yacc as yacc
from lexer import Lexer

class Parser:
    tokens = Lexer.tokens

    def p_json(self, p):
        """json : array
                | object"""

    def p_array(self , p):
        """array : LEFT_BRACKET valuelist RIGHT_BRACKET"""

    def p_valuelist(self, p):
        '''valuelist : valuelist COMMA value
                    | value
                    | empty
                    '''

    def p_object(self, p):
        """object : LEFT_BRACES middle_section RIGHT_BRACES"""

    def p_middle_section(self, p):
        """middle_section : middle_section COMMA pair
                        | pair
                        | empty"""

    def p_pair(self, p):
        """pair : STRING COLON value"""

    def p_value(self, p):
        """value : STRING
                | NUM
                | array
                | object
                | TRUE
                | FALSE
                | NULL
                """

    def p_empty(self, p):
        "empty :  "

    def p_error(self, p):
        raise SyntaxError(p)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser