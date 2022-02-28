# Generated from c:\Users\rober\OneDrive\Documents\BKU\212\PPL\Programming Code\AST\CSEL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\6\2\36\n\2\r\2\16\2\37\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5;\n\5\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\tM\n\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16d\n\16\3\16")
        buf.write("\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\4\3\2\f\16")
        buf.write("\3\2\17\21\2`\2\35\3\2\2\2\4#\3\2\2\2\6.\3\2\2\2\b:\3")
        buf.write("\2\2\2\n<\3\2\2\2\f@\3\2\2\2\16C\3\2\2\2\20L\3\2\2\2\22")
        buf.write("N\3\2\2\2\24R\3\2\2\2\26X\3\2\2\2\30Z\3\2\2\2\32c\3\2")
        buf.write("\2\2\34\36\5\6\4\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3")
        buf.write("\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\7\2\2\3\"\3\3\2\2\2#$")
        buf.write("\t\2\2\2$\5\3\2\2\2%&\5\n\6\2&\'\5\b\5\2\'/\3\2\2\2()")
        buf.write("\5\22\n\2)*\5\b\5\2*/\3\2\2\2+,\5\30\r\2,-\5\b\5\2-/\3")
        buf.write("\2\2\2.%\3\2\2\2.(\3\2\2\2.+\3\2\2\2/\7\3\2\2\2\60\61")
        buf.write("\5\n\6\2\61\62\5\b\5\2\62;\3\2\2\2\63\64\5\22\n\2\64\65")
        buf.write("\5\b\5\2\65;\3\2\2\2\66\67\5\30\r\2\678\5\b\5\28;\3\2")
        buf.write("\2\29;\3\2\2\2:\60\3\2\2\2:\63\3\2\2\2:\66\3\2\2\2:9\3")
        buf.write("\2\2\2;\t\3\2\2\2<=\7\3\2\2=>\5\f\7\2>?\7\6\2\2?\13\3")
        buf.write("\2\2\2@A\5\16\b\2AB\5\20\t\2B\r\3\2\2\2CD\7\22\2\2DE\7")
        buf.write("\7\2\2EF\5\4\3\2F\17\3\2\2\2GH\7\b\2\2HI\5\16\b\2IJ\5")
        buf.write("\20\t\2JM\3\2\2\2KM\3\2\2\2LG\3\2\2\2LK\3\2\2\2M\21\3")
        buf.write("\2\2\2NO\7\4\2\2OP\5\24\13\2PQ\7\6\2\2Q\23\3\2\2\2RS\7")
        buf.write("\22\2\2ST\7\7\2\2TU\5\4\3\2UV\7\13\2\2VW\5\26\f\2W\25")
        buf.write("\3\2\2\2XY\t\3\2\2Y\27\3\2\2\2Z[\7\5\2\2[\\\7\22\2\2\\")
        buf.write("]\7\t\2\2]^\5\32\16\2^_\7\n\2\2_`\7\6\2\2`\31\3\2\2\2")
        buf.write("ad\5\f\7\2bd\3\2\2\2ca\3\2\2\2cb\3\2\2\2d\33\3\2\2\2\7")
        buf.write("\37.:Lc")
        return buf.getvalue()


