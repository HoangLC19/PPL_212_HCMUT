import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # def test_lower_identifier1(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    # def test_lower_identifier2(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         "192.168.0.1", "192.168.0.1,<EOF>", 102))

    # def test_lower_identifier3(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("0.001", "0.001,<EOF>", 103))

    # def test_lower_identifier4(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         "'Yanxi Palace - 2018'", "'Yanxi Palace - 2018',<EOF>", 104))

    def test_lower_identifier5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            "1_234_567", "1234567,<EOF>", 105))

    def test_lower_identifier6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            "0_123", "0,Error Token _", 106))

    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))
