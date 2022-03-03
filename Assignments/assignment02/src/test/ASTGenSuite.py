import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_simple_program1(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program {}"""
    #     expect = str(Program([ClassDecl(Id("Program"), [])]))
    #     self.assertTrue(TestAST.test(input, expect, 301))

    # def test_simple_program2(self):
    #     """Simple program: int main() {} """
    #     input = """Class Rectangle : Shape {}"""
    #     expect = str(Program([ClassDecl(Id("Rectangle"), [], Id("Shape"))]))
    #     self.assertTrue(TestAST.test(input, expect, 302))

    # def test_simple_program3(self):
    #     """Simple program: int main() {} """
    #     input = """Class Rectangle {
    #                     Var length: Int;
    #             }"""
    #     expect = str(Program([ClassDecl(Id("Rectangle"), [
    #                  AttributeDecl(Instance(), VarDecl(Id("length"), IntType()))])]))
    #     self.assertTrue(TestAST.test(input, expect, 303))

    # def test_simple_program4(self):
    #     """Simple program: int main() {} """
    #     input = """Class Rectangle {
    #                     Var length: Int = 10;
    #             }"""
    #     expect = str(Program([ClassDecl(Id("Rectangle"), [
    #                  AttributeDecl(Instance(), VarDecl(Id("length"), IntType(), IntLiteral("10")))])]))
    #     self.assertTrue(TestAST.test(input, expect, 304))

    # def test_simple_program5(self):
    #     input = """Class Rectangle {
    #             getArea() {
    #                 Return Self.length * Self.width;
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Rectangle"), [MethodDecl(Instance(), Id("getArea"), [], Block([Return(
    #         BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 305))

    # def test_simple_program6(self):
    #     input = """Class Rectangle: Shape {
    #             getArea() {
    #                 Return Self.length * Self.width;
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Rectangle"), [MethodDecl(Instance(), Id("getArea"), [], Block([Return(
    #         BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))))]))], Id("Shape"))]))
    #     self.assertTrue(TestAST.test(input, expect, 306))

    # def test_simple_program7(self):
    #     input = """Class Shape {
    #             $getNumOfShape(sum: Int) {
    #                 Return Self.length * Self.width;
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Shape"), [MethodDecl(Static(), Id("$getNumOfShape"), [VarDecl(Id("sum"), IntType())], Block([Return(
    #         BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 307))

    # def test_simple_program8(self):
    #     input = """Class Shape {
    #             Val $numOfShape: Int = 0;
    #             Val immutableAttribute: Int = 0;
    #             Var length, width: Int;

    #             $getNumOfShape() {
    #                 Return $numOfShape;
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Shape"), [AttributeDecl(Static(), ConstDecl(Id("$numOfShape"), IntType(), IntLiteral(0))), AttributeDecl(Instance(), ConstDecl(Id("immutableAttribute"), IntType(), IntLiteral(
    #         0))), AttributeDecl(Instance(), VarDecl(Id("length"), IntType())), AttributeDecl(Instance(), VarDecl(Id("width"), IntType())), MethodDecl(Static(), Id("$getNumOfShape"), [], Block([Return(Id("$numOfShape"))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 308))

    # def test_simple_program9(self):
    #     input = """Class Program {
    #             main() {
    #                 Out.printInt(Shape::$numOfShape);
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
    #         [CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))])]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 309))

    # def test_simple_program10(self):
    #     input = """Class Program {
    #             main() {
    #                 Val My1stCons, My2ndCons: Int = 1 + 5, 2; Var x, y : Int = 0, 0;
    #                 Out.printInt(Shape::$numOfShape);
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
    #         [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), IntLiteral("0")), VarDecl(Id("y"), IntType(), IntLiteral("0")), CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))])]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 310))

    # def test_simple_program11(self):
    #     input = """## This is
    #         a multi-line
    #         comment. ##
    #         Class Program {
    #             main() {
    #                 Val My1stCons, My2ndCons: Int = 1 + 5; Var x, y : Int = 0, 0;
    #                 Out.printInt(Shape::$numOfShape);
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
    #         [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType()), VarDecl(Id("x"), IntType(), IntLiteral("0")), VarDecl(Id("y"), IntType(), IntLiteral("0")), CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))])]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 311))

    # def test_simple_program12(self):
    #     input = """Class Program {
    #             main() {
    #                 Val My1stCons, My2ndCons: Int = 1 + 5, 2; Var x, y : Int = 0, 0;
    #                 Out.printInt(Shape::$numOfShape);
    #             }
    #         }

    #         Class Shape {
    #             Val $numOfShape: Int = 0;
    #             Val immutableAttribute: Int = 0;
    #             Var length, width: Int;

    #             $getNumOfShape() {
    #                 Return $numOfShape;
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
    #         [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral(2)), VarDecl(Id("x"), IntType(), IntLiteral("0")), VarDecl(Id("y"), IntType(), IntLiteral("0")), CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))])]))]), ClassDecl(Id("Shape"), [AttributeDecl(Static(), ConstDecl(Id("$numOfShape"), IntType(), IntLiteral(0))), AttributeDecl(Instance(), ConstDecl(Id("immutableAttribute"), IntType(), IntLiteral(
    #             0))), AttributeDecl(Instance(), VarDecl(Id("length"), IntType())), AttributeDecl(Instance(), VarDecl(Id("width"), IntType())), MethodDecl(Static(), Id("$getNumOfShape"), [], Block([Return(Id("$numOfShape"))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 312))

    # def test_simple_program13(self):
    #     input = """Class Program {
    #             main() {
    #                 Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    #                 Var x, y : Int = 1e-3.54, 1_2324_545;
    #                 Out.printInt(Shape::$numOfShape);
    #                 Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
    #         [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("12324545")), CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))]), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))]))])]))

    #     self.assertTrue(TestAST.test(input, expect, 313))

    # def test_simple_program14(self):
    #     input = """Class Program {
    #             main() {
    #                 Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    #                 Var x, y : Int = 1e-3.54, 1_2324_545;
    #                 Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
    #                 Var _dfjkld: String = "fdskjfsd";
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
    #         [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("12324545")), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("_dfjkld"), StringType(), StringLiteral("fdskjfsd"))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 314))

    # def test_simple_program15(self):
    #     input = """Class Program {
    #             main() {
    #                 Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    #                 Var x, y : Int = 1e-3.54, 1_2324_545;
    #                 Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
    #                 Var _dfjkld: String = "fdskjfsd";
    #                 Val b: Array[String, 4] = Array("a", "b", "c", "d");
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
    #         [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("12324545")), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("_dfjkld"), StringType(), StringLiteral("fdskjfsd")), ConstDecl(Id("b"), ArrayType(4, StringType()), ArrayLiteral([StringLiteral("a"), StringLiteral("b"), StringLiteral("c"), StringLiteral("d")]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 315))

    # def test_simple_program16(self):
    #     input = """Class Program {
    #             main() {
    #                 Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    #                 Var x, y : Int = 1e-3.54, 1_2324_545;
    #                 Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
    #                 Var _dfjkld: String = "fdskjfsd";
    #                 Val b: Array[String, 4] = Array("a", "b", "c", "d");
    #                 Var c: Array[Array[String, 4], 4] = Array(Array(1, 2) , Array("dsfhk"));
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
    #         [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("12324545")), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("_dfjkld"), StringType(), StringLiteral("fdskjfsd")), ConstDecl(Id("b"), ArrayType(4, StringType()), ArrayLiteral([StringLiteral("a"), StringLiteral("b"), StringLiteral("c"), StringLiteral("d")])), VarDecl(Id("c"), ArrayType(4, ArrayType(4, StringType())), ArrayLiteral([ArrayLiteral([IntLiteral("1"), IntLiteral(2)]), ArrayLiteral([StringLiteral("dsfhk")])]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 316))

    # def test_simple_program17(self):
    #     input = """Class Program {
    #             Val $x : Int = 3248923;
    #             main() {
    #                 Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    #                 Var x, y : Int = 1e-3.54, 0x1AD;
    #                 Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
    #                 Var _dfjkld: String = "This is a string containing tab \\t";
    #                 Var c: Array[Array[Int, 3], 4] = Array(Array(1, 2) , Array("dsfhk"));
    #                 $x = a + b;
    #                 $x = New Program();
    #                 $x = a[6+4][b[3]];
    #                 Return $x;
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Static(), ConstDecl(Id("$x"), IntType(), IntLiteral("3248923"))), MethodDecl(Instance(), Id("main"), [], Block(
    #         [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("0x1AD")), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("_dfjkld"), StringType(), StringLiteral("This is a string containing tab \\t")), VarDecl(Id("c"), ArrayType(4, ArrayType(3, IntType())), ArrayLiteral([ArrayLiteral([IntLiteral("1"), IntLiteral("2")]), ArrayLiteral([StringLiteral("dsfhk")])])), Assign(Id("$x"), BinaryOp("+", Id("a"), Id("b"))), Assign(Id("$x"), NewExpr(Id("Program"), [])), Assign(Id("$x"), ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(6), IntLiteral(4)), ArrayCell(Id("b"), [IntLiteral("3")])])), Return(Id("$x"))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 317))

    # def test_simple_program18(self):
    #     input = """Class foo {
    #             Val y: String = "HEllo";
    #             Constructor () {
    #                 Var a: Int = 34243;
    #                 If (!a || a == 10) {
    #                     a = -a;
    #                 }
    #                 Elseif (a%2 != 0) {
    #                     a = Self.a + 4;
    #                 }
    #                 Else {
    #                     a = 0;
    #                 }
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Instance(), ConstDecl(Id("y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Constructor"), [], Block([VarDecl(Id("a"), IntType(), IntLiteral("34243")), If(BinaryOp("==", BinaryOp("||", UnaryOp("!", Id("a")), Id(
    #         "a")), IntLiteral("10")), Block([Assign(Id("a"), UnaryOp("-", Id("a")))]), If(BinaryOp("!=", BinaryOp("%", Id("a"), IntLiteral("2")), IntLiteral("0")), Block([Assign(Id("a"), BinaryOp("+", FieldAccess(SelfLiteral(), Id("a")), IntLiteral("4")))]), Block([Assign(Id("a"), IntLiteral("0"))])))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 318))

    # def test_simple_program19(self):
    #     input = """Class foo {
    #             Val y: String = "HEllo";
    #             Constructor () {
    #                 Var a: Int = 34243;
    #                 If (!a || a == 10) {
    #                     a = -a;
    #                 }
    #                 Elseif (a%2 != 0) {
    #                     a = Self.a + 4;
    #                 }
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Instance(), ConstDecl(Id("y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Constructor"), [], Block([VarDecl(Id("a"), IntType(), IntLiteral("34243")), If(BinaryOp("==", BinaryOp("||", UnaryOp("!", Id("a")), Id(
    #         "a")), IntLiteral("10")), Block([Assign(Id("a"), UnaryOp("-", Id("a")))]), If(BinaryOp("!=", BinaryOp("%", Id("a"), IntLiteral("2")), IntLiteral("0")), Block([Assign(Id("a"), BinaryOp("+", FieldAccess(SelfLiteral(), Id("a")), IntLiteral("4")))])))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 319))

    # def test_simple_program20(self):
    #     input = """Class foo {
    #             Val y: String = "HEllo";
    #             Constructor () {
    #                 Var a: Int = 34243;
    #                 If (!a || a == 10) {
    #                     a = -a;
    #                 }
    #                 Else {
    #                     a = 0;
    #                 }
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Instance(), ConstDecl(Id("y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Constructor"), [], Block([VarDecl(Id("a"), IntType(), IntLiteral("34243")), If(BinaryOp("==", BinaryOp("||", UnaryOp("!", Id("a")), Id(
    #         "a")), IntLiteral("10")), Block([Assign(Id("a"), UnaryOp("-", Id("a")))]), Block([Assign(Id("a"), IntLiteral("0"))]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 320))

    # def test_simple_program21(self):
    #     input = """Class foo {
    #             Val y: String = "HEllo";
    #             Constructor () {
    #                 Var a: Int = 34243;
    #                 If (!a || a == 10) {
    #                     a = -a;
    #                 }
    #                 Elseif (a%2 != 0) {
    #                     a = Self.a + 4;
    #                 }
    #                 Else {
    #                     a = 0;
    #                 }
    #             }

    #             Destructor() {
    #                 Foreach (i In 1 .. 100 By 2) {
    #                     Out.printInt(i);
    #                 }

    #                 Foreach (x In 5 .. 2) {
    #                     Out.printInt(arr[x]);
    #                 }
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Instance(), ConstDecl(Id("y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Constructor"), [], Block([VarDecl(Id("a"), IntType(), IntLiteral("34243")), If(BinaryOp("==", BinaryOp("||", UnaryOp("!", Id("a")), Id(
    #         "a")), IntLiteral("10")), Block([Assign(Id("a"), UnaryOp("-", Id("a")))]), If(BinaryOp("!=", BinaryOp("%", Id("a"), IntLiteral("2")), IntLiteral("0")), Block([Assign(Id("a"), BinaryOp("+", FieldAccess(SelfLiteral(), Id("a")), IntLiteral("4")))]), Block([Assign(Id("a"), IntLiteral("0"))])))])), MethodDecl(Instance(), Id("Destructor"), [], Block([For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block([CallStmt(Id("Out"), Id("printInt"), [Id("i")])]), IntLiteral("2")), For(Id("x"), IntLiteral("5"), IntLiteral("2"), Block([CallStmt(Id("Out"), Id("printInt"), [ArrayCell(Id("arr"), [Id("x")])])]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 321))

    # def test_simple_program22(self):
    #     input = """Class foo {
    #             Val $y: String = "HEllo";

    #             Destructor() {
    #                 Foreach (i In 1 .. 100 By 2) {
    #                     Out.printInt(i);
    #                 }

    #                 Foreach (x In 5 .. 2) {
    #                     Out.printInt(arr[x]);
    #                     If (x == 4) {
    #                         x = x*a;
    #                         Break;
    #                     }
    #                     Elseif(x == 3) {
    #                         Continue;
    #                     }
    #                 }
    #             }
    #         }"""
    #     expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Static(), ConstDecl(Id("$y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Destructor"), [], Block([For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block([CallStmt(Id("Out"), Id("printInt"), [Id("i")])]), IntLiteral("2")), For(
    #         Id("x"), IntLiteral("5"), IntLiteral("2"), Block([CallStmt(Id("Out"), Id("printInt"), [ArrayCell(Id("arr"), [Id("x")])]), If(BinaryOp("==", Id("x"), IntLiteral("4")), Block([Assign(Id("x"), BinaryOp("*", Id("x"), Id("a"))), Break()]), If(BinaryOp("==", Id("x"), IntLiteral("3")), Block([Continue()])))]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 322))

    # def test_simple_program23(self):
    #     input = """Class foo {
    #                 Val $y: String = "HEllo";

    #                 Destructor() {
    #                     Foreach (i In 1 .. 100 By 2) {
    #                         Var r, s: Int;
    #                         r = 2.0;
    #                         Var a, b: Array[Int, 5];
    #                         s = r * r * Self.myPI;
    #                         a[0] = s;
    #                     }

    #                     Foreach (x In 5 .. 2) {
    #                         Out.printInt(arr[x]);
    #                         If (x == 4) {
    #                             x = x*a;
    #                             Break;
    #                         }
    #                         Elseif(x == 3) {
    #                             Continue;
    #                         }
    #                     }
    #                 }
    #             }"""
    #     expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Static(), ConstDecl(Id("$y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Destructor"), [], Block([For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block([VarDecl(Id("r"), IntType()), VarDecl(Id("s"), IntType()), Assign(Id("r"), FloatLiteral("2.0")), VarDecl(Id("a"), ArrayType(5, IntType())), VarDecl(Id("b"), ArrayType(5, IntType())), Assign(Id("s"), BinaryOp("*", BinaryOp("*", Id("r"), Id("r")), FieldAccess(SelfLiteral(), Id("myPI")))), Assign(ArrayCell(Id("a"), [IntLiteral("0")]), Id("s"))]), IntLiteral("2")), For(
    #         Id("x"), IntLiteral("5"), IntLiteral("2"), Block([CallStmt(Id("Out"), Id("printInt"), [ArrayCell(Id("arr"), [Id("x")])]), If(BinaryOp("==", Id("x"), IntLiteral("4")), Block([Assign(Id("x"), BinaryOp("*", Id("x"), Id("a"))), Break()]), If(BinaryOp("==", Id("x"), IntLiteral("3")), Block([Continue()])))]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 323))

    # def test_simple_program23(self):
    #     input = """Class foo {
    #         Val $y: String = "HEllo";

    #         Destructor() {
    #             Foreach (i In 1 .. 100 By 2) {
    #                 Var r, s: Int;
    #                 r = 2.0;
    #                 Var a, b: Array[Int, 5];
    #                 s = r * r * Self.myPI;
    #                 a[0] = s;
    #             }

    #             Foreach (x In 5 .. 2) {
    #                 Out.printInt(arr[x]);
    #                 If (x == 4) {
    #                     x = x*a;
    #                     Break;
    #                 }
    #                 Elseif(x == 3) {
    #                     Continue;
    #                 }
    #             }
    #         }
    #     }

    #     Class Program {
    #         main() {
    #             Val x : Int = 1232;
    #             x = New foo();
    #             Shape::$getNumOfShape();
    #             x = foo.y;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Static(), ConstDecl(Id("$y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Destructor"), [], Block([For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block([VarDecl(Id("r"), IntType()), VarDecl(Id("s"), IntType()), Assign(Id("r"), FloatLiteral("2.0")), VarDecl(Id("a"), ArrayType(5, IntType())), VarDecl(Id("b"), ArrayType(5, IntType())), Assign(Id("s"), BinaryOp("*", BinaryOp("*", Id("r"), Id("r")), FieldAccess(SelfLiteral(), Id("myPI")))), Assign(ArrayCell(Id("a"), [IntLiteral("0")]), Id("s"))]), IntLiteral("2")), For(
    #         Id("x"), IntLiteral("5"), IntLiteral("2"), Block([CallStmt(Id("Out"), Id("printInt"), [ArrayCell(Id("arr"), [Id("x")])]), If(BinaryOp("==", Id("x"), IntLiteral("4")), Block([Assign(Id("x"), BinaryOp("*", Id("x"), Id("a"))), Break()]), If(BinaryOp("==", Id("x"), IntLiteral("3")), Block([Continue()])))]))]))]), ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("x"), IntType(), IntLiteral("1232")), Assign(Id("x"), NewExpr(Id("foo"), [])), CallStmt(Id("Shape"), Id("$getNumOfShape"), []), Assign(Id("x"), FieldAccess(Id("foo"), Id("y")))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 323))

    # def test_simple_program24(self):
    #     input = """Class Program {
    #     main() {
    #         Val x : Int = 2323242;
    #         x = New foo();
    #         Shape::$getNumOfShape();
    #         x = foo.y;
    #         Foreach(a In 1 .. 10) {
    #             If ((a[x] >= 9) || (a + 4 >= 0)) {
    #                 x = x + 1;
    #                 If (a[x] <= 0) {
    #                     Out.printInt(x);
    #                 }
    #             }
    #         }
    #     }
    # }"""
    #     expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("x"), IntType(), IntLiteral("2323242")), Assign(
    #         Id("x"), NewExpr(Id("foo"), [])), CallStmt(Id("Shape"), Id("$getNumOfShape"), []), Assign(Id("x"), FieldAccess(Id("foo"), Id("y"))), For(Id("a"), IntLiteral("1"), IntLiteral("10"), Block([If(BinaryOp("||", BinaryOp(">=", ArrayCell(Id("a"), [Id("x")]), IntLiteral("9")), BinaryOp(">=", BinaryOp("+", Id("a"), IntLiteral("4")), IntLiteral("0"))), Block([Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral("1"))), If(BinaryOp("<=", ArrayCell(Id("a"), [Id("x")]), IntLiteral("0")), Block([CallStmt(Id("Out"), Id("printInt"), [Id("x")])]))]))]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 324))

    #     def test_simple_program25(self):
    #         input = """Class Program {
    #     Val x : Int = 00;
    #     Constructor (y, b: Int) {
    #         Var c: Int = 8;
    #     }

    #     main() {
    #         a[c] = b[a + c][a/c];
    #         Self.a = 4;
    #     }
    # }"""
    #         expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Instance(), ConstDecl(Id("x"), IntType(), IntLiteral("00"))), MethodDecl(Instance(), Id("Constructor"), [VarDecl(Id("y"), IntType()), VarDecl(Id("b"), IntType())], Block([VarDecl(
    #             Id("c"), IntType(), IntLiteral("8"))])), MethodDecl(Instance(), Id("main"), [], Block([Assign(ArrayCell(Id("a"), [Id("c")]), ArrayCell(Id("b"), [BinaryOp("+", Id("a"), Id("c")), BinaryOp("/", Id("a"), Id("c"))])), Assign(FieldAccess(SelfLiteral(), Id("a")), IntLiteral("4"))]))])]))
    #         self.assertTrue(TestAST.test(input, expect, 325))

    def test_simple_program26(self):
        input = """Class Program {
    main(a: Array[String, 5]) {
        a[4] = a[4] +. "hello";
    }

}"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [VarDecl(Id("a"), ArrayType(5, StringType()))], Block(
            [Assign(ArrayCell(Id("a"), [IntLiteral(4)]), BinaryOp("+.", ArrayCell(Id("a"), [IntLiteral(4)]), StringLiteral("hello")))]))])]))
        print(expect)
        self.assertTrue(TestAST.test(input, expect, 326))
