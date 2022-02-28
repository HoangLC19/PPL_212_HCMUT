# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\6\20V\n\20\r\20\16")
        buf.write("\20W\3\21\6\21[\n\21\r\21\16\21\\\3\21\5\21`\n\21\3\22")
        buf.write("\6\22c\n\22\r\22\16\22d\3\22\5\22h\n\22\3\23\3\23\6\23")
        buf.write("l\n\23\r\23\16\23m\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\2\2\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\2%\2\'")
        buf.write("\23)\24+\25\3\2\6\4\2C\\c|\3\2\63;\3\2\62;\4\2\13\f\17")
        buf.write("\17\2|\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5\61\3\2\2\2\7\67")
        buf.write("\3\2\2\2\t>\3\2\2\2\13@\3\2\2\2\rB\3\2\2\2\17D\3\2\2\2")
        buf.write("\21F\3\2\2\2\23H\3\2\2\2\25J\3\2\2\2\27L\3\2\2\2\31N\3")
        buf.write("\2\2\2\33P\3\2\2\2\35R\3\2\2\2\37U\3\2\2\2!_\3\2\2\2#")
        buf.write("g\3\2\2\2%i\3\2\2\2\'o\3\2\2\2)r\3\2\2\2+v\3\2\2\2-.\7")
        buf.write("k\2\2./\7p\2\2/\60\7v\2\2\60\4\3\2\2\2\61\62\7h\2\2\62")
        buf.write("\63\7n\2\2\63\64\7q\2\2\64\65\7c\2\2\65\66\7v\2\2\66\6")
        buf.write("\3\2\2\2\678\7t\2\289\7g\2\29:\7v\2\2:;\7w\2\2;<\7t\2")
        buf.write("\2<=\7p\2\2=\b\3\2\2\2>?\7?\2\2?\n\3\2\2\2@A\7*\2\2A\f")
        buf.write("\3\2\2\2BC\7+\2\2C\16\3\2\2\2DE\7}\2\2E\20\3\2\2\2FG\7")
        buf.write("\177\2\2G\22\3\2\2\2HI\7=\2\2I\24\3\2\2\2JK\7.\2\2K\26")
        buf.write("\3\2\2\2LM\7-\2\2M\30\3\2\2\2NO\7/\2\2O\32\3\2\2\2PQ\7")
        buf.write(",\2\2Q\34\3\2\2\2RS\7\61\2\2S\36\3\2\2\2TV\t\2\2\2UT\3")
        buf.write("\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X \3\2\2\2Y[\t\3\2")
        buf.write("\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]`\3\2\2")
        buf.write("\2^`\7\62\2\2_Z\3\2\2\2_^\3\2\2\2`\"\3\2\2\2ac\t\3\2\2")
        buf.write("ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2eh\3\2\2\2fh\7")
        buf.write("\62\2\2gb\3\2\2\2gf\3\2\2\2h$\3\2\2\2ik\7\60\2\2jl\t\4")
        buf.write("\2\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2n&\3\2\2\2")
        buf.write("op\5#\22\2pq\5%\23\2q(\3\2\2\2rs\t\5\2\2st\3\2\2\2tu\b")
        buf.write("\25\2\2u*\3\2\2\2vw\13\2\2\2wx\b\26\3\2x,\3\2\2\2\t\2")
        buf.write("W\\_dgm\4\b\2\2\3\26\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    FLOATTYPE = 2
    RETURN = 3
    EQ = 4
    LP = 5
    RP = 6
    LB = 7
    RB = 8
    SM = 9
    CM = 10
    ADD = 11
    SUB = 12
    MUL = 13
    DIV = 14
    ID = 15
    INTLIT = 16
    FLOATLIT = 17
    WS = 18
    ERROR_CHAR = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "'='", "'('", "')'", "'{'", 
            "'}'", "';'", "','", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "RETURN", "EQ", "LP", "RP", "LB", "RB", 
            "SM", "CM", "ADD", "SUB", "MUL", "DIV", "ID", "INTLIT", "FLOATLIT", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "INTTYPE", "FLOATTYPE", "RETURN", "EQ", "LP", "RP", "LB", 
                  "RB", "SM", "CM", "ADD", "SUB", "MUL", "DIV", "ID", "INTLIT", 
                  "INTPART", "FRACPART", "FLOATLIT", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[20] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


