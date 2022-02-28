import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # test identifiers
    def test_identifier1(self):
        self.assertTrue(TestLexer.test("My1stCons", "My1stCons,<EOF>", 101))

    def test_identifier2(self):
        self.assertTrue(TestLexer.test("$x", "$x,<EOF>", 102))

    def test_identifier3(self):
        self.assertTrue(TestLexer.test("_abHJJ1223", "_abHJJ1223,<EOF>", 103))

    def test_identifier4(self):
        self.assertTrue(TestLexer.test("$1223", "$1223,<EOF>", 104))

    def test_identifier5(self):
        self.assertTrue(TestLexer.test(
            "$1223_fsdjl_928", "$1223_fsdjl_928,<EOF>", 105))

    def test_identifier6(self):
        self.assertTrue(TestLexer.test(
            "WriteLn writeln WRITELN", "WriteLn,writeln,WRITELN,<EOF>", 106))

    def test_identifier7(self):
        self.assertTrue(TestLexer.test(
            "My1stCons $x _abHJJ1223", "My1stCons,$x,_abHJJ1223,<EOF>", 107))

    def test_identifier8(self):
        self.assertTrue(TestLexer.test(
            "_", "_,<EOF>", 108))

    def test_identifier9(self):
        self.assertTrue(TestLexer.test(
            "WriteLn $x _abHJJ1223", "WriteLn,$x,_abHJJ1223,<EOF>", 109))

    def test_identifier10(self):
        self.assertTrue(TestLexer.test(
            "abc#", "abc,Error Token #", 110))

    # test comments

    def test_comment1(self):
        self.assertTrue(TestLexer.test(
            "##Lorem100dsfijdsklf##", "<EOF>", 111))

    def test_comment2(self):
        self.assertTrue(TestLexer.test(
            "_sdfklsdjlf ##Lorem100dsfijdsklf##", "_sdfklsdjlf,<EOF>", 112))

    def test_comment3(self):
        self.assertTrue(TestLexer.test(
            "##Lorem100dsfijdsklf##_sdfklsdjlf ", "_sdfklsdjlf,<EOF>", 113))

    def test_comment4(self):
        self.assertTrue(TestLexer.test(
            "##Lorem100dsfijdsklf## ## dsklfjlsadr09238402-1391239890124 ## ", "<EOF>", 114))

    def test_comment5(self):
        self.assertTrue(TestLexer.test(
            "##Lorem100dsfijdsklf## _sdfklsdjlf ## dsklfjlsadr09238402-1391239890124 ## ", "_sdfklsdjlf,<EOF>", 115))

    # test numbers

    def test_literal_integer1(self):
        self.assertTrue(TestLexer.test(
            "124", "124,<EOF>", 116))

    def test_literal_integer2(self):
        self.assertTrue(TestLexer.test(
            "0123", "0123,<EOF>", 117))

    def test_literal_integer3(self):
        self.assertTrue(TestLexer.test(
            "0x1A", "0x1A,<EOF>", 118))

    def test_literal_integer4(self):
        self.assertTrue(TestLexer.test(
            "0b11111111", "0b11111111,<EOF>", 119))

    def test_literal_integer5(self):
        self.assertTrue(TestLexer.test(
            "1_234_567", "1234567,<EOF>", 120))

    def test_literal_integer6(self):
        self.assertTrue(TestLexer.test(
            "01_234_567", "01234567,<EOF>", 121))

    def test_literal_integer7(self):
        self.assertTrue(TestLexer.test(
            "0X1A_234B_567", "0X1A234B567,<EOF>", 122))

    def test_literal_integer8(self):
        self.assertTrue(TestLexer.test(
            "0B111_11_111", "0B11111111,<EOF>", 123))

    def test_literal_integer9(self):
        self.assertTrue(TestLexer.test(
            "0B111_11_111 31278_3479_2", "0B11111111,3127834792,<EOF>", 124))

    def test_literal_integer10(self):
        self.assertTrue(TestLexer.test(
            "0B111_11_111 31278_3479_2 0xA_438F_BD_328", "0B11111111,3127834792,0xA438FBD328,<EOF>", 125))

    def test_literal_float1(self):
        self.assertTrue(TestLexer.test(
            "1.234", "1.234,<EOF>", 126))

    def test_literal_float2(self):
        self.assertTrue(TestLexer.test(
            "1.2e3", "1.2e3,<EOF>", 127))

    def test_literal_float3(self):
        self.assertTrue(TestLexer.test(
            "7E-10", "7E-10,<EOF>", 128))

    def test_literal_float4(self):
        self.assertTrue(TestLexer.test(
            "1_234.567", "1234.567,<EOF>", 129))

    def test_literal_float5(self):
        self.assertTrue(TestLexer.test(
            "1E+10.2e3", "1E+10.2e3,<EOF>", 130))

    def test_literal_float6(self):
        self.assertTrue(TestLexer.test(
            "1_234E+10.2e3", "1234E+10.2e3,<EOF>", 131))

    def test_literal_float7(self):
        self.assertTrue(TestLexer.test(
            "1_3_4.343E+3", "134.343E+3,<EOF>", 132))

    def test_literal_float8(self):
        self.assertTrue(TestLexer.test(
            "1_3_4.343E+3 1E+10.2e3", "134.343E+3,1E+10.2e3,<EOF>", 133))

    def test_literal_float9(self):
        self.assertTrue(TestLexer.test(
            "1_3_4.343E+31E+10.2e3", "134.343E+31,E,+,10.2e3,<EOF>", 134))

    def test_literal_float10(self):
        self.assertTrue(TestLexer.test(
            "1_3_4.343E+31 7E-10", "134.343E+31,7E-10,<EOF>", 135))

    # test string
    def test_literal_string1(self):
        self.assertTrue(TestLexer.test(
            '"This is a string"', 'This is a string,<EOF>', 136))

    def test_literal_string2(self):
        self.assertTrue(TestLexer.test(
            '"This is a string containing tab \\t"', 'This is a string containing tab \\t,<EOF>', 137))

    def test_literal_string3(self):
        self.assertTrue(TestLexer.test(
            '"He asked me: \'"Where is John?\'""',  'He asked me: \'"Where is John?\'",<EOF>', 138))

    def test_literal_string4(self):
        self.assertTrue(TestLexer.test(
            '"abc\\ta\\nbc"', 'abc\\ta\\nbc,<EOF>', 139))

    def test_literal_string5(self):
        self.assertTrue(TestLexer.test(
            '"^^ Huynh Thi Truong Duy^^"', '^^ Huynh Thi Truong Duy^^,<EOF>', 140))

    def test_literal_string6(self):
        self.assertTrue(TestLexer.test(
            '"Run\\n Run\\n BTSRun!!!"', 'Run\\n Run\\n BTSRun!!!,<EOF>', 141))

    def test_literal_string7(self):
        self.assertTrue(TestLexer.test(
            """ "a\\tb\\f\\b%33\\r\\'hello" """, """a\\tb\\f\\b%33\\r\\'hello,<EOF>""", 142))

    def test_literal_string8(self):
        self.assertTrue(TestLexer.test(
            """ "\\\\\\'\\'"hello """, """\\\\\\'\\',hello,<EOF>""", 143))

    def test_literal_string9(self):
        self.assertTrue(TestLexer.test(
            """ "LAST!!! ^_^ \\'_\\' ~_~ @_@ =.= !_!" """, "LAST!!! ^_^ \\'_\\' ~_~ @_@ =.= !_!,<EOF>", 144))

    def test_literal_string10(self):
        self.assertTrue(TestLexer.test(
            """ "T\\rV" """, """T\\rV,<EOF>""", 145))


