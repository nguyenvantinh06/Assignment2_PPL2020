# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u018a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\3\2\6\2N\n\2\r\2\16\2O\3\2\3\2\3\3\3\3\5\3V\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5`\n\5\f\5\16\5c\13\5\3")
        buf.write("\6\3\6\5\6g\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7p\n\7\5")
        buf.write("\7r\n\7\3\b\3\b\3\b\3\b\3\b\6\by\n\b\r\b\16\bz\3\b\3\b")
        buf.write("\5\b\177\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u0088\n\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0090\n\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\7\f\u0097\n\f\f\f\16\f\u009a\13\f\3\r")
        buf.write("\3\r\3\r\3\r\7\r\u00a0\n\r\f\r\16\r\u00a3\13\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\7\17\u00ac\n\17\f\17\16\17")
        buf.write("\u00af\13\17\3\17\7\17\u00b2\n\17\f\17\16\17\u00b5\13")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00c0\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\7\21\u00cb\n\21\f\21\16\21\u00ce\13\21\3\21\3\21\5")
        buf.write("\21\u00d2\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\7\27\u00ff\n\27\f\27\16\27\u0102\13\27\5\27")
        buf.write("\u0104\n\27\3\27\3\27\3\27\3\30\3\30\5\30\u010b\n\30\3")
        buf.write("\30\3\30\3\31\3\31\5\31\u0111\n\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\7\32\u011c\n\32\f\32\16\32\u011f")
        buf.write("\13\32\5\32\u0121\n\32\3\32\3\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u012b\n\33\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0132\n\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u013a\n")
        buf.write("\35\f\35\16\35\u013d\13\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\7\36\u0145\n\36\f\36\16\36\u0148\13\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\7\37\u0150\n\37\f\37\16\37\u0153\13")
        buf.write("\37\3 \3 \3 \5 \u0158\n \3!\3!\3!\5!\u015d\n!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\6\"\u0164\n\"\r\"\16\"\u0165\3\"\5\"\u0169")
        buf.write("\n\"\3#\3#\5#\u016d\n#\3$\3$\3$\3$\3$\5$\u0174\n$\3%\3")
        buf.write("%\3%\3%\3%\5%\u017b\n%\3&\3&\3&\3&\7&\u0181\n&\f&\16&")
        buf.write("\u0184\13&\5&\u0186\n&\3&\3&\3&\2\58:<\'\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJ\2\7\3\2\61;\3\2<=\3\2),\4\2\'(-/\3\2)*\2\u019d\2M\3")
        buf.write("\2\2\2\4U\3\2\2\2\6W\3\2\2\2\b\\\3\2\2\2\nf\3\2\2\2\f")
        buf.write("h\3\2\2\2\16s\3\2\2\2\20\u0080\3\2\2\2\22\u0087\3\2\2")
        buf.write("\2\24\u0089\3\2\2\2\26\u0093\3\2\2\2\30\u009b\3\2\2\2")
        buf.write("\32\u00a4\3\2\2\2\34\u00ad\3\2\2\2\36\u00bf\3\2\2\2 \u00c1")
        buf.write("\3\2\2\2\"\u00d6\3\2\2\2$\u00e5\3\2\2\2&\u00ec\3\2\2\2")
        buf.write("(\u00f3\3\2\2\2*\u00f6\3\2\2\2,\u00f9\3\2\2\2.\u0108\3")
        buf.write("\2\2\2\60\u0110\3\2\2\2\62\u0116\3\2\2\2\64\u012a\3\2")
        buf.write("\2\2\66\u0131\3\2\2\28\u0133\3\2\2\2:\u013e\3\2\2\2<\u0149")
        buf.write("\3\2\2\2>\u0157\3\2\2\2@\u015c\3\2\2\2B\u0168\3\2\2\2")
        buf.write("D\u016c\3\2\2\2F\u0173\3\2\2\2H\u017a\3\2\2\2J\u017c\3")
        buf.write("\2\2\2LN\5\4\3\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2")
        buf.write("\2PQ\3\2\2\2QR\7\2\2\3R\3\3\2\2\2SV\5\6\4\2TV\5\24\13")
        buf.write("\2US\3\2\2\2UT\3\2\2\2V\5\3\2\2\2WX\7\31\2\2XY\7%\2\2")
        buf.write("YZ\5\b\5\2Z[\7#\2\2[\7\3\2\2\2\\a\5\n\6\2]^\7$\2\2^`\5")
        buf.write("\n\6\2_]\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\t\3\2")
        buf.write("\2\2ca\3\2\2\2dg\5\f\7\2eg\5\16\b\2fd\3\2\2\2fe\3\2\2")
        buf.write("\2g\13\3\2\2\2hq\7\4\2\2io\7&\2\2jp\7\6\2\2kp\7\5\2\2")
        buf.write("lp\7\b\2\2mp\7\7\2\2np\5J&\2oj\3\2\2\2ok\3\2\2\2ol\3\2")
        buf.write("\2\2om\3\2\2\2on\3\2\2\2pr\3\2\2\2qi\3\2\2\2qr\3\2\2\2")
        buf.write("r\r\3\2\2\2sx\7\4\2\2tu\7\36\2\2uv\5\20\t\2vw\7\37\2\2")
        buf.write("wy\3\2\2\2xt\3\2\2\2yz\3\2\2\2zx\3\2\2\2z{\3\2\2\2{~\3")
        buf.write("\2\2\2|}\7&\2\2}\177\5\22\n\2~|\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\17\3\2\2\2\u0080\u0081\7\5\2\2\u0081\21\3\2\2\2\u0082")
        buf.write("\u0088\7\6\2\2\u0083\u0088\7\5\2\2\u0084\u0088\7\b\2\2")
        buf.write("\u0085\u0088\7\7\2\2\u0086\u0088\5J&\2\u0087\u0082\3\2")
        buf.write("\2\2\u0087\u0083\3\2\2\2\u0087\u0084\3\2\2\2\u0087\u0085")
        buf.write("\3\2\2\2\u0087\u0086\3\2\2\2\u0088\23\3\2\2\2\u0089\u008a")
        buf.write("\7\24\2\2\u008a\u008b\7%\2\2\u008b\u008f\7\4\2\2\u008c")
        buf.write("\u008d\7\26\2\2\u008d\u008e\7%\2\2\u008e\u0090\5\26\f")
        buf.write("\2\u008f\u008c\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0092\5\32\16\2\u0092\25\3\2\2\2\u0093")
        buf.write("\u0098\5\30\r\2\u0094\u0095\7$\2\2\u0095\u0097\5\30\r")
        buf.write("\2\u0096\u0094\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\27\3\2\2\2\u009a\u0098")
        buf.write("\3\2\2\2\u009b\u00a1\7\4\2\2\u009c\u009d\7\36\2\2\u009d")
        buf.write("\u009e\7\5\2\2\u009e\u00a0\7\37\2\2\u009f\u009c\3\2\2")
        buf.write("\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\31\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5")
        buf.write("\7\t\2\2\u00a5\u00a6\7%\2\2\u00a6\u00a7\5\34\17\2\u00a7")
        buf.write("\u00a8\7\17\2\2\u00a8\u00a9\7\"\2\2\u00a9\33\3\2\2\2\u00aa")
        buf.write("\u00ac\5\6\4\2\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2")
        buf.write("\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b3\3")
        buf.write("\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b2\5\36\20\2\u00b1")
        buf.write("\u00b0\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4\35\3\2\2\2\u00b5\u00b3\3\2")
        buf.write("\2\2\u00b6\u00c0\5\60\31\2\u00b7\u00c0\5 \21\2\u00b8\u00c0")
        buf.write("\5\"\22\2\u00b9\u00c0\5$\23\2\u00ba\u00c0\5&\24\2\u00bb")
        buf.write("\u00c0\5(\25\2\u00bc\u00c0\5*\26\2\u00bd\u00c0\5,\27\2")
        buf.write("\u00be\u00c0\5.\30\2\u00bf\u00b6\3\2\2\2\u00bf\u00b7\3")
        buf.write("\2\2\2\u00bf\u00b8\3\2\2\2\u00bf\u00b9\3\2\2\2\u00bf\u00ba")
        buf.write("\3\2\2\2\u00bf\u00bb\3\2\2\2\u00bf\u00bc\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\37\3\2\2\2\u00c1")
        buf.write("\u00c2\7\25\2\2\u00c2\u00c3\5\66\34\2\u00c3\u00c4\7\30")
        buf.write("\2\2\u00c4\u00cc\5\34\17\2\u00c5\u00c6\7\16\2\2\u00c6")
        buf.write("\u00c7\5\66\34\2\u00c7\u00c8\7\30\2\2\u00c8\u00c9\5\34")
        buf.write("\17\2\u00c9\u00cb\3\2\2\2\u00ca\u00c5\3\2\2\2\u00cb\u00ce")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00d1\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7\r\2\2")
        buf.write("\u00d0\u00d2\5\34\17\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\7\20\2\2\u00d4")
        buf.write("\u00d5\7\"\2\2\u00d5!\3\2\2\2\u00d6\u00d7\7\23\2\2\u00d7")
        buf.write("\u00d8\7 \2\2\u00d8\u00d9\5\f\7\2\u00d9\u00da\7&\2\2\u00da")
        buf.write("\u00db\5\66\34\2\u00db\u00dc\7$\2\2\u00dc\u00dd\5\66\34")
        buf.write("\2\u00dd\u00de\7$\2\2\u00de\u00df\5\66\34\2\u00df\u00e0")
        buf.write("\7!\2\2\u00e0\u00e1\7\f\2\2\u00e1\u00e2\5\34\17\2\u00e2")
        buf.write("\u00e3\7\21\2\2\u00e3\u00e4\7\"\2\2\u00e4#\3\2\2\2\u00e5")
        buf.write("\u00e6\7\32\2\2\u00e6\u00e7\5\66\34\2\u00e7\u00e8\7\f")
        buf.write("\2\2\u00e8\u00e9\5\34\17\2\u00e9\u00ea\7\22\2\2\u00ea")
        buf.write("\u00eb\7\"\2\2\u00eb%\3\2\2\2\u00ec\u00ed\7\f\2\2\u00ed")
        buf.write("\u00ee\5\34\17\2\u00ee\u00ef\7\32\2\2\u00ef\u00f0\5\66")
        buf.write("\34\2\u00f0\u00f1\7\33\2\2\u00f1\u00f2\7\"\2\2\u00f2\'")
        buf.write("\3\2\2\2\u00f3\u00f4\7\n\2\2\u00f4\u00f5\7#\2\2\u00f5")
        buf.write(")\3\2\2\2\u00f6\u00f7\7\13\2\2\u00f7\u00f8\7#\2\2\u00f8")
        buf.write("+\3\2\2\2\u00f9\u00fa\7\4\2\2\u00fa\u0103\7 \2\2\u00fb")
        buf.write("\u0100\5\66\34\2\u00fc\u00fd\7$\2\2\u00fd\u00ff\5\66\34")
        buf.write("\2\u00fe\u00fc\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0104\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0103\u00fb\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u0105\3\2\2\2\u0105\u0106\7!\2\2\u0106\u0107\7")
        buf.write("#\2\2\u0107-\3\2\2\2\u0108\u010a\7\27\2\2\u0109\u010b")
        buf.write("\5\66\34\2\u010a\u0109\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u010c\3\2\2\2\u010c\u010d\7#\2\2\u010d/\3\2\2\2\u010e")
        buf.write("\u0111\7\4\2\2\u010f\u0111\5B\"\2\u0110\u010e\3\2\2\2")
        buf.write("\u0110\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7")
        buf.write("&\2\2\u0113\u0114\5\66\34\2\u0114\u0115\7#\2\2\u0115\61")
        buf.write("\3\2\2\2\u0116\u0117\7\4\2\2\u0117\u0120\7 \2\2\u0118")
        buf.write("\u011d\5\66\34\2\u0119\u011a\7$\2\2\u011a\u011c\5\66\34")
        buf.write("\2\u011b\u0119\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0121\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u0120\u0118\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0123\7!\2\2\u0123\63\3\2\2")
        buf.write("\2\u0124\u012b\7\5\2\2\u0125\u012b\7\6\2\2\u0126\u012b")
        buf.write("\7\4\2\2\u0127\u012b\7\b\2\2\u0128\u012b\7\7\2\2\u0129")
        buf.write("\u012b\5J&\2\u012a\u0124\3\2\2\2\u012a\u0125\3\2\2\2\u012a")
        buf.write("\u0126\3\2\2\2\u012a\u0127\3\2\2\2\u012a\u0128\3\2\2\2")
        buf.write("\u012a\u0129\3\2\2\2\u012b\65\3\2\2\2\u012c\u012d\58\35")
        buf.write("\2\u012d\u012e\t\2\2\2\u012e\u012f\58\35\2\u012f\u0132")
        buf.write("\3\2\2\2\u0130\u0132\58\35\2\u0131\u012c\3\2\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132\67\3\2\2\2\u0133\u0134\b\35\1\2\u0134")
        buf.write("\u0135\5:\36\2\u0135\u013b\3\2\2\2\u0136\u0137\f\4\2\2")
        buf.write("\u0137\u0138\t\3\2\2\u0138\u013a\5:\36\2\u0139\u0136\3")
        buf.write("\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c")
        buf.write("\3\2\2\2\u013c9\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f")
        buf.write("\b\36\1\2\u013f\u0140\5<\37\2\u0140\u0146\3\2\2\2\u0141")
        buf.write("\u0142\f\4\2\2\u0142\u0143\t\4\2\2\u0143\u0145\5<\37\2")
        buf.write("\u0144\u0141\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3")
        buf.write("\2\2\2\u0146\u0147\3\2\2\2\u0147;\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0149\u014a\b\37\1\2\u014a\u014b\5> \2\u014b")
        buf.write("\u0151\3\2\2\2\u014c\u014d\f\4\2\2\u014d\u014e\t\5\2\2")
        buf.write("\u014e\u0150\5> \2\u014f\u014c\3\2\2\2\u0150\u0153\3\2")
        buf.write("\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152=\3")
        buf.write("\2\2\2\u0153\u0151\3\2\2\2\u0154\u0155\7\60\2\2\u0155")
        buf.write("\u0158\5> \2\u0156\u0158\5@!\2\u0157\u0154\3\2\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158?\3\2\2\2\u0159\u015a\t\6\2\2\u015a")
        buf.write("\u015d\5@!\2\u015b\u015d\5B\"\2\u015c\u0159\3\2\2\2\u015c")
        buf.write("\u015b\3\2\2\2\u015dA\3\2\2\2\u015e\u0163\5D#\2\u015f")
        buf.write("\u0160\7\36\2\2\u0160\u0161\5\66\34\2\u0161\u0162\7\37")
        buf.write("\2\2\u0162\u0164\3\2\2\2\u0163\u015f\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write("\u0169\3\2\2\2\u0167\u0169\5D#\2\u0168\u015e\3\2\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169C\3\2\2\2\u016a\u016d\5\62\32\2\u016b")
        buf.write("\u016d\5F$\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("E\3\2\2\2\u016e\u016f\7 \2\2\u016f\u0170\5\66\34\2\u0170")
        buf.write("\u0171\7!\2\2\u0171\u0174\3\2\2\2\u0172\u0174\5\64\33")
        buf.write("\2\u0173\u016e\3\2\2\2\u0173\u0172\3\2\2\2\u0174G\3\2")
        buf.write("\2\2\u0175\u017b\7\5\2\2\u0176\u017b\7\b\2\2\u0177\u017b")
        buf.write("\7\7\2\2\u0178\u017b\7\6\2\2\u0179\u017b\5J&\2\u017a\u0175")
        buf.write("\3\2\2\2\u017a\u0176\3\2\2\2\u017a\u0177\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017bI\3\2\2\2\u017c")
        buf.write("\u0185\7\34\2\2\u017d\u0182\5H%\2\u017e\u017f\7$\2\2\u017f")
        buf.write("\u0181\5H%\2\u0180\u017e\3\2\2\2\u0181\u0184\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0186\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0185\u017d\3\2\2\2\u0185\u0186\3")
        buf.write("\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\7\35\2\2\u0188")
        buf.write("K\3\2\2\2\'OUafoqz~\u0087\u008f\u0098\u00a1\u00ad\u00b3")
        buf.write("\u00bf\u00cc\u00d1\u0100\u0103\u010a\u0110\u011d\u0120")
        buf.write("\u012a\u0131\u013b\u0146\u0151\u0157\u015c\u0165\u0168")
        buf.write("\u016c\u0173\u017a\u0182\u0185")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", 
                     "'While'", "'EndDo'", "'{'", "'}'", "'['", "']'", "'('", 
                     "')'", "'.'", "';'", "','", "':'", "'='", "'*'", "'*.'", 
                     "'-'", "'-.'", "'+'", "'+.'", "'\\'", "'\\.'", "'%'", 
                     "'!'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'&&'", 
                     "'||'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "ID", "INTEGER", "FLOAT", 
                      "BOOL", "STRING", "BODY", "BREAK", "CONTINUE", "DO", 
                      "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "ENDDO", "LB", "RB", "LSB", "RSB", 
                      "LP", "RP", "DOT", "SM", "CM", "CL", "EQ", "MUL", 
                      "MULFLOAT", "SUB", "SUBFLOAT", "ADD", "ADDFLOAT", 
                      "DIV", "DIVFLOAT", "PERCENT", "NOT", "ASSIGN", "NOTEQ", 
                      "LT", "GT", "LET", "GET", "ASSIGNFLOAT", "LTFLOAT", 
                      "GTFLOAT", "LETFLOAT", "GETFLOAT", "AND", "OR", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_var_declare = 2
    RULE_variable_list = 3
    RULE_variable = 4
    RULE_scalar = 5
    RULE_composit = 6
    RULE_intbkit = 7
    RULE_typebkit = 8
    RULE_function_declare = 9
    RULE_parameter_list = 10
    RULE_param_id = 11
    RULE_body = 12
    RULE_stmt_list = 13
    RULE_function_list = 14
    RULE_if_stmt = 15
    RULE_for_stmt = 16
    RULE_while_stmt = 17
    RULE_do_while_stmt = 18
    RULE_break_stmt = 19
    RULE_continue_stmt = 20
    RULE_call_stmt = 21
    RULE_return_stmt = 22
    RULE_assign_stmt = 23
    RULE_function_call = 24
    RULE_exp9 = 25
    RULE_exp = 26
    RULE_exp1 = 27
    RULE_exp2 = 28
    RULE_exp3 = 29
    RULE_exp4 = 30
    RULE_exp5 = 31
    RULE_exp6 = 32
    RULE_exp7 = 33
    RULE_exp8 = 34
    RULE_array = 35
    RULE_array_list = 36

    ruleNames =  [ "program", "declaration", "var_declare", "variable_list", 
                   "variable", "scalar", "composit", "intbkit", "typebkit", 
                   "function_declare", "parameter_list", "param_id", "body", 
                   "stmt_list", "function_list", "if_stmt", "for_stmt", 
                   "while_stmt", "do_while_stmt", "break_stmt", "continue_stmt", 
                   "call_stmt", "return_stmt", "assign_stmt", "function_call", 
                   "exp9", "exp", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "array", "array_list" ]

    EOF = Token.EOF
    COMMENT=1
    ID=2
    INTEGER=3
    FLOAT=4
    BOOL=5
    STRING=6
    BODY=7
    BREAK=8
    CONTINUE=9
    DO=10
    ELSE=11
    ELSEIF=12
    ENDBODY=13
    ENDIF=14
    ENDFOR=15
    ENDWHILE=16
    FOR=17
    FUNCTION=18
    IF=19
    PARAMETER=20
    RETURN=21
    THEN=22
    VAR=23
    WHILE=24
    ENDDO=25
    LB=26
    RB=27
    LSB=28
    RSB=29
    LP=30
    RP=31
    DOT=32
    SM=33
    CM=34
    CL=35
    EQ=36
    MUL=37
    MULFLOAT=38
    SUB=39
    SUBFLOAT=40
    ADD=41
    ADDFLOAT=42
    DIV=43
    DIVFLOAT=44
    PERCENT=45
    NOT=46
    ASSIGN=47
    NOTEQ=48
    LT=49
    GT=50
    LET=51
    GET=52
    ASSIGNFLOAT=53
    LTFLOAT=54
    GTFLOAT=55
    LETFLOAT=56
    GETFLOAT=57
    AND=58
    OR=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    UNTERMINATED_COMMENT=64

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
            return self.getToken(BKITParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(BKITParser.DeclarationContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.declaration()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.FUNCTION or _la==BKITParser.VAR):
                    break

            self.state = 79
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def function_declare(self):
            return self.getTypedRuleContext(BKITParser.Function_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = BKITParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.var_declare()
                pass
            elif token in [BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.function_declare()
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


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def CL(self):
            return self.getToken(BKITParser.CL, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(BKITParser.VAR)
            self.state = 86
            self.match(BKITParser.CL)
            self.state = 87
            self.variable_list()
            self.state = 88
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VariableContext)
            else:
                return self.getTypedRuleContext(BKITParser.VariableContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list" ):
                return visitor.visitVariable_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_list(self):

        localctx = BKITParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.variable()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 91
                self.match(BKITParser.CM)
                self.state = 92
                self.variable()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar(self):
            return self.getTypedRuleContext(BKITParser.ScalarContext,0)


        def composit(self):
            return self.getTypedRuleContext(BKITParser.CompositContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.scalar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.composit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def BOOL(self):
            return self.getToken(BKITParser.BOOL, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar" ):
                return visitor.visitScalar(self)
            else:
                return visitor.visitChildren(self)




    def scalar(self):

        localctx = BKITParser.ScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_scalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BKITParser.ID)
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 103
                self.match(BKITParser.EQ)
                self.state = 109
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.FLOAT]:
                    self.state = 104
                    self.match(BKITParser.FLOAT)
                    pass
                elif token in [BKITParser.INTEGER]:
                    self.state = 105
                    self.match(BKITParser.INTEGER)
                    pass
                elif token in [BKITParser.STRING]:
                    self.state = 106
                    self.match(BKITParser.STRING)
                    pass
                elif token in [BKITParser.BOOL]:
                    self.state = 107
                    self.match(BKITParser.BOOL)
                    pass
                elif token in [BKITParser.LB]:
                    self.state = 108
                    self.array_list()
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


    class CompositContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def intbkit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.IntbkitContext)
            else:
                return self.getTypedRuleContext(BKITParser.IntbkitContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def typebkit(self):
            return self.getTypedRuleContext(BKITParser.TypebkitContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposit" ):
                return visitor.visitComposit(self)
            else:
                return visitor.visitChildren(self)




    def composit(self):

        localctx = BKITParser.CompositContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_composit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(BKITParser.ID)
            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.match(BKITParser.LSB)
                self.state = 115
                self.intbkit()
                self.state = 116
                self.match(BKITParser.RSB)
                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LSB):
                    break

            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.EQ:
                self.state = 122
                self.match(BKITParser.EQ)

                self.state = 123
                self.typebkit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntbkitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_intbkit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntbkit" ):
                return visitor.visitIntbkit(self)
            else:
                return visitor.visitChildren(self)




    def intbkit(self):

        localctx = BKITParser.IntbkitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_intbkit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(BKITParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypebkitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def BOOL(self):
            return self.getToken(BKITParser.BOOL, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_typebkit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypebkit" ):
                return visitor.visitTypebkit(self)
            else:
                return visitor.visitChildren(self)




    def typebkit(self):

        localctx = BKITParser.TypebkitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typebkit)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.match(BKITParser.STRING)
                pass
            elif token in [BKITParser.BOOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.match(BKITParser.BOOL)
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.array_list()
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


    class Function_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def CL(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CL)
            else:
                return self.getToken(BKITParser.CL, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(BKITParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declare" ):
                return visitor.visitFunction_declare(self)
            else:
                return visitor.visitChildren(self)




    def function_declare(self):

        localctx = BKITParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(BKITParser.FUNCTION)
            self.state = 136
            self.match(BKITParser.CL)
            self.state = 137
            self.match(BKITParser.ID)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 138
                self.match(BKITParser.PARAMETER)
                self.state = 139
                self.match(BKITParser.CL)
                self.state = 140
                self.parameter_list()


            self.state = 143
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Param_idContext)
            else:
                return self.getTypedRuleContext(BKITParser.Param_idContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = BKITParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.param_id()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 146
                self.match(BKITParser.CM)
                self.state = 147
                self.param_id()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTEGER)
            else:
                return self.getToken(BKITParser.INTEGER, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_id" ):
                return visitor.visitParam_id(self)
            else:
                return visitor.visitChildren(self)




    def param_id(self):

        localctx = BKITParser.Param_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(BKITParser.ID)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 154
                self.match(BKITParser.LSB)

                self.state = 155
                self.match(BKITParser.INTEGER)
                self.state = 156
                self.match(BKITParser.RSB)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def CL(self):
            return self.getToken(BKITParser.CL, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(BKITParser.BODY)
            self.state = 163
            self.match(BKITParser.CL)
            self.state = 164
            self.stmt_list()
            self.state = 165
            self.match(BKITParser.ENDBODY)
            self.state = 166
            self.match(BKITParser.DOT)
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

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def function_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Function_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Function_listContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 168
                self.var_declare()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 174
                    self.function_list() 
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_list" ):
                return visitor.visitFunction_list(self)
            else:
                return visitor.visitChildren(self)




    def function_list(self):

        localctx = BKITParser.Function_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function_list)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 185
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 186
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 187
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 188
                self.return_stmt()
                pass


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
            return self.getToken(BKITParser.IF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(BKITParser.IF)
            self.state = 192
            self.exp()
            self.state = 193
            self.match(BKITParser.THEN)
            self.state = 194
            self.stmt_list()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 195
                self.match(BKITParser.ELSEIF)
                self.state = 196
                self.exp()
                self.state = 197
                self.match(BKITParser.THEN)
                self.state = 198
                self.stmt_list()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 205
                self.match(BKITParser.ELSE)
                self.state = 206
                self.stmt_list()


            self.state = 209
            self.match(BKITParser.ENDIF)
            self.state = 210
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def scalar(self):
            return self.getTypedRuleContext(BKITParser.ScalarContext,0)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(BKITParser.FOR)
            self.state = 213
            self.match(BKITParser.LP)
            self.state = 214
            self.scalar()
            self.state = 215
            self.match(BKITParser.EQ)
            self.state = 216
            self.exp()
            self.state = 217
            self.match(BKITParser.CM)
            self.state = 218
            self.exp()
            self.state = 219
            self.match(BKITParser.CM)
            self.state = 220
            self.exp()
            self.state = 221
            self.match(BKITParser.RP)
            self.state = 222
            self.match(BKITParser.DO)
            self.state = 223
            self.stmt_list()
            self.state = 224
            self.match(BKITParser.ENDFOR)
            self.state = 225
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(BKITParser.WHILE)
            self.state = 228
            self.exp()
            self.state = 229
            self.match(BKITParser.DO)
            self.state = 230
            self.stmt_list()
            self.state = 231
            self.match(BKITParser.ENDWHILE)
            self.state = 232
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BKITParser.DO)
            self.state = 235
            self.stmt_list()
            self.state = 236
            self.match(BKITParser.WHILE)
            self.state = 237
            self.exp()
            self.state = 238
            self.match(BKITParser.ENDDO)
            self.state = 239
            self.match(BKITParser.DOT)
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
            return self.getToken(BKITParser.BREAK, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(BKITParser.BREAK)
            self.state = 242
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(BKITParser.CONTINUE)
            self.state = 245
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(BKITParser.ID)
            self.state = 248
            self.match(BKITParser.LP)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOOL) | (1 << BKITParser.STRING) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT))) != 0):
                self.state = 249
                self.exp()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 250
                    self.match(BKITParser.CM)
                    self.state = 251
                    self.exp()
                    self.state = 256
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 259
            self.match(BKITParser.RP)
            self.state = 260
            self.match(BKITParser.SM)
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

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(BKITParser.RETURN)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOOL) | (1 << BKITParser.STRING) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT))) != 0):
                self.state = 263
                self.exp()


            self.state = 266
            self.match(BKITParser.SM)
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

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 268
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 269
                self.exp6()
                pass


            self.state = 272
            self.match(BKITParser.EQ)
            self.state = 273
            self.exp()
            self.state = 274
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(BKITParser.ID)
            self.state = 277
            self.match(BKITParser.LP)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOOL) | (1 << BKITParser.STRING) | (1 << BKITParser.LB) | (1 << BKITParser.LP) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT))) != 0):
                self.state = 278
                self.exp()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 279
                    self.match(BKITParser.CM)
                    self.state = 280
                    self.exp()
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 288
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def BOOL(self):
            return self.getToken(BKITParser.BOOL, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = BKITParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp9)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.match(BKITParser.ID)
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 293
                self.match(BKITParser.STRING)
                pass
            elif token in [BKITParser.BOOL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 294
                self.match(BKITParser.BOOL)
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 295
                self.array_list()
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


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def NOTEQ(self):
            return self.getToken(BKITParser.NOTEQ, 0)

        def LT(self):
            return self.getToken(BKITParser.LT, 0)

        def GT(self):
            return self.getToken(BKITParser.GT, 0)

        def LET(self):
            return self.getToken(BKITParser.LET, 0)

        def GET(self):
            return self.getToken(BKITParser.GET, 0)

        def ASSIGNFLOAT(self):
            return self.getToken(BKITParser.ASSIGNFLOAT, 0)

        def LETFLOAT(self):
            return self.getToken(BKITParser.LETFLOAT, 0)

        def GETFLOAT(self):
            return self.getToken(BKITParser.GETFLOAT, 0)

        def LTFLOAT(self):
            return self.getToken(BKITParser.LTFLOAT, 0)

        def GTFLOAT(self):
            return self.getToken(BKITParser.GTFLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.exp1(0)
                self.state = 299
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ASSIGN) | (1 << BKITParser.NOTEQ) | (1 << BKITParser.LT) | (1 << BKITParser.GT) | (1 << BKITParser.LET) | (1 << BKITParser.GET) | (1 << BKITParser.ASSIGNFLOAT) | (1 << BKITParser.LTFLOAT) | (1 << BKITParser.GTFLOAT) | (1 << BKITParser.LETFLOAT) | (1 << BKITParser.GETFLOAT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 300
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.exp1(0)
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

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.exp2(0) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBFLOAT(self):
            return self.getToken(BKITParser.SUBFLOAT, 0)

        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADDFLOAT(self):
            return self.getToken(BKITParser.ADDFLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.ADD) | (1 << BKITParser.ADDFLOAT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 321
                    self.exp3(0) 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def MULFLOAT(self):
            return self.getToken(BKITParser.MULFLOAT, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def DIVFLOAT(self):
            return self.getToken(BKITParser.DIVFLOAT, 0)

        def PERCENT(self):
            return self.getToken(BKITParser.PERCENT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 330
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 331
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.MULFLOAT) | (1 << BKITParser.DIV) | (1 << BKITParser.DIVFLOAT) | (1 << BKITParser.PERCENT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 332
                    self.exp4() 
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp4)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(BKITParser.NOT)
                self.state = 339
                self.exp4()
                pass
            elif token in [BKITParser.ID, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOOL, BKITParser.STRING, BKITParser.LB, BKITParser.LP, BKITParser.SUB, BKITParser.SUBFLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.exp5()
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


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBFLOAT(self):
            return self.getToken(BKITParser.SUBFLOAT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBFLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBFLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 344
                self.exp5()
                pass
            elif token in [BKITParser.ID, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOOL, BKITParser.STRING, BKITParser.LB, BKITParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
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

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp6)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.exp7()
                self.state = 353 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 349
                        self.match(BKITParser.LSB)
                        self.state = 350
                        self.exp()
                        self.state = 351
                        self.match(BKITParser.RSB)

                    else:
                        raise NoViableAltException(self)
                    self.state = 355 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.exp7()
                pass


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

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def exp8(self):
            return self.getTypedRuleContext(BKITParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp7)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def exp9(self):
            return self.getTypedRuleContext(BKITParser.Exp9Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKITParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp8)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(BKITParser.LP)
                self.state = 365
                self.exp()
                self.state = 366
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.ID, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.BOOL, BKITParser.STRING, BKITParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.exp9()
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


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def BOOL(self):
            return self.getToken(BKITParser.BOOL, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(BKITParser.STRING)
                pass
            elif token in [BKITParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self.match(BKITParser.BOOL)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 374
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 375
                self.array_list()
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


    class Array_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ArrayContext)
            else:
                return self.getTypedRuleContext(BKITParser.ArrayContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKITParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(BKITParser.LB)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOOL) | (1 << BKITParser.STRING) | (1 << BKITParser.LB))) != 0):
                self.state = 379
                self.array()
                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 380
                    self.match(BKITParser.CM)
                    self.state = 381
                    self.array()
                    self.state = 386
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 389
            self.match(BKITParser.RB)
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
        self._predicates[27] = self.exp1_sempred
        self._predicates[28] = self.exp2_sempred
        self._predicates[29] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




