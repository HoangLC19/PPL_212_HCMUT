# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\u0224\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3j\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4z\n\4\3\5\3\5\5\5~\n\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u0085\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6\u0095\n\6\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\b\u00a1\n\b\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t\u00a8\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00b3\n\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00bb\n\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00c9\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00d0\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00d8\n\20\f\20")
        buf.write("\16\20\u00db\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21")
        buf.write("\u00e3\n\21\f\21\16\21\u00e6\13\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\7\22\u00ee\n\22\f\22\16\22\u00f1\13\22\3\23")
        buf.write("\3\23\3\23\5\23\u00f6\n\23\3\24\3\24\3\24\5\24\u00fb\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\7\25\u0102\n\25\f\25\16\25")
        buf.write("\u0105\13\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26")
        buf.write("\u0119\n\26\f\26\16\26\u011c\13\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u0127\n\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\7\27\u0131\n\27\f\27\16\27")
        buf.write("\u0134\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u0141\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0148\n\31\3\32\3\32\3\32\3\32\5\32\u014e\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u0155\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0160\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\5\35\u0168\n\35\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u016e\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\5\37\u0178\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \5 \u0188\n \3!\3!\3!\3!\5!\u018e\n!\3\"")
        buf.write("\3\"\5\"\u0192\n\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\5#\u01b4\n#\3$\3$\3$\3$\5$\u01ba\n$\3%\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01db\n(\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\5,\u01ed\n")
        buf.write(",\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5")
        buf.write("-\u0200\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\5.\u0213\n.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\5\60\u0220\n\60\3\61\3\61\3\61\2\b\36 \"(*")
        buf.write(",\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\13\3\2\25\26\4\2\30")
        buf.write("\3189\3\289\3\2+,\4\2$$&*\3\2\"#\3\2\34\35\3\2\36 \3\2")
        buf.write("\n\13\2\u0234\2b\3\2\2\2\4i\3\2\2\2\6y\3\2\2\2\b\u0084")
        buf.write("\3\2\2\2\n\u0094\3\2\2\2\f\u0096\3\2\2\2\16\u00a0\3\2")
        buf.write("\2\2\20\u00a7\3\2\2\2\22\u00a9\3\2\2\2\24\u00b2\3\2\2")
        buf.write("\2\26\u00ba\3\2\2\2\30\u00bc\3\2\2\2\32\u00c8\3\2\2\2")
        buf.write("\34\u00cf\3\2\2\2\36\u00d1\3\2\2\2 \u00dc\3\2\2\2\"\u00e7")
        buf.write("\3\2\2\2$\u00f5\3\2\2\2&\u00fa\3\2\2\2(\u00fc\3\2\2\2")
        buf.write("*\u0106\3\2\2\2,\u0126\3\2\2\2.\u0140\3\2\2\2\60\u0147")
        buf.write("\3\2\2\2\62\u014d\3\2\2\2\64\u0154\3\2\2\2\66\u015f\3")
        buf.write("\2\2\28\u0167\3\2\2\2:\u016d\3\2\2\2<\u0177\3\2\2\2>\u0187")
        buf.write("\3\2\2\2@\u018d\3\2\2\2B\u0191\3\2\2\2D\u01b3\3\2\2\2")
        buf.write("F\u01b9\3\2\2\2H\u01bb\3\2\2\2J\u01c1\3\2\2\2L\u01c4\3")
        buf.write("\2\2\2N\u01da\3\2\2\2P\u01dc\3\2\2\2R\u01df\3\2\2\2T\u01e2")
        buf.write("\3\2\2\2V\u01ec\3\2\2\2X\u01ff\3\2\2\2Z\u0212\3\2\2\2")
        buf.write("\\\u0214\3\2\2\2^\u021f\3\2\2\2`\u0221\3\2\2\2bc\5\4\3")
        buf.write("\2cd\7\2\2\3d\3\3\2\2\2ef\5\6\4\2fg\5\4\3\2gj\3\2\2\2")
        buf.write("hj\5\6\4\2ie\3\2\2\2ih\3\2\2\2j\5\3\2\2\2kl\7\24\2\2l")
        buf.write("m\78\2\2mn\7\63\2\2no\5\b\5\2op\7\64\2\2pz\3\2\2\2qr\7")
        buf.write("\24\2\2rs\78\2\2st\7\67\2\2tu\78\2\2uv\7\63\2\2vw\5\b")
        buf.write("\5\2wx\7\64\2\2xz\3\2\2\2yk\3\2\2\2yq\3\2\2\2z\7\3\2\2")
        buf.write("\2{~\5\n\6\2|~\5\f\7\2}{\3\2\2\2}|\3\2\2\2~\177\3\2\2")
        buf.write("\2\177\u0080\5\b\5\2\u0080\u0085\3\2\2\2\u0081\u0085\5")
        buf.write("\n\6\2\u0082\u0085\5\f\7\2\u0083\u0085\3\2\2\2\u0084}")
        buf.write("\3\2\2\2\u0084\u0081\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\t\3\2\2\2\u0086\u0087\t\2\2\2\u0087")
        buf.write("\u0088\5\24\13\2\u0088\u0089\7\67\2\2\u0089\u008a\5\26")
        buf.write("\f\2\u008a\u008b\7\66\2\2\u008b\u0095\3\2\2\2\u008c\u008d")
        buf.write("\t\2\2\2\u008d\u008e\5\24\13\2\u008e\u008f\7\67\2\2\u008f")
        buf.write("\u0090\5\26\f\2\u0090\u0091\7%\2\2\u0091\u0092\5\64\33")
        buf.write("\2\u0092\u0093\7\66\2\2\u0093\u0095\3\2\2\2\u0094\u0086")
        buf.write("\3\2\2\2\u0094\u008c\3\2\2\2\u0095\13\3\2\2\2\u0096\u0097")
        buf.write("\t\3\2\2\u0097\u0098\5\16\b\2\u0098\u0099\58\35\2\u0099")
        buf.write("\r\3\2\2\2\u009a\u009b\7/\2\2\u009b\u009c\5\20\t\2\u009c")
        buf.write("\u009d\7\60\2\2\u009d\u00a1\3\2\2\2\u009e\u009f\7/\2\2")
        buf.write("\u009f\u00a1\7\60\2\2\u00a0\u009a\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a1\17\3\2\2\2\u00a2\u00a3\5\22\n\2\u00a3\u00a4")
        buf.write("\7\66\2\2\u00a4\u00a5\5\20\t\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write("\u00a8\5\22\n\2\u00a7\u00a2\3\2\2\2\u00a7\u00a6\3\2\2")
        buf.write("\2\u00a8\21\3\2\2\2\u00a9\u00aa\5\24\13\2\u00aa\u00ab")
        buf.write("\7\67\2\2\u00ab\u00ac\5\26\f\2\u00ac\23\3\2\2\2\u00ad")
        buf.write("\u00ae\t\4\2\2\u00ae\u00af\7\65\2\2\u00af\u00b3\5\24\13")
        buf.write("\2\u00b0\u00b3\78\2\2\u00b1\u00b3\79\2\2\u00b2\u00ad\3")
        buf.write("\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\25")
        buf.write("\3\2\2\2\u00b4\u00bb\7\16\2\2\u00b5\u00bb\7\17\2\2\u00b6")
        buf.write("\u00bb\7\21\2\2\u00b7\u00bb\5\30\r\2\u00b8\u00bb\7\f\2")
        buf.write("\2\u00b9\u00bb\7\20\2\2\u00ba\u00b4\3\2\2\2\u00ba\u00b5")
        buf.write("\3\2\2\2\u00ba\u00b6\3\2\2\2\u00ba\u00b7\3\2\2\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\27\3\2\2\2\u00bc")
        buf.write("\u00bd\7\f\2\2\u00bd\u00be\7\61\2\2\u00be\u00bf\5\26\f")
        buf.write("\2\u00bf\u00c0\7\65\2\2\u00c0\u00c1\7:\2\2\u00c1\u00c2")
        buf.write("\7\62\2\2\u00c2\31\3\2\2\2\u00c3\u00c4\5\34\17\2\u00c4")
        buf.write("\u00c5\t\5\2\2\u00c5\u00c6\5\34\17\2\u00c6\u00c9\3\2\2")
        buf.write("\2\u00c7\u00c9\5\34\17\2\u00c8\u00c3\3\2\2\2\u00c8\u00c7")
        buf.write("\3\2\2\2\u00c9\33\3\2\2\2\u00ca\u00cb\5\36\20\2\u00cb")
        buf.write("\u00cc\t\6\2\2\u00cc\u00cd\5\36\20\2\u00cd\u00d0\3\2\2")
        buf.write("\2\u00ce\u00d0\5\36\20\2\u00cf\u00ca\3\2\2\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00d0\35\3\2\2\2\u00d1\u00d2\b\20\1\2\u00d2\u00d3")
        buf.write("\5 \21\2\u00d3\u00d9\3\2\2\2\u00d4\u00d5\f\4\2\2\u00d5")
        buf.write("\u00d6\t\7\2\2\u00d6\u00d8\5 \21\2\u00d7\u00d4\3\2\2\2")
        buf.write("\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da\37\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd")
        buf.write("\b\21\1\2\u00dd\u00de\5\"\22\2\u00de\u00e4\3\2\2\2\u00df")
        buf.write("\u00e0\f\4\2\2\u00e0\u00e1\t\b\2\2\u00e1\u00e3\5\"\22")
        buf.write("\2\u00e2\u00df\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5!\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e7\u00e8\b\22\1\2\u00e8\u00e9\5$\23\2\u00e9")
        buf.write("\u00ef\3\2\2\2\u00ea\u00eb\f\4\2\2\u00eb\u00ec\t\t\2\2")
        buf.write("\u00ec\u00ee\5$\23\2\u00ed\u00ea\3\2\2\2\u00ee\u00f1\3")
        buf.write("\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0#")
        buf.write("\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7!\2\2\u00f3")
        buf.write("\u00f6\5$\23\2\u00f4\u00f6\5&\24\2\u00f5\u00f2\3\2\2\2")
        buf.write("\u00f5\u00f4\3\2\2\2\u00f6%\3\2\2\2\u00f7\u00f8\7\35\2")
        buf.write("\2\u00f8\u00fb\5&\24\2\u00f9\u00fb\5(\25\2\u00fa\u00f7")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\'\3\2\2\2\u00fc\u00fd")
        buf.write("\b\25\1\2\u00fd\u00fe\5*\26\2\u00fe\u0103\3\2\2\2\u00ff")
        buf.write("\u0100\f\4\2\2\u0100\u0102\5\66\34\2\u0101\u00ff\3\2\2")
        buf.write("\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104)\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107")
        buf.write("\b\26\1\2\u0107\u0108\5,\27\2\u0108\u011a\3\2\2\2\u0109")
        buf.write("\u010a\f\6\2\2\u010a\u010b\7.\2\2\u010b\u010c\78\2\2\u010c")
        buf.write("\u010d\7/\2\2\u010d\u010e\5\64\33\2\u010e\u010f\7\60\2")
        buf.write("\2\u010f\u0119\3\2\2\2\u0110\u0111\f\5\2\2\u0111\u0112")
        buf.write("\7.\2\2\u0112\u0119\78\2\2\u0113\u0114\f\4\2\2\u0114\u0115")
        buf.write("\7.\2\2\u0115\u0116\78\2\2\u0116\u0117\7/\2\2\u0117\u0119")
        buf.write("\7\60\2\2\u0118\u0109\3\2\2\2\u0118\u0110\3\2\2\2\u0118")
        buf.write("\u0113\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b+\3\2\2\2\u011c\u011a\3\2\2")
        buf.write("\2\u011d\u011e\b\27\1\2\u011e\u011f\5.\30\2\u011f\u0120")
        buf.write("\7-\2\2\u0120\u0121\79\2\2\u0121\u0122\7/\2\2\u0122\u0123")
        buf.write("\5\64\33\2\u0123\u0124\7\60\2\2\u0124\u0127\3\2\2\2\u0125")
        buf.write("\u0127\5.\30\2\u0126\u011d\3\2\2\2\u0126\u0125\3\2\2\2")
        buf.write("\u0127\u0132\3\2\2\2\u0128\u0129\f\5\2\2\u0129\u012a\7")
        buf.write("-\2\2\u012a\u0131\79\2\2\u012b\u012c\f\4\2\2\u012c\u012d")
        buf.write("\7-\2\2\u012d\u012e\79\2\2\u012e\u012f\7/\2\2\u012f\u0131")
        buf.write("\7\60\2\2\u0130\u0128\3\2\2\2\u0130\u012b\3\2\2\2\u0131")
        buf.write("\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133-\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136\7\32\2")
        buf.write("\2\u0136\u0137\78\2\2\u0137\u0138\7/\2\2\u0138\u0139\5")
        buf.write("\64\33\2\u0139\u013a\7\60\2\2\u013a\u0141\3\2\2\2\u013b")
        buf.write("\u013c\7\32\2\2\u013c\u013d\78\2\2\u013d\u013e\7/\2\2")
        buf.write("\u013e\u0141\7\60\2\2\u013f\u0141\5\60\31\2\u0140\u0135")
        buf.write("\3\2\2\2\u0140\u013b\3\2\2\2\u0140\u013f\3\2\2\2\u0141")
        buf.write("/\3\2\2\2\u0142\u0143\7/\2\2\u0143\u0144\5\32\16\2\u0144")
        buf.write("\u0145\7\60\2\2\u0145\u0148\3\2\2\2\u0146\u0148\5\62\32")
        buf.write("\2\u0147\u0142\3\2\2\2\u0147\u0146\3\2\2\2\u0148\61\3")
        buf.write("\2\2\2\u0149\u014e\5^\60\2\u014a\u014e\78\2\2\u014b\u014e")
        buf.write("\79\2\2\u014c\u014e\7\27\2\2\u014d\u0149\3\2\2\2\u014d")
        buf.write("\u014a\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e\63\3\2\2\2\u014f\u0150\5\32\16\2\u0150\u0151\7")
        buf.write("\65\2\2\u0151\u0152\5\64\33\2\u0152\u0155\3\2\2\2\u0153")
        buf.write("\u0155\5\32\16\2\u0154\u014f\3\2\2\2\u0154\u0153\3\2\2")
        buf.write("\2\u0155\65\3\2\2\2\u0156\u0157\7\61\2\2\u0157\u0158\5")
        buf.write("\32\16\2\u0158\u0159\7\62\2\2\u0159\u015a\5\66\34\2\u015a")
        buf.write("\u0160\3\2\2\2\u015b\u015c\7\61\2\2\u015c\u015d\5\32\16")
        buf.write("\2\u015d\u015e\7\62\2\2\u015e\u0160\3\2\2\2\u015f\u0156")
        buf.write("\3\2\2\2\u015f\u015b\3\2\2\2\u0160\67\3\2\2\2\u0161\u0162")
        buf.write("\7\63\2\2\u0162\u0163\5:\36\2\u0163\u0164\7\64\2\2\u0164")
        buf.write("\u0168\3\2\2\2\u0165\u0166\7\63\2\2\u0166\u0168\7\64\2")
        buf.write("\2\u0167\u0161\3\2\2\2\u0167\u0165\3\2\2\2\u01689\3\2")
        buf.write("\2\2\u0169\u016a\5<\37\2\u016a\u016b\5:\36\2\u016b\u016e")
        buf.write("\3\2\2\2\u016c\u016e\5<\37\2\u016d\u0169\3\2\2\2\u016d")
        buf.write("\u016c\3\2\2\2\u016e;\3\2\2\2\u016f\u0178\5> \2\u0170")
        buf.write("\u0178\5B\"\2\u0171\u0178\5D#\2\u0172\u0178\5L\'\2\u0173")
        buf.write("\u0178\5P)\2\u0174\u0178\5R*\2\u0175\u0178\5T+\2\u0176")
        buf.write("\u0178\5V,\2\u0177\u016f\3\2\2\2\u0177\u0170\3\2\2\2\u0177")
        buf.write("\u0171\3\2\2\2\u0177\u0172\3\2\2\2\u0177\u0173\3\2\2\2")
        buf.write("\u0177\u0174\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0176\3")
        buf.write("\2\2\2\u0178=\3\2\2\2\u0179\u017a\t\2\2\2\u017a\u017b")
        buf.write("\5@!\2\u017b\u017c\7\67\2\2\u017c\u017d\5\26\f\2\u017d")
        buf.write("\u017e\7\66\2\2\u017e\u0188\3\2\2\2\u017f\u0180\t\2\2")
        buf.write("\2\u0180\u0181\5@!\2\u0181\u0182\7\67\2\2\u0182\u0183")
        buf.write("\5\26\f\2\u0183\u0184\7%\2\2\u0184\u0185\5\64\33\2\u0185")
        buf.write("\u0186\7\66\2\2\u0186\u0188\3\2\2\2\u0187\u0179\3\2\2")
        buf.write("\2\u0187\u017f\3\2\2\2\u0188?\3\2\2\2\u0189\u018a\78\2")
        buf.write("\2\u018a\u018b\7\65\2\2\u018b\u018e\5@!\2\u018c\u018e")
        buf.write("\78\2\2\u018d\u0189\3\2\2\2\u018d\u018c\3\2\2\2\u018e")
        buf.write("A\3\2\2\2\u018f\u0192\5(\25\2\u0190\u0192\5^\60\2\u0191")
        buf.write("\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193\u0194\7%\2\2\u0194\u0195\5\32\16\2\u0195\u0196")
        buf.write("\7\66\2\2\u0196C\3\2\2\2\u0197\u0198\7\6\2\2\u0198\u0199")
        buf.write("\7/\2\2\u0199\u019a\5\32\16\2\u019a\u019b\7\60\2\2\u019b")
        buf.write("\u019c\58\35\2\u019c\u019d\5F$\2\u019d\u019e\5J&\2\u019e")
        buf.write("\u01b4\3\2\2\2\u019f\u01a0\7\6\2\2\u01a0\u01a1\7/\2\2")
        buf.write("\u01a1\u01a2\5\32\16\2\u01a2\u01a3\7\60\2\2\u01a3\u01a4")
        buf.write("\58\35\2\u01a4\u01a5\5F$\2\u01a5\u01b4\3\2\2\2\u01a6\u01a7")
        buf.write("\7\6\2\2\u01a7\u01a8\7/\2\2\u01a8\u01a9\5\32\16\2\u01a9")
        buf.write("\u01aa\7\60\2\2\u01aa\u01ab\58\35\2\u01ab\u01ac\5J&\2")
        buf.write("\u01ac\u01b4\3\2\2\2\u01ad\u01ae\7\6\2\2\u01ae\u01af\7")
        buf.write("/\2\2\u01af\u01b0\5\32\16\2\u01b0\u01b1\7\60\2\2\u01b1")
        buf.write("\u01b2\58\35\2\u01b2\u01b4\3\2\2\2\u01b3\u0197\3\2\2\2")
        buf.write("\u01b3\u019f\3\2\2\2\u01b3\u01a6\3\2\2\2\u01b3\u01ad\3")
        buf.write("\2\2\2\u01b4E\3\2\2\2\u01b5\u01b6\5H%\2\u01b6\u01b7\5")
        buf.write("F$\2\u01b7\u01ba\3\2\2\2\u01b8\u01ba\5H%\2\u01b9\u01b5")
        buf.write("\3\2\2\2\u01b9\u01b8\3\2\2\2\u01baG\3\2\2\2\u01bb\u01bc")
        buf.write("\7\7\2\2\u01bc\u01bd\7/\2\2\u01bd\u01be\5\32\16\2\u01be")
        buf.write("\u01bf\7\60\2\2\u01bf\u01c0\58\35\2\u01c0I\3\2\2\2\u01c1")
        buf.write("\u01c2\7\b\2\2\u01c2\u01c3\58\35\2\u01c3K\3\2\2\2\u01c4")
        buf.write("\u01c5\7\t\2\2\u01c5\u01c6\7/\2\2\u01c6\u01c7\5N(\2\u01c7")
        buf.write("\u01c8\7\60\2\2\u01c8\u01c9\58\35\2\u01c9M\3\2\2\2\u01ca")
        buf.write("\u01cb\5\32\16\2\u01cb\u01cc\7\r\2\2\u01cc\u01cd\5\32")
        buf.write("\16\2\u01cd\u01ce\7.\2\2\u01ce\u01cf\7.\2\2\u01cf\u01d0")
        buf.write("\5\32\16\2\u01d0\u01db\3\2\2\2\u01d1\u01d2\5\32\16\2\u01d2")
        buf.write("\u01d3\7\r\2\2\u01d3\u01d4\5\32\16\2\u01d4\u01d5\7.\2")
        buf.write("\2\u01d5\u01d6\7.\2\2\u01d6\u01d7\5\32\16\2\u01d7\u01d8")
        buf.write("\7\33\2\2\u01d8\u01d9\5\32\16\2\u01d9\u01db\3\2\2\2\u01da")
        buf.write("\u01ca\3\2\2\2\u01da\u01d1\3\2\2\2\u01dbO\3\2\2\2\u01dc")
        buf.write("\u01dd\7\4\2\2\u01dd\u01de\7\66\2\2\u01deQ\3\2\2\2\u01df")
        buf.write("\u01e0\7\5\2\2\u01e0\u01e1\7\66\2\2\u01e1S\3\2\2\2\u01e2")
        buf.write("\u01e3\7\22\2\2\u01e3\u01e4\5\32\16\2\u01e4\u01e5\7\66")
        buf.write("\2\2\u01e5U\3\2\2\2\u01e6\u01e7\5X-\2\u01e7\u01e8\7\66")
        buf.write("\2\2\u01e8\u01ed\3\2\2\2\u01e9\u01ea\5Z.\2\u01ea\u01eb")
        buf.write("\7\66\2\2\u01eb\u01ed\3\2\2\2\u01ec\u01e6\3\2\2\2\u01ec")
        buf.write("\u01e9\3\2\2\2\u01edW\3\2\2\2\u01ee\u01ef\5\32\16\2\u01ef")
        buf.write("\u01f0\7.\2\2\u01f0\u01f1\78\2\2\u01f1\u01f2\7/\2\2\u01f2")
        buf.write("\u01f3\5\64\33\2\u01f3\u01f4\7\60\2\2\u01f4\u0200\3\2")
        buf.write("\2\2\u01f5\u01f6\5\32\16\2\u01f6\u01f7\7.\2\2\u01f7\u01f8")
        buf.write("\78\2\2\u01f8\u0200\3\2\2\2\u01f9\u01fa\5\32\16\2\u01fa")
        buf.write("\u01fb\7.\2\2\u01fb\u01fc\78\2\2\u01fc\u01fd\7/\2\2\u01fd")
        buf.write("\u01fe\7\60\2\2\u01fe\u0200\3\2\2\2\u01ff\u01ee\3\2\2")
        buf.write("\2\u01ff\u01f5\3\2\2\2\u01ff\u01f9\3\2\2\2\u0200Y\3\2")
        buf.write("\2\2\u0201\u0202\5\32\16\2\u0202\u0203\7-\2\2\u0203\u0204")
        buf.write("\79\2\2\u0204\u0205\7/\2\2\u0205\u0206\5\64\33\2\u0206")
        buf.write("\u0207\7\60\2\2\u0207\u0213\3\2\2\2\u0208\u0209\5\32\16")
        buf.write("\2\u0209\u020a\7-\2\2\u020a\u020b\79\2\2\u020b\u0213\3")
        buf.write("\2\2\2\u020c\u020d\5\32\16\2\u020d\u020e\7-\2\2\u020e")
        buf.write("\u020f\79\2\2\u020f\u0210\7/\2\2\u0210\u0211\7\60\2\2")
        buf.write("\u0211\u0213\3\2\2\2\u0212\u0201\3\2\2\2\u0212\u0208\3")
        buf.write("\2\2\2\u0212\u020c\3\2\2\2\u0213[\3\2\2\2\u0214\u0215")
        buf.write("\7\f\2\2\u0215\u0216\7/\2\2\u0216\u0217\5\64\33\2\u0217")
        buf.write("\u0218\7\60\2\2\u0218]\3\2\2\2\u0219\u0220\7:\2\2\u021a")
        buf.write("\u0220\7;\2\2\u021b\u0220\7<\2\2\u021c\u0220\5\\/\2\u021d")
        buf.write("\u0220\5`\61\2\u021e\u0220\7\27\2\2\u021f\u0219\3\2\2")
        buf.write("\2\u021f\u021a\3\2\2\2\u021f\u021b\3\2\2\2\u021f\u021c")
        buf.write("\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u021e\3\2\2\2\u0220")
        buf.write("_\3\2\2\2\u0221\u0222\t\n\2\2\u0222a\3\2\2\2*iy}\u0084")
        buf.write("\u0094\u00a0\u00a7\u00b2\u00ba\u00c8\u00cf\u00d9\u00e4")
        buf.write("\u00ef\u00f5\u00fa\u0103\u0118\u011a\u0126\u0130\u0132")
        buf.write("\u0140\u0147\u014d\u0154\u015f\u0167\u016d\u0177\u0187")
        buf.write("\u018d\u0191\u01b3\u01b9\u01da\u01ec\u01ff\u0212\u021f")
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
    RULE_mptype = 10
    RULE_array_type = 11
    RULE_exp = 12
    RULE_exp1 = 13
    RULE_exp2 = 14
    RULE_exp3 = 15
    RULE_exp4 = 16
    RULE_exp5 = 17
    RULE_exp6 = 18
    RULE_exp7 = 19
    RULE_exp8 = 20
    RULE_exp9 = 21
    RULE_exp10 = 22
    RULE_exp11 = 23
    RULE_exp12 = 24
    RULE_exp_list = 25
    RULE_index_list = 26
    RULE_block_stmt = 27
    RULE_stmt_list = 28
    RULE_stmt = 29
    RULE_decl_stmt = 30
    RULE_idlist = 31
    RULE_assign_stmt = 32
    RULE_if_stmt = 33
    RULE_elseif_list = 34
    RULE_elseif_stmt = 35
    RULE_else_stmt = 36
    RULE_loop_stmt = 37
    RULE_loop_condition = 38
    RULE_break_stmt = 39
    RULE_cont_stmt = 40
    RULE_return_stmt = 41
    RULE_method_stmt = 42
    RULE_instance = 43
    RULE_static = 44
    RULE_arraylit = 45
    RULE_literals = 46
    RULE_boolit = 47

    ruleNames =  [ "program", "classdecl_list", "classdecl", "members", 
                   "attribute", "method", "param_list", "params_decl", "param_decl", 
                   "idglist", "mptype", "array_type", "exp", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", 
                   "exp10", "exp11", "exp12", "exp_list", "index_list", 
                   "block_stmt", "stmt_list", "stmt", "decl_stmt", "idlist", 
                   "assign_stmt", "if_stmt", "elseif_list", "elseif_stmt", 
                   "else_stmt", "loop_stmt", "loop_condition", "break_stmt", 
                   "cont_stmt", "return_stmt", "method_stmt", "instance", 
                   "static", "arraylit", "literals", "boolit" ]

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
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl_list(self):
            return self.getTypedRuleContext(D96Parser.Classdecl_listContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.classdecl_list()
            self.state = 97
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Classdecl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclContext,0)


        def classdecl_list(self):
            return self.getTypedRuleContext(D96Parser.Classdecl_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl_list" ):
                return visitor.visitClassdecl_list(self)
            else:
                return visitor.visitChildren(self)




    def classdecl_list(self):

        localctx = D96Parser.Classdecl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl_list)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.classdecl()
                self.state = 100
                self.classdecl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(D96Parser.CLASS)
                self.state = 106
                self.match(D96Parser.ID)
                self.state = 107
                self.match(D96Parser.LP)
                self.state = 108
                self.members()
                self.state = 109
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(D96Parser.CLASS)
                self.state = 112
                self.match(D96Parser.ID)
                self.state = 113
                self.match(D96Parser.CL)
                self.state = 114
                self.match(D96Parser.ID)
                self.state = 115
                self.match(D96Parser.LP)
                self.state = 116
                self.members()
                self.state = 117
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = D96Parser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_members)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 121
                    self.attribute()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.IDUSD]:
                    self.state = 122
                    self.method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 125
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.attribute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = D96Parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.idglist()
                self.state = 134
                self.match(D96Parser.CL)
                self.state = 135
                self.mptype()
                self.state = 136
                self.match(D96Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self.idglist()
                self.state = 140
                self.match(D96Parser.CL)
                self.state = 141
                self.mptype()
                self.state = 142
                self.match(D96Parser.ASSIGN)
                self.state = 143
                self.exp_list()
                self.state = 144
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.IDUSD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 149
            self.param_list()
            self.state = 150
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = D96Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param_list)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(D96Parser.LB)
                self.state = 153
                self.params_decl()
                self.state = 154
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(D96Parser.LB)
                self.state = 157
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_decl" ):
                return visitor.visitParams_decl(self)
            else:
                return visitor.visitChildren(self)




    def params_decl(self):

        localctx = D96Parser.Params_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params_decl)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.param_decl()
                self.state = 161
                self.match(D96Parser.SM)
                self.state = 162
                self.params_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idglist(self):
            return self.getTypedRuleContext(D96Parser.IdglistContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = D96Parser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.idglist()
            self.state = 168
            self.match(D96Parser.CL)
            self.state = 169
            self.mptype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdglistContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdglist" ):
                return visitor.visitIdglist(self)
            else:
                return visitor.visitChildren(self)




    def idglist(self):

        localctx = D96Parser.IdglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idglist)
        self._la = 0 # Token type
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.IDUSD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 172
                self.match(D96Parser.CM)
                self.state = 173
                self.idglist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(D96Parser.STRINGTYPE, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def BOOLTYPE(self):
            return self.getToken(D96Parser.BOOLTYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mptype)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(D96Parser.INTTYPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(D96Parser.FLOATTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.match(D96Parser.STRINGTYPE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.array_type()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.match(D96Parser.ARRAY)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.match(D96Parser.BOOLTYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(D96Parser.ARRAY)
            self.state = 187
            self.match(D96Parser.LS)
            self.state = 188
            self.mptype()
            self.state = 189
            self.match(D96Parser.CM)
            self.state = 190
            self.match(D96Parser.INTLIT)
            self.state = 191
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.exp1()
                self.state = 194
                _la = self._input.LA(1)
                if not(_la==D96Parser.ET or _la==D96Parser.ADDT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 195
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = D96Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.exp2(0)
                self.state = 201
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NEQ) | (1 << D96Parser.LT) | (1 << D96Parser.LE) | (1 << D96Parser.GT) | (1 << D96Parser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 202
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 210
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 211
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 212
                    self.exp3(0) 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 221
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 222
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 223
                    self.exp4(0) 
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 232
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 233
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 234
                    self.exp5() 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp5)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(D96Parser.NOT)
                self.state = 241
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.SUB, D96Parser.LB, D96Parser.ID, D96Parser.IDUSD, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp6)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(D96Parser.SUB)
                self.state = 246
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.ID, D96Parser.IDUSD, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    self.index_list() 
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 278
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 263
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 264
                        self.match(D96Parser.DOT)
                        self.state = 265
                        self.match(D96Parser.ID)
                        self.state = 266
                        self.match(D96Parser.LB)
                        self.state = 267
                        self.exp_list()
                        self.state = 268
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 270
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 271
                        self.match(D96Parser.DOT)
                        self.state = 272
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 273
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 274
                        self.match(D96Parser.DOT)
                        self.state = 275
                        self.match(D96Parser.ID)
                        self.state = 276
                        self.match(D96Parser.LB)
                        self.state = 277
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


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

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 284
                self.exp10()
                self.state = 285
                self.match(D96Parser.STA)
                self.state = 286
                self.match(D96Parser.IDUSD)
                self.state = 287
                self.match(D96Parser.LB)
                self.state = 288
                self.exp_list()
                self.state = 289
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.state = 291
                self.exp10()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 302
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                        self.state = 294
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 295
                        self.match(D96Parser.STA)
                        self.state = 296
                        self.match(D96Parser.IDUSD)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                        self.state = 297
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 298
                        self.match(D96Parser.STA)
                        self.state = 299
                        self.match(D96Parser.IDUSD)
                        self.state = 300
                        self.match(D96Parser.LB)
                        self.state = 301
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp10)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(D96Parser.NEW)
                self.state = 308
                self.match(D96Parser.ID)
                self.state = 309
                self.match(D96Parser.LB)
                self.state = 310
                self.exp_list()
                self.state = 311
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(D96Parser.NEW)
                self.state = 314
                self.match(D96Parser.ID)
                self.state = 315
                self.match(D96Parser.LB)
                self.state = 316
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp11)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(D96Parser.LB)
                self.state = 321
                self.exp()
                self.state = 322
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.IDUSD, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IDUSD(self):
            return self.getToken(D96Parser.IDUSD, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp12" ):
                return visitor.visitExp12(self)
            else:
                return visitor.visitChildren(self)




    def exp12(self):

        localctx = D96Parser.Exp12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp12)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 329
                self.match(D96Parser.IDUSD)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 330
                self.match(D96Parser.SELF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = D96Parser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp_list)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.exp()
                self.state = 334
                self.match(D96Parser.CM)
                self.state = 335
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_list" ):
                return visitor.visitIndex_list(self)
            else:
                return visitor.visitChildren(self)




    def index_list(self):

        localctx = D96Parser.Index_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_index_list)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(D96Parser.LS)
                self.state = 341
                self.exp()
                self.state = 342
                self.match(D96Parser.RS)
                self.state = 343
                self.index_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.match(D96Parser.LS)
                self.state = 346
                self.exp()
                self.state = 347
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block_stmt)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(D96Parser.LP)
                self.state = 352
                self.stmt_list()
                self.state = 353
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.match(D96Parser.LP)
                self.state = 356
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Stmt_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = D96Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_list)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.stmt()
                self.state = 360
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 368
                self.loop_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 369
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 370
                self.cont_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 371
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 372
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmt" ):
                return visitor.visitDecl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def decl_stmt(self):

        localctx = D96Parser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_decl_stmt)
        self._la = 0 # Token type
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 376
                self.idlist()
                self.state = 377
                self.match(D96Parser.CL)
                self.state = 378
                self.mptype()
                self.state = 379
                self.match(D96Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 382
                self.idlist()
                self.state = 383
                self.match(D96Parser.CL)
                self.state = 384
                self.mptype()
                self.state = 385
                self.match(D96Parser.ASSIGN)
                self.state = 386
                self.exp_list()
                self.state = 387
                self.match(D96Parser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_idlist)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(D96Parser.ID)
                self.state = 392
                self.match(D96Parser.CM)
                self.state = 393
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 397
                self.exp7(0)
                pass

            elif la_ == 2:
                self.state = 398
                self.literals()
                pass


            self.state = 401
            self.match(D96Parser.ASSIGN)
            self.state = 402
            self.exp()
            self.state = 403
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def elseif_list(self):
            return self.getTypedRuleContext(D96Parser.Elseif_listContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_stmt)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.match(D96Parser.IF)
                self.state = 406
                self.match(D96Parser.LB)
                self.state = 407
                self.exp()
                self.state = 408
                self.match(D96Parser.RB)
                self.state = 409
                self.block_stmt()
                self.state = 410
                self.elseif_list()
                self.state = 411
                self.else_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.match(D96Parser.IF)
                self.state = 414
                self.match(D96Parser.LB)
                self.state = 415
                self.exp()
                self.state = 416
                self.match(D96Parser.RB)
                self.state = 417
                self.block_stmt()
                self.state = 418
                self.elseif_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 420
                self.match(D96Parser.IF)
                self.state = 421
                self.match(D96Parser.LB)
                self.state = 422
                self.exp()
                self.state = 423
                self.match(D96Parser.RB)
                self.state = 424
                self.block_stmt()
                self.state = 425
                self.else_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
                self.match(D96Parser.IF)
                self.state = 428
                self.match(D96Parser.LB)
                self.state = 429
                self.exp()
                self.state = 430
                self.match(D96Parser.RB)
                self.state = 431
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,0)


        def elseif_list(self):
            return self.getTypedRuleContext(D96Parser.Elseif_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_list" ):
                return visitor.visitElseif_list(self)
            else:
                return visitor.visitChildren(self)




    def elseif_list(self):

        localctx = D96Parser.Elseif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elseif_list)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.elseif_stmt()
                self.state = 436
                self.elseif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.elseif_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = D96Parser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(D96Parser.ELSEIF)
            self.state = 442
            self.match(D96Parser.LB)
            self.state = 443
            self.exp()
            self.state = 444
            self.match(D96Parser.RB)
            self.state = 445
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(D96Parser.ELSE)
            self.state = 448
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stmt" ):
                return visitor.visitLoop_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_stmt(self):

        localctx = D96Parser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_loop_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(D96Parser.FOREACH)
            self.state = 451
            self.match(D96Parser.LB)
            self.state = 452
            self.loop_condition()
            self.state = 453
            self.match(D96Parser.RB)
            self.state = 454
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOT)
            else:
                return self.getToken(D96Parser.DOT, i)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_loop_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_condition" ):
                return visitor.visitLoop_condition(self)
            else:
                return visitor.visitChildren(self)




    def loop_condition(self):

        localctx = D96Parser.Loop_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_loop_condition)
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.exp()
                self.state = 457
                self.match(D96Parser.IN)
                self.state = 458
                self.exp()
                self.state = 459
                self.match(D96Parser.DOT)
                self.state = 460
                self.match(D96Parser.DOT)
                self.state = 461
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.exp()
                self.state = 464
                self.match(D96Parser.IN)
                self.state = 465
                self.exp()
                self.state = 466
                self.match(D96Parser.DOT)
                self.state = 467
                self.match(D96Parser.DOT)
                self.state = 468
                self.exp()
                self.state = 469
                self.match(D96Parser.BY)
                self.state = 470
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(D96Parser.BREAK)
            self.state = 475
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_cont_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_stmt" ):
                return visitor.visitCont_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cont_stmt(self):

        localctx = D96Parser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(D96Parser.CONTINUE)
            self.state = 478
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(D96Parser.RET)
            self.state = 481
            self.exp()
            self.state = 482
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_stmt" ):
                return visitor.visitMethod_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_stmt(self):

        localctx = D96Parser.Method_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_method_stmt)
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance" ):
                return visitor.visitInstance(self)
            else:
                return visitor.visitChildren(self)




    def instance(self):

        localctx = D96Parser.InstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_instance)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic" ):
                return visitor.visitStatic(self)
            else:
                return visitor.visitChildren(self)




    def static(self):

        localctx = D96Parser.StaticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_static)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = D96Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arraylit)
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
        __slots__ = 'parser'

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

        def getRuleIndex(self):
            return D96Parser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literals)
        try:
            self.state = 541
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_boolit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolit" ):
                return visitor.visitBoolit(self)
            else:
                return visitor.visitChildren(self)




    def boolit(self):

        localctx = D96Parser.BoolitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
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
        self._predicates[14] = self.exp2_sempred
        self._predicates[15] = self.exp3_sempred
        self._predicates[16] = self.exp4_sempred
        self._predicates[19] = self.exp7_sempred
        self._predicates[20] = self.exp8_sempred
        self._predicates[21] = self.exp9_sempred
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