# test unclose string


    def test_unclose_string1(self):
        self.assertTrue(TestLexer.test(""" 0 "TDuy\r" """,
                        "0,Unclosed String: TDuy", 146))

    def test_literal_unclose_string2(self):
        self.assertTrue(TestLexer.test(
            """ "PPL\n" """, "Unclosed String: PPL", 147))

    def test_unclose_string3(self):
        self.assertTrue(TestLexer.test(
            """ 3 "HLC""", "3,Unclosed String: HLC", 148))

    def test_unclose_string4(self):
        self.assertTrue(TestLexer.test(
            """ 1e+2 "closedString?\\' """, """1e+2,Unclosed String: closedString?\\' """, 149))

    def test_unclose_string5(self):
        self.assertTrue(TestLexer.test(
            """ Hlc123\n"Hello\r"World """, """Hlc123,Unclosed String: Hello""", 150))

    def test_unclose_string6(self):
        self.assertTrue(TestLexer.test(
            """ _PPL $ppl PPL 123 1_234_567 "adidas""", "_PPL,$ppl,PPL,123,1234567,Unclosed String: adidas", 151))

    def test_unclose_string7(self):
        self.assertTrue(TestLexer.test(
            """ "CSE \n BKU HCMUT" """, """Unclosed String: CSE """, 152))

    def test_unclose_string8(self):
        self.assertTrue(TestLexer.test(
            """ ##fsdklfjskldfjl##Bypass \r "Abysss\\t (R00000t)\\b""", """Bypass,Unclosed String: Abysss\\t (R00000t)\\b""", 153))

    def test_unclose_string9(self):
        self.assertTrue(TestLexer.test(
            """ "This is the end """, """Unclosed String: This is the end """, 154))

    def test_unclose_string10(self):
        self.assertTrue(TestLexer.test(
            """ Bypasss \n " """, """Bypasss,Unclosed String:  """, 155))


