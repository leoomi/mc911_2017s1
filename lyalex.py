# ------------------------------------------------------------
# lyalex.py
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
)

reserved = {
        'array': 'ARRAY',
        'by': 'BY',
        'chars': 'CHARS', 
        'dcl': 'DCL', 
        'do': 'DO', 
        'down': 'DOWN',
        'else': 'ELSE',
        'elsif': 'ELSIF',
        'end': 'END',
        'exit': 'EXIT,
        'fi': 'FI',
        'for': 'FOR',
        'if': 'IF', 
        'in': 'IN', 
        'loc': 'LOC',
        'type': 'TYPE',
        'od': 'OD',
        'proc': 'PROC', REF, RESULT, RETURN, RETURNS,
        SYN, THEN, TO, WHILE, ABS, ASC, BOOL, CHAR, FALSE, INT, LENGTH, LOWER, NULL, NUM,
        PRINT, READ, TRUE, UPPER
}

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)    
                return t

            # Define a rule so we can track line numbers
            def t_newline(t):
                    r'\n+'
                    t.lexer.lineno += len(t.value)

                        # A string containing ignored characters (spaces and tabs)
                        t_ignore  = ' \t'

                        # Error handling rule
                        def t_error(t):
                                print("Illegal character '%s'" % t.value[0])
                                t.lexer.skip(1)

                                    # Build the lexer
                                    lexer = lex.lex()