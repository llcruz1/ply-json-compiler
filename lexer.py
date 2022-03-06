import ply.lex as lex

class Lexer:
    tokens = [
        "NUM",
        "COMMA",
        "LEFT_BRACKET",
        "RIGHT_BRACKET",
        "LEFT_BRACES", 
        "RIGHT_BRACES",
        "COLON",
        "STRING",
        "TRUE",
        "FALSE",
        "NULL"
    ]

    t_COMMA = r","
    t_COLON = r":"
    t_LEFT_BRACKET = r"\["
    t_RIGHT_BRACKET = r"\]"
    t_LEFT_BRACES = r"\{"
    t_RIGHT_BRACES = r"\}"
    t_TRUE = r"true"
    t_FALSE = r"false"
    t_NULL = r"null"

    t_ignore = " \t\n"

    def t_STRING(self, t):
        r'\"([^\\"]|(\\(("|\\|\/|b|f|n|r|t)|u[0-9A-Fa-f]{4})))*"'
        return t

    def t_NUM(self, t):
        r"-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?"
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer