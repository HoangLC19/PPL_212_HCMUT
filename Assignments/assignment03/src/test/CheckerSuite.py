import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):

    def test_redeclared_1(self):
        input = Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([])), AttributeDecl(Instance(), VarDecl(
            Id("myVar"), StringType(), StringLiteral("Hello World"))), AttributeDecl(Instance(), VarDecl(Id("myVar"), IntType()))])])
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_2(self):
        input = Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([])), AttributeDecl(Instance(), VarDecl(
            Id("myVar"), StringType(), StringLiteral("Hello World"))), MethodDecl(Static(), Id("main"), [], Block([])), MethodDecl(Static(), Id("main"), [], Block([]))])])
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_3(self):
        input = Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([])), AttributeDecl(Instance(), VarDecl(
            Id("myVar"), StringType(), StringLiteral("Hello World"))), MethodDecl(Static(), Id("foo"), [VarDecl(
                Id("var"), StringType()), VarDecl(
                Id("var"), StringType())], Block([]))])])
        expect = "Redeclared Parameter: var"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared_4(self):
        input = Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([])), AttributeDecl(Instance(), VarDecl(
            Id("myVar"), StringType(), StringLiteral("Hello World"))), MethodDecl(Static(), Id("foo"), [VarDecl(
                Id("var"), StringType())], Block([VarDecl(
                    Id("a"), StringType()), VarDecl(
                    Id("a"), StringType())]))])])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared_5(self):
        input = Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([])), AttributeDecl(Instance(), VarDecl(
            Id("myVar"), StringType(), StringLiteral("Hello World"))), MethodDecl(Static(), Id("foo"), [VarDecl(
                Id("var"), StringType())], Block([VarDecl(
                    Id("a"), StringType(), StringLiteral("hello")), VarDecl(
                    Id("a"), StringType())]))])])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_5(self):
        input = Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([])), AttributeDecl(Instance(), VarDecl(
            Id("myVar"), StringType(), StringLiteral("Hello World"))), MethodDecl(Static(), Id("foo"), [VarDecl(
                Id("var"), StringType())], Block([VarDecl(
                    Id("a"), StringType(), StringLiteral("hello")), ConstDecl(
                    Id("a"), StringType())]))])])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_6(self):
        input = Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([])), AttributeDecl(Instance(), VarDecl(
            Id("myVar"), StringType(), StringLiteral("Hello World")))]), ClassDecl(Id("Program"), [])])
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input, expect, 406))

    # def test_redeclared_6(self):
    #     input = Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id(
    #         "main"), [], Block([Assign(Id("myVar"), IntLiteral(10))]))])])
    #     expect = "Undeclared Identifier: myVar"
    #     self.assertTrue(TestChecker.test(input, expect, 406))
