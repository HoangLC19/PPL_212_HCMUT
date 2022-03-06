import unittest
from TestUtils import TestAST
from AST import *
from main.d96.utils.AST import AttributeDecl, FieldAccess


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

    def test_simple_program5(self):
        input = """Class Rectangle {
                    getArea() {
                        Return Self.length * Self.width;
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [MethodDecl(Instance(), Id("getArea"), [], Block([Return(
            BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_simple_program6(self):
        input = """Class Rectangle: Shape {
                    getArea() {
                        Return Self.length * Self.width;
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Rectangle"), [MethodDecl(Instance(), Id("getArea"), [], Block([Return(
            BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))))]))], Id("Shape"))]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_simple_program7(self):
        input = """Class Shape {
                    $getNumOfShape(sum: Int) {
                        Return Self.length * Self.width;
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Shape"), [MethodDecl(Static(), Id("$getNumOfShape"), [VarDecl(Id("sum"), IntType())], Block([Return(
            BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_simple_program8(self):
        input = """Class Shape {
                    Val $numOfShape: Int = 0;
                    Val immutableAttribute: Int = 0;
                    Var length, width: Int;

                    $getNumOfShape() {
                        Return $numOfShape;
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Shape"), [AttributeDecl(Static(), ConstDecl(Id("$numOfShape"), IntType(), IntLiteral(0))), AttributeDecl(Instance(), ConstDecl(Id("immutableAttribute"), IntType(), IntLiteral(
            0))), AttributeDecl(Instance(), VarDecl(Id("length"), IntType())), AttributeDecl(Instance(), VarDecl(Id("width"), IntType())), MethodDecl(Static(), Id("$getNumOfShape"), [], Block([Return(Id("$numOfShape"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_simple_program9(self):
        input = """Class Program {
                    main() {
                        Out.printInt(Shape::$numOfShape);
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
            [CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))])]))])]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_simple_program10(self):
        input = """Class Program {
                    main() {
                        Val My1stCons, My2ndCons: Int = 1 + 5, 2; Var x, y : Int = 0, 0;
                        Out.printInt(Shape::$numOfShape);
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
            [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), IntLiteral("0")), VarDecl(Id("y"), IntType(), IntLiteral("0")), CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))])]))])]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_simple_program11(self):
        input = """## This is
                a multi-line
                comment. ##
                Class Program {
                    main() {
                        Val My1stCons, My2ndCons: Int = 1 + 5; Var x, y : Int = 0, 0;
                        Out.printInt(Shape::$numOfShape);
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
            [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType()), VarDecl(Id("x"), IntType(), IntLiteral("0")), VarDecl(Id("y"), IntType(), IntLiteral("0")), CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))])]))])]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_simple_program12(self):
        input = """Class Program {
                    main() {
                        Val My1stCons, My2ndCons: Int = 1 + 5, 2; Var x, y : Int = 0, 0;
                        Out.printInt(Shape::$numOfShape);
                    }
                }

                Class Shape {
                    Val $numOfShape: Int = 0;
                    Val immutableAttribute: Int = 0;
                    Var length, width: Int;

                    $getNumOfShape() {
                        Return $numOfShape;
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
            [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral(2)), VarDecl(Id("x"), IntType(), IntLiteral("0")), VarDecl(Id("y"), IntType(), IntLiteral("0")), CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))])]))]), ClassDecl(Id("Shape"), [AttributeDecl(Static(), ConstDecl(Id("$numOfShape"), IntType(), IntLiteral(0))), AttributeDecl(Instance(), ConstDecl(Id("immutableAttribute"), IntType(), IntLiteral(
                0))), AttributeDecl(Instance(), VarDecl(Id("length"), IntType())), AttributeDecl(Instance(), VarDecl(Id("width"), IntType())), MethodDecl(Static(), Id("$getNumOfShape"), [], Block([Return(Id("$numOfShape"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_simple_program13(self):
        input = """Class Program {
                    main() {
                        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                        Var x, y : Int = 1e-3.54, 1_2324_545;
                        Out.printInt(Shape::$numOfShape);
                        Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
            [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("12324545")), CallStmt(Id("Out"), Id("printInt"), [FieldAccess(Id("Shape"), Id("$numOfShape"))]), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))]))])]))

        self.assertTrue(TestAST.test(input, expect, 313))

    def test_simple_program14(self):
        input = """Class Program {
                    main() {
                        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                        Var x, y : Int = 1e-3.54, 1_2324_545;
                        Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                        Var _dfjkld: String = "fdskjfsd";
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
            [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("12324545")), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("_dfjkld"), StringType(), StringLiteral("fdskjfsd"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_simple_program15(self):
        input = """Class Program {
                    main() {
                        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                        Var x, y : Int = 1e-3.54, 1_2324_545;
                        Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                        Var _dfjkld: String = "fdskjfsd";
                        Val b: Array[String, 4] = Array("a", "b", "c", "d");
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
            [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("12324545")), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("_dfjkld"), StringType(), StringLiteral("fdskjfsd")), ConstDecl(Id("b"), ArrayType(4, StringType()), ArrayLiteral([StringLiteral("a"), StringLiteral("b"), StringLiteral("c"), StringLiteral("d")]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_simple_program16(self):
        input = """Class Program {
                    main() {
                        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                        Var x, y : Int = 1e-3.54, 1_2324_545;
                        Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                        Var _dfjkld: String = "fdskjfsd";
                        Val b: Array[String, 4] = Array("a", "b", "c", "d");
                        Var c: Array[Array[String, 4], 4] = Array(Array(1, 2) , Array("dsfhk"));
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block(
            [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("12324545")), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("_dfjkld"), StringType(), StringLiteral("fdskjfsd")), ConstDecl(Id("b"), ArrayType(4, StringType()), ArrayLiteral([StringLiteral("a"), StringLiteral("b"), StringLiteral("c"), StringLiteral("d")])), VarDecl(Id("c"), ArrayType(4, ArrayType(4, StringType())), ArrayLiteral([ArrayLiteral([IntLiteral("1"), IntLiteral(2)]), ArrayLiteral([StringLiteral("dsfhk")])]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_simple_program17(self):
        input = """Class Program {
                    Val $x : Int = 3248923;
                    main() {
                        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                        Var x, y : Int = 1e-3.54, 0x1AD;
                        Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                        Var _dfjkld: String = "This is a string containing tab \\t";
                        Var c: Array[Array[Int, 3], 4] = Array(Array(1, 2) , Array("dsfhk"));
                        $x = a + b;
                        $x = New Program();
                        $x = a[6+4][b[3]];
                        Return $x;
                    }
                }"""
        expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Static(), ConstDecl(Id("$x"), IntType(), IntLiteral("3248923"))), MethodDecl(Instance(), Id("main"), [], Block(
            [ConstDecl(Id("My1stCons"), IntType(), BinaryOp("+", IntLiteral("1"), IntLiteral("5"))), ConstDecl(Id("My2ndCons"), IntType(), IntLiteral("2")), VarDecl(Id("x"), IntType(), FloatLiteral("1e-3.54")), VarDecl(Id("y"), IntType(), IntLiteral("0x1AD")), ConstDecl(Id("a"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])), VarDecl(Id("_dfjkld"), StringType(), StringLiteral("This is a string containing tab \\t")), VarDecl(Id("c"), ArrayType(4, ArrayType(3, IntType())), ArrayLiteral([ArrayLiteral([IntLiteral("1"), IntLiteral("2")]), ArrayLiteral([StringLiteral("dsfhk")])])), Assign(Id("$x"), BinaryOp("+", Id("a"), Id("b"))), Assign(Id("$x"), NewExpr(Id("Program"), [])), Assign(Id("$x"), ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(6), IntLiteral(4)), ArrayCell(Id("b"), [IntLiteral("3")])])), Return(Id("$x"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_simple_program18(self):
        input = """Class foo {
                    Val y: String = "HEllo";
                    Constructor () {
                        Var a: Int = 34243;
                        If (!a || a == 10) {
                            a = -a;
                        }
                        Elseif (a%2 != 0) {
                            a = Self.a + 4;
                        }
                        Else {
                            a = 0;
                        }
                    }
                }"""
        expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Instance(), ConstDecl(Id("y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Constructor"), [], Block([VarDecl(Id("a"), IntType(), IntLiteral("34243")), If(BinaryOp("==", BinaryOp("||", UnaryOp("!", Id("a")), Id(
            "a")), IntLiteral("10")), Block([Assign(Id("a"), UnaryOp("-", Id("a")))]), If(BinaryOp("!=", BinaryOp("%", Id("a"), IntLiteral("2")), IntLiteral("0")), Block([Assign(Id("a"), BinaryOp("+", FieldAccess(SelfLiteral(), Id("a")), IntLiteral("4")))]), Block([Assign(Id("a"), IntLiteral("0"))])))]))])]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_simple_program19(self):
        input = """Class foo {
                    Val y: String = "HEllo";
                    Constructor () {
                        Var a: Int = 34243;
                        If (!a || a == 10) {
                            a = -a;
                        }
                        Elseif (a%2 != 0) {
                            a = Self.a + 4;
                        }
                    }
                }"""
        expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Instance(), ConstDecl(Id("y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Constructor"), [], Block([VarDecl(Id("a"), IntType(), IntLiteral("34243")), If(BinaryOp("==", BinaryOp("||", UnaryOp("!", Id("a")), Id(
            "a")), IntLiteral("10")), Block([Assign(Id("a"), UnaryOp("-", Id("a")))]), If(BinaryOp("!=", BinaryOp("%", Id("a"), IntLiteral("2")), IntLiteral("0")), Block([Assign(Id("a"), BinaryOp("+", FieldAccess(SelfLiteral(), Id("a")), IntLiteral("4")))])))]))])]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_simple_program20(self):
        input = """Class foo {
                    Val y: String = "HEllo";
                    Constructor () {
                        Var a: Int = 34243;
                        If (!a || a == 10) {
                            a = -a;
                        }
                        Else {
                            a = 0;
                        }
                    }
                }"""
        expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Instance(), ConstDecl(Id("y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Constructor"), [], Block([VarDecl(Id("a"), IntType(), IntLiteral("34243")), If(BinaryOp("==", BinaryOp("||", UnaryOp("!", Id("a")), Id(
            "a")), IntLiteral("10")), Block([Assign(Id("a"), UnaryOp("-", Id("a")))]), Block([Assign(Id("a"), IntLiteral("0"))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_simple_program21(self):
        input = """Class foo {
                    Val y: String = "HEllo";
                    Constructor () {
                        Var a: Int = 34243;
                        If (!a || a == 10) {
                            a = -a;
                        }
                        Elseif (a%2 != 0) {
                            a = Self.a + 4;
                        }
                        Else {
                            a = 0;
                        }
                    }

                    Destructor() {
                        Foreach (i In 1 .. 100 By 2) {
                            Out.printInt(i);
                        }

                        Foreach (x In 5 .. 2) {
                            Out.printInt(arr[x]);
                        }
                    }
                }"""
        expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Instance(), ConstDecl(Id("y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Constructor"), [], Block([VarDecl(Id("a"), IntType(), IntLiteral("34243")), If(BinaryOp("==", BinaryOp("||", UnaryOp("!", Id("a")), Id(
            "a")), IntLiteral("10")), Block([Assign(Id("a"), UnaryOp("-", Id("a")))]), If(BinaryOp("!=", BinaryOp("%", Id("a"), IntLiteral("2")), IntLiteral("0")), Block([Assign(Id("a"), BinaryOp("+", FieldAccess(SelfLiteral(), Id("a")), IntLiteral("4")))]), Block([Assign(Id("a"), IntLiteral("0"))])))])), MethodDecl(Instance(), Id("Destructor"), [], Block([For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block([CallStmt(Id("Out"), Id("printInt"), [Id("i")])]), IntLiteral("2")), For(Id("x"), IntLiteral("5"), IntLiteral("2"), Block([CallStmt(Id("Out"), Id("printInt"), [ArrayCell(Id("arr"), [Id("x")])])]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_simple_program22(self):
        input = """Class foo {
                    Val $y: String = "HEllo";

                    Destructor() {
                        Foreach (i In 1 .. 100 By 2) {
                            Out.printInt(i);
                        }

                        Foreach (x In 5 .. 2) {
                            Out.printInt(arr[x]);
                            If (x == 4) {
                                x = x*a;
                                Break;
                            }
                            Elseif(x == 3) {
                                Continue;
                            }
                        }
                    }
                }"""
        expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Static(), ConstDecl(Id("$y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Destructor"), [], Block([For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block([CallStmt(Id("Out"), Id("printInt"), [Id("i")])]), IntLiteral("2")), For(
            Id("x"), IntLiteral("5"), IntLiteral("2"), Block([CallStmt(Id("Out"), Id("printInt"), [ArrayCell(Id("arr"), [Id("x")])]), If(BinaryOp("==", Id("x"), IntLiteral("4")), Block([Assign(Id("x"), BinaryOp("*", Id("x"), Id("a"))), Break()]), If(BinaryOp("==", Id("x"), IntLiteral("3")), Block([Continue()])))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_simple_program23(self):
        input = """Class foo {
                        Val $y: String = "HEllo";

                        Destructor() {
                            Foreach (i In 1 .. 100 By 2) {
                                Var r, s: Int;
                                r = 2.0;
                                Var a, b: Array[Int, 5];
                                s = r * r * Self.myPI;
                                a[0] = s;
                            }

                            Foreach (x In 5 .. 2) {
                                Out.printInt(arr[x]);
                                If (x == 4) {
                                    x = x*a;
                                    Break;
                                }
                                Elseif(x == 3) {
                                    Continue;
                                }
                            }
                        }
                    }"""
        expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Static(), ConstDecl(Id("$y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Destructor"), [], Block([For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block([VarDecl(Id("r"), IntType()), VarDecl(Id("s"), IntType()), Assign(Id("r"), FloatLiteral("2.0")), VarDecl(Id("a"), ArrayType(5, IntType())), VarDecl(Id("b"), ArrayType(5, IntType())), Assign(Id("s"), BinaryOp("*", BinaryOp("*", Id("r"), Id("r")), FieldAccess(SelfLiteral(), Id("myPI")))), Assign(ArrayCell(Id("a"), [IntLiteral("0")]), Id("s"))]), IntLiteral("2")), For(
            Id("x"), IntLiteral("5"), IntLiteral("2"), Block([CallStmt(Id("Out"), Id("printInt"), [ArrayCell(Id("arr"), [Id("x")])]), If(BinaryOp("==", Id("x"), IntLiteral("4")), Block([Assign(Id("x"), BinaryOp("*", Id("x"), Id("a"))), Break()]), If(BinaryOp("==", Id("x"), IntLiteral("3")), Block([Continue()])))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_simple_program24(self):
        input = """Class foo {
                Val $y: String = "HEllo";

                Destructor() {
                    Foreach (i In 1 .. 100 By 2) {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                    }

                    Foreach (x In 5 .. 2) {
                        Out.printInt(arr[x]);
                        If (x == 4) {
                            x = x*a;
                            Break;
                        }
                        Elseif(x == 3) {
                            Continue;
                        }
                    }
                }
            }

            Class Program {
                main() {
                    Val x : Int = 1232;
                    x = New foo();
                    Shape::$getNumOfShape();
                    x = foo.y;
                }
            }"""
        expect = str(Program([ClassDecl(Id("foo"), [AttributeDecl(Static(), ConstDecl(Id("$y"), StringType(), StringLiteral("HEllo"))), MethodDecl(Instance(), Id("Destructor"), [], Block([For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block([VarDecl(Id("r"), IntType()), VarDecl(Id("s"), IntType()), Assign(Id("r"), FloatLiteral("2.0")), VarDecl(Id("a"), ArrayType(5, IntType())), VarDecl(Id("b"), ArrayType(5, IntType())), Assign(Id("s"), BinaryOp("*", BinaryOp("*", Id("r"), Id("r")), FieldAccess(SelfLiteral(), Id("myPI")))), Assign(ArrayCell(Id("a"), [IntLiteral("0")]), Id("s"))]), IntLiteral("2")), For(
            Id("x"), IntLiteral("5"), IntLiteral("2"), Block([CallStmt(Id("Out"), Id("printInt"), [ArrayCell(Id("arr"), [Id("x")])]), If(BinaryOp("==", Id("x"), IntLiteral("4")), Block([Assign(Id("x"), BinaryOp("*", Id("x"), Id("a"))), Break()]), If(BinaryOp("==", Id("x"), IntLiteral("3")), Block([Continue()])))]))]))]), ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("x"), IntType(), IntLiteral("1232")), Assign(Id("x"), NewExpr(Id("foo"), [])), CallStmt(Id("Shape"), Id("$getNumOfShape"), []), Assign(Id("x"), FieldAccess(Id("foo"), Id("y")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_simple_program25(self):
        input = """Class Program {
            main() {
                Val x : Int = 2323242;
                x = New foo();
                Shape::$getNumOfShape();
                x = foo.y;
                Foreach(a In 1 .. 10) {
                    If ((a[x] >= 9) || (a + 4 >= 0)) {
                        x = x + 1;
                        If (a[x] <= 0) {
                            Out.printInt(x);
                        }
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("x"), IntType(), IntLiteral("2323242")), Assign(
            Id("x"), NewExpr(Id("foo"), [])), CallStmt(Id("Shape"), Id("$getNumOfShape"), []), Assign(Id("x"), FieldAccess(Id("foo"), Id("y"))), For(Id("a"), IntLiteral("1"), IntLiteral("10"), Block([If(BinaryOp("||", BinaryOp(">=", ArrayCell(Id("a"), [Id("x")]), IntLiteral("9")), BinaryOp(">=", BinaryOp("+", Id("a"), IntLiteral("4")), IntLiteral("0"))), Block([Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral("1"))), If(BinaryOp("<=", ArrayCell(Id("a"), [Id("x")]), IntLiteral("0")), Block([CallStmt(Id("Out"), Id("printInt"), [Id("x")])]))]))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_simple_program26(self):
        input = """Class Program {
            Val x : Int = 00;
            Constructor (y, b: Int) {
                Var c: Int = 8;
            }

            main() {
                a[c] = b[a + c][a/c];
                Self.a = 4;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"), [AttributeDecl(Instance(), ConstDecl(Id("x"), IntType(), IntLiteral("00"))), MethodDecl(Instance(), Id("Constructor"), [VarDecl(Id("y"), IntType()), VarDecl(Id("b"), IntType())], Block([VarDecl(
            Id("c"), IntType(), IntLiteral("8"))])), MethodDecl(Instance(), Id("main"), [], Block([Assign(ArrayCell(Id("a"), [Id("c")]), ArrayCell(Id("b"), [BinaryOp("+", Id("a"), Id("c")), BinaryOp("/", Id("a"), Id("c"))])), Assign(FieldAccess(SelfLiteral(), Id("a")), IntLiteral("4"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_simple_program27(self):
        input = """Class Program {
            main(a: Array[String, 5]) {
                a[4] = a[4] +. "hello";
            }

        }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [VarDecl(Id("a"), ArrayType(5, StringType()))], Block(
            [Assign(ArrayCell(Id("a"), [IntLiteral(4)]), BinaryOp("+.", ArrayCell(Id("a"), [IntLiteral(4)]), StringLiteral("hello")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_simple_program28(self):
        input = """Class Program {
            main(a: Array[String, 5]) {
                a[4] = a[4] +. "hello";
                Var _ : Int = 023 + a[2]/(5*6);
                Return _;

            }

        }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [VarDecl(Id("a"), ArrayType(5, StringType()))], Block(
            [Assign(ArrayCell(Id("a"), [IntLiteral(4)]), BinaryOp("+.", ArrayCell(Id("a"), [IntLiteral(4)]), StringLiteral("hello"))), VarDecl(Id("_"), IntType(), BinaryOp("+", IntLiteral("023"), BinaryOp("/", ArrayCell(Id("a"), [IntLiteral("2")]), BinaryOp("*", IntLiteral("5"), IntLiteral("6"))))), Return(Id("_"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_simple_program29(self):
        input = """Class Program {
            main(a: Array[String, 5]) {
                a[4] = a[4] +. "hello";
                Var _ : Int = 023 + a[2]/(5*6);
                a[3] = (_ - -6)%400;

            }

        }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [VarDecl(Id("a"), ArrayType(5, StringType()))], Block(
            [Assign(ArrayCell(Id("a"), [IntLiteral(4)]), BinaryOp("+.", ArrayCell(Id("a"), [IntLiteral(4)]), StringLiteral("hello"))), VarDecl(Id("_"), IntType(), BinaryOp("+", IntLiteral("023"), BinaryOp("/", ArrayCell(Id("a"), [IntLiteral("2")]), BinaryOp("*", IntLiteral("5"), IntLiteral("6"))))), Assign(ArrayCell(Id("a"), [IntLiteral("3")]), BinaryOp("%", BinaryOp("-", Id("_"), UnaryOp("-", IntLiteral("6"))), IntLiteral("400")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_simple_program30(self):
        input = """Class Program {
            main(a: Array[String, 5]) {
                a[4] = a[4] +. "hello";
                Var _ : Int = 023 + a[2]/(5*6);
                a[0] = Program::$main();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Instance(), Id("main"), [VarDecl(Id("a"), ArrayType(5, StringType()))], Block(
            [Assign(ArrayCell(Id("a"), [IntLiteral(4)]), BinaryOp("+.", ArrayCell(Id("a"), [IntLiteral(4)]), StringLiteral("hello"))), VarDecl(Id("_"), IntType(), BinaryOp("+", IntLiteral("023"), BinaryOp("/", ArrayCell(Id("a"), [IntLiteral("2")]), BinaryOp("*", IntLiteral("5"), IntLiteral("6"))))), Assign(ArrayCell(Id("a"), [IntLiteral("0")]), CallExpr(Id("Program"), Id("$main"), []))]))])]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_simple_program31(self):
        input = """Class Dog: Animal{
                    $gaugau() {
                        ae = b[6][8];
                    }
                }
                Class Snake: lizard {
                    $OpOp() {
                        Return Self.Op;
                    }
                }"""
        expect = "Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($gaugau),Static,[],Block([AssignStmt(Id(ae),ArrayCell(Id(b),[IntLit(6),IntLit(8)]))]))]),ClassDecl(Id(Snake),Id(lizard),[MethodDecl(Id($OpOp),Static,[],Block([Return(FieldAccess(Self(),Id(Op)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_simple_program32(self):
        input = """Class Program {
                    getName() {
                        Var b: Float = 1E10.2;
                    }
                    main() {
                        Var a: String;
                    }
                }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getName),Instance,[],Block([VarDecl(Id(b),FloatType,FloatLit(1E10.2))])),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),StringType)]))])])"
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_simple_program33(self):
        input = """
                Class MeowMeow: Dog {
                    Var b: Int;
                    Var $a, c, d: Float = 2.4, 2., 78.9;
                    Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
                }
                """
        expect = "Program([ClassDecl(Id(MeowMeow),Id(Dog),[AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(2.4))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(2.))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(78.9))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,FloatType),[FloatLit(1.2),FloatLit(3.6),IntLit(34e5),IntLit(23e4),FloatLit(12.7e4)]))])])"
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_simple_program34(self):
        input = """
                Class mini {
                    loop(a: Int; b: Float) {
                        Foreach (i In 0 .. 150 By i <= 8) {
                            sum = sum + a[i];
                        }
                    }
                }
                """
        expect = "Program([ClassDecl(Id(mini),[MethodDecl(Id(loop),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([For(Id(i),IntLit(0),IntLit(150),BinaryOp(<=,Id(i),IntLit(8)),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),ArrayCell(Id(a),[Id(i)])))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_simple_program35(self):
        input = """
                Class Pro {
                    Main(a: Int; b: Int) {
                        Return a || b < c.get(1,2) && 23 + 1.4;
                    }
                }
                """
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id(Main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(<,BinaryOp(||,Id(a),Id(b)),BinaryOp(&&,CallExpr(Id(c),Id(get),[IntLit(1),IntLit(2)]),BinaryOp(+,IntLit(23),FloatLit(1.4)))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_simple_program36(self):
        input = """
                Class Pro {
                    MainMenu(a: Int; b: Int) {
                        Self.arr[4] = b.getName() + a.exp();
                    }
                }
                Class ProMax {
                    iPhone13(){
                        Return 40000000;
                    }
                }
                """
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id(MainMenu),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[IntLit(4)]),BinaryOp(+,CallExpr(Id(b),Id(getName),[]),CallExpr(Id(a),Id(exp),[])))]))]),ClassDecl(Id(ProMax),[MethodDecl(Id(iPhone13),Instance,[],Block([Return(IntLit(40000000))]))])])"
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_simple_program37(self):
        input = """
                    Class MyClass {
                        Var name: String;
                        Var age: Int = 0;
                        $printName() {
                            Out.print(Self.name);
                        }
                        setAge(_age: Int) {
                            Self.age = _age;
                        }
                    }
                """
        expect = "Program([ClassDecl(Id(MyClass),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(age),IntType,IntLit(0))),MethodDecl(Id($printName),Static,[],Block([Call(Id(Out),Id(print),[FieldAccess(Self(),Id(name))])])),MethodDecl(Id(setAge),Instance,[param(Id(_age),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(age)),Id(_age))]))])])"
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_simple_program38(self):
        """More complex program"""
        input = """Class Shape {
                            Val numOfShape,$b,c: Int = 1,2,3;
                            Var n,$m,q : Float;
                            Test(a,b : Int; c : Float){
                                If (b + c == 3)
                                {
                                    Self.numOfShape = 3;
                                    Return a + 1;
                                }
                                Elseif (a == 4)
                                {
                                    Return 0;
                                }
                                Else
                                {
                                    Return 1;
                                }
                            }
                            }
                            """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(numOfShape),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(2))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(n),FloatType)),AttributeDecl(Static,VarDecl(Id($m),FloatType)),AttributeDecl(Instance,VarDecl(Id(q),FloatType)),MethodDecl(Id(Test),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([If(BinaryOp(==,BinaryOp(+,Id(b),Id(c)),IntLit(3)),Block([AssignStmt(FieldAccess(Self(),Id(numOfShape)),IntLit(3)),Return(BinaryOp(+,Id(a),IntLit(1)))]),If(BinaryOp(==,Id(a),IntLit(4)),Block([Return(IntLit(0))]),Block([Return(IntLit(1))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_simple_program39(self):
        input = """
                Class myClass {
                    method() {
                        Foreach (i In 0 .. 100 By e <= i) {
                            a[1][2] = a[1][1] + b[1][3][i];
                        }
                        Return a <= b;
                    }
                }
            """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id(method),Instance,[],Block([For(Id(i),IntLit(0),IntLit(100),BinaryOp(<=,Id(e),Id(i)),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(1)]),ArrayCell(Id(b),[IntLit(1),IntLit(3),Id(i)])))])]),Return(BinaryOp(<=,Id(a),Id(b)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_simple_program40(self):
        input = """
                    Class Student {
            main() {
                Val i: Int = 0;
                Foreach (i In 1 .. 100 By i*3) {
                    ##
                    this is a loop
                    ##
                    If (i % 2 == 0) {Out.printInt(i);}
                }
            }
        }
                """
        expect = str(Program([ClassDecl(Id("Student"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("i"), IntType(), IntLiteral("0")), For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block(
            [If(BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral("2")), IntLiteral("0")), Block([CallStmt(Id("Out"), Id("printInt"), [Id("i")])]))]), BinaryOp("*", Id("i"), IntLiteral("3")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_simple_program41(self):
        input = """
                Class A{
            main(){
                Foreach(i In a.k[3] .. 100) {
                    If (i%2==0) {i = i*2;}
                }
            }
    }
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], Block([For(Id("i"), ArrayCell(FieldAccess(Id("a"), Id("k")), [IntLiteral("3")]), IntLiteral("100"), Block(
            [If(BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral("2")), IntLiteral("0")), Block([Assign(Id("i"), BinaryOp("*", Id("i"), IntLiteral("2")))]))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_simple_program42(self):
        input = """
                Class A{
        main(){
            Foreach (i In 1 .. a[3] By 3) {
                i = 1000;
                io.writeInt(i);
                Break;
            }
        }
    }
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], Block([For(Id("i"), IntLiteral("1"), ArrayCell(Id("a"), [IntLiteral("3")]), Block(
            [Assign(Id("i"), IntLiteral("1000")), CallStmt(Id("io"), Id("writeInt"), [Id("i")]), Break()]), IntLiteral("3"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_simple_program43(self):
        input = """
                Class A{
            m(){}
            main(){
            Val x: Int = 123213_2321;
            Foreach (i In 1 .. 100) {
                x.m();
                Continue;
            }
            }}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("m"), [], Block([])), MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("x"), IntType(), IntLiteral("1232132321")), For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block(
            [CallStmt(Id("x"), Id("m"), []), Continue()]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_simple_program44(self):
        input = """
                Class A{
            main(){
            Foreach (i In 1 .. a+2) {
                io.writeInt(i*2);
                }
            }}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], Block([For(Id("i"), IntLiteral("1"), BinaryOp("+", Id("a"), IntLiteral("2")), Block(
            [CallStmt(Id("io"), Id("writeInt"), [BinaryOp("*", Id("i"), IntLiteral("2"))])]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_simple_program45(self):
        input = """
            Class A{
            main(){
            Val x: Boolean = True;
            If (x)  {x=True;}
            }}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(
            Id("x"), BoolType(), BooleanLiteral("True")), If(Id("x"), Block([Assign(Id("x"), BooleanLiteral("True"))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_simple_program46(self):
        input = """
            Class A{
            main(){
            Val _x: Boolean = True;
            If (x) {
            If (x) {If (m==6) {m=1000;}}
            }
            }}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(
            Id("_x"), BoolType(), BooleanLiteral("True")), If(Id("x"), Block([If(Id("x"), Block([If(BinaryOp("==", Id("m"), IntLiteral("6")), Block([Assign(Id("m"), IntLiteral("1000"))]))]))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_simple_program47(self):
        input = """
            Class A{
            main(){
            Val _x: Boolean = True;
            If (x) {If (y) {x=False;}}
            Else {x=True;}
            }}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(
            Id("_x"), BoolType(), BooleanLiteral("True")), If(Id("x"), Block([If(Id("y"), Block([Assign(Id("x"), BooleanLiteral("False"))]))]), Block([Assign(Id("x"), BooleanLiteral("True"))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_simple_program48(self):
        input = """
            Class A{
            main(){
            Val _x: Boolean = True;
            If (x) { If(this.m==7) {x=True;}
            Else {io.writeInt(100);}}
            Else {io.writeInt(1);}
            }}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(
            Id("_x"), BoolType(), BooleanLiteral("True")), If(Id("x"), Block([If(BinaryOp("==", FieldAccess(Id("this"), Id("m")), IntLiteral("7")), Block([Assign(Id("x"), BooleanLiteral("True"))]), Block([CallStmt(Id("io"), Id("writeInt"), [IntLiteral("100")])]))]), Block([CallStmt(Id("io"), Id("writeInt"), [IntLiteral("1")])]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_simple_program49(self):
        input = """
            Class A{
            main(){
            Var m: Float;
            m =   x.m(b[1*3+4-9*1.3]) - this.kd;
            }}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], Block([VarDecl(Id("m"), FloatType()), Assign(Id("m"), BinaryOp("-", CallExpr(Id("x"), Id("m"), [ArrayCell(Id("b"), [BinaryOp(
            "-", BinaryOp("+", BinaryOp("*", IntLiteral("1"), IntLiteral("3")), IntLiteral("4")), BinaryOp("*", IntLiteral("9"), FloatLiteral("1.3")))])]), FieldAccess(Id("this"), Id("kd"))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_simple_program50(self):
        input = """
            Class A{
            main(){
            Val x: Boolean = False;
            If (x) {x = Array(3, 4, 5);}
            }}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("x"), BoolType(), BooleanLiteral(
            "False")), If(Id("x"), Block([Assign(Id("x"), ArrayLiteral([IntLiteral("3"), IntLiteral("4"), IntLiteral("5")]))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_simple_program51(self):
        input = """
            Class A{ Var x: Int;
        }
        ##cmt##
            """
        expect = str(Program(
            [ClassDecl(Id("A"), [AttributeDecl(Instance(), VarDecl(Id("x"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_simple_program52(self):
        input = """
            Class A{ Var x: Int;
        }
        Class B: A {
            B(){}
            $B(x,y: String; m: Int){}
        }
        ##cmt##
            """
        expect = str(Program(
            [ClassDecl(Id("A"), [AttributeDecl(Instance(), VarDecl(Id("x"), IntType()))]), ClassDecl(Id("B"), [MethodDecl(Instance(), Id("B"), [], Block([])), MethodDecl(Static(), Id("$B"), [VarDecl(Id("x"), StringType()), VarDecl(Id("y"), StringType()), VarDecl(Id("m"), IntType())], Block([]))], Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_simple_program53(self):
        input = """
                Class Shape {
    Var length,width: Float;
    getArea() {}
    Shape(length,width: Float){
    this.length = length;
    this.width = width;
    }
    }
    Class Rectangle: Shape {
    getArea(){
    Return this.length*this.width;
    }
    }
    Class Triangle: Shape {
    getArea(){
    Return this.length*this.width / 2;
    }
    }
    Class Example2 {
    main(){

    s = New Rectangle(3,4);
    io.writeFloatLn(s.getArea());
    s = New Triangle(3,4);
    io.writeFloatLn(s.getArea());
    }
    }
                """
        expect = str(Program([ClassDecl(Id("Shape"), [AttributeDecl(Instance(), VarDecl(Id("length"), FloatType())), AttributeDecl(Instance(), VarDecl(
            Id("width"), FloatType())), MethodDecl(Instance(), Id("getArea"), [], Block([])), MethodDecl(Instance(), Id("Shape"), [VarDecl(Id("length"), FloatType()), VarDecl(
                Id("width"), FloatType())], Block([Assign(FieldAccess(Id("this"), Id("length")), Id("length")), Assign(FieldAccess(Id("this"), Id("width")), Id("width"))]))]), ClassDecl(Id("Rectangle"), [MethodDecl(Instance(), Id("getArea"), [], Block([Return(BinaryOp("*", FieldAccess(Id("this"), Id("length")), FieldAccess(Id("this"), Id("width"))))]))], Id("Shape")), ClassDecl(Id("Triangle"), [MethodDecl(Instance(), Id("getArea"), [], Block([Return(BinaryOp("/", BinaryOp("*", FieldAccess(Id("this"), Id("length")), FieldAccess(Id("this"), Id("width"))), IntLiteral("2")))]))], Id("Shape")), ClassDecl(Id("Example2"), [MethodDecl(Instance(), Id("main"), [], Block([Assign(Id("s"), NewExpr(Id("Rectangle"), [IntLiteral("3"), IntLiteral("4")])), CallStmt(Id("io"), Id("writeFloatLn"), [CallExpr(Id("s"), Id("getArea"), [])]), Assign(Id("s"), NewExpr(Id("Triangle"), [IntLiteral("3"), IntLiteral("4")])), CallStmt(Id("io"), Id("writeFloatLn"), [CallExpr(Id("s"), Id("getArea"), [])])]))])]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_simple_program53(self):
        input = """
                Class Example1 {
    factorial(n: Int){
    If (n == 0) {Return 1;} Else {Return n * this.factorial(n - 1);}
    }
    main(){
    Val x: Int = 3434;
    x = io.readInt();
    io.writeIntLn(this.factorial(x));
    }
    }
                """
        expect = str(Program([ClassDecl(Id("Example1"), [MethodDecl(Instance(), Id("factorial"), [VarDecl(Id("n"), IntType())], Block([If(BinaryOp("==", Id("n"), IntLiteral("0")), Block([Return(IntLiteral("1"))]), Block([Return(BinaryOp("*", Id("n"), CallExpr(Id("this"), Id("factorial"), [BinaryOp(
            "-", Id("n"), IntLiteral("1"))])))]))])), MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("x"), IntType(), IntLiteral("3434")), Assign(Id("x"), CallExpr(Id("io"), Id("readInt"), [])), CallStmt(Id("io"), Id("writeIntLn"), [CallExpr(Id("this"), Id("factorial"), [Id("x")])])]))])]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_simple_program54(self):
        input = """
                Class X{
            Val x: Array[Int, 5] = Array(1, 2132, 2_343, 343, 565);
            X(){
            Foreach (i In 1 .. 100) {
    io.writeIntLn(i);
    x[i] = i + 1;
    }
    Foreach (x In 5 .. 2) {
    io.writeIntLn(x);}
    }}
                """
        expect = str(Program([ClassDecl(Id("X"), [AttributeDecl(Instance(), ConstDecl(Id("x"), ArrayType(5, IntType()), ArrayLiteral([IntLiteral("1"), IntLiteral("2132"), IntLiteral("2343"), IntLiteral("343"), IntLiteral("565")]))), MethodDecl(Instance(), Id("X"), [], Block(
            [For(Id("i"), IntLiteral("1"), IntLiteral("100"), Block([CallStmt(Id("io"), Id("writeIntLn"), [Id("i")]), Assign(ArrayCell(Id("x"), [Id("i")]), BinaryOp("+", Id("i"), IntLiteral("1")))])), For(Id("x"), IntLiteral("5"), IntLiteral("2"), Block([CallStmt(Id("io"), Id("writeIntLn"), [Id("x")])]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_simple_program55(self):
        input = """
                Class Shape {
    Var $numOfShape: Int = 0;
    Val $immuAttribute: Int = 0;
    Val length,width: Float = 1.3e10;
    $getNumOfShape() {
    Return numOfShape;
    }
    }
    Class Rectangle: Shape {
    getArea(){
    Return this.length*this.width;
    }
    }
                """
        expect = str(Program([ClassDecl(Id("Shape"), [AttributeDecl(Static(), VarDecl(Id("$numOfShape"), IntType(), IntLiteral("0"))), AttributeDecl(Static(), ConstDecl(Id("$immuAttribute"), IntType(), IntLiteral("0"))), AttributeDecl(Instance(), ConstDecl(Id("length"), FloatType(), FloatLiteral("1.3e10"))), AttributeDecl(
            Instance(), ConstDecl(Id("width"), FloatType())), MethodDecl(Static(), Id("$getNumOfShape"), [], Block([Return(Id("numOfShape"))]))]), ClassDecl(Id("Rectangle"), [MethodDecl(Instance(), Id("getArea"), [], Block([Return(BinaryOp("*", FieldAccess(Id("this"), Id("length")), FieldAccess(Id("this"), Id("width"))))]))], Id("Shape"))]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_simple_program56(self):
        input = """
            Class A{Var b: Int;}
        Class B: A{ Val d: Int = 324234;}
            """
        expect = str(Program([ClassDecl(Id("A"), [AttributeDecl(Instance(), VarDecl(Id("b"), IntType()))]), ClassDecl(
            Id("B"), [AttributeDecl(Instance(), ConstDecl(Id("d"), IntType(), IntLiteral("324234")))], Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_simple_program57(self):
        input = """
            Class A{Val x: Float = 1.2;}
        Class B: A{Val c: String = "HLC";}
        Class C: B{ Val d: Int = 4;}
            """
        expect = str(Program([ClassDecl(Id("A"), [AttributeDecl(Instance(), ConstDecl(Id("x"), FloatType(), FloatLiteral("1.2")))]), ClassDecl(
            Id("B"), [AttributeDecl(Instance(), ConstDecl(Id("c"), StringType(), StringLiteral("HLC")))], Id("A")), ClassDecl(Id("C"), [AttributeDecl(Instance(), ConstDecl(Id("d"), IntType(), IntLiteral("4")))], Id("B"))]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_simple_program58(self):
        input = """
            Class A{x(){}}
        Class B: A{main(){this.x();}}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("x"), [], Block([]))]), ClassDecl(
            Id("B"), [MethodDecl(Instance(), Id("main"), [], Block([CallStmt(Id("this"), Id("x"), [])]))], Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_simple_program59(self):
        input = """
            Class A{x(){}}
        Class B: A{x(){io.writeInt(a[1][2]);}}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("x"), [], Block([]))]), ClassDecl(
            Id("B"), [MethodDecl(Instance(), Id("x"), [], Block([CallStmt(Id("io"), Id("writeInt"), [ArrayCell(Id("a"), [IntLiteral("1"), IntLiteral("2")])])]))], Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_simple_program60(self):
        input = """
            Class A{x(){}}
        Class B:A {main(){Val a: Int = 7;}}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("x"), [], Block([]))]), ClassDecl(
            Id("B"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("a"), IntType(), IntLiteral("7"))]))], Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_simple_program61(self):
        input = """
           Class A{x(){}}
        Class B:A {main(){Val a: Int = 7; a = a*6/10;}}
            """
        expect = str(Program([ClassDecl(Id("A"), [MethodDecl(Instance(), Id("x"), [], Block([]))]), ClassDecl(
            Id("B"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(Id("a"), IntType(), IntLiteral("7")), Assign(Id("a"), BinaryOp("/", BinaryOp("*", Id("a"), IntLiteral("6")), IntLiteral("10")))]))], Id("A"))]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_simple_program62(self):
        input = """
           Class School{ Val $longitude,$latitude: Int;}
            """
        expect = str(Program([ClassDecl(Id("School"), [AttributeDecl(Static(), ConstDecl(
            Id("$longitude"), IntType())), AttributeDecl(Static(), ConstDecl(Id("$latitude"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_simple_program63(self):
        input = """
           Class School{Val id: Float;}
        Class Faculty { Var id: Int;}
            """
        expect = str(Program([ClassDecl(Id("School"), [AttributeDecl(Instance(), ConstDecl(
            Id("id"), FloatType()))]), ClassDecl(Id("Faculty"), [AttributeDecl(Instance(), VarDecl(Id("id"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_simple_program64(self):
        input = """
           Class School{
        Val id: Int;
        print(){io.writeInt(this.id);}
        }
            """
        expect = str(Program([ClassDecl(Id("School"), [AttributeDecl(Instance(), ConstDecl(
            Id("id"), IntType())), MethodDecl(Instance(), Id("print"), [], Block([CallStmt(Id("io"), Id("writeInt"), [FieldAccess(Id("this"), Id("id"))])]))])]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_simple_program65(self):
        input = """
          Class School{
        Val id: Int;
        print(){io.writeInt(this.id);}
        }
        Class Faculty{Var id: String; main(){Return 0;}}
            """
        expect = str(Program([ClassDecl(Id("School"), [AttributeDecl(Instance(), ConstDecl(
            Id("id"), IntType())), MethodDecl(Instance(), Id("print"), [], Block([CallStmt(Id("io"), Id("writeInt"), [FieldAccess(Id("this"), Id("id"))])]))]), ClassDecl(Id("Faculty"), [AttributeDecl(Instance(), VarDecl(Id("id"), StringType())), MethodDecl(Instance(), Id("main"), [], Block([Return(IntLiteral("0"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_simple_program66(self):
        input = """
          Class School{
        Val id: Int;
        print(){
        Val a: Int =100;
        io.writeInt(a);}
        }
            """
        expect = str(Program([ClassDecl(Id("School"), [AttributeDecl(Instance(), ConstDecl(
            Id("id"), IntType())), MethodDecl(Instance(), Id("print"), [], Block([ConstDecl(Id("a"), IntType(), IntLiteral("100")), CallStmt(Id("io"), Id("writeInt"), [Id("a")])]))])]))
        self.assertTrue(TestAST.test(input, expect, 366))

        def test_simple_program67(self):
            input = """
              Class Program {
        Var x: String = "sdfsdfdsfsdf";
        main(a: Array[String, 5]) {
            a[4] = a[4] +. ("hello" ==. "HELLO") * 2%3;
            Var _ : Int = 023 + a[2]/(5*6);
        }
    }
                """
            expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),StringType,StringLit(sdfsdfdsfsdf))),MethodDecl(Id(main),Instance,[param(Id(a),ArrayType(5,StringType))],Block([AssignStmt(ArrayCell(Id(a),[IntLit(4)]),BinaryOp(+.,ArrayCell(Id(a),[IntLit(4)]),BinaryOp(%,BinaryOp(*,BinaryOp(==.,StringLit(hello),StringLit(HELLO)),IntLit(2)),IntLit(3)))),VarDecl(Id(_),IntType,BinaryOp(+,IntLit(023),BinaryOp(/,ArrayCell(Id(a),[IntLit(2)]),BinaryOp(*,IntLit(5),IntLit(6)))))]))])])"
            self.assertTrue(TestAST.test(input, expect, 367))

    def test_simple_program68(self):
        input = """
          Class Lit{
        main(){
        Val A: String;
        A="He asked me: '"Where is John?'"";}}
            """
        expect = str(Program([ClassDecl(Id("Lit"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(
            Id("A"), StringType()), Assign(Id("A"), StringLiteral("He asked me: '\"Where is John?'\""))]))])]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_simple_program69(self):
        input = """
          Class Lit{
        main(){
        Val A: String;
        A="^^ Huynh Thi Truong DUng^^";}}
            """
        expect = str(Program([ClassDecl(Id("Lit"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(
            Id("A"), StringType()), Assign(Id("A"), StringLiteral("^^ Huynh Thi Truong DUng^^"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_simple_program70(self):
        input = """
          Class Lit{
        main(){
        Val A: String;
        A= "a\\tb\\f\\b%33\\r\\'hello";}}
            """
        expect = str(Program([ClassDecl(Id("Lit"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(
            Id("A"), StringType()), Assign(Id("A"), StringLiteral("a\\tb\\f\\b%33\\r\\'hello"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_simple_program71(self):
        input = """
         Class Lit{
        main(){
        Val A: Array[String, 1] = Array("adsklf");
        A=Array("\\t\\b\\f");}}
            """
        expect = str(Program([ClassDecl(Id("Lit"), [MethodDecl(Instance(), Id("main"), [], Block([ConstDecl(
            Id("A"), ArrayType(1, StringType()), ArrayLiteral([StringLiteral("adsklf")])), Assign(Id("A"), ArrayLiteral([StringLiteral("\\t\\b\\f")]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 371))
