# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01ea\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\7\2\u0088\n\2\f\2\16\2\u008b\13\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\7\3\u0094\n\3\f\3\16\3\u0097\13\3\3\4\3\4")
        buf.write("\7\4\u009b\n\4\f\4\16\4\u009e\13\4\3\4\5\4\u00a1\n\4\3")
        buf.write("\4\3\4\3\4\3\4\7\4\u00a7\n\4\f\4\16\4\u00aa\13\4\3\4\3")
        buf.write("\4\3\4\7\4\u00af\n\4\f\4\16\4\u00b2\13\4\5\4\u00b4\n\4")
        buf.write("\3\5\6\5\u00b7\n\5\r\5\16\5\u00b8\3\5\3\5\7\5\u00bd\n")
        buf.write("\5\f\5\16\5\u00c0\13\5\5\5\u00c2\n\5\3\5\3\5\3\5\5\5\u00c7")
        buf.write("\n\5\3\5\6\5\u00ca\n\5\r\5\16\5\u00cb\5\5\u00ce\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00d9\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\7\7\u00e1\n\7\f\7\16\7\u00e4\13\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\39\3")
        buf.write("9\39\39\3:\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\6=\u01b7\n=\r")
        buf.write("=\16=\u01b8\3=\3=\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?")
        buf.write("\3?\3?\3?\7?\u01cc\n?\f?\16?\u01cf\13?\3?\3?\3@\3@\3@")
        buf.write("\3@\3@\3@\7@\u01d9\n@\f@\16@\u01dc\13@\3@\3@\3@\3@\3A")
        buf.write("\3A\3A\3A\7A\u01e6\nA\fA\16A\u01e9\13A\4\u0089\u01e7\2")
        buf.write("B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;")
        buf.write("u<w=y>{?}@\177A\u0081B\3\2\21\3\2c|\6\2\62;C\\aac|\3\2")
        buf.write("\63;\3\2\62;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\62")
        buf.write("9\4\2GGgg\4\2--//\4\2$$^^\t\2))^^ddhhppttvv\5\2\13\f\17")
        buf.write("\17\"\"\7\2ddhhppttvv\2\u0205\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u0091\3\2\2")
        buf.write("\2\7\u00b3\3\2\2\2\t\u00b6\3\2\2\2\13\u00d8\3\2\2\2\r")
        buf.write("\u00da\3\2\2\2\17\u00e8\3\2\2\2\21\u00ed\3\2\2\2\23\u00f3")
        buf.write("\3\2\2\2\25\u00fc\3\2\2\2\27\u00ff\3\2\2\2\31\u0104\3")
        buf.write("\2\2\2\33\u010b\3\2\2\2\35\u0113\3\2\2\2\37\u0119\3\2")
        buf.write("\2\2!\u0120\3\2\2\2#\u0129\3\2\2\2%\u012d\3\2\2\2\'\u0136")
        buf.write("\3\2\2\2)\u0139\3\2\2\2+\u0143\3\2\2\2-\u014a\3\2\2\2")
        buf.write("/\u014f\3\2\2\2\61\u0153\3\2\2\2\63\u0159\3\2\2\2\65\u015f")
        buf.write("\3\2\2\2\67\u0161\3\2\2\29\u0163\3\2\2\2;\u0165\3\2\2")
        buf.write("\2=\u0167\3\2\2\2?\u0169\3\2\2\2A\u016b\3\2\2\2C\u016d")
        buf.write("\3\2\2\2E\u016f\3\2\2\2G\u0171\3\2\2\2I\u0173\3\2\2\2")
        buf.write("K\u0175\3\2\2\2M\u0177\3\2\2\2O\u017a\3\2\2\2Q\u017c\3")
        buf.write("\2\2\2S\u017f\3\2\2\2U\u0181\3\2\2\2W\u0184\3\2\2\2Y\u0186")
        buf.write("\3\2\2\2[\u0189\3\2\2\2]\u018b\3\2\2\2_\u018d\3\2\2\2")
        buf.write("a\u0190\3\2\2\2c\u0193\3\2\2\2e\u0195\3\2\2\2g\u0197\3")
        buf.write("\2\2\2i\u019a\3\2\2\2k\u019d\3\2\2\2m\u01a1\3\2\2\2o\u01a4")
        buf.write("\3\2\2\2q\u01a7\3\2\2\2s\u01ab\3\2\2\2u\u01af\3\2\2\2")
        buf.write("w\u01b2\3\2\2\2y\u01b6\3\2\2\2{\u01bc\3\2\2\2}\u01bf\3")
        buf.write("\2\2\2\177\u01d2\3\2\2\2\u0081\u01e1\3\2\2\2\u0083\u0084")
        buf.write("\7,\2\2\u0084\u0085\7,\2\2\u0085\u0089\3\2\2\2\u0086\u0088")
        buf.write("\13\2\2\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008c\3\2\2\2")
        buf.write("\u008b\u0089\3\2\2\2\u008c\u008d\7,\2\2\u008d\u008e\7")
        buf.write(",\2\2\u008e\u008f\3\2\2\2\u008f\u0090\b\2\2\2\u0090\4")
        buf.write("\3\2\2\2\u0091\u0095\t\2\2\2\u0092\u0094\t\3\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\6\3\2\2\2\u0097\u0095\3\2\2")
        buf.write("\2\u0098\u009c\t\4\2\2\u0099\u009b\t\5\2\2\u009a\u0099")
        buf.write("\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u00a1\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009f\u00a1\7\62\2\2\u00a0\u0098\3\2\2\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a1\u00b4\3\2\2\2\u00a2\u00a3\7\62\2\2\u00a3")
        buf.write("\u00a4\t\6\2\2\u00a4\u00a8\t\7\2\2\u00a5\u00a7\t\b\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00b4\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ac\7\62\2\2\u00ac\u00b0\t\t\2\2\u00ad")
        buf.write("\u00af\t\n\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b4\3")
        buf.write("\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00a0\3\2\2\2\u00b3\u00a2")
        buf.write("\3\2\2\2\u00b3\u00ab\3\2\2\2\u00b4\b\3\2\2\2\u00b5\u00b7")
        buf.write("\t\5\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00c1\3\2\2\2")
        buf.write("\u00ba\u00be\7\60\2\2\u00bb\u00bd\t\5\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c1\u00ba\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00cd\3")
        buf.write("\2\2\2\u00c3\u00c6\t\13\2\2\u00c4\u00c7\t\f\2\2\u00c5")
        buf.write("\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2")
        buf.write("\u00c7\u00c9\3\2\2\2\u00c8\u00ca\t\5\2\2\u00c9\u00c8\3")
        buf.write("\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00c3\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\n\3\2\2\2\u00cf\u00d0\7H\2\2\u00d0")
        buf.write("\u00d1\7c\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3")
        buf.write("\u00d9\7g\2\2\u00d4\u00d5\7V\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write("\u00d7\7w\2\2\u00d7\u00d9\7g\2\2\u00d8\u00cf\3\2\2\2\u00d8")
        buf.write("\u00d4\3\2\2\2\u00d9\f\3\2\2\2\u00da\u00e2\7$\2\2\u00db")
        buf.write("\u00e1\n\r\2\2\u00dc\u00dd\7^\2\2\u00dd\u00e1\t\16\2\2")
        buf.write("\u00de\u00df\7)\2\2\u00df\u00e1\7$\2\2\u00e0\u00db\3\2")
        buf.write("\2\2\u00e0\u00dc\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e4")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e5\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6\7$\2\2")
        buf.write("\u00e6\u00e7\b\7\3\2\u00e7\16\3\2\2\2\u00e8\u00e9\7D\2")
        buf.write("\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7f\2\2\u00eb\u00ec\7")
        buf.write("{\2\2\u00ec\20\3\2\2\2\u00ed\u00ee\7D\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7m\2\2\u00f2\22\3\2\2\2\u00f3\u00f4\7E\2\2\u00f4\u00f5")
        buf.write("\7q\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\24\3\2\2\2\u00fc\u00fd\7F\2\2\u00fd\u00fe")
        buf.write("\7q\2\2\u00fe\26\3\2\2\2\u00ff\u0100\7G\2\2\u0100\u0101")
        buf.write("\7n\2\2\u0101\u0102\7u\2\2\u0102\u0103\7g\2\2\u0103\30")
        buf.write("\3\2\2\2\u0104\u0105\7G\2\2\u0105\u0106\7n\2\2\u0106\u0107")
        buf.write("\7u\2\2\u0107\u0108\7g\2\2\u0108\u0109\7K\2\2\u0109\u010a")
        buf.write("\7h\2\2\u010a\32\3\2\2\2\u010b\u010c\7G\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010d\u010e\7f\2\2\u010e\u010f\7D\2\2\u010f\u0110")
        buf.write("\7q\2\2\u0110\u0111\7f\2\2\u0111\u0112\7{\2\2\u0112\34")
        buf.write("\3\2\2\2\u0113\u0114\7G\2\2\u0114\u0115\7p\2\2\u0115\u0116")
        buf.write("\7f\2\2\u0116\u0117\7K\2\2\u0117\u0118\7h\2\2\u0118\36")
        buf.write("\3\2\2\2\u0119\u011a\7G\2\2\u011a\u011b\7p\2\2\u011b\u011c")
        buf.write("\7f\2\2\u011c\u011d\7H\2\2\u011d\u011e\7q\2\2\u011e\u011f")
        buf.write("\7t\2\2\u011f \3\2\2\2\u0120\u0121\7G\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122\u0123\7f\2\2\u0123\u0124\7Y\2\2\u0124\u0125")
        buf.write("\7j\2\2\u0125\u0126\7k\2\2\u0126\u0127\7n\2\2\u0127\u0128")
        buf.write("\7g\2\2\u0128\"\3\2\2\2\u0129\u012a\7H\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\u012c\7t\2\2\u012c$\3\2\2\2\u012d\u012e")
        buf.write("\7H\2\2\u012e\u012f\7w\2\2\u012f\u0130\7p\2\2\u0130\u0131")
        buf.write("\7e\2\2\u0131\u0132\7v\2\2\u0132\u0133\7k\2\2\u0133\u0134")
        buf.write("\7q\2\2\u0134\u0135\7p\2\2\u0135&\3\2\2\2\u0136\u0137")
        buf.write("\7K\2\2\u0137\u0138\7h\2\2\u0138(\3\2\2\2\u0139\u013a")
        buf.write("\7R\2\2\u013a\u013b\7c\2\2\u013b\u013c\7t\2\2\u013c\u013d")
        buf.write("\7c\2\2\u013d\u013e\7o\2\2\u013e\u013f\7g\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140\u0141\7g\2\2\u0141\u0142\7t\2\2\u0142*\3")
        buf.write("\2\2\2\u0143\u0144\7T\2\2\u0144\u0145\7g\2\2\u0145\u0146")
        buf.write("\7v\2\2\u0146\u0147\7w\2\2\u0147\u0148\7t\2\2\u0148\u0149")
        buf.write("\7p\2\2\u0149,\3\2\2\2\u014a\u014b\7V\2\2\u014b\u014c")
        buf.write("\7j\2\2\u014c\u014d\7g\2\2\u014d\u014e\7p\2\2\u014e.\3")
        buf.write("\2\2\2\u014f\u0150\7X\2\2\u0150\u0151\7c\2\2\u0151\u0152")
        buf.write("\7t\2\2\u0152\60\3\2\2\2\u0153\u0154\7Y\2\2\u0154\u0155")
        buf.write("\7j\2\2\u0155\u0156\7k\2\2\u0156\u0157\7n\2\2\u0157\u0158")
        buf.write("\7g\2\2\u0158\62\3\2\2\2\u0159\u015a\7G\2\2\u015a\u015b")
        buf.write("\7p\2\2\u015b\u015c\7f\2\2\u015c\u015d\7F\2\2\u015d\u015e")
        buf.write("\7q\2\2\u015e\64\3\2\2\2\u015f\u0160\7}\2\2\u0160\66\3")
        buf.write("\2\2\2\u0161\u0162\7\177\2\2\u01628\3\2\2\2\u0163\u0164")
        buf.write("\7]\2\2\u0164:\3\2\2\2\u0165\u0166\7_\2\2\u0166<\3\2\2")
        buf.write("\2\u0167\u0168\7*\2\2\u0168>\3\2\2\2\u0169\u016a\7+\2")
        buf.write("\2\u016a@\3\2\2\2\u016b\u016c\7\60\2\2\u016cB\3\2\2\2")
        buf.write("\u016d\u016e\7=\2\2\u016eD\3\2\2\2\u016f\u0170\7.\2\2")
        buf.write("\u0170F\3\2\2\2\u0171\u0172\7<\2\2\u0172H\3\2\2\2\u0173")
        buf.write("\u0174\7?\2\2\u0174J\3\2\2\2\u0175\u0176\7,\2\2\u0176")
        buf.write("L\3\2\2\2\u0177\u0178\7,\2\2\u0178\u0179\7\60\2\2\u0179")
        buf.write("N\3\2\2\2\u017a\u017b\7/\2\2\u017bP\3\2\2\2\u017c\u017d")
        buf.write("\7/\2\2\u017d\u017e\7\60\2\2\u017eR\3\2\2\2\u017f\u0180")
        buf.write("\7-\2\2\u0180T\3\2\2\2\u0181\u0182\7-\2\2\u0182\u0183")
        buf.write("\7\60\2\2\u0183V\3\2\2\2\u0184\u0185\7^\2\2\u0185X\3\2")
        buf.write("\2\2\u0186\u0187\7^\2\2\u0187\u0188\7\60\2\2\u0188Z\3")
        buf.write("\2\2\2\u0189\u018a\7\'\2\2\u018a\\\3\2\2\2\u018b\u018c")
        buf.write("\7#\2\2\u018c^\3\2\2\2\u018d\u018e\7?\2\2\u018e\u018f")
        buf.write("\7?\2\2\u018f`\3\2\2\2\u0190\u0191\7#\2\2\u0191\u0192")
        buf.write("\7?\2\2\u0192b\3\2\2\2\u0193\u0194\7>\2\2\u0194d\3\2\2")
        buf.write("\2\u0195\u0196\7@\2\2\u0196f\3\2\2\2\u0197\u0198\7>\2")
        buf.write("\2\u0198\u0199\7?\2\2\u0199h\3\2\2\2\u019a\u019b\7@\2")
        buf.write("\2\u019b\u019c\7?\2\2\u019cj\3\2\2\2\u019d\u019e\7?\2")
        buf.write("\2\u019e\u019f\7\61\2\2\u019f\u01a0\7?\2\2\u01a0l\3\2")
        buf.write("\2\2\u01a1\u01a2\7>\2\2\u01a2\u01a3\7\60\2\2\u01a3n\3")
        buf.write("\2\2\2\u01a4\u01a5\7@\2\2\u01a5\u01a6\7\60\2\2\u01a6p")
        buf.write("\3\2\2\2\u01a7\u01a8\7>\2\2\u01a8\u01a9\7?\2\2\u01a9\u01aa")
        buf.write("\7\60\2\2\u01aar\3\2\2\2\u01ab\u01ac\7@\2\2\u01ac\u01ad")
        buf.write("\7?\2\2\u01ad\u01ae\7\60\2\2\u01aet\3\2\2\2\u01af\u01b0")
        buf.write("\7(\2\2\u01b0\u01b1\7(\2\2\u01b1v\3\2\2\2\u01b2\u01b3")
        buf.write("\7~\2\2\u01b3\u01b4\7~\2\2\u01b4x\3\2\2\2\u01b5\u01b7")
        buf.write("\t\17\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\3\2\2\2")
        buf.write("\u01ba\u01bb\b=\2\2\u01bbz\3\2\2\2\u01bc\u01bd\13\2\2")
        buf.write("\2\u01bd\u01be\b>\4\2\u01be|\3\2\2\2\u01bf\u01cd\7$\2")
        buf.write("\2\u01c0\u01cc\n\r\2\2\u01c1\u01cc\7\f\2\2\u01c2\u01c3")
        buf.write("\7>\2\2\u01c3\u01c4\7G\2\2\u01c4\u01c5\7Q\2\2\u01c5\u01c6")
        buf.write("\7H\2\2\u01c6\u01cc\7@\2\2\u01c7\u01c8\7^\2\2\u01c8\u01cc")
        buf.write("\t\16\2\2\u01c9\u01ca\7)\2\2\u01ca\u01cc\7$\2\2\u01cb")
        buf.write("\u01c0\3\2\2\2\u01cb\u01c1\3\2\2\2\u01cb\u01c2\3\2\2\2")
        buf.write("\u01cb\u01c7\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cf\3")
        buf.write("\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d0")
        buf.write("\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1\b?\5\2\u01d1")
        buf.write("~\3\2\2\2\u01d2\u01da\7$\2\2\u01d3\u01d9\n\r\2\2\u01d4")
        buf.write("\u01d5\7^\2\2\u01d5\u01d9\t\16\2\2\u01d6\u01d7\7)\2\2")
        buf.write("\u01d7\u01d9\7$\2\2\u01d8\u01d3\3\2\2\2\u01d8\u01d4\3")
        buf.write("\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dd\3\2\2\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dd\u01de\7^\2\2\u01de\u01df\n\20\2\2")
        buf.write("\u01df\u01e0\b@\6\2\u01e0\u0080\3\2\2\2\u01e1\u01e2\7")
        buf.write(",\2\2\u01e2\u01e3\7,\2\2\u01e3\u01e7\3\2\2\2\u01e4\u01e6")
        buf.write("\13\2\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u0082\3\2\2\2")
        buf.write("\u01e9\u01e7\3\2\2\2\32\2\u0089\u0095\u009c\u00a0\u00a6")
        buf.write("\u00a8\u00b0\u00b3\u00b8\u00be\u00c1\u00c6\u00cb\u00cd")
        buf.write("\u00d8\u00e0\u00e2\u01b8\u01cb\u01cd\u01d8\u01da\u01e7")
        buf.write("\7\b\2\2\3\7\2\3>\3\3?\4\3@\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    ID = 2
    INTEGER = 3
    FLOAT = 4
    BOOL = 5
    STRING = 6
    BODY = 7
    BREAK = 8
    CONTINUE = 9
    DO = 10
    ELSE = 11
    ELSEIF = 12
    ENDBODY = 13
    ENDIF = 14
    ENDFOR = 15
    ENDWHILE = 16
    FOR = 17
    FUNCTION = 18
    IF = 19
    PARAMETER = 20
    RETURN = 21
    THEN = 22
    VAR = 23
    WHILE = 24
    ENDDO = 25
    LB = 26
    RB = 27
    LSB = 28
    RSB = 29
    LP = 30
    RP = 31
    DOT = 32
    SM = 33
    CM = 34
    CL = 35
    EQ = 36
    MUL = 37
    MULFLOAT = 38
    SUB = 39
    SUBFLOAT = 40
    ADD = 41
    ADDFLOAT = 42
    DIV = 43
    DIVFLOAT = 44
    PERCENT = 45
    NOT = 46
    ASSIGN = 47
    NOTEQ = 48
    LT = 49
    GT = 50
    LET = 51
    GET = 52
    ASSIGNFLOAT = 53
    LTFLOAT = 54
    GTFLOAT = 55
    LETFLOAT = 56
    GETFLOAT = 57
    AND = 58
    OR = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    UNTERMINATED_COMMENT = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'EndDo'", "'{'", "'}'", "'['", "']'", "'('", "')'", "'.'", 
            "';'", "','", "':'", "'='", "'*'", "'*.'", "'-'", "'-.'", "'+'", 
            "'+.'", "'\\'", "'\\.'", "'%'", "'!'", "'=='", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
            "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "ID", "INTEGER", "FLOAT", "BOOL", "STRING", "BODY", 
            "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
            "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "LB", "RB", "LSB", 
            "RSB", "LP", "RP", "DOT", "SM", "CM", "CL", "EQ", "MUL", "MULFLOAT", 
            "SUB", "SUBFLOAT", "ADD", "ADDFLOAT", "DIV", "DIVFLOAT", "PERCENT", 
            "NOT", "ASSIGN", "NOTEQ", "LT", "GT", "LET", "GET", "ASSIGNFLOAT", 
            "LTFLOAT", "GTFLOAT", "LETFLOAT", "GETFLOAT", "AND", "OR", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "COMMENT", "ID", "INTEGER", "FLOAT", "BOOL", "STRING", 
                  "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                  "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", 
                  "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "ENDDO", 
                  "LB", "RB", "LSB", "RSB", "LP", "RP", "DOT", "SM", "CM", 
                  "CL", "EQ", "MUL", "MULFLOAT", "SUB", "SUBFLOAT", "ADD", 
                  "ADDFLOAT", "DIV", "DIVFLOAT", "PERCENT", "NOT", "ASSIGN", 
                  "NOTEQ", "LT", "GT", "LET", "GET", "ASSIGNFLOAT", "LTFLOAT", 
                  "GTFLOAT", "LETFLOAT", "GETFLOAT", "AND", "OR", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.STRING_action 
            actions[60] = self.ERROR_CHAR_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             raise ErrorToken(self.text) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     


