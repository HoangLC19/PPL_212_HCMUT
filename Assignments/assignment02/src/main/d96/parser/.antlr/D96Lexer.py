# Generated from c:\Users\rober\OneDrive\Documents\BKU\212\PPL\Assignments\assignment02\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0242\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\7\2\u009a\n\2\f\2\16\2\u009d\13\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\5\67\u0177\n\67\38\38\39\39\59\u017d\n9\39\39\39\79\u0182")
        buf.write("\n9\f9\169\u0185\139\3:\3:\3:\3:\6:\u018b\n:\r:\16:\u018c")
        buf.write("\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u019b\n;\3<\3")
        buf.write("<\3<\7<\u01a0\n<\f<\16<\u01a3\13<\3<\3<\6<\u01a7\n<\r")
        buf.write("<\16<\u01a8\7<\u01ab\n<\f<\16<\u01ae\13<\3<\5<\u01b1\n")
        buf.write("<\5<\u01b3\n<\3=\3=\6=\u01b7\n=\r=\16=\u01b8\3=\3=\6=")
        buf.write("\u01bd\n=\r=\16=\u01be\7=\u01c1\n=\f=\16=\u01c4\13=\3")
        buf.write(">\3>\3>\6>\u01c9\n>\r>\16>\u01ca\3>\3>\6>\u01cf\n>\r>")
        buf.write("\16>\u01d0\7>\u01d3\n>\f>\16>\u01d6\13>\3?\3?\3?\6?\u01db")
        buf.write("\n?\r?\16?\u01dc\3?\3?\6?\u01e1\n?\r?\16?\u01e2\7?\u01e5")
        buf.write("\n?\f?\16?\u01e8\13?\3@\3@\5@\u01ec\n@\3@\3@\3@\5@\u01f1")
        buf.write("\n@\3@\3@\3@\5@\u01f6\n@\3A\3A\5A\u01fa\nA\3A\6A\u01fd")
        buf.write("\nA\rA\16A\u01fe\3B\3B\7B\u0203\nB\fB\16B\u0206\13B\3")
        buf.write("B\5B\u0209\nB\3C\3C\7C\u020d\nC\fC\16C\u0210\13C\3C\3")
        buf.write("C\3C\3D\3D\3D\3D\5D\u0219\nD\3E\3E\3E\3F\6F\u021f\nF\r")
        buf.write("F\16F\u0220\3F\3F\3G\3G\3G\3H\3H\7H\u022a\nH\fH\16H\u022d")
        buf.write("\13H\3H\5H\u0230\nH\3H\3H\3I\3I\7I\u0236\nI\fI\16I\u0239")
        buf.write("\13I\3I\3I\3I\3J\3J\3J\5J\u0241\nJ\3\u009b\2K\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q8s9u:w\2y\2")
        buf.write("{\2}\2\177;\u0081\2\u0083\2\u0085<\u0087\2\u0089\2\u008b")
        buf.write("=\u008d>\u008f?\u0091@\u0093\2\3\2\21\4\2C\\c|\3\2\63")
        buf.write(";\3\2\62;\3\2\629\4\2ZZzz\4\2\62;CH\4\2DDdd\3\2\62\63")
        buf.write("\4\2GGgg\4\2--//\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttv")
        buf.write("v\5\2\n\f\16\17\"\"\6\3\n\f\16\17))^^\3\2^^\2\u025d\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2\2\2\u008b\3\2\2\2")
        buf.write("\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0095")
        buf.write("\3\2\2\2\5\u00a3\3\2\2\2\7\u00a9\3\2\2\2\t\u00b2\3\2\2")
        buf.write("\2\13\u00b5\3\2\2\2\r\u00bc\3\2\2\2\17\u00c1\3\2\2\2\21")
        buf.write("\u00c9\3\2\2\2\23\u00ce\3\2\2\2\25\u00d4\3\2\2\2\27\u00da")
        buf.write("\3\2\2\2\31\u00dd\3\2\2\2\33\u00e1\3\2\2\2\35\u00e7\3")
        buf.write("\2\2\2\37\u00ef\3\2\2\2!\u00f6\3\2\2\2#\u00fd\3\2\2\2")
        buf.write("%\u0102\3\2\2\2\'\u0108\3\2\2\2)\u010c\3\2\2\2+\u0110")
        buf.write("\3\2\2\2-\u0115\3\2\2\2/\u0121\3\2\2\2\61\u012c\3\2\2")
        buf.write("\2\63\u0130\3\2\2\2\65\u0133\3\2\2\2\67\u0135\3\2\2\2")
        buf.write("9\u0137\3\2\2\2;\u0139\3\2\2\2=\u013b\3\2\2\2?\u013d\3")
        buf.write("\2\2\2A\u013f\3\2\2\2C\u0142\3\2\2\2E\u0145\3\2\2\2G\u0148")
        buf.write("\3\2\2\2I\u014a\3\2\2\2K\u014d\3\2\2\2M\u014f\3\2\2\2")
        buf.write("O\u0152\3\2\2\2Q\u0154\3\2\2\2S\u0157\3\2\2\2U\u015b\3")
        buf.write("\2\2\2W\u015e\3\2\2\2Y\u0161\3\2\2\2[\u0163\3\2\2\2]\u0165")
        buf.write("\3\2\2\2_\u0167\3\2\2\2a\u0169\3\2\2\2c\u016b\3\2\2\2")
        buf.write("e\u016d\3\2\2\2g\u016f\3\2\2\2i\u0171\3\2\2\2k\u0173\3")
        buf.write("\2\2\2m\u0176\3\2\2\2o\u0178\3\2\2\2q\u017c\3\2\2\2s\u0186")
        buf.write("\3\2\2\2u\u019a\3\2\2\2w\u01b2\3\2\2\2y\u01b4\3\2\2\2")
        buf.write("{\u01c5\3\2\2\2}\u01d7\3\2\2\2\177\u01f5\3\2\2\2\u0081")
        buf.write("\u01f7\3\2\2\2\u0083\u0200\3\2\2\2\u0085\u020a\3\2\2\2")
        buf.write("\u0087\u0218\3\2\2\2\u0089\u021a\3\2\2\2\u008b\u021e\3")
        buf.write("\2\2\2\u008d\u0224\3\2\2\2\u008f\u0227\3\2\2\2\u0091\u0233")
        buf.write("\3\2\2\2\u0093\u0240\3\2\2\2\u0095\u0096\7%\2\2\u0096")
        buf.write("\u0097\7%\2\2\u0097\u009b\3\2\2\2\u0098\u009a\13\2\2\2")
        buf.write("\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009b\u0099\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b")
        buf.write("\3\2\2\2\u009e\u009f\7%\2\2\u009f\u00a0\7%\2\2\u00a0\u00a1")
        buf.write("\3\2\2\2\u00a1\u00a2\b\2\2\2\u00a2\4\3\2\2\2\u00a3\u00a4")
        buf.write("\7D\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7")
        buf.write("\7c\2\2\u00a7\u00a8\7m\2\2\u00a8\6\3\2\2\2\u00a9\u00aa")
        buf.write("\7E\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7w\2\2\u00b0\u00b1\7g\2\2\u00b1\b\3\2\2\2\u00b2\u00b3")
        buf.write("\7K\2\2\u00b3\u00b4\7h\2\2\u00b4\n\3\2\2\2\u00b5\u00b6")
        buf.write("\7G\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7h\2\2\u00bb\f")
        buf.write("\3\2\2\2\u00bc\u00bd\7G\2\2\u00bd\u00be\7n\2\2\u00be\u00bf")
        buf.write("\7u\2\2\u00bf\u00c0\7g\2\2\u00c0\16\3\2\2\2\u00c1\u00c2")
        buf.write("\7H\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8")
        buf.write("\7j\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\7V\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd\7g\2\2\u00cd\22")
        buf.write("\3\2\2\2\u00ce\u00cf\7H\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7g\2\2\u00d3\24")
        buf.write("\3\2\2\2\u00d4\u00d5\7C\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7")
        buf.write("\7t\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7{\2\2\u00d9\26")
        buf.write("\3\2\2\2\u00da\u00db\7K\2\2\u00db\u00dc\7p\2\2\u00dc\30")
        buf.write("\3\2\2\2\u00dd\u00de\7K\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\32\3\2\2\2\u00e1\u00e2\7H\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\34\3\2\2\2\u00e7\u00e8\7D\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7p\2\2\u00ee\36")
        buf.write("\3\2\2\2\u00ef\u00f0\7U\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5")
        buf.write("\7i\2\2\u00f5 \3\2\2\2\u00f6\u00f7\7T\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\u00fc\7p\2\2\u00fc\"\3\2\2\2\u00fd\u00fe")
        buf.write("\7P\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100\7n\2\2\u0100\u0101")
        buf.write("\7n\2\2\u0101$\3\2\2\2\u0102\u0103\7E\2\2\u0103\u0104")
        buf.write("\7n\2\2\u0104\u0105\7c\2\2\u0105\u0106\7u\2\2\u0106\u0107")
        buf.write("\7u\2\2\u0107&\3\2\2\2\u0108\u0109\7X\2\2\u0109\u010a")
        buf.write("\7c\2\2\u010a\u010b\7n\2\2\u010b(\3\2\2\2\u010c\u010d")
        buf.write("\7X\2\2\u010d\u010e\7c\2\2\u010e\u010f\7t\2\2\u010f*\3")
        buf.write("\2\2\2\u0110\u0111\7U\2\2\u0111\u0112\7g\2\2\u0112\u0113")
        buf.write("\7n\2\2\u0113\u0114\7h\2\2\u0114,\3\2\2\2\u0115\u0116")
        buf.write("\7E\2\2\u0116\u0117\7q\2\2\u0117\u0118\7p\2\2\u0118\u0119")
        buf.write("\7u\2\2\u0119\u011a\7v\2\2\u011a\u011b\7t\2\2\u011b\u011c")
        buf.write("\7w\2\2\u011c\u011d\7e\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7q\2\2\u011f\u0120\7t\2\2\u0120.\3\2\2\2\u0121\u0122")
        buf.write("\7F\2\2\u0122\u0123\7g\2\2\u0123\u0124\7u\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7t\2\2\u0126\u0127\7w\2\2\u0127\u0128")
        buf.write("\7e\2\2\u0128\u0129\7v\2\2\u0129\u012a\7q\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b\60\3\2\2\2\u012c\u012d\7P\2\2\u012d\u012e")
        buf.write("\7g\2\2\u012e\u012f\7y\2\2\u012f\62\3\2\2\2\u0130\u0131")
        buf.write("\7D\2\2\u0131\u0132\7{\2\2\u0132\64\3\2\2\2\u0133\u0134")
        buf.write("\7-\2\2\u0134\66\3\2\2\2\u0135\u0136\7/\2\2\u01368\3\2")
        buf.write("\2\2\u0137\u0138\7,\2\2\u0138:\3\2\2\2\u0139\u013a\7\61")
        buf.write("\2\2\u013a<\3\2\2\2\u013b\u013c\7\'\2\2\u013c>\3\2\2\2")
        buf.write("\u013d\u013e\7#\2\2\u013e@\3\2\2\2\u013f\u0140\7(\2\2")
        buf.write("\u0140\u0141\7(\2\2\u0141B\3\2\2\2\u0142\u0143\7~\2\2")
        buf.write("\u0143\u0144\7~\2\2\u0144D\3\2\2\2\u0145\u0146\7?\2\2")
        buf.write("\u0146\u0147\7?\2\2\u0147F\3\2\2\2\u0148\u0149\7?\2\2")
        buf.write("\u0149H\3\2\2\2\u014a\u014b\7#\2\2\u014b\u014c\7?\2\2")
        buf.write("\u014cJ\3\2\2\2\u014d\u014e\7>\2\2\u014eL\3\2\2\2\u014f")
        buf.write("\u0150\7>\2\2\u0150\u0151\7?\2\2\u0151N\3\2\2\2\u0152")
        buf.write("\u0153\7@\2\2\u0153P\3\2\2\2\u0154\u0155\7@\2\2\u0155")
        buf.write("\u0156\7?\2\2\u0156R\3\2\2\2\u0157\u0158\7?\2\2\u0158")
        buf.write("\u0159\7?\2\2\u0159\u015a\7\60\2\2\u015aT\3\2\2\2\u015b")
        buf.write("\u015c\7-\2\2\u015c\u015d\7\60\2\2\u015dV\3\2\2\2\u015e")
        buf.write("\u015f\7<\2\2\u015f\u0160\7<\2\2\u0160X\3\2\2\2\u0161")
        buf.write("\u0162\7\60\2\2\u0162Z\3\2\2\2\u0163\u0164\7*\2\2\u0164")
        buf.write("\\\3\2\2\2\u0165\u0166\7+\2\2\u0166^\3\2\2\2\u0167\u0168")
        buf.write("\7]\2\2\u0168`\3\2\2\2\u0169\u016a\7_\2\2\u016ab\3\2\2")
        buf.write("\2\u016b\u016c\7}\2\2\u016cd\3\2\2\2\u016d\u016e\7\177")
        buf.write("\2\2\u016ef\3\2\2\2\u016f\u0170\7.\2\2\u0170h\3\2\2\2")
        buf.write("\u0171\u0172\7=\2\2\u0172j\3\2\2\2\u0173\u0174\7<\2\2")
        buf.write("\u0174l\3\2\2\2\u0175\u0177\4\62;\2\u0176\u0175\3\2\2")
        buf.write("\2\u0177n\3\2\2\2\u0178\u0179\t\2\2\2\u0179p\3\2\2\2\u017a")
        buf.write("\u017d\5o8\2\u017b\u017d\7a\2\2\u017c\u017a\3\2\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017d\u0183\3\2\2\2\u017e\u0182\5o8\2\u017f")
        buf.write("\u0182\7a\2\2\u0180\u0182\5m\67\2\u0181\u017e\3\2\2\2")
        buf.write("\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2\u0182\u0185\3")
        buf.write("\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184r")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u018a\7&\2\2\u0187")
        buf.write("\u018b\5o8\2\u0188\u018b\7a\2\2\u0189\u018b\5m\67\2\u018a")
        buf.write("\u0187\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u0189\3\2\2\2")
        buf.write("\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3")
        buf.write("\2\2\2\u018dt\3\2\2\2\u018e\u018f\5w<\2\u018f\u0190\b")
        buf.write(";\3\2\u0190\u019b\3\2\2\2\u0191\u0192\5y=\2\u0192\u0193")
        buf.write("\b;\4\2\u0193\u019b\3\2\2\2\u0194\u0195\5{>\2\u0195\u0196")
        buf.write("\b;\5\2\u0196\u019b\3\2\2\2\u0197\u0198\5}?\2\u0198\u0199")
        buf.write("\b;\6\2\u0199\u019b\3\2\2\2\u019a\u018e\3\2\2\2\u019a")
        buf.write("\u0191\3\2\2\2\u019a\u0194\3\2\2\2\u019a\u0197\3\2\2\2")
        buf.write("\u019bv\3\2\2\2\u019c\u01b3\7\62\2\2\u019d\u01a1\t\3\2")
        buf.write("\2\u019e\u01a0\t\4\2\2\u019f\u019e\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01ac\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a6\7a\2\2")
        buf.write("\u01a5\u01a7\t\4\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3")
        buf.write("\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab")
        buf.write("\3\2\2\2\u01aa\u01a4\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01b0\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01af\u01b1\5\u0081A\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2")
        buf.write("\u019c\3\2\2\2\u01b2\u019d\3\2\2\2\u01b3x\3\2\2\2\u01b4")
        buf.write("\u01b6\7\62\2\2\u01b5\u01b7\t\5\2\2\u01b6\u01b5\3\2\2")
        buf.write("\2\u01b7\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9")
        buf.write("\3\2\2\2\u01b9\u01c2\3\2\2\2\u01ba\u01bc\7a\2\2\u01bb")
        buf.write("\u01bd\t\5\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c1\3")
        buf.write("\2\2\2\u01c0\u01ba\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3z\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c5\u01c6\7\62\2\2\u01c6\u01c8\t\6\2\2\u01c7")
        buf.write("\u01c9\t\7\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2")
        buf.write("\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01d4\3")
        buf.write("\2\2\2\u01cc\u01ce\7a\2\2\u01cd\u01cf\t\7\2\2\u01ce\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01d3\3\2\2\2\u01d2\u01cc\3\2\2\2")
        buf.write("\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3")
        buf.write("\2\2\2\u01d5|\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8")
        buf.write("\7\62\2\2\u01d8\u01da\t\b\2\2\u01d9\u01db\t\t\2\2\u01da")
        buf.write("\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da\3\2\2\2")
        buf.write("\u01dc\u01dd\3\2\2\2\u01dd\u01e6\3\2\2\2\u01de\u01e0\7")
        buf.write("a\2\2\u01df\u01e1\t\t\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3")
        buf.write("\u01e5\3\2\2\2\u01e4\u01de\3\2\2\2\u01e5\u01e8\3\2\2\2")
        buf.write("\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7~\3\2\2")
        buf.write("\2\u01e8\u01e6\3\2\2\2\u01e9\u01eb\5w<\2\u01ea\u01ec\5")
        buf.write("\u0083B\2\u01eb\u01ea\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01ed\u01ee\b@\7\2\u01ee\u01f6\3\2\2\2")
        buf.write("\u01ef\u01f1\5w<\2\u01f0\u01ef\3\2\2\2\u01f0\u01f1\3\2")
        buf.write("\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\5\u0083B\2\u01f3")
        buf.write("\u01f4\b@\b\2\u01f4\u01f6\3\2\2\2\u01f5\u01e9\3\2\2\2")
        buf.write("\u01f5\u01f0\3\2\2\2\u01f6\u0080\3\2\2\2\u01f7\u01f9\t")
        buf.write("\n\2\2\u01f8\u01fa\t\13\2\2\u01f9\u01f8\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2\u01fb\u01fd\5m\67\2")
        buf.write("\u01fc\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01fc\3")
        buf.write("\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0082\3\2\2\2\u0200\u0204")
        buf.write("\7\60\2\2\u0201\u0203\5m\67\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0208\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0209\5")
        buf.write("\u0081A\2\u0208\u0207\3\2\2\2\u0208\u0209\3\2\2\2\u0209")
        buf.write("\u0084\3\2\2\2\u020a\u020e\7$\2\2\u020b\u020d\5\u0087")
        buf.write("D\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3\2\2\2\u0210")
        buf.write("\u020e\3\2\2\2\u0211\u0212\7$\2\2\u0212\u0213\bC\t\2\u0213")
        buf.write("\u0086\3\2\2\2\u0214\u0219\n\f\2\2\u0215\u0219\5\u0089")
        buf.write("E\2\u0216\u0217\7)\2\2\u0217\u0219\7$\2\2\u0218\u0214")
        buf.write("\3\2\2\2\u0218\u0215\3\2\2\2\u0218\u0216\3\2\2\2\u0219")
        buf.write("\u0088\3\2\2\2\u021a\u021b\7^\2\2\u021b\u021c\t\r\2\2")
        buf.write("\u021c\u008a\3\2\2\2\u021d\u021f\t\16\2\2\u021e\u021d")
        buf.write("\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u021e\3\2\2\2\u0220")
        buf.write("\u0221\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0223\bF\2\2")
        buf.write("\u0223\u008c\3\2\2\2\u0224\u0225\13\2\2\2\u0225\u0226")
        buf.write("\bG\n\2\u0226\u008e\3\2\2\2\u0227\u022b\7$\2\2\u0228\u022a")
        buf.write("\5\u0087D\2\u0229\u0228\3\2\2\2\u022a\u022d\3\2\2\2\u022b")
        buf.write("\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022f\3\2\2\2")
        buf.write("\u022d\u022b\3\2\2\2\u022e\u0230\t\17\2\2\u022f\u022e")
        buf.write("\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0232\bH\13\2\u0232")
        buf.write("\u0090\3\2\2\2\u0233\u0237\7$\2\2\u0234\u0236\5\u0087")
        buf.write("D\2\u0235\u0234\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u023a\3\2\2\2\u0239")
        buf.write("\u0237\3\2\2\2\u023a\u023b\5\u0093J\2\u023b\u023c\bI\f")
        buf.write("\2\u023c\u0092\3\2\2\2\u023d\u023e\7^\2\2\u023e\u0241")
        buf.write("\n\r\2\2\u023f\u0241\n\20\2\2\u0240\u023d\3\2\2\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241\u0094\3\2\2\2\'\2\u009b\u0176\u017c")
        buf.write("\u0181\u0183\u018a\u018c\u019a\u01a1\u01a8\u01ac\u01b0")
        buf.write("\u01b2\u01b8\u01be\u01c2\u01ca\u01d0\u01d4\u01dc\u01e2")
        buf.write("\u01e6\u01eb\u01f0\u01f5\u01f9\u01fe\u0204\u0208\u020e")
        buf.write("\u0218\u0220\u022b\u022f\u0237\u0240\r\b\2\2\3;\2\3;\3")
        buf.write("\3;\4\3;\5\3@\6\3@\7\3C\b\3G\t\3H\n\3I\13")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CMT = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSEIF = 5
    ELSE = 6
    FOREACH = 7
    TRUE = 8
    FALSE = 9
    ARRAY = 10
    IN = 11
    INTTYPE = 12
    FLOATTYPE = 13
    BOOLTYPE = 14
    STRINGTYPE = 15
    RET = 16
    NULL = 17
    CLASS = 18
    VAL = 19
    VAR = 20
    SELF = 21
    CONSTRUCTOR = 22
    DESTRUCTOR = 23
    NEW = 24
    BY = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    NOT = 31
    AND = 32
    OR = 33
    EQ = 34
    ASSIGN = 35
    NEQ = 36
    LT = 37
    LE = 38
    GT = 39
    GE = 40
    ET = 41
    ADDT = 42
    STA = 43
    DOT = 44
    LB = 45
    RB = 46
    LS = 47
    RS = 48
    LP = 49
    RP = 50
    CM = 51
    SM = 52
    CL = 53
    ID = 54
    IDUSD = 55
    INTLIT = 56
    FLOATLIT = 57
    STRINGLIT = 58
    WS = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Self'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", 
            "'+.'", "'::'", "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "CMT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "INTTYPE", "FLOATTYPE", "BOOLTYPE", 
            "STRINGTYPE", "RET", "NULL", "CLASS", "VAL", "VAR", "SELF", 
            "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQ", "ASSIGN", "NEQ", "LT", 
            "LE", "GT", "GE", "ET", "ADDT", "STA", "DOT", "LB", "RB", "LS", 
            "RS", "LP", "RP", "CM", "SM", "CL", "ID", "IDUSD", "INTLIT", 
            "FLOATLIT", "STRINGLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "CMT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "INTTYPE", "FLOATTYPE", 
                  "BOOLTYPE", "STRINGTYPE", "RET", "NULL", "CLASS", "VAL", 
                  "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQ", "ASSIGN", "NEQ", "LT", "LE", "GT", "GE", "ET", "ADDT", 
                  "STA", "DOT", "LB", "RB", "LS", "RS", "LP", "RP", "CM", 
                  "SM", "CL", "DIGITS", "LETTERS", "ID", "IDUSD", "INTLIT", 
                  "INT", "OCT", "HEX", "BIN", "FLOATLIT", "EXP", "DEC", 
                  "STRINGLIT", "STR_CHAR", "ESC_SEQ", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_ILLEGAL" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[57] = self.INTLIT_action 
            actions[62] = self.FLOATLIT_action 
            actions[65] = self.STRINGLIT_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 3:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 5:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	temp = self.text
            	self.text = temp[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

            y = str(self.text)
            p = ['\b', '\t', '\n', '\f', '\r', "'", '\\']
            if y[-1] in p:
                raise UncloseString(y[1:-1])
            else:
                raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])

     


