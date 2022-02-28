# Generated from C:/Users/rober/OneDrive/Documents/BKU/212/PPL/initial/src/main/bkit/parser\BKIT.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("\67\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\5\2\25\n\2\3\3\3\3\6\3\31\n\3\r")
        buf.write("\3\16\3\32\3\3\7\3\36\n\3\f\3\16\3!\13\3\5\3#\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\6\5*\n\5\r\5\16\5+\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\2\2\n\3\2\5\3\7\4\t\5\13\6\r\7")
        buf.write("\17\b\21\t\3\2\3\5\2\13\f\17\17\"\"\29\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\3\24\3\2\2\2\5\"\3\2\2\2\7$\3\2\2\2")
        buf.write("\t)\3\2\2\2\13/\3\2\2\2\r\61\3\2\2\2\17\63\3\2\2\2\21")
        buf.write("\65\3\2\2\2\23\25\4\62;\2\24\23\3\2\2\2\25\4\3\2\2\2\26")
        buf.write("#\7\62\2\2\27\31\5\3\2\2\30\27\3\2\2\2\31\32\3\2\2\2\32")
        buf.write("\30\3\2\2\2\32\33\3\2\2\2\33\37\3\2\2\2\34\36\5\3\2\2")
        buf.write("\35\34\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 ")
        buf.write("#\3\2\2\2!\37\3\2\2\2\"\26\3\2\2\2\"\30\3\2\2\2#\6\3\2")
        buf.write("\2\2$%\7a\2\2%&\3\2\2\2&\'\b\4\2\2\'\b\3\2\2\2(*\t\2\2")
        buf.write("\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,-\3\2\2\2-")
        buf.write(".\b\5\2\2.\n\3\2\2\2/\60\13\2\2\2\60\f\3\2\2\2\61\62\13")
        buf.write("\2\2\2\62\16\3\2\2\2\63\64\13\2\2\2\64\20\3\2\2\2\65\66")
        buf.write("\13\2\2\2\66\22\3\2\2\2\b\2\24\32\37\"+\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PHPI = 1
    UNDERSCORE = 2
    WS = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6
    UNTERMINATED_COMMENT = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'_'" ]

    symbolicNames = [ "<INVALID>",
            "PHPI", "UNDERSCORE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "DIGITS", "PHPI", "UNDERSCORE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


