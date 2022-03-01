import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """Class Program {}"""
        expect = str(Program([ClassDecl(Id("Program"), [])]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """Class Rectangle : Shape {}"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [], Id("Shape"))]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """Class Rectangle {
                        Var length: Int;
                }"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [
                     AttributeDecl(Instance(), VarDecl(Id("length"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_simple_program4(self):
        """Simple program: int main() {} """
        input = """Class Rectangle {
                        Var length: Int = 10;
                }"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [
                     AttributeDecl(Instance(), VarDecl(Id("length"), IntType(), IntLiteral("10")))])]))
        self.assertTrue(TestAST.test(input, expect, 304))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block(
    #         [], [CallExpr(Id("putIntLn"), [IntLiteral(4)])]))]))
    #     self.assertTrue(TestAST.test(input, expect, 301))

    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = str(Program(
    #         [FuncDecl(Id("main"), [], IntType(), Block([], [CallExpr(Id("getIntLn"), [])]))]))
    #     self.assertTrue(TestAST.test(input, expect, 302))
