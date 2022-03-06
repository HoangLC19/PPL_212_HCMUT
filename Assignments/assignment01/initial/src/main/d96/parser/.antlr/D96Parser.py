# Generated from c:\Users\rober\OneDrive\Documents\BKU\212\PPL\Assignments\assignment01\initial\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0225\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3n\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4~\n\4\3\5\3\5\5\5\u0082")
        buf.write("\n\5\3\5\3\5\3\5\3\5\3\5\5\5\u0089\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0099\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a5\n\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00ac\n\t\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00b7\n\13\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00bd\n\f\3\r\3\r\3\r\3\r\5\r\u00c3\n\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00cb\n\16\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00d3\n\20\3\20\3\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00de\n\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u00e5\n\22\3\23\3\23\3\23\3\23\3\23\3\23\7")
        buf.write("\23\u00ed\n\23\f\23\16\23\u00f0\13\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\7\24\u00f8\n\24\f\24\16\24\u00fb\13\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\7\25\u0103\n\25\f\25\16\25")
        buf.write("\u0106\13\25\3\26\3\26\3\26\5\26\u010b\n\26\3\27\3\27")
        buf.write("\3\27\5\27\u0110\n\27\3\30\3\30\3\30\3\30\3\30\7\30\u0117")
        buf.write("\n\30\f\30\16\30\u011a\13\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\7\31\u012e\n\31\f\31\16\31\u0131\13\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0145\n\32\f\32\16")
        buf.write("\32\u0148\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u0155\n\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\5\34\u015c\n\34\3\35\3\35\3\35\5\35\u0161\n\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u0168\n\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\5\37\u0173\n\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \5 \u017b\n \3!\3!\3!\3!\5!\u0181\n!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u018b\n\"\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u019b\n#\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01af\n%\3")
        buf.write("&\3&\3&\3&\3&\5&\u01b6\n&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\5*\u01d7\n*\3+\3+\3+\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3-\5-\u01e5\n-\3.\3.\3.\3.\3.\3.\5.\u01ed\n.\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u0200")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0213\n\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\5\62\u0221\n\62\3\63\3\63\3\63\2\b$&(.\60\62\64")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\13\3\2\25\26\4\2\30\31")
        buf.write("89\3\289\3\2+,\4\2$$&*\3\2\"#\3\2\34\35\3\2\36 \3\2\n")
        buf.write("\13\2\u0234\2f\3\2\2\2\4m\3\2\2\2\6}\3\2\2\2\b\u0088\3")
        buf.write("\2\2\2\n\u0098\3\2\2\2\f\u009a\3\2\2\2\16\u00a4\3\2\2")
        buf.write("\2\20\u00ab\3\2\2\2\22\u00ad\3\2\2\2\24\u00b6\3\2\2\2")
        buf.write("\26\u00bc\3\2\2\2\30\u00c2\3\2\2\2\32\u00ca\3\2\2\2\34")
        buf.write("\u00cc\3\2\2\2\36\u00ce\3\2\2\2 \u00dd\3\2\2\2\"\u00e4")
        buf.write("\3\2\2\2$\u00e6\3\2\2\2&\u00f1\3\2\2\2(\u00fc\3\2\2\2")
        buf.write("*\u010a\3\2\2\2,\u010f\3\2\2\2.\u0111\3\2\2\2\60\u011b")
        buf.write("\3\2\2\2\62\u0132\3\2\2\2\64\u0154\3\2\2\2\66\u015b\3")
        buf.write("\2\2\28\u0160\3\2\2\2:\u0167\3\2\2\2<\u0172\3\2\2\2>\u017a")
        buf.write("\3\2\2\2@\u0180\3\2\2\2B\u018a\3\2\2\2D\u019a\3\2\2\2")
        buf.write("F\u019c\3\2\2\2H\u01ae\3\2\2\2J\u01b5\3\2\2\2L\u01b7\3")
        buf.write("\2\2\2N\u01bd\3\2\2\2P\u01c0\3\2\2\2R\u01d6\3\2\2\2T\u01d8")
        buf.write("\3\2\2\2V\u01db\3\2\2\2X\u01e4\3\2\2\2Z\u01ec\3\2\2\2")
        buf.write("\\\u01ff\3\2\2\2^\u0212\3\2\2\2`\u0214\3\2\2\2b\u0220")
        buf.write("\3\2\2\2d\u0222\3\2\2\2fg\5\4\3\2gh\7\2\2\3h\3\3\2\2\2")
        buf.write("ij\5\6\4\2jk\5\4\3\2kn\3\2\2\2ln\5\6\4\2mi\3\2\2\2ml\3")
        buf.write("\2\2\2n\5\3\2\2\2op\7\24\2\2pq\78\2\2qr\7\63\2\2rs\5\b")
        buf.write("\5\2st\7\64\2\2t~\3\2\2\2uv\7\24\2\2vw\78\2\2wx\7\67\2")
        buf.write("\2xy\78\2\2yz\7\63\2\2z{\5\b\5\2{|\7\64\2\2|~\3\2\2\2")
        buf.write("}o\3\2\2\2}u\3\2\2\2~\7\3\2\2\2\177\u0082\5\n\6\2\u0080")
        buf.write("\u0082\5\f\7\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083\u0084\5\b\5\2\u0084\u0089\3\2\2\2")
        buf.write("\u0085\u0089\5\n\6\2\u0086\u0089\5\f\7\2\u0087\u0089\3")
        buf.write("\2\2\2\u0088\u0081\3\2\2\2\u0088\u0085\3\2\2\2\u0088\u0086")
        buf.write("\3\2\2\2\u0088\u0087\3\2\2\2\u0089\t\3\2\2\2\u008a\u008b")
        buf.write("\t\2\2\2\u008b\u008c\5\24\13\2\u008c\u008d\7\67\2\2\u008d")
        buf.write("\u008e\5\32\16\2\u008e\u008f\7\66\2\2\u008f\u0099\3\2")
        buf.write("\2\2\u0090\u0091\t\2\2\2\u0091\u0092\5\24\13\2\u0092\u0093")
        buf.write("\7\67\2\2\u0093\u0094\5\32\16\2\u0094\u0095\7%\2\2\u0095")
        buf.write("\u0096\5:\36\2\u0096\u0097\7\66\2\2\u0097\u0099\3\2\2")
        buf.write("\2\u0098\u008a\3\2\2\2\u0098\u0090\3\2\2\2\u0099\13\3")
        buf.write("\2\2\2\u009a\u009b\t\3\2\2\u009b\u009c\5\16\b\2\u009c")
        buf.write("\u009d\5> \2\u009d\r\3\2\2\2\u009e\u009f\7/\2\2\u009f")
        buf.write("\u00a0\5\20\t\2\u00a0\u00a1\7\60\2\2\u00a1\u00a5\3\2\2")
        buf.write("\2\u00a2\u00a3\7/\2\2\u00a3\u00a5\7\60\2\2\u00a4\u009e")
        buf.write("\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\17\3\2\2\2\u00a6\u00a7")
        buf.write("\5\22\n\2\u00a7\u00a8\7\66\2\2\u00a8\u00a9\5\20\t\2\u00a9")
        buf.write("\u00ac\3\2\2\2\u00aa\u00ac\5\22\n\2\u00ab\u00a6\3\2\2")
        buf.write("\2\u00ab\u00aa\3\2\2\2\u00ac\21\3\2\2\2\u00ad\u00ae\5")
        buf.write("\26\f\2\u00ae\u00af\7\67\2\2\u00af\u00b0\5\32\16\2\u00b0")
        buf.write("\23\3\2\2\2\u00b1\u00b2\t\4\2\2\u00b2\u00b3\7\65\2\2\u00b3")
        buf.write("\u00b7\5\24\13\2\u00b4\u00b7\78\2\2\u00b5\u00b7\79\2\2")
        buf.write("\u00b6\u00b1\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3")
        buf.write("\2\2\2\u00b7\25\3\2\2\2\u00b8\u00b9\78\2\2\u00b9\u00ba")
        buf.write("\7\65\2\2\u00ba\u00bd\5\26\f\2\u00bb\u00bd\78\2\2\u00bc")
        buf.write("\u00b8\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\27\3\2\2\2\u00be")
        buf.write("\u00bf\79\2\2\u00bf\u00c0\7\65\2\2\u00c0\u00c3\5\30\r")
        buf.write("\2\u00c1\u00c3\79\2\2\u00c2\u00be\3\2\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\31\3\2\2\2\u00c4\u00cb\7\16\2\2\u00c5\u00cb")
        buf.write("\7\17\2\2\u00c6\u00cb\7\20\2\2\u00c7\u00cb\7\21\2\2\u00c8")
        buf.write("\u00cb\5\36\20\2\u00c9\u00cb\5\34\17\2\u00ca\u00c4\3\2")
        buf.write("\2\2\u00ca\u00c5\3\2\2\2\u00ca\u00c6\3\2\2\2\u00ca\u00c7")
        buf.write("\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb")
        buf.write("\33\3\2\2\2\u00cc\u00cd\5\64\33\2\u00cd\35\3\2\2\2\u00ce")
        buf.write("\u00cf\7\f\2\2\u00cf\u00d2\7\61\2\2\u00d0\u00d3\5\32\16")
        buf.write("\2\u00d1\u00d3\7\f\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\7\65\2\2\u00d5")
        buf.write("\u00d6\7:\2\2\u00d6\u00d7\7\62\2\2\u00d7\37\3\2\2\2\u00d8")
        buf.write("\u00d9\5\"\22\2\u00d9\u00da\t\5\2\2\u00da\u00db\5\"\22")
        buf.write("\2\u00db\u00de\3\2\2\2\u00dc\u00de\5\"\22\2\u00dd\u00d8")
        buf.write("\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de!\3\2\2\2\u00df\u00e0")
        buf.write("\5$\23\2\u00e0\u00e1\t\6\2\2\u00e1\u00e2\5$\23\2\u00e2")
        buf.write("\u00e5\3\2\2\2\u00e3\u00e5\5$\23\2\u00e4\u00df\3\2\2\2")
        buf.write("\u00e4\u00e3\3\2\2\2\u00e5#\3\2\2\2\u00e6\u00e7\b\23\1")
        buf.write("\2\u00e7\u00e8\5&\24\2\u00e8\u00ee\3\2\2\2\u00e9\u00ea")
        buf.write("\f\4\2\2\u00ea\u00eb\t\7\2\2\u00eb\u00ed\5&\24\2\u00ec")
        buf.write("\u00e9\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef%\3\2\2\2\u00f0\u00ee\3\2\2")
        buf.write("\2\u00f1\u00f2\b\24\1\2\u00f2\u00f3\5(\25\2\u00f3\u00f9")
        buf.write("\3\2\2\2\u00f4\u00f5\f\4\2\2\u00f5\u00f6\t\b\2\2\u00f6")
        buf.write("\u00f8\5(\25\2\u00f7\u00f4\3\2\2\2\u00f8\u00fb\3\2\2\2")
        buf.write("\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\'\3\2\2")
        buf.write("\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\b\25\1\2\u00fd\u00fe")
        buf.write("\5*\26\2\u00fe\u0104\3\2\2\2\u00ff\u0100\f\4\2\2\u0100")
        buf.write("\u0101\t\t\2\2\u0101\u0103\5*\26\2\u0102\u00ff\3\2\2\2")
        buf.write("\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3")
        buf.write("\2\2\2\u0105)\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108")
        buf.write("\7!\2\2\u0108\u010b\5*\26\2\u0109\u010b\5,\27\2\u010a")
        buf.write("\u0107\3\2\2\2\u010a\u0109\3\2\2\2\u010b+\3\2\2\2\u010c")
        buf.write("\u010d\7\35\2\2\u010d\u0110\5,\27\2\u010e\u0110\5.\30")
        buf.write("\2\u010f\u010c\3\2\2\2\u010f\u010e\3\2\2\2\u0110-\3\2")
        buf.write("\2\2\u0111\u0112\b\30\1\2\u0112\u0113\5\60\31\2\u0113")
        buf.write("\u0118\3\2\2\2\u0114\u0115\f\4\2\2\u0115\u0117\5<\37\2")
        buf.write("\u0116\u0114\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3")
        buf.write("\2\2\2\u0118\u0119\3\2\2\2\u0119/\3\2\2\2\u011a\u0118")
        buf.write("\3\2\2\2\u011b\u011c\b\31\1\2\u011c\u011d\5\62\32\2\u011d")
        buf.write("\u012f\3\2\2\2\u011e\u011f\f\6\2\2\u011f\u0120\7.\2\2")
        buf.write("\u0120\u0121\78\2\2\u0121\u0122\7/\2\2\u0122\u0123\5:")
        buf.write("\36\2\u0123\u0124\7\60\2\2\u0124\u012e\3\2\2\2\u0125\u0126")
        buf.write("\f\5\2\2\u0126\u0127\7.\2\2\u0127\u012e\78\2\2\u0128\u0129")
        buf.write("\f\4\2\2\u0129\u012a\7.\2\2\u012a\u012b\78\2\2\u012b\u012c")
        buf.write("\7/\2\2\u012c\u012e\7\60\2\2\u012d\u011e\3\2\2\2\u012d")
        buf.write("\u0125\3\2\2\2\u012d\u0128\3\2\2\2\u012e\u0131\3\2\2\2")
        buf.write("\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\61\3\2")
        buf.write("\2\2\u0131\u012f\3\2\2\2\u0132\u0133\b\32\1\2\u0133\u0134")
        buf.write("\5\64\33\2\u0134\u0146\3\2\2\2\u0135\u0136\f\6\2\2\u0136")
        buf.write("\u0137\7-\2\2\u0137\u0138\79\2\2\u0138\u0139\7/\2\2\u0139")
        buf.write("\u013a\5:\36\2\u013a\u013b\7\60\2\2\u013b\u0145\3\2\2")
        buf.write("\2\u013c\u013d\f\5\2\2\u013d\u013e\7-\2\2\u013e\u0145")
        buf.write("\79\2\2\u013f\u0140\f\4\2\2\u0140\u0141\7-\2\2\u0141\u0142")
        buf.write("\79\2\2\u0142\u0143\7/\2\2\u0143\u0145\7\60\2\2\u0144")
        buf.write("\u0135\3\2\2\2\u0144\u013c\3\2\2\2\u0144\u013f\3\2\2\2")
        buf.write("\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3")
        buf.write("\2\2\2\u0147\63\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a")
        buf.write("\7\32\2\2\u014a\u014b\78\2\2\u014b\u014c\7/\2\2\u014c")
        buf.write("\u014d\5:\36\2\u014d\u014e\7\60\2\2\u014e\u0155\3\2\2")
        buf.write("\2\u014f\u0150\7\32\2\2\u0150\u0151\78\2\2\u0151\u0152")
        buf.write("\7/\2\2\u0152\u0155\7\60\2\2\u0153\u0155\5\66\34\2\u0154")
        buf.write("\u0149\3\2\2\2\u0154\u014f\3\2\2\2\u0154\u0153\3\2\2\2")
        buf.write("\u0155\65\3\2\2\2\u0156\u0157\7/\2\2\u0157\u0158\5 \21")
        buf.write("\2\u0158\u0159\7\60\2\2\u0159\u015c\3\2\2\2\u015a\u015c")
        buf.write("\58\35\2\u015b\u0156\3\2\2\2\u015b\u015a\3\2\2\2\u015c")
        buf.write("\67\3\2\2\2\u015d\u0161\5b\62\2\u015e\u0161\78\2\2\u015f")
        buf.write("\u0161\79\2\2\u0160\u015d\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0160\u015f\3\2\2\2\u01619\3\2\2\2\u0162\u0163\5 \21")
        buf.write("\2\u0163\u0164\7\65\2\2\u0164\u0165\5:\36\2\u0165\u0168")
        buf.write("\3\2\2\2\u0166\u0168\5 \21\2\u0167\u0162\3\2\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0168;\3\2\2\2\u0169\u016a\7\61\2\2\u016a")
        buf.write("\u016b\5 \21\2\u016b\u016c\7\62\2\2\u016c\u016d\5<\37")
        buf.write("\2\u016d\u0173\3\2\2\2\u016e\u016f\7\61\2\2\u016f\u0170")
        buf.write("\5 \21\2\u0170\u0171\7\62\2\2\u0171\u0173\3\2\2\2\u0172")
        buf.write("\u0169\3\2\2\2\u0172\u016e\3\2\2\2\u0173=\3\2\2\2\u0174")
        buf.write("\u0175\7\63\2\2\u0175\u0176\5@!\2\u0176\u0177\7\64\2\2")
        buf.write("\u0177\u017b\3\2\2\2\u0178\u0179\7\63\2\2\u0179\u017b")
        buf.write("\7\64\2\2\u017a\u0174\3\2\2\2\u017a\u0178\3\2\2\2\u017b")
        buf.write("?\3\2\2\2\u017c\u017d\5B\"\2\u017d\u017e\5@!\2\u017e\u0181")
        buf.write("\3\2\2\2\u017f\u0181\5B\"\2\u0180\u017c\3\2\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181A\3\2\2\2\u0182\u018b\5D#\2\u0183")
        buf.write("\u018b\5F$\2\u0184\u018b\5H%\2\u0185\u018b\5P)\2\u0186")
        buf.write("\u018b\5T+\2\u0187\u018b\5V,\2\u0188\u018b\5X-\2\u0189")
        buf.write("\u018b\5Z.\2\u018a\u0182\3\2\2\2\u018a\u0183\3\2\2\2\u018a")
        buf.write("\u0184\3\2\2\2\u018a\u0185\3\2\2\2\u018a\u0186\3\2\2\2")
        buf.write("\u018a\u0187\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u0189\3")
        buf.write("\2\2\2\u018bC\3\2\2\2\u018c\u018d\t\2\2\2\u018d\u018e")
        buf.write("\5\26\f\2\u018e\u018f\7\67\2\2\u018f\u0190\5\32\16\2\u0190")
        buf.write("\u0191\7\66\2\2\u0191\u019b\3\2\2\2\u0192\u0193\t\2\2")
        buf.write("\2\u0193\u0194\5\26\f\2\u0194\u0195\7\67\2\2\u0195\u0196")
        buf.write("\5\32\16\2\u0196\u0197\7%\2\2\u0197\u0198\5:\36\2\u0198")
        buf.write("\u0199\7\66\2\2\u0199\u019b\3\2\2\2\u019a\u018c\3\2\2")
        buf.write("\2\u019a\u0192\3\2\2\2\u019bE\3\2\2\2\u019c\u019d\5.\30")
        buf.write("\2\u019d\u019e\7%\2\2\u019e\u019f\5 \21\2\u019f\u01a0")
        buf.write("\7\66\2\2\u01a0G\3\2\2\2\u01a1\u01a2\7\6\2\2\u01a2\u01a3")
        buf.write("\7/\2\2\u01a3\u01a4\5 \21\2\u01a4\u01a5\7\60\2\2\u01a5")
        buf.write("\u01a6\5> \2\u01a6\u01a7\5J&\2\u01a7\u01af\3\2\2\2\u01a8")
        buf.write("\u01a9\7\6\2\2\u01a9\u01aa\7/\2\2\u01aa\u01ab\5 \21\2")
        buf.write("\u01ab\u01ac\7\60\2\2\u01ac\u01ad\5> \2\u01ad\u01af\3")
        buf.write("\2\2\2\u01ae\u01a1\3\2\2\2\u01ae\u01a8\3\2\2\2\u01afI")
        buf.write("\3\2\2\2\u01b0\u01b1\5L\'\2\u01b1\u01b2\5J&\2\u01b2\u01b6")
        buf.write("\3\2\2\2\u01b3\u01b6\5L\'\2\u01b4\u01b6\5N(\2\u01b5\u01b0")
        buf.write("\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6")
        buf.write("K\3\2\2\2\u01b7\u01b8\7\7\2\2\u01b8\u01b9\7/\2\2\u01b9")
        buf.write("\u01ba\5 \21\2\u01ba\u01bb\7\60\2\2\u01bb\u01bc\5> \2")
        buf.write("\u01bcM\3\2\2\2\u01bd\u01be\7\b\2\2\u01be\u01bf\5> \2")
        buf.write("\u01bfO\3\2\2\2\u01c0\u01c1\7\t\2\2\u01c1\u01c2\7/\2\2")
        buf.write("\u01c2\u01c3\5R*\2\u01c3\u01c4\7\60\2\2\u01c4\u01c5\5")
        buf.write("> \2\u01c5Q\3\2\2\2\u01c6\u01c7\78\2\2\u01c7\u01c8\7\r")
        buf.write("\2\2\u01c8\u01c9\5 \21\2\u01c9\u01ca\7.\2\2\u01ca\u01cb")
        buf.write("\7.\2\2\u01cb\u01cc\5 \21\2\u01cc\u01d7\3\2\2\2\u01cd")
        buf.write("\u01ce\78\2\2\u01ce\u01cf\7\r\2\2\u01cf\u01d0\5 \21\2")
        buf.write("\u01d0\u01d1\7.\2\2\u01d1\u01d2\7.\2\2\u01d2\u01d3\5 ")
        buf.write("\21\2\u01d3\u01d4\7\33\2\2\u01d4\u01d5\5 \21\2\u01d5\u01d7")
        buf.write("\3\2\2\2\u01d6\u01c6\3\2\2\2\u01d6\u01cd\3\2\2\2\u01d7")
        buf.write("S\3\2\2\2\u01d8\u01d9\7\4\2\2\u01d9\u01da\7\66\2\2\u01da")
        buf.write("U\3\2\2\2\u01db\u01dc\7\5\2\2\u01dc\u01dd\7\66\2\2\u01dd")
        buf.write("W\3\2\2\2\u01de\u01df\7\22\2\2\u01df\u01e0\5 \21\2\u01e0")
        buf.write("\u01e1\7\66\2\2\u01e1\u01e5\3\2\2\2\u01e2\u01e3\7\22\2")
        buf.write("\2\u01e3\u01e5\7\66\2\2\u01e4\u01de\3\2\2\2\u01e4\u01e2")
        buf.write("\3\2\2\2\u01e5Y\3\2\2\2\u01e6\u01e7\5\\/\2\u01e7\u01e8")
        buf.write("\7\66\2\2\u01e8\u01ed\3\2\2\2\u01e9\u01ea\5^\60\2\u01ea")
        buf.write("\u01eb\7\66\2\2\u01eb\u01ed\3\2\2\2\u01ec\u01e6\3\2\2")
        buf.write("\2\u01ec\u01e9\3\2\2\2\u01ed[\3\2\2\2\u01ee\u01ef\5 \21")
        buf.write("\2\u01ef\u01f0\7.\2\2\u01f0\u01f1\78\2\2\u01f1\u01f2\7")
        buf.write("/\2\2\u01f2\u01f3\5:\36\2\u01f3\u01f4\7\60\2\2\u01f4\u0200")
        buf.write("\3\2\2\2\u01f5\u01f6\5 \21\2\u01f6\u01f7\7.\2\2\u01f7")
        buf.write("\u01f8\78\2\2\u01f8\u0200\3\2\2\2\u01f9\u01fa\5 \21\2")
        buf.write("\u01fa\u01fb\7.\2\2\u01fb\u01fc\78\2\2\u01fc\u01fd\7/")
        buf.write("\2\2\u01fd\u01fe\7\60\2\2\u01fe\u0200\3\2\2\2\u01ff\u01ee")
        buf.write("\3\2\2\2\u01ff\u01f5\3\2\2\2\u01ff\u01f9\3\2\2\2\u0200")
        buf.write("]\3\2\2\2\u0201\u0202\5 \21\2\u0202\u0203\7-\2\2\u0203")
        buf.write("\u0204\79\2\2\u0204\u0205\7/\2\2\u0205\u0206\5:\36\2\u0206")
        buf.write("\u0207\7\60\2\2\u0207\u0213\3\2\2\2\u0208\u0209\5 \21")
        buf.write("\2\u0209\u020a\7-\2\2\u020a\u020b\79\2\2\u020b\u0213\3")
        buf.write("\2\2\2\u020c\u020d\5 \21\2\u020d\u020e\7-\2\2\u020e\u020f")
        buf.write("\79\2\2\u020f\u0210\7/\2\2\u0210\u0211\7\60\2\2\u0211")
        buf.write("\u0213\3\2\2\2\u0212\u0201\3\2\2\2\u0212\u0208\3\2\2\2")
        buf.write("\u0212\u020c\3\2\2\2\u0213_\3\2\2\2\u0214\u0215\7\f\2")
        buf.write("\2\u0215\u0216\7/\2\2\u0216\u0217\5:\36\2\u0217\u0218")
        buf.write("\7\60\2\2\u0218a\3\2\2\2\u0219\u0221\7:\2\2\u021a\u0221")
        buf.write("\7;\2\2\u021b\u0221\7<\2\2\u021c\u0221\5`\61\2\u021d\u0221")
        buf.write("\5d\63\2\u021e\u0221\7\27\2\2\u021f\u0221\7\23\2\2\u0220")
        buf.write("\u0219\3\2\2\2\u0220\u021a\3\2\2\2\u0220\u021b\3\2\2\2")
        buf.write("\u0220\u021c\3\2\2\2\u0220\u021d\3\2\2\2\u0220\u021e\3")
        buf.write("\2\2\2\u0220\u021f\3\2\2\2\u0221c\3\2\2\2\u0222\u0223")
        buf.write("\t\n\2\2\u0223e\3\2\2\2+m}\u0081\u0088\u0098\u00a4\u00ab")
        buf.write("\u00b6\u00bc\u00c2\u00ca\u00d2\u00dd\u00e4\u00ee\u00f9")
        buf.write("\u0104\u010a\u010f\u0118\u012d\u012f\u0144\u0146\u0154")
        buf.write("\u015b\u0160\u0167\u0172\u017a\u0180\u018a\u019a\u01ae")
        buf.write("\u01b5\u01d6\u01e4\u01ec\u01ff\u0212\u0220")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Self'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'==.'", "'+.'", "'::'", "'.'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "';'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "CMT", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
                      "INTTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", 
                      "RET", "NULL", "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "NOT", "AND", "OR", "EQ", "ASSIGN", "NEQ", 
                      "LT", "LE", "GT", "GE", "ET", "ADDT", "STA", "DOT", 
                      "LB", "RB", "LS", "RS", "LP", "RP", "CM", "SM", "CL", 
                      "ID", "IDUSD", "INTLIT", "FLOATLIT", "STRINGLIT", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl_list = 1
    RULE_classdecl = 2
    RULE_members = 3
    RULE_attribute = 4
    RULE_method = 5
    RULE_param_list = 6
    RULE_params_decl = 7
    RULE_param_decl = 8
    RULE_idglist = 9
    RULE_idlist = 10
    RULE_idulist = 11
    RULE_mptype = 12
    RULE_class_type = 13
    RULE_array_type = 14
    RULE_exp = 15
    RULE_exp1 = 16
    RULE_exp2 = 17
    RULE_exp3 = 18
    RULE_exp4 = 19
    RULE_exp5 = 20
    RULE_exp6 = 21
    RULE_exp7 = 22
    RULE_exp8 = 23
    RULE_exp9 = 24
    RULE_exp10 = 25
    RULE_exp11 = 26
    RULE_exp12 = 27
    RULE_exp_list = 28
    RULE_index_list = 29
    RULE_block_stmt = 30
    RULE_stmt_list = 31
    RULE_stmt = 32
    RULE_decl_stmt = 33
    RULE_assign_stmt = 34
    RULE_if_stmt = 35
    RULE_else_list = 36
    RULE_elseif_stmt = 37
    RULE_else_stmt = 38
    RULE_loop_stmt = 39
    RULE_loop_condition = 40
    RULE_break_stmt = 41
    RULE_cont_stmt = 42
    RULE_return_stmt = 43
    RULE_method_stmt = 44
    RULE_instance = 45
    RULE_static = 46
    RULE_arraylit = 47
    RULE_literals = 48
    RULE_boolit = 49

    ruleNames =  [ "program", "classdecl_list", "classdecl", "members", 
                   "attribute", "method", "param_list", "params_decl", "param_decl", 
                   "idglist", "idlist", "idulist", "mptype", "class_type", 
                   "array_type", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", "exp11", 
                   "exp12", "exp_list", "index_list", "block_stmt", "stmt_list", 
                   "stmt", "decl_stmt", "assign_stmt", "if_stmt", "else_list", 
                   "elseif_stmt", "else_stmt", "loop_stmt", "loop_condition", 
                   "break_stmt", "cont_stmt", "return_stmt", "method_stmt", 
                   "instance", "static", "arraylit", "literals", "boolit" ]

    EOF = Token.EOF
    CMT=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    TRUE=8
    FALSE=9
    ARRAY=10
    IN=11
    INTTYPE=12
    FLOATTYPE=13
    BOOLTYPE=14
    STRINGTYPE=15
    RET=16
    NULL=17
    CLASS=18
    VAL=19
    VAR=20
    SELF=21
    CONSTRUCTOR=22
    DESTRUCTOR=23
    NEW=24
    BY=25
    ADD=26
    SUB=27
    MUL=28
    DIV=29
    MOD=30
    NOT=31
    AND=32
    OR=33
    EQ=34
    ASSIGN=35
    NEQ=36
    LT=37
    LE=38
    GT=39
    GE=40
    ET=41
    ADDT=42
    STA=43
    DOT=44
    LB=45
    RB=46
    LS=47
    RS=48
    LP=49
    RP=50
    CM=51
    SM=52
    CL=53
    ID=54
    IDUSD=55
    INTLIT=56
    FLOATLIT=57
    STRINGLIT=58
    WS=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl_list(self):
            return self.getTypedRuleContext(D96Parser.Classdecl_listContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.classdecl_list()
            self.state = 101
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Classdecl_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclContext,0)


        def classdecl_list(self):
            return self.getTypedRuleContext(D96Parser.Classdecl_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecl_list




    def classdecl_list(self):

        localctx = D96Parser.Classdecl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl_list)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.classdecl()
                self.state = 104
                self.classdecl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.classdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def members(self):
            return self.getTypedRuleContext(D96Parser.MembersContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classdecl




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(D96Parser.CLASS)
                self.state = 110
                self.match(D96Parser.ID)
                self.state = 111
                self.match(D96Parser.LP)
                self.state = 112
                self.members()
                self.state = 113
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(D96Parser.CLASS)
                self.state = 116
                self.match(D96Parser.ID)
                self.state = 117
                self.match(D96Parser.CL)
                self.state = 118
                self.match(D96Parser.ID)
                self.state = 119
                self.match(D96Parser.LP)
                self.state = 120
                self.members()
                self.state = 121
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def members(self):
            return self.getTypedRuleContext(D96Parser.MembersContext,0)


        def attribute(self):
            return self.getTypedRuleContext(D96Parser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_members




    def members(self):

        localctx = D96Parser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_members)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 125
                    self.attribute()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.IDUSD]:
                    self.state = 126
                    self.method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 129
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.attribute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.method()
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


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idglist(self):
            return self.getTypedRuleContext(D96Parser.IdglistContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute




    def attribute(self):

        localctx = D96Parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 137
                self.idglist()
                self.state = 138
                self.match(D96Parser.CL)
                self.state = 139
                self.mptype()
                self.state = 140
                self.match(D96Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self.idglist()
                self.state = 144
                self.match(D96Parser.CL)
                self.state = 145
                self.mptype()
                self.state = 146
                self.match(D96Parser.ASSIGN)
                self.state = 147
                self.exp_list()
                self.state = 148
                self.match(D96Parser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_list(self):
            return self.getTypedRuleContext(D96Parser.Param_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IDUSD(self):
            return self.getToken(D96Parser.IDUSD, 0)

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.IDUSD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 153
            self.param_list()
            self.state = 154
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def params_decl(self):
            return self.getTypedRuleContext(D96Parser.Params_declContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_param_list




    def param_list(self):

        localctx = D96Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param_list)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(D96Parser.LB)
                self.state = 157
                self.params_decl()
                self.state = 158
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(D96Parser.LB)
                self.state = 161
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self):
            return self.getTypedRuleContext(D96Parser.Param_declContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def params_decl(self):
            return self.getTypedRuleContext(D96Parser.Params_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_params_decl




    def params_decl(self):

        localctx = D96Parser.Params_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params_decl)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.param_decl()
                self.state = 165
                self.match(D96Parser.SM)
                self.state = 166
                self.params_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.param_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param_decl




    def param_decl(self):

        localctx = D96Parser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.idlist()
            self.state = 172
            self.match(D96Parser.CL)
            self.state = 173
            self.mptype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdglistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def idglist(self):
            return self.getTypedRuleContext(D96Parser.IdglistContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IDUSD(self):
            return self.getToken(D96Parser.IDUSD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idglist




    def idglist(self):

        localctx = D96Parser.IdglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idglist)
        self._la = 0 # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.IDUSD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.match(D96Parser.CM)
                self.state = 177
                self.idglist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(D96Parser.IDUSD)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idlist




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idlist)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(D96Parser.ID)
                self.state = 183
                self.match(D96Parser.CM)
                self.state = 184
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdulistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDUSD(self):
            return self.getToken(D96Parser.IDUSD, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def idulist(self):
            return self.getTypedRuleContext(D96Parser.IdulistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idulist




    def idulist(self):

        localctx = D96Parser.IdulistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_idulist)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(D96Parser.IDUSD)
                self.state = 189
                self.match(D96Parser.CM)
                self.state = 190
                self.idulist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(D96Parser.IDUSD)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(D96Parser.BOOLTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(D96Parser.STRINGTYPE, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mptype




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mptype)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(D96Parser.INTTYPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(D96Parser.FLOATTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.match(D96Parser.BOOLTYPE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.match(D96Parser.STRINGTYPE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                self.array_type()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 199
                self.class_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_type




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.exp10()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ARRAY)
            else:
                return self.getToken(D96Parser.ARRAY, i)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_type




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(D96Parser.ARRAY)
            self.state = 205
            self.match(D96Parser.LS)
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 206
                self.mptype()
                pass

            elif la_ == 2:
                self.state = 207
                self.match(D96Parser.ARRAY)
                pass


            self.state = 210
            self.match(D96Parser.CM)
            self.state = 211
            self.match(D96Parser.INTLIT)
            self.state = 212
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def ADDT(self):
            return self.getToken(D96Parser.ADDT, 0)

        def ET(self):
            return self.getToken(D96Parser.ET, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.exp1()
                self.state = 215
                _la = self._input.LA(1)
                if not(_la==D96Parser.ET or _la==D96Parser.ADDT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 216
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp2Context,i)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(D96Parser.NEQ, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LE(self):
            return self.getToken(D96Parser.LE, 0)

        def GE(self):
            return self.getToken(D96Parser.GE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1




    def exp1(self):

        localctx = D96Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.exp2(0)
                self.state = 222
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NEQ) | (1 << D96Parser.LT) | (1 << D96Parser.LE) | (1 << D96Parser.GT) | (1 << D96Parser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 231
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 232
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 233
                    self.exp3(0) 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 244
                    self.exp4(0) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 255
                    self.exp5() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp5)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(D96Parser.NOT)
                self.state = 262
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.SUB, D96Parser.LB, D96Parser.ID, D96Parser.IDUSD, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.exp6()
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


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp6)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(D96Parser.SUB)
                self.state = 267
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.ID, D96Parser.IDUSD, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.exp7(0)
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


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def index_list(self):
            return self.getTypedRuleContext(D96Parser.Index_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp7



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 274
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 275
                    self.index_list() 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp8



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 299
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 284
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 285
                        self.match(D96Parser.DOT)
                        self.state = 286
                        self.match(D96Parser.ID)
                        self.state = 287
                        self.match(D96Parser.LB)
                        self.state = 288
                        self.exp_list()
                        self.state = 289
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 291
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 292
                        self.match(D96Parser.DOT)
                        self.state = 293
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 294
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 295
                        self.match(D96Parser.DOT)
                        self.state = 296
                        self.match(D96Parser.ID)
                        self.state = 297
                        self.match(D96Parser.LB)
                        self.state = 298
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def STA(self):
            return self.getToken(D96Parser.STA, 0)

        def IDUSD(self):
            return self.getToken(D96Parser.IDUSD, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp9



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 322
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                        self.state = 307
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 308
                        self.match(D96Parser.STA)
                        self.state = 309
                        self.match(D96Parser.IDUSD)
                        self.state = 310
                        self.match(D96Parser.LB)
                        self.state = 311
                        self.exp_list()
                        self.state = 312
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                        self.state = 314
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 315
                        self.match(D96Parser.STA)
                        self.state = 316
                        self.match(D96Parser.IDUSD)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                        self.state = 317
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 318
                        self.match(D96Parser.STA)
                        self.state = 319
                        self.match(D96Parser.IDUSD)
                        self.state = 320
                        self.match(D96Parser.LB)
                        self.state = 321
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp11(self):
            return self.getTypedRuleContext(D96Parser.Exp11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp10)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(D96Parser.NEW)
                self.state = 328
                self.match(D96Parser.ID)
                self.state = 329
                self.match(D96Parser.LB)
                self.state = 330
                self.exp_list()
                self.state = 331
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(D96Parser.NEW)
                self.state = 334
                self.match(D96Parser.ID)
                self.state = 335
                self.match(D96Parser.LB)
                self.state = 336
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
                self.exp11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp12(self):
            return self.getTypedRuleContext(D96Parser.Exp12Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp11




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp11)
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(D96Parser.LB)
                self.state = 341
                self.exp()
                self.state = 342
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.ID, D96Parser.IDUSD, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.exp12()
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


    class Exp12Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IDUSD(self):
            return self.getToken(D96Parser.IDUSD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp12




    def exp12(self):

        localctx = D96Parser.Exp12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp12)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.literals()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.IDUSD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.match(D96Parser.IDUSD)
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


    class Exp_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_list




    def exp_list(self):

        localctx = D96Parser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp_list)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.exp()
                self.state = 353
                self.match(D96Parser.CM)
                self.state = 354
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def index_list(self):
            return self.getTypedRuleContext(D96Parser.Index_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_list




    def index_list(self):

        localctx = D96Parser.Index_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_index_list)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(D96Parser.LS)
                self.state = 360
                self.exp()
                self.state = 361
                self.match(D96Parser.RS)
                self.state = 362
                self.index_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.match(D96Parser.LS)
                self.state = 365
                self.exp()
                self.state = 366
                self.match(D96Parser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Stmt_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_block_stmt)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(D96Parser.LP)
                self.state = 371
                self.stmt_list()
                self.state = 372
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(D96Parser.LP)
                self.state = 375
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Stmt_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_list




    def stmt_list(self):

        localctx = D96Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stmt_list)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.stmt()
                self.state = 379
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_stmt(self):
            return self.getTypedRuleContext(D96Parser.Decl_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def loop_stmt(self):
            return self.getTypedRuleContext(D96Parser.Loop_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def cont_stmt(self):
            return self.getTypedRuleContext(D96Parser.Cont_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stmt)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.loop_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 388
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 389
                self.cont_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 390
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 391
                self.method_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_decl_stmt




    def decl_stmt(self):

        localctx = D96Parser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_decl_stmt)
        self._la = 0 # Token type
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 395
                self.idlist()
                self.state = 396
                self.match(D96Parser.CL)
                self.state = 397
                self.mptype()
                self.state = 398
                self.match(D96Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 401
                self.idlist()
                self.state = 402
                self.match(D96Parser.CL)
                self.state = 403
                self.mptype()
                self.state = 404
                self.match(D96Parser.ASSIGN)
                self.state = 405
                self.exp_list()
                self.state = 406
                self.match(D96Parser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.exp7(0)
            self.state = 411
            self.match(D96Parser.ASSIGN)
            self.state = 412
            self.exp()
            self.state = 413
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def else_list(self):
            return self.getTypedRuleContext(D96Parser.Else_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_stmt)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.match(D96Parser.IF)
                self.state = 416
                self.match(D96Parser.LB)
                self.state = 417
                self.exp()
                self.state = 418
                self.match(D96Parser.RB)
                self.state = 419
                self.block_stmt()
                self.state = 420
                self.else_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(D96Parser.IF)
                self.state = 423
                self.match(D96Parser.LB)
                self.state = 424
                self.exp()
                self.state = 425
                self.match(D96Parser.RB)
                self.state = 426
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,0)


        def else_list(self):
            return self.getTypedRuleContext(D96Parser.Else_listContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_list




    def else_list(self):

        localctx = D96Parser.Else_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_else_list)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.elseif_stmt()
                self.state = 431
                self.else_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.elseif_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 434
                self.else_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmt




    def elseif_stmt(self):

        localctx = D96Parser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(D96Parser.ELSEIF)
            self.state = 438
            self.match(D96Parser.LB)
            self.state = 439
            self.exp()
            self.state = 440
            self.match(D96Parser.RB)
            self.state = 441
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(D96Parser.ELSE)
            self.state = 444
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def loop_condition(self):
            return self.getTypedRuleContext(D96Parser.Loop_conditionContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_loop_stmt




    def loop_stmt(self):

        localctx = D96Parser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_loop_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(D96Parser.FOREACH)
            self.state = 447
            self.match(D96Parser.LB)
            self.state = 448
            self.loop_condition()
            self.state = 449
            self.match(D96Parser.RB)
            self.state = 450
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOT)
            else:
                return self.getToken(D96Parser.DOT, i)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_loop_condition




    def loop_condition(self):

        localctx = D96Parser.Loop_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_loop_condition)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(D96Parser.ID)
                self.state = 453
                self.match(D96Parser.IN)
                self.state = 454
                self.exp()
                self.state = 455
                self.match(D96Parser.DOT)
                self.state = 456
                self.match(D96Parser.DOT)
                self.state = 457
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.match(D96Parser.ID)
                self.state = 460
                self.match(D96Parser.IN)
                self.state = 461
                self.exp()
                self.state = 462
                self.match(D96Parser.DOT)
                self.state = 463
                self.match(D96Parser.DOT)
                self.state = 464
                self.exp()
                self.state = 465
                self.match(D96Parser.BY)
                self.state = 466
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(D96Parser.BREAK)
            self.state = 471
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_cont_stmt




    def cont_stmt(self):

        localctx = D96Parser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(D96Parser.CONTINUE)
            self.state = 474
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RET(self):
            return self.getToken(D96Parser.RET, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_return_stmt)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                self.match(D96Parser.RET)
                self.state = 477
                self.exp()
                self.state = 478
                self.match(D96Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.match(D96Parser.RET)
                self.state = 481
                self.match(D96Parser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance(self):
            return self.getTypedRuleContext(D96Parser.InstanceContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def static(self):
            return self.getTypedRuleContext(D96Parser.StaticContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_stmt




    def method_stmt(self):

        localctx = D96Parser.Method_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_method_stmt)
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.instance()
                self.state = 485
                self.match(D96Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.static()
                self.state = 488
                self.match(D96Parser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance




    def instance(self):

        localctx = D96Parser.InstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_instance)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.exp()
                self.state = 493
                self.match(D96Parser.DOT)
                self.state = 494
                self.match(D96Parser.ID)
                self.state = 495
                self.match(D96Parser.LB)
                self.state = 496
                self.exp_list()
                self.state = 497
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.exp()
                self.state = 500
                self.match(D96Parser.DOT)
                self.state = 501
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 503
                self.exp()
                self.state = 504
                self.match(D96Parser.DOT)
                self.state = 505
                self.match(D96Parser.ID)
                self.state = 506
                self.match(D96Parser.LB)
                self.state = 507
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def STA(self):
            return self.getToken(D96Parser.STA, 0)

        def IDUSD(self):
            return self.getToken(D96Parser.IDUSD, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static




    def static(self):

        localctx = D96Parser.StaticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_static)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.exp()
                self.state = 512
                self.match(D96Parser.STA)
                self.state = 513
                self.match(D96Parser.IDUSD)
                self.state = 514
                self.match(D96Parser.LB)
                self.state = 515
                self.exp_list()
                self.state = 516
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.exp()
                self.state = 519
                self.match(D96Parser.STA)
                self.state = 520
                self.match(D96Parser.IDUSD)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 522
                self.exp()
                self.state = 523
                self.match(D96Parser.STA)
                self.state = 524
                self.match(D96Parser.IDUSD)
                self.state = 525
                self.match(D96Parser.LB)
                self.state = 526
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arraylit




    def arraylit(self):

        localctx = D96Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(D96Parser.ARRAY)
            self.state = 531
            self.match(D96Parser.LB)
            self.state = 532
            self.exp_list()
            self.state = 533
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(D96Parser.ArraylitContext,0)


        def boolit(self):
            return self.getTypedRuleContext(D96Parser.BoolitContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literals




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literals)
        try:
            self.state = 542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 537
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 538
                self.arraylit()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 539
                self.boolit()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 6)
                self.state = 540
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 541
                self.match(D96Parser.NULL)
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


    class BoolitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_boolit




    def boolit(self):

        localctx = D96Parser.BoolitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUE or _la==D96Parser.FALSE):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.exp2_sempred
        self._predicates[18] = self.exp3_sempred
        self._predicates[19] = self.exp4_sempred
        self._predicates[22] = self.exp7_sempred
        self._predicates[23] = self.exp8_sempred
        self._predicates[24] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