# test illegal escape

    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.test(""" "Illegal\\Escapes!" """,
                        """Illegal Escape In String: Illegal\\E""", 156))

    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.test(""" "SUGARDADDY\\!" """,
                        """Illegal Escape In String: SUGARDADDY\\!""", 157))

    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.test(
            """ "\\ " """, """Illegal Escape In String: \\ """, 158))

    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.test(""" Hello "\\\n (Roott)\\b" """,
                        """Hello,Illegal Escape In String: \\\n""", 159))

    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.test(""" 123_342 "123a\\ne\\abc""",
                        """123342,Illegal Escape In String: 123a\\ne\\a""", 160))

    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.test(""" "hlc\\a\\" """,
                        """Illegal Escape In String: hlc\\a""", 161))

    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.test("""  "Lazy \\s" """,
                        "Illegal Escape In String: Lazy \s", 162))

    def test_illegal_escape8(self):
        self.assertTrue(TestLexer.test(""" 123 "123a\\m123" """,
                        """123,Illegal Escape In String: 123a\\m""", 163))

    def test_illegal_escape9(self):
        self.assertTrue(TestLexer.test(""" a+"avt\\d\\ndd """,
                        """a,+,Illegal Escape In String: avt\d""", 164))

    def test_illegal_escape10(self):
        self.assertTrue(TestLexer.test(""" "CSE \\zzz BK" """,
                        """Illegal Escape In String: CSE \z""", 165))

# test operators
    def test_operator1(self):
        self.assertTrue(TestLexer.test("a % b", "a,%,b,<EOF>", 166))

    def test_operator2(self):
        self.assertTrue(TestLexer.test(
            "a = b + c*c", "a,=,b,+,c,*,c,<EOF>", 167))

    def test_operator3(self):
        self.assertTrue(TestLexer.test("+-*/", "+,-,*,/,<EOF>", 168))

    def test_operator4(self):
        self.assertTrue(TestLexer.test("a[b[c[d[a + b + 2 * c + d]]]] = x * y / z + 5 - 6;",
                        "a,[,b,[,c,[,d,[,a,+,b,+,2,*,c,+,d,],],],],=,x,*,y,/,z,+,5,-,6,;,<EOF>", 169))

    def test_operator5(self):
        self.assertTrue(TestLexer.test("a + b = c => a = c - b",
                        "a,+,b,=,c,=,>,a,=,c,-,b,<EOF>", 170))

    def test_operator6(self):
        self.assertTrue(TestLexer.test(
            """abbb/*654+8hkl;l-2&*RAWoir2][lpsdk"{IPP#"p3[]"" """, "abbb,/,*,654,+,8,hkl,;,l,-,2,Error Token &", 171))

    def test_operator7(self):
        self.assertTrue(TestLexer.test(
            ";,km83po[)(*&/%QW#)+6]", ";,,,km83po,[,),(,*,Error Token &", 172))

    def test_operator8(self):
        self.assertTrue(TestLexer.test("{a[b + c / (d - e)] - x} % 18 = 123, @_@ ^_^",
                        "{,a,[,b,+,c,/,(,d,-,e,),],-,x,},%,18,=,123,,,Error Token @", 173))

    def test_operator9(self):
        self.assertTrue(TestLexer.test("==!=>=<=<>&&||!",
                        "==,!=,>=,<=,<,>,&&,||,!,<EOF>", 174))

    def test_operator10(self):
        self.assertTrue(TestLexer.test(
            "foo(2)[3+x]=a[b[5]]+2;", "foo,(,2,),[,3,+,x,],=,a,[,b,[,5,],],+,2,;,<EOF>", 175))

