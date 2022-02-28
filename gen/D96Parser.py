# Generated from C:/Users/rober/OneDrive/Documents/BKU/212/PPL/Assignments/01/initial/src/main/d96/parser\D96.g4 by ANTLR 4.9.1
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01d8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3j\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4t\n\4\3\5\3")
        buf.write("\5\3\5\5\5y\n\5\3\5\3\5\3\5\3\5\5\5\177\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008f")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u009b")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u00a2\n\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00ac\n\13\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00b2\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00c0\n\16\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00c7\n\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00cf")
        buf.write("\n\20\f\20\16\20\u00d2\13\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00da\n\21\f\21\16\21\u00dd\13\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\7\22\u00e5\n\22\f\22\16\22\u00e8")
        buf.write("\13\22\3\23\3\23\3\23\5\23\u00ed\n\23\3\24\3\24\3\24\5")
        buf.write("\24\u00f2\n\24\3\25\3\25\3\25\3\25\3\25\7\25\u00f9\n\25")
        buf.write("\f\25\16\25\u00fc\13\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u0108\n\26\f\26\16\26\u010b")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\7\27\u0117\n\27\f\27\16\27\u011a\13\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0127")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u012e\n\31\3\32\3")
        buf.write("\32\5\32\u0132\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u0139")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0144\n\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u014e\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u0158\n\37\3 \3 \3!\3!\5!\u015e\n!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\5\"\u0180\n\"\3#\3#\3#\3#\5#\u0186\n#\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'")
        buf.write("\u01aa\n\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\5,\u01bb\n,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\5.\u01c7\n")
        buf.write(".\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01d4")
        buf.write("\n\60\3\61\3\61\3\61\2\b\36 \"(*,\62\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`\2\n\3\2\25\26\4\2\30\3188\3\2+,\4\2$$&*\3")
        buf.write("\2\"#\3\2\34\35\3\2\36 \3\2\n\13\2\u01d7\2b\3\2\2\2\4")
        buf.write("i\3\2\2\2\6s\3\2\2\2\b~\3\2\2\2\n\u008e\3\2\2\2\f\u0090")
        buf.write("\3\2\2\2\16\u009a\3\2\2\2\20\u00a1\3\2\2\2\22\u00a3\3")
        buf.write("\2\2\2\24\u00ab\3\2\2\2\26\u00b1\3\2\2\2\30\u00b3\3\2")
        buf.write("\2\2\32\u00bf\3\2\2\2\34\u00c6\3\2\2\2\36\u00c8\3\2\2")
        buf.write("\2 \u00d3\3\2\2\2\"\u00de\3\2\2\2$\u00ec\3\2\2\2&\u00f1")
        buf.write("\3\2\2\2(\u00f3\3\2\2\2*\u00fd\3\2\2\2,\u010c\3\2\2\2")
        buf.write(".\u0126\3\2\2\2\60\u012d\3\2\2\2\62\u0131\3\2\2\2\64\u0138")
        buf.write("\3\2\2\2\66\u0143\3\2\2\28\u0145\3\2\2\2:\u014d\3\2\2")
        buf.write("\2<\u0157\3\2\2\2>\u0159\3\2\2\2@\u015d\3\2\2\2B\u017f")
        buf.write("\3\2\2\2D\u0185\3\2\2\2F\u0187\3\2\2\2H\u018d\3\2\2\2")
        buf.write("J\u0193\3\2\2\2L\u01a9\3\2\2\2N\u01ab\3\2\2\2P\u01ae\3")
        buf.write("\2\2\2R\u01b1\3\2\2\2T\u01b5\3\2\2\2V\u01ba\3\2\2\2X\u01bc")
        buf.write("\3\2\2\2Z\u01c6\3\2\2\2\\\u01c8\3\2\2\2^\u01d3\3\2\2\2")
        buf.write("`\u01d5\3\2\2\2bc\5\4\3\2cd\7\2\2\3d\3\3\2\2\2ef\5\6\4")
        buf.write("\2fg\5\4\3\2gj\3\2\2\2hj\5\6\4\2ie\3\2\2\2ih\3\2\2\2j")
        buf.write("\5\3\2\2\2kl\7\24\2\2lm\78\2\2mt\5\b\5\2no\7\24\2\2op")
        buf.write("\78\2\2pq\7\67\2\2qr\78\2\2rt\5\b\5\2sk\3\2\2\2sn\3\2")
        buf.write("\2\2t\7\3\2\2\2ux\7\63\2\2vy\5\n\6\2wy\5\f\7\2xv\3\2\2")
        buf.write("\2xw\3\2\2\2yz\3\2\2\2z{\7\64\2\2{\177\3\2\2\2|}\7\63")
        buf.write("\2\2}\177\7\64\2\2~u\3\2\2\2~|\3\2\2\2\177\t\3\2\2\2\u0080")
        buf.write("\u0081\t\2\2\2\u0081\u0082\5\24\13\2\u0082\u0083\7\67")
        buf.write("\2\2\u0083\u0084\5\26\f\2\u0084\u0085\7\66\2\2\u0085\u008f")
        buf.write("\3\2\2\2\u0086\u0087\t\2\2\2\u0087\u0088\5\24\13\2\u0088")
        buf.write("\u0089\7\67\2\2\u0089\u008a\5\26\f\2\u008a\u008b\7$\2")
        buf.write("\2\u008b\u008c\5\64\33\2\u008c\u008d\7\66\2\2\u008d\u008f")
        buf.write("\3\2\2\2\u008e\u0080\3\2\2\2\u008e\u0086\3\2\2\2\u008f")
        buf.write("\13\3\2\2\2\u0090\u0091\t\3\2\2\u0091\u0092\5\16\b\2\u0092")
        buf.write("\u0093\58\35\2\u0093\r\3\2\2\2\u0094\u0095\7/\2\2\u0095")
        buf.write("\u0096\5\20\t\2\u0096\u0097\7\60\2\2\u0097\u009b\3\2\2")
        buf.write("\2\u0098\u0099\7/\2\2\u0099\u009b\7\60\2\2\u009a\u0094")
        buf.write("\3\2\2\2\u009a\u0098\3\2\2\2\u009b\17\3\2\2\2\u009c\u009d")
        buf.write("\5\22\n\2\u009d\u009e\7\66\2\2\u009e\u009f\5\20\t\2\u009f")
        buf.write("\u00a2\3\2\2\2\u00a0\u00a2\5\22\n\2\u00a1\u009c\3\2\2")
        buf.write("\2\u00a1\u00a0\3\2\2\2\u00a2\21\3\2\2\2\u00a3\u00a4\5")
        buf.write("\24\13\2\u00a4\u00a5\7\67\2\2\u00a5\u00a6\5\26\f\2\u00a6")
        buf.write("\23\3\2\2\2\u00a7\u00a8\78\2\2\u00a8\u00a9\7\65\2\2\u00a9")
        buf.write("\u00ac\5\24\13\2\u00aa\u00ac\78\2\2\u00ab\u00a7\3\2\2")
        buf.write("\2\u00ab\u00aa\3\2\2\2\u00ac\25\3\2\2\2\u00ad\u00b2\7")
        buf.write("\16\2\2\u00ae\u00b2\7\17\2\2\u00af\u00b2\7\21\2\2\u00b0")
        buf.write("\u00b2\5\30\r\2\u00b1\u00ad\3\2\2\2\u00b1\u00ae\3\2\2")
        buf.write("\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\27\3")
        buf.write("\2\2\2\u00b3\u00b4\7\f\2\2\u00b4\u00b5\7\61\2\2\u00b5")
        buf.write("\u00b6\5\26\f\2\u00b6\u00b7\7\65\2\2\u00b7\u00b8\79\2")
        buf.write("\2\u00b8\u00b9\7\62\2\2\u00b9\31\3\2\2\2\u00ba\u00bb\5")
        buf.write("\34\17\2\u00bb\u00bc\t\4\2\2\u00bc\u00bd\5\34\17\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00c0\5\34\17\2\u00bf\u00ba\3\2\2")
        buf.write("\2\u00bf\u00be\3\2\2\2\u00c0\33\3\2\2\2\u00c1\u00c2\5")
        buf.write("\36\20\2\u00c2\u00c3\t\5\2\2\u00c3\u00c4\5\36\20\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c7\5\36\20\2\u00c6\u00c1\3\2\2")
        buf.write("\2\u00c6\u00c5\3\2\2\2\u00c7\35\3\2\2\2\u00c8\u00c9\b")
        buf.write("\20\1\2\u00c9\u00ca\5 \21\2\u00ca\u00d0\3\2\2\2\u00cb")
        buf.write("\u00cc\f\4\2\2\u00cc\u00cd\t\6\2\2\u00cd\u00cf\5 \21\2")
        buf.write("\u00ce\u00cb\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3")
        buf.write("\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\37\3\2\2\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d3\u00d4\b\21\1\2\u00d4\u00d5\5\"\22\2\u00d5")
        buf.write("\u00db\3\2\2\2\u00d6\u00d7\f\4\2\2\u00d7\u00d8\t\7\2\2")
        buf.write("\u00d8\u00da\5\"\22\2\u00d9\u00d6\3\2\2\2\u00da\u00dd")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("!\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\b\22\1\2\u00df")
        buf.write("\u00e0\5$\23\2\u00e0\u00e6\3\2\2\2\u00e1\u00e2\f\4\2\2")
        buf.write("\u00e2\u00e3\t\b\2\2\u00e3\u00e5\5$\23\2\u00e4\u00e1\3")
        buf.write("\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7")
        buf.write("\3\2\2\2\u00e7#\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea")
        buf.write("\7!\2\2\u00ea\u00ed\5$\23\2\u00eb\u00ed\5&\24\2\u00ec")
        buf.write("\u00e9\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed%\3\2\2\2\u00ee")
        buf.write("\u00ef\7\35\2\2\u00ef\u00f2\5&\24\2\u00f0\u00f2\5(\25")
        buf.write("\2\u00f1\u00ee\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2\'\3\2")
        buf.write("\2\2\u00f3\u00f4\b\25\1\2\u00f4\u00f5\5*\26\2\u00f5\u00fa")
        buf.write("\3\2\2\2\u00f6\u00f7\f\4\2\2\u00f7\u00f9\5\66\34\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb)\3\2\2\2\u00fc\u00fa\3\2\2")
        buf.write("\2\u00fd\u00fe\b\26\1\2\u00fe\u00ff\5,\27\2\u00ff\u0109")
        buf.write("\3\2\2\2\u0100\u0101\f\4\2\2\u0101\u0102\7.\2\2\u0102")
        buf.write("\u0103\78\2\2\u0103\u0104\7/\2\2\u0104\u0105\5\64\33\2")
        buf.write("\u0105\u0106\7\60\2\2\u0106\u0108\3\2\2\2\u0107\u0100")
        buf.write("\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a+\3\2\2\2\u010b\u0109\3\2\2\2\u010c")
        buf.write("\u010d\b\27\1\2\u010d\u010e\5.\30\2\u010e\u0118\3\2\2")
        buf.write("\2\u010f\u0110\f\4\2\2\u0110\u0111\7-\2\2\u0111\u0112")
        buf.write("\78\2\2\u0112\u0113\7/\2\2\u0113\u0114\5\64\33\2\u0114")
        buf.write("\u0115\7\60\2\2\u0115\u0117\3\2\2\2\u0116\u010f\3\2\2")
        buf.write("\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119")
        buf.write("\3\2\2\2\u0119-\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u011c")
        buf.write("\7\32\2\2\u011c\u011d\78\2\2\u011d\u011e\7/\2\2\u011e")
        buf.write("\u011f\5\64\33\2\u011f\u0120\7\60\2\2\u0120\u0127\3\2")
        buf.write("\2\2\u0121\u0122\7\32\2\2\u0122\u0123\78\2\2\u0123\u0124")
        buf.write("\7/\2\2\u0124\u0127\7\60\2\2\u0125\u0127\5\60\31\2\u0126")
        buf.write("\u011b\3\2\2\2\u0126\u0121\3\2\2\2\u0126\u0125\3\2\2\2")
        buf.write("\u0127/\3\2\2\2\u0128\u0129\7/\2\2\u0129\u012a\5\32\16")
        buf.write("\2\u012a\u012b\7\60\2\2\u012b\u012e\3\2\2\2\u012c\u012e")
        buf.write("\5\62\32\2\u012d\u0128\3\2\2\2\u012d\u012c\3\2\2\2\u012e")
        buf.write("\61\3\2\2\2\u012f\u0132\5^\60\2\u0130\u0132\78\2\2\u0131")
        buf.write("\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132\63\3\2\2\2\u0133")
        buf.write("\u0134\5\32\16\2\u0134\u0135\7\65\2\2\u0135\u0136\5\64")
        buf.write("\33\2\u0136\u0139\3\2\2\2\u0137\u0139\5\32\16\2\u0138")
        buf.write("\u0133\3\2\2\2\u0138\u0137\3\2\2\2\u0139\65\3\2\2\2\u013a")
        buf.write("\u013b\7\61\2\2\u013b\u013c\5\32\16\2\u013c\u013d\7\62")
        buf.write("\2\2\u013d\u013e\5\66\34\2\u013e\u0144\3\2\2\2\u013f\u0140")
        buf.write("\7\61\2\2\u0140\u0141\5\32\16\2\u0141\u0142\7\62\2\2\u0142")
        buf.write("\u0144\3\2\2\2\u0143\u013a\3\2\2\2\u0143\u013f\3\2\2\2")
        buf.write("\u0144\67\3\2\2\2\u0145\u0146\7\63\2\2\u0146\u0147\5:")
        buf.write("\36\2\u0147\u0148\7\64\2\2\u01489\3\2\2\2\u0149\u014a")
        buf.write("\5<\37\2\u014a\u014b\5:\36\2\u014b\u014e\3\2\2\2\u014c")
        buf.write("\u014e\5<\37\2\u014d\u0149\3\2\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e;\3\2\2\2\u014f\u0158\5> \2\u0150\u0158\5@!\2\u0151")
        buf.write("\u0158\5B\"\2\u0152\u0158\5J&\2\u0153\u0158\5N(\2\u0154")
        buf.write("\u0158\5P)\2\u0155\u0158\5R*\2\u0156\u0158\5T+\2\u0157")
        buf.write("\u014f\3\2\2\2\u0157\u0150\3\2\2\2\u0157\u0151\3\2\2\2")
        buf.write("\u0157\u0152\3\2\2\2\u0157\u0153\3\2\2\2\u0157\u0154\3")
        buf.write("\2\2\2\u0157\u0155\3\2\2\2\u0157\u0156\3\2\2\2\u0158=")
        buf.write("\3\2\2\2\u0159\u015a\5\n\6\2\u015a?\3\2\2\2\u015b\u015e")
        buf.write("\5(\25\2\u015c\u015e\5^\60\2\u015d\u015b\3\2\2\2\u015d")
        buf.write("\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\7$\2\2")
        buf.write("\u0160\u0161\5\32\16\2\u0161\u0162\7\66\2\2\u0162A\3\2")
        buf.write("\2\2\u0163\u0164\7\6\2\2\u0164\u0165\7/\2\2\u0165\u0166")
        buf.write("\5\32\16\2\u0166\u0167\7\60\2\2\u0167\u0168\58\35\2\u0168")
        buf.write("\u0169\5D#\2\u0169\u016a\5H%\2\u016a\u0180\3\2\2\2\u016b")
        buf.write("\u016c\7\6\2\2\u016c\u016d\7/\2\2\u016d\u016e\5\32\16")
        buf.write("\2\u016e\u016f\7\60\2\2\u016f\u0170\58\35\2\u0170\u0171")
        buf.write("\5D#\2\u0171\u0180\3\2\2\2\u0172\u0173\7\6\2\2\u0173\u0174")
        buf.write("\7/\2\2\u0174\u0175\5\32\16\2\u0175\u0176\7\60\2\2\u0176")
        buf.write("\u0177\58\35\2\u0177\u0178\5H%\2\u0178\u0180\3\2\2\2\u0179")
        buf.write("\u017a\7\6\2\2\u017a\u017b\7/\2\2\u017b\u017c\5\32\16")
        buf.write("\2\u017c\u017d\7\60\2\2\u017d\u017e\58\35\2\u017e\u0180")
        buf.write("\3\2\2\2\u017f\u0163\3\2\2\2\u017f\u016b\3\2\2\2\u017f")
        buf.write("\u0172\3\2\2\2\u017f\u0179\3\2\2\2\u0180C\3\2\2\2\u0181")
        buf.write("\u0182\5F$\2\u0182\u0183\5D#\2\u0183\u0186\3\2\2\2\u0184")
        buf.write("\u0186\5F$\2\u0185\u0181\3\2\2\2\u0185\u0184\3\2\2\2\u0186")
        buf.write("E\3\2\2\2\u0187\u0188\7\7\2\2\u0188\u0189\7/\2\2\u0189")
        buf.write("\u018a\5\32\16\2\u018a\u018b\7\60\2\2\u018b\u018c\58\35")
        buf.write("\2\u018cG\3\2\2\2\u018d\u018e\7\b\2\2\u018e\u018f\7/\2")
        buf.write("\2\u018f\u0190\5\32\16\2\u0190\u0191\7\60\2\2\u0191\u0192")
        buf.write("\58\35\2\u0192I\3\2\2\2\u0193\u0194\7\t\2\2\u0194\u0195")
        buf.write("\7/\2\2\u0195\u0196\5L\'\2\u0196\u0197\7\60\2\2\u0197")
        buf.write("\u0198\58\35\2\u0198K\3\2\2\2\u0199\u019a\5^\60\2\u019a")
        buf.write("\u019b\7\r\2\2\u019b\u019c\5\32\16\2\u019c\u019d\7.\2")
        buf.write("\2\u019d\u019e\7.\2\2\u019e\u019f\5\32\16\2\u019f\u01aa")
        buf.write("\3\2\2\2\u01a0\u01a1\5\32\16\2\u01a1\u01a2\7\r\2\2\u01a2")
        buf.write("\u01a3\5\32\16\2\u01a3\u01a4\7.\2\2\u01a4\u01a5\7.\2\2")
        buf.write("\u01a5\u01a6\5\32\16\2\u01a6\u01a7\7\33\2\2\u01a7\u01a8")
        buf.write("\5\32\16\2\u01a8\u01aa\3\2\2\2\u01a9\u0199\3\2\2\2\u01a9")
        buf.write("\u01a0\3\2\2\2\u01aaM\3\2\2\2\u01ab\u01ac\7\4\2\2\u01ac")
        buf.write("\u01ad\7\66\2\2\u01adO\3\2\2\2\u01ae\u01af\7\5\2\2\u01af")
        buf.write("\u01b0\7\66\2\2\u01b0Q\3\2\2\2\u01b1\u01b2\7\22\2\2\u01b2")
        buf.write("\u01b3\5\32\16\2\u01b3\u01b4\7\66\2\2\u01b4S\3\2\2\2\u01b5")
        buf.write("\u01b6\5*\26\2\u01b6\u01b7\7\66\2\2\u01b7U\3\2\2\2\u01b8")
        buf.write("\u01bb\5X-\2\u01b9\u01bb\5\\/\2\u01ba\u01b8\3\2\2\2\u01ba")
        buf.write("\u01b9\3\2\2\2\u01bbW\3\2\2\2\u01bc\u01bd\7\f\2\2\u01bd")
        buf.write("\u01be\7/\2\2\u01be\u01bf\5\64\33\2\u01bf\u01c0\7\60\2")
        buf.write("\2\u01c0Y\3\2\2\2\u01c1\u01c2\5X-\2\u01c2\u01c3\7\65\2")
        buf.write("\2\u01c3\u01c4\5Z.\2\u01c4\u01c7\3\2\2\2\u01c5\u01c7\5")
        buf.write("X-\2\u01c6\u01c1\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7[\3")
        buf.write("\2\2\2\u01c8\u01c9\7\f\2\2\u01c9\u01ca\7/\2\2\u01ca\u01cb")
        buf.write("\5Z.\2\u01cb\u01cc\7\60\2\2\u01cc]\3\2\2\2\u01cd\u01d4")
        buf.write("\79\2\2\u01ce\u01d4\7:\2\2\u01cf\u01d4\7;\2\2\u01d0\u01d4")
        buf.write("\5V,\2\u01d1\u01d4\5`\61\2\u01d2\u01d4\7\27\2\2\u01d3")
        buf.write("\u01cd\3\2\2\2\u01d3\u01ce\3\2\2\2\u01d3\u01cf\3\2\2\2")
        buf.write("\u01d3\u01d0\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3")
        buf.write("\2\2\2\u01d4_\3\2\2\2\u01d5\u01d6\t\t\2\2\u01d6a\3\2\2")
        buf.write("\2#isx~\u008e\u009a\u00a1\u00ab\u00b1\u00bf\u00c6\u00d0")
        buf.write("\u00db\u00e6\u00ec\u00f1\u00fa\u0109\u0118\u0126\u012d")
        buf.write("\u0131\u0138\u0143\u014d\u0157\u015d\u017f\u0185\u01a9")
        buf.write("\u01ba\u01c6\u01d3")
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
                      "IDG", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl_list = 1
    RULE_classdecl = 2
    RULE_members = 3
    RULE_attribute = 4
    RULE_method = 5
    RULE_param_list = 6
    RULE_params_decl = 7
    RULE_param_decl = 8
    RULE_idlist = 9
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
    RULE_assign_stmt = 31
    RULE_if_stmt = 32
    RULE_elseif_list = 33
    RULE_elseif_stmt = 34
    RULE_else_stmt = 35
    RULE_loop_stmt = 36
    RULE_loop_condition = 37
    RULE_break_stmt = 38
    RULE_cont_stmt = 39
    RULE_return_stmt = 40
    RULE_method_stmt = 41
    RULE_arraylit = 42
    RULE_indexed_array = 43
    RULE_indexed_array_list = 44
    RULE_multi_array = 45
    RULE_literals = 46
    RULE_boolit = 47

    ruleNames =  [ "program", "classdecl_list", "classdecl", "members", 
                   "attribute", "method", "param_list", "params_decl", "param_decl", 
                   "idlist", "mptype", "array_type", "exp", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", 
                   "exp10", "exp11", "exp12", "exp_list", "index_list", 
                   "block_stmt", "stmt_list", "stmt", "decl_stmt", "assign_stmt", 
                   "if_stmt", "elseif_list", "elseif_stmt", "else_stmt", 
                   "loop_stmt", "loop_condition", "break_stmt", "cont_stmt", 
                   "return_stmt", "method_stmt", "arraylit", "indexed_array", 
                   "indexed_array_list", "multi_array", "literals", "boolit" ]

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
    IDG=54
    INTLIT=55
    FLOATLIT=56
    STRINGLIT=57
    WS=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassdecl_list" ):
                listener.enterClassdecl_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassdecl_list" ):
                listener.exitClassdecl_list(self)

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

        def IDG(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDG)
            else:
                return self.getToken(D96Parser.IDG, i)

        def members(self):
            return self.getTypedRuleContext(D96Parser.MembersContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassdecl" ):
                listener.enterClassdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassdecl" ):
                listener.exitClassdecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(D96Parser.CLASS)
                self.state = 106
                self.match(D96Parser.IDG)
                self.state = 107
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(D96Parser.CLASS)
                self.state = 109
                self.match(D96Parser.IDG)
                self.state = 110
                self.match(D96Parser.CL)
                self.state = 111
                self.match(D96Parser.IDG)
                self.state = 112
                self.members()
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

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def attribute(self):
            return self.getTypedRuleContext(D96Parser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_members

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMembers" ):
                listener.enterMembers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMembers" ):
                listener.exitMembers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = D96Parser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_members)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(D96Parser.LP)
                self.state = 118
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 116
                    self.attribute()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.IDG]:
                    self.state = 117
                    self.method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 120
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(D96Parser.LP)
                self.state = 123
                self.match(D96Parser.RP)
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

        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

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
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 127
                self.idlist()
                self.state = 128
                self.match(D96Parser.CL)
                self.state = 129
                self.mptype()
                self.state = 130
                self.match(D96Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.idlist()
                self.state = 134
                self.match(D96Parser.CL)
                self.state = 135
                self.mptype()
                self.state = 136
                self.match(D96Parser.EQ)
                self.state = 137
                self.exp_list()
                self.state = 138
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


        def IDG(self):
            return self.getToken(D96Parser.IDG, 0)

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)

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
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDG))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 143
            self.param_list()
            self.state = 144
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = D96Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param_list)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(D96Parser.LB)
                self.state = 147
                self.params_decl()
                self.state = 148
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(D96Parser.LB)
                self.state = 151
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams_decl" ):
                listener.enterParams_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams_decl" ):
                listener.exitParams_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_decl" ):
                return visitor.visitParams_decl(self)
            else:
                return visitor.visitChildren(self)




    def params_decl(self):

        localctx = D96Parser.Params_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params_decl)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.param_decl()
                self.state = 155
                self.match(D96Parser.SM)
                self.state = 156
                self.params_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
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

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_decl" ):
                listener.enterParam_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_decl" ):
                listener.exitParam_decl(self)

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
            self.state = 161
            self.idlist()
            self.state = 162
            self.match(D96Parser.CL)
            self.state = 163
            self.mptype()
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

        def IDG(self):
            return self.getToken(D96Parser.IDG, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdlist" ):
                listener.enterIdlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdlist" ):
                listener.exitIdlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idlist)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(D96Parser.IDG)
                self.state = 166
                self.match(D96Parser.CM)
                self.state = 167
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(D96Parser.IDG)
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


        def getRuleIndex(self):
            return D96Parser.RULE_mptype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMptype" ):
                listener.enterMptype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMptype" ):
                listener.exitMptype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mptype)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(D96Parser.STRINGTYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.array_type()
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type" ):
                listener.enterArray_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type" ):
                listener.exitArray_type(self)

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
            self.state = 177
            self.match(D96Parser.ARRAY)
            self.state = 178
            self.match(D96Parser.LS)
            self.state = 179
            self.mptype()
            self.state = 180
            self.match(D96Parser.CM)
            self.state = 181
            self.match(D96Parser.INTLIT)
            self.state = 182
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

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
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.exp1()
                self.state = 185
                _la = self._input.LA(1)
                if not(_la==D96Parser.ET or _la==D96Parser.ADDT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp1" ):
                listener.enterExp1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp1" ):
                listener.exitExp1(self)

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
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.exp2(0)
                self.state = 192
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NEQ) | (1 << D96Parser.LT) | (1 << D96Parser.LE) | (1 << D96Parser.GT) | (1 << D96Parser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 193
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp2" ):
                listener.enterExp2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp2" ):
                listener.exitExp2(self)

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
            self.state = 199
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 201
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 202
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 203
                    self.exp3(0) 
                self.state = 208
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp3" ):
                listener.enterExp3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp3" ):
                listener.exitExp3(self)

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
            self.state = 210
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 212
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 213
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 214
                    self.exp4(0) 
                self.state = 219
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp4" ):
                listener.enterExp4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp4" ):
                listener.exitExp4(self)

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
            self.state = 221
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.exp5() 
                self.state = 230
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp5" ):
                listener.enterExp5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp5" ):
                listener.exitExp5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp5)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(D96Parser.NOT)
                self.state = 232
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.SUB, D96Parser.LB, D96Parser.IDG, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp6" ):
                listener.enterExp6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp6" ):
                listener.exitExp6(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp6)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(D96Parser.SUB)
                self.state = 237
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.IDG, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp7" ):
                listener.enterExp7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp7" ):
                listener.exitExp7(self)

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
            self.state = 242
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    self.index_list() 
                self.state = 250
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

        def IDG(self):
            return self.getToken(D96Parser.IDG, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp8" ):
                listener.enterExp8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp8" ):
                listener.exitExp8(self)

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
            self.state = 252
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    self.match(D96Parser.DOT)
                    self.state = 256
                    self.match(D96Parser.IDG)
                    self.state = 257
                    self.match(D96Parser.LB)
                    self.state = 258
                    self.exp_list()
                    self.state = 259
                    self.match(D96Parser.RB) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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


        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def STA(self):
            return self.getToken(D96Parser.STA, 0)

        def IDG(self):
            return self.getToken(D96Parser.IDG, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp9

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp9" ):
                listener.enterExp9(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp9" ):
                listener.exitExp9(self)

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
            self.state = 267
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 269
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 270
                    self.match(D96Parser.STA)
                    self.state = 271
                    self.match(D96Parser.IDG)
                    self.state = 272
                    self.match(D96Parser.LB)
                    self.state = 273
                    self.exp_list()
                    self.state = 274
                    self.match(D96Parser.RB) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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

        def IDG(self):
            return self.getToken(D96Parser.IDG, 0)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp10" ):
                listener.enterExp10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp10" ):
                listener.exitExp10(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp10)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(D96Parser.NEW)
                self.state = 282
                self.match(D96Parser.IDG)
                self.state = 283
                self.match(D96Parser.LB)
                self.state = 284
                self.exp_list()
                self.state = 285
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(D96Parser.NEW)
                self.state = 288
                self.match(D96Parser.IDG)
                self.state = 289
                self.match(D96Parser.LB)
                self.state = 290
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp11" ):
                listener.enterExp11(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp11" ):
                listener.exitExp11(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp11)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(D96Parser.LB)
                self.state = 295
                self.exp()
                self.state = 296
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.IDG, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
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


        def IDG(self):
            return self.getToken(D96Parser.IDG, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp12

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp12" ):
                listener.enterExp12(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp12" ):
                listener.exitExp12(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp12" ):
                return visitor.visitExp12(self)
            else:
                return visitor.visitChildren(self)




    def exp12(self):

        localctx = D96Parser.Exp12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp12)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.literals()
                pass
            elif token in [D96Parser.IDG]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(D96Parser.IDG)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_list" ):
                listener.enterExp_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_list" ):
                listener.exitExp_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = D96Parser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp_list)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.exp()
                self.state = 306
                self.match(D96Parser.CM)
                self.state = 307
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_list" ):
                listener.enterIndex_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_list" ):
                listener.exitIndex_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_list" ):
                return visitor.visitIndex_list(self)
            else:
                return visitor.visitChildren(self)




    def index_list(self):

        localctx = D96Parser.Index_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_index_list)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(D96Parser.LS)
                self.state = 313
                self.exp()
                self.state = 314
                self.match(D96Parser.RS)
                self.state = 315
                self.index_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(D96Parser.LS)
                self.state = 318
                self.exp()
                self.state = 319
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_stmt" ):
                listener.enterBlock_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_stmt" ):
                listener.exitBlock_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(D96Parser.LP)
            self.state = 324
            self.stmt_list()
            self.state = 325
            self.match(D96Parser.RP)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_list" ):
                listener.enterStmt_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_list" ):
                listener.exitStmt_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = D96Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_list)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.stmt()
                self.state = 328
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 336
                self.loop_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 337
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 338
                self.cont_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 339
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 340
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

        def attribute(self):
            return self.getTypedRuleContext(D96Parser.AttributeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_decl_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_stmt" ):
                listener.enterDecl_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_stmt" ):
                listener.exitDecl_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmt" ):
                return visitor.visitDecl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def decl_stmt(self):

        localctx = D96Parser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.attribute()
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

        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 345
                self.exp7(0)
                pass

            elif la_ == 2:
                self.state = 346
                self.literals()
                pass


            self.state = 349
            self.match(D96Parser.EQ)
            self.state = 350
            self.exp()
            self.state = 351
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_stmt)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(D96Parser.IF)
                self.state = 354
                self.match(D96Parser.LB)
                self.state = 355
                self.exp()
                self.state = 356
                self.match(D96Parser.RB)
                self.state = 357
                self.block_stmt()
                self.state = 358
                self.elseif_list()
                self.state = 359
                self.else_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.match(D96Parser.IF)
                self.state = 362
                self.match(D96Parser.LB)
                self.state = 363
                self.exp()
                self.state = 364
                self.match(D96Parser.RB)
                self.state = 365
                self.block_stmt()
                self.state = 366
                self.elseif_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self.match(D96Parser.IF)
                self.state = 369
                self.match(D96Parser.LB)
                self.state = 370
                self.exp()
                self.state = 371
                self.match(D96Parser.RB)
                self.state = 372
                self.block_stmt()
                self.state = 373
                self.else_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 375
                self.match(D96Parser.IF)
                self.state = 376
                self.match(D96Parser.LB)
                self.state = 377
                self.exp()
                self.state = 378
                self.match(D96Parser.RB)
                self.state = 379
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_list" ):
                listener.enterElseif_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_list" ):
                listener.exitElseif_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_list" ):
                return visitor.visitElseif_list(self)
            else:
                return visitor.visitChildren(self)




    def elseif_list(self):

        localctx = D96Parser.Elseif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elseif_list)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.elseif_stmt()
                self.state = 384
                self.elseif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_stmt" ):
                listener.enterElseif_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_stmt" ):
                listener.exitElseif_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = D96Parser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(D96Parser.ELSEIF)
            self.state = 390
            self.match(D96Parser.LB)
            self.state = 391
            self.exp()
            self.state = 392
            self.match(D96Parser.RB)
            self.state = 393
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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_stmt" ):
                listener.enterElse_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_stmt" ):
                listener.exitElse_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(D96Parser.ELSE)
            self.state = 396
            self.match(D96Parser.LB)
            self.state = 397
            self.exp()
            self.state = 398
            self.match(D96Parser.RB)
            self.state = 399
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_stmt" ):
                listener.enterLoop_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_stmt" ):
                listener.exitLoop_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stmt" ):
                return visitor.visitLoop_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_stmt(self):

        localctx = D96Parser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_loop_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(D96Parser.FOREACH)
            self.state = 402
            self.match(D96Parser.LB)
            self.state = 403
            self.loop_condition()
            self.state = 404
            self.match(D96Parser.RB)
            self.state = 405
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

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_condition" ):
                listener.enterLoop_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_condition" ):
                listener.exitLoop_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_condition" ):
                return visitor.visitLoop_condition(self)
            else:
                return visitor.visitChildren(self)




    def loop_condition(self):

        localctx = D96Parser.Loop_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_loop_condition)
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.literals()
                self.state = 408
                self.match(D96Parser.IN)
                self.state = 409
                self.exp()
                self.state = 410
                self.match(D96Parser.DOT)
                self.state = 411
                self.match(D96Parser.DOT)
                self.state = 412
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.exp()
                self.state = 415
                self.match(D96Parser.IN)
                self.state = 416
                self.exp()
                self.state = 417
                self.match(D96Parser.DOT)
                self.state = 418
                self.match(D96Parser.DOT)
                self.state = 419
                self.exp()
                self.state = 420
                self.match(D96Parser.BY)
                self.state = 421
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_stmt" ):
                listener.enterBreak_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_stmt" ):
                listener.exitBreak_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(D96Parser.BREAK)
            self.state = 426
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCont_stmt" ):
                listener.enterCont_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCont_stmt" ):
                listener.exitCont_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_stmt" ):
                return visitor.visitCont_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cont_stmt(self):

        localctx = D96Parser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.CONTINUE)
            self.state = 429
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(D96Parser.RET)
            self.state = 432
            self.exp()
            self.state = 433
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

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_stmt" ):
                listener.enterMethod_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_stmt" ):
                listener.exitMethod_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_stmt" ):
                return visitor.visitMethod_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_stmt(self):

        localctx = D96Parser.Method_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_method_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.exp8(0)
            self.state = 436
            self.match(D96Parser.SM)
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

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def multi_array(self):
            return self.getTypedRuleContext(D96Parser.Multi_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arraylit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraylit" ):
                listener.enterArraylit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraylit" ):
                listener.exitArraylit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = D96Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arraylit)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.indexed_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.multi_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):
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
            return D96Parser.RULE_indexed_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexed_array" ):
                listener.enterIndexed_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexed_array" ):
                listener.exitIndexed_array(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_indexed_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(D96Parser.ARRAY)
            self.state = 443
            self.match(D96Parser.LB)
            self.state = 444
            self.exp_list()
            self.state = 445
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def indexed_array_list(self):
            return self.getTypedRuleContext(D96Parser.Indexed_array_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexed_array_list" ):
                listener.enterIndexed_array_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexed_array_list" ):
                listener.exitIndexed_array_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array_list" ):
                return visitor.visitIndexed_array_list(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array_list(self):

        localctx = D96Parser.Indexed_array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_indexed_array_list)
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.indexed_array()
                self.state = 448
                self.match(D96Parser.CM)
                self.state = 449
                self.indexed_array_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.indexed_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def indexed_array_list(self):
            return self.getTypedRuleContext(D96Parser.Indexed_array_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multi_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulti_array" ):
                listener.enterMulti_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulti_array" ):
                listener.exitMulti_array(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_array" ):
                return visitor.visitMulti_array(self)
            else:
                return visitor.visitChildren(self)




    def multi_array(self):

        localctx = D96Parser.Multi_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_multi_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(D96Parser.ARRAY)
            self.state = 455
            self.match(D96Parser.LB)
            self.state = 456
            self.indexed_array_list()
            self.state = 457
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiterals" ):
                listener.enterLiterals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiterals" ):
                listener.exitLiterals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literals)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 462
                self.arraylit()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 463
                self.boolit()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 6)
                self.state = 464
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolit" ):
                listener.enterBoolit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolit" ):
                listener.exitBoolit(self)

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
            self.state = 467
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
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