class CSELParser ( Parser ):

    grammarFileName = "CSEL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Let'", "'Constant'", "'Function'", "';'", 
                     "':'", "','", "'('", "')'", "'='", "'Int'", "'Float'", 
                     "'Boolean'" ]

    symbolicNames = [ "<INVALID>", "LET", "CONST", "FUNCTION", "SEMI", "COLON", 
                      "COMMA", "LR", "RR", "EQ", "INT", "FLOAT", "BOOLEAN", 
                      "INTLIT", "FLOATLIT", "BOOLEANLIT", "ID", "WS" ]

    RULE_program = 0
    RULE_cseltype = 1
    RULE_decl = 2
    RULE_decltail = 3
    RULE_vardecl = 4
    RULE_single_vardecls = 5
    RULE_single_vardecl = 6
    RULE_single_vardecltail = 7
    RULE_constdecl = 8
    RULE_single_constdecl = 9
    RULE_expr = 10
    RULE_funcdecl = 11
    RULE_paramlist = 12

    ruleNames =  [ "program", "cseltype", "decl", "decltail", "vardecl", 
                   "single_vardecls", "single_vardecl", "single_vardecltail", 
                   "constdecl", "single_constdecl", "expr", "funcdecl", 
                   "paramlist" ]

    EOF = Token.EOF
    LET=1
    CONST=2
    FUNCTION=3
    SEMI=4
    COLON=5
    COMMA=6
    LR=7
    RR=8
    EQ=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    INTLIT=13
    FLOATLIT=14
    BOOLEANLIT=15
    ID=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSELParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.DeclContext)
            else:
                return self.getTypedRuleContext(CSELParser.DeclContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_program




    def program(self):

        localctx = CSELParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.decl()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.LET) | (1 << CSELParser.CONST) | (1 << CSELParser.FUNCTION))) != 0)):
                    break

            self.state = 31
            self.match(CSELParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CseltypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSELParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSELParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(CSELParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_cseltype




    def cseltype(self):

        localctx = CSELParser.CseltypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cseltype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.INT) | (1 << CSELParser.FLOAT) | (1 << CSELParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(CSELParser.VardeclContext,0)


        def decltail(self):
            return self.getTypedRuleContext(CSELParser.DecltailContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(CSELParser.ConstdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(CSELParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_decl




    def decl(self):

        localctx = CSELParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.LET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.vardecl()
                self.state = 36
                self.decltail()
                pass
            elif token in [CSELParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.constdecl()
                self.state = 39
                self.decltail()
                pass
            elif token in [CSELParser.FUNCTION]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.funcdecl()
                self.state = 42
                self.decltail()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecltailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(CSELParser.VardeclContext,0)


        def decltail(self):
            return self.getTypedRuleContext(CSELParser.DecltailContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(CSELParser.ConstdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(CSELParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_decltail




    def decltail(self):

        localctx = CSELParser.DecltailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decltail)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.vardecl()
                self.state = 47
                self.decltail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.constdecl()
                self.state = 50
                self.decltail()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.funcdecl()
                self.state = 53
                self.decltail()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(CSELParser.LET, 0)

        def single_vardecls(self):
            return self.getTypedRuleContext(CSELParser.Single_vardeclsContext,0)


        def SEMI(self):
            return self.getToken(CSELParser.SEMI, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_vardecl




    def vardecl(self):

        localctx = CSELParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(CSELParser.LET)
            self.state = 59
            self.single_vardecls()
            self.state = 60
            self.match(CSELParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_vardeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_vardecl(self):
            return self.getTypedRuleContext(CSELParser.Single_vardeclContext,0)


        def single_vardecltail(self):
            return self.getTypedRuleContext(CSELParser.Single_vardecltailContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_single_vardecls




    def single_vardecls(self):

        localctx = CSELParser.Single_vardeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_single_vardecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.single_vardecl()
            self.state = 63
            self.single_vardecltail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_vardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def COLON(self):
            return self.getToken(CSELParser.COLON, 0)

        def cseltype(self):
            return self.getTypedRuleContext(CSELParser.CseltypeContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_single_vardecl




    def single_vardecl(self):

        localctx = CSELParser.Single_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_single_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(CSELParser.ID)
            self.state = 66
            self.match(CSELParser.COLON)
            self.state = 67
            self.cseltype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_vardecltailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(CSELParser.COMMA, 0)

        def single_vardecl(self):
            return self.getTypedRuleContext(CSELParser.Single_vardeclContext,0)


        def single_vardecltail(self):
            return self.getTypedRuleContext(CSELParser.Single_vardecltailContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_single_vardecltail




    def single_vardecltail(self):

        localctx = CSELParser.Single_vardecltailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_single_vardecltail)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(CSELParser.COMMA)
                self.state = 70
                self.single_vardecl()
                self.state = 71
                self.single_vardecltail()
                pass
            elif token in [CSELParser.SEMI, CSELParser.RR]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSELParser.CONST, 0)

        def single_constdecl(self):
            return self.getTypedRuleContext(CSELParser.Single_constdeclContext,0)


        def SEMI(self):
            return self.getToken(CSELParser.SEMI, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_constdecl




    def constdecl(self):

        localctx = CSELParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(CSELParser.CONST)
            self.state = 77
            self.single_constdecl()
            self.state = 78
            self.match(CSELParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_constdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def COLON(self):
            return self.getToken(CSELParser.COLON, 0)

        def cseltype(self):
            return self.getTypedRuleContext(CSELParser.CseltypeContext,0)


        def EQ(self):
            return self.getToken(CSELParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(CSELParser.ExprContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_single_constdecl




    def single_constdecl(self):

        localctx = CSELParser.Single_constdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_single_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(CSELParser.ID)
            self.state = 81
            self.match(CSELParser.COLON)
            self.state = 82
            self.cseltype()
            self.state = 83
            self.match(CSELParser.EQ)
            self.state = 84
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSELParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSELParser.FLOATLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(CSELParser.BOOLEANLIT, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_expr




    def expr(self):

        localctx = CSELParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.INTLIT) | (1 << CSELParser.FLOATLIT) | (1 << CSELParser.BOOLEANLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(CSELParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def LR(self):
            return self.getToken(CSELParser.LR, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSELParser.ParamlistContext,0)


        def RR(self):
            return self.getToken(CSELParser.RR, 0)

        def SEMI(self):
            return self.getToken(CSELParser.SEMI, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_funcdecl




    def funcdecl(self):

        localctx = CSELParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(CSELParser.FUNCTION)
            self.state = 89
            self.match(CSELParser.ID)
            self.state = 90
            self.match(CSELParser.LR)
            self.state = 91
            self.paramlist()
            self.state = 92
            self.match(CSELParser.RR)
            self.state = 93
            self.match(CSELParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_vardecls(self):
            return self.getTypedRuleContext(CSELParser.Single_vardeclsContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_paramlist




    def paramlist(self):

        localctx = CSELParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramlist)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.single_vardecls()
                pass
            elif token in [CSELParser.RR]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