# test WS
    def test_WS1(self):
        self.assertTrue(TestLexer.test("\b", "<EOF>", 176))

    def test_WS2(self):
        self.assertTrue(TestLexer.test("\t\t\r", "<EOF>", 177))

    def test_WS3(self):
        self.assertTrue(TestLexer.test("\n\t\f", "<EOF>", 178))

    def test_WS4(self):
        self.assertTrue(TestLexer.test("\r\tProgramming\nLanguages and Principle  \t",
                        "Programming,Languages,and,Principle,<EOF>", 179))

    def test_WS5(self):
        self.assertTrue(TestLexer.test(
            "\r\tMy heart\nwill go on  \t", "My,heart,will,go,on,<EOF>", 180))

    def test_sample1(self):
        self.assertTrue(TestLexer.test("{12e4,10.5}", "{,12e4,,,10.5,},<EOF>", 181))

    def test_sample2(self):
        self.assertTrue(TestLexer.test("{True,False}", "{,True,,,False,},<EOF>", 182))

    def test_sample3(self):
        self.assertTrue(TestLexer.test("{-0x7F,0,2}", "{,-,0x7F,,,0,,,2,},<EOF>", 183))

    def test_sample4(self):
        self.assertTrue(TestLexer.test("{\"Lam Thanh Huy\",{\"1812360\",\"PPL\"}, {\"HK2\"}}",
                                       "{,Lam Thanh Huy,,,{,1812360,,,PPL,},,,{,HK2,},},<EOF>", 184))

    def test_sample5(self):
        self.assertTrue(TestLexer.test("## khai #bao bien ## Let a,b = 2,5,6 ; () {  x = 10; funcn(a);  } ",
                                       "Let,a,,,b,=,2,,,5,,,6,;,(,),{,x,=,10,;,funcn,(,a,),;,},<EOF>", 185))

    def test_sample6(self):
        self.assertTrue(TestLexer.test("If root == NULL { root = newPtr; taller = true; return root; } ",
                                       "If,root,==,NULL,{,root,=,newPtr,;,taller,=,true,;,return,root,;,},<EOF>", 186))

    def test_sample7(self):
        self.assertTrue(TestLexer.test("inOrder(root_left); process(root); inOrder(root_right); }",
                                       "inOrder,(,root_left,),;,process,(,root,),;,inOrder,(,root_right,),;,},<EOF>",
                                       187))

    def test_sample8(self):
        self.assertTrue(
            TestLexer.test("If i % 2 == 0 ##biendem## { write(i); dem:=dem+1;}.If dem = 15 { dem:=0;writeLn(dem);",
                           "If,i,%,2,==,0,{,write,(,i,),;,dem,:,=,dem,+,1,;,},.,If,dem,=,15,{,dem,:,=,0,;,writeLn,(,dem,),;,<EOF>",
                           188))

    def test_sample9(self):
        self.assertTrue(
            TestLexer.test("{ If a>b { tg=a; a=b;  b=g;  } }", "{,If,a,>,b,{,tg,=,a,;,a,=,b,;,b,=,g,;,},},<EOF>", 189))

    def test_sample10(self):
        self.assertTrue(TestLexer.test(" (a,b) FUction: main", "(,a,,,b,),FUction,:,main,<EOF>", 190))

    def test_sample11(self):
        self.assertTrue(
            TestLexer.test("Let a = 5; ##khai bao ,b", "Let,a,=,5,;,Error Token #", 191))  # mo ma khong dong cmt

    def test_sample12(self):
        self.assertTrue(TestLexer.test("a##ifidf##,f5", "a,,,f5,<EOF>", 192))

    def test_sample13(self):
        self.assertTrue(TestLexer.test("\"##ifidf##\",f5", "##ifidf##,,,f5,<EOF>", 193))

    def test_sample14(self):
        input = """"##Endie
    		Let a = 9; 
    		foo(2); 
    		##",f5"""
        self.assertTrue(TestLexer.test(input, "Unclosed String: ##Endie", 194))

    def test_sample15(self):
        self.assertTrue(TestLexer.test(
            "{{\"dog ##smartdog##\", ##Supercat## \"cat\",\"Peguin\" ##best Peguin},{\"height\",\"weight\",{\"4.5\",\"8.7\"}}}",
            "{,{,dog ##smartdog##,,,cat,,,Peguin,Error Token #", 195))

    def test_sample16(self):
        self.assertTrue(TestLexer.test("#one\n#two\n#three\n#", "Error Token #", 196))

    def test_sample17(self):
        self.assertTrue(TestLexer.test("#one\\n#two\\n#three\\n#", "Error Token #", 197))

    def test_sample18(self):
        self.assertTrue(TestLexer.test("#####", "Error Token #", 198))

    def test_sample19(self):
        self.assertTrue(TestLexer.test(" \"15  09 //2020\", 15 + 9 = 24, arr[5] = {7,8,9}, ELSEIF",
                                       "15  09 //2020,,,15,+,9,=,24,,,arr,[,5,],=,{,7,,,8,,,9,},,,ELSEIF,<EOF>", 199))

    def test_sample20(self):
        self.assertTrue(TestLexer.test("a = 7 ;", "a,=,7,;,<EOF>", 200))
