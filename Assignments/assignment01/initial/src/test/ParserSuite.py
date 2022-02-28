import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program1(self):
        input = """Class main {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program2(self):
        input = """Class Rectangle: Shape {
                getArea() {
                    Return Self.length * Self.width;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program2(self):
        input = """Class Rectangle: Shape {
                getArea() {
                    Return Self.length * Self.width;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program3(self):
        input = """Class Shape {
                $getNumOfShape( {
                    Return Self.length * Self.width;
                }
            }"""
        expect = "Error on line 2 col 32: {"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_simple_program4(self):
        input = """Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;

                $getNumOfShape() {
                    Return $numOfShape;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_simple_program5(self):
        input = """Class Program {
                main() {
                    Out.printInt(Shape::$numOfShape);
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_simple_program6(self):
        input = """Class Program {
                main() {
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2; Var x, y : Int = 0, 0;
                    Out.printInt(Shape::$numOfShape);
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_simple_program7(self):
        input = """
            ## This is
            a multi-line
            comment. ##
            Class Program {
                main() {
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2; Var x, y : Int = 0, 0;
                    Out.printInt(Shape::$numOfShape);
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_simple_program8(self):
        input = """
            ## This is
            a multi-line
            comment. ##
            Class Program {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_simple_program9(self):
        input = """
            Class Program {
                main() {
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                    Var x, y : Int = 1e-3.54, 1_2324_545;
                    Out.printInt(Shape::$numOfShape);
                    Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_simple_program10(self):
        input = """
            Class Program {
                main() {
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                    Var x, y : Int = 1e-3.54, 1_2324_545;
                    Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                    Var _dfjkld: String = "fdskjfsd";
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_simple_program11(self):
        input = """
            Class Program {
                main() {
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                    Var x, y : Int = 1e-3.54, 1_2324_545;
                    Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                    Var _dfjkld: String = "fdskjfsd";
                    Val b: Array[String, 4] = Array("a", "b", "c", "d");
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_simple_program12(self):
        input = """
            Class Program {
                main() {
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                    Var x, y : Int = 1e-3.54, 1_2324_545;
                    Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                    Var _dfjkld: String = "fdskjfsd";
                    Val b: Array[String, 4] = Array("a", "b", "c", "d");
                    Var c: Array[Array, 4] = Array(Array(1, 2) , Array("dsfhk"));
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_simple_program13(self):
        input = """
            Class Program {
                Val $x : Int;
                main() {
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                    Var x, y : Int = 1e-3.54, 0x1AD;
                    Val a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                    Var _dfjkld: String = "This is a string containing tab \\t";
                    Var c: Array[Array, 4] = Array(Array(1, 2) , Array("dsfhk"));
                    $x = a + b;
                    $x = New Program();
                    $x = a[6+4][b[3]];
                    Return $x;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_simple_program14(self):
        input = """
            Class foo {
                Val y: String = "HEllo";
                Constructor () {
                    Var a: Int = O34243;
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_simple_program15(self):
        input = """
            Class foo {
                Val y: String = "HEllo";
                Constructor () {
                    Var a: Int = O34243;
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_simple_program16(self):
        input = """
            Class foo {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_simple_program17(self):
        input = """
                Class foo {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_simple_program18(self):
        input = """
                Class foo {
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
                Val x : Int;
                x = New foo();
                Shape::$getNumOfShape();
                x = foo.y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_simple_program19(self):
        input = """
                Class foo {
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
                Val x : Int;
                x = New foo();
                Shape::$getNumOfShape();
                x = foo.y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_simple_program20(self):
            input = """
                    Class Program {
        main() {
            Val x : Int;
            x = New foo();
            Shape::$getNumOfShape();
            x = foo.y;
            Foreach(a[x] In 1 .. 10) {
                If ((a[x] >= 9) || (a + 4 >= 0)) {
                    x = x + 1;
                    If (a[x] <= 0) {
                        Out.printInt(x);
                    }
                }
            }
        }
    }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 220))

    def test_simple_program21(self):
        input = """
            Class foo {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_simple_program22(self):
        input = """
            Class Program ({
    Val x : Int = 00;
}"""
        expect = "Error on line 2 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_simple_program23(self):
        input = """
               Class Program {
    Val x : Int = 00;
    Constructor ($y, b: Int) {
        Var c = 8;;
    }
}"""
        expect = "Error on line 5 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_simple_program24(self):
        input = """
                   Class Program {
    Val x : Int = 00;
    Constructor ($y, b: Int) {
        Var c: Int = 8;
    }

    main() {
        a[c] = b[a + c][a/c];
        Self.a = 4;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_simple_program25(self):
        input = """
                   Class Shape { Val $numOfShape: Int = 0; Val immutableAttribute: Int = 0; Var length, width: Int;
$getNumOfShape() { Return $numOfShape;
}}

Class Rectangle: Shape { getArea() { Return Self.length * Self.width;
} }
Class Program { main() {
Out.printInt(Shape::$numOfShape); } }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_exp1(self):
        input = """Class Program {
    main(a: Array[String, 5]) {
        a[4] = a[4] +. "hello";
    }

}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))


    def test_exp2(self):
        input = """Class Program {
    main(a: Array[String, 5]) {
        a[4] = a[4] +. "hello";
        Var _ : Int = 023 + a[2]/(5*6);
        Return _;

    }

}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_exp3(self):
        input = """Class Program {
    main(a: Array[String, 5]) {
        a[4] = a[4] +. "hello";
        Var _ : Int = 023 + a[2]/(5*6);
        a[3] = (_ - -6)%400;

    }

}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_exp4(self):
        input = """Class Program {
    main(a: Array[String, 5]) {
        a[4] = a[4] +. "hello";
        Var _ : Int = 023 + a[2]/(5*6);
        a[0] = Program::$main();
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_exp5(self):
        input = """Class Program {
    Var x: String = "sdfsdfdsfsdf";
    main(a: Array[String, 5]) {
        a[4] = a[4] +. "hello";
        Var _ : Int = 023 + a[2]/(5*6);
        a[0] = Program::$main();
        a[1] = a.x;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_exp6(self):
        input = """Class Program {
    Var x: String = "sdfsdfdsfsdf";
    main(a: Array[String, 5]) {
        a[4] = a[4] +. ("hello" ==. "HELLO") * 2%3;
        Var _ : Int = 023 + a[2]/(5*6);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_exp7(self):
        input = """Class Program {
    Var x: String = "sdfsdfdsfsdf";
    main(a: Array[String, 5]) {
        a[4] = a[4] +. ("hello" ==. "HELLO") * 2%3;
        Var _ : Int = 023 + a[2]/(5*6);
        b = 1.2e3 + 1.2e4 * 1_245.5;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_exp8(self):
        input = """Class Program {
    Var x: String = "sdfsdfdsfsdf";
    main(a: Array[String, 5]) {
        a[4] = a[4] +. ("hello" ==. "HELLO") * 2%3;
        Var _ : Int = 023 + a[2]/(5*6);
        c = .e3 + 1_3.e+23;
        a[c/b+(c%d)] = 2;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_exp9(self):
        input = """## fdslakjflsdf ##
Class Program {
    Var x: String = "sdfsdfdsfsdf";
    main(a: Array[String, 5]) {
        a[4] = a[4] +. ("hello" ==. "HELLO") * 2%3;
        Var _ : Int = 023 + a[2]/(5*6);
        c = .e3 + 1_3.e+23;
        a[c/b+(c%d)] = 2;
    }

    foo() {
        ## fdslakjflsdf ##
        a = 6 +. 7;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_exp10(self):
        input = """## fdslakjflsdf ##
Class Program {
    Var x: String = "sdfsdfdsfsdf";
    main(a: Array[String, 5]) {
        a[4] = a[4] +. ("hello" ==. "HELLO") * 2%3;
        Var _ : Int = 023 + a[2]/(5*6);
        c = .e3 + 1_3.e+23;
        a[c/b+(c%d)] = 2;
    }

    foo() {
        ## fdslakjflsdf ##
        a = 6 +. 7;
        Self.a = "dsf";
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_loop1(self):
        input = """Class Student {
    main() {
        Val i: Int = 0;
        Foreach (i In 1 .. 100) {
            Out.printInt(i);
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_loop2(self):
        input = """Class Student {
    main() {
        Val i: Int = 0;

        Foreach (i In 1 .. 100 By i*3) {
            Out.printInt(i);
            i = i/2;
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_loop3(self):
        input = """Class Student {
    main() {
        Val i: Int = 0;

        Foreach (b[d][c] In 1 .. 100 By i*3) {
            Out.printString(a[c + d]);


        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_loop4(self):
        input = """Class Student {
    main() {
        Val i: Int = 0;
        Foreach (i In 1 .. 100 By i*3) {
            ##
            this is a loop
            ##
            If (i % 2 == 0) {Out.printInt(i);}
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_loop5(self):
        input = """Class A{
        main(){
            Foreach(i In a.k[3] .. 100) {
                If (i%2==0) {i = i*2;}
            }
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_loop6(self):
        input = """Class A{
    main(){
        Foreach (i In 1 .. a[3] By 3) {
            i = 1000;
            io.writeInt(i);
            Break;
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_loop7(self):
        input = """Class A{
        main(){
        Foreach (i In 1 .. 100) {
        io.writeInt(i);
            Break;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_loop8(self):
        input = """Class A{
        main(){
        Foreach (i In 1 .. 100 By 4) {
            i = i"123";
        }
        }}"""
        expect = "Error on line 4 col 17: 123"
        self.assertTrue(TestParser.test(input, expect, 243))


    def test_loop9(self):
        input = """Class A{
        m(){}
        main(){
        Val x: Int;
        Foreach (i In 1 .. 100) {
            x.m();
            Continue;
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_loop10(self):
        input = """Class A{
        main(){
        Foreach (i In 1 .. a+2) {
            io.writeInt(i*2);
            }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_if1(self):
        input = """Class A{
        main(){
        Val x: Boolean = True;
        If (x)  {x=True;}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_if2(self):
        input = """Class A{
        main(){
        Var x: Boolean = False;
        If (x) {io.writeInt(100);}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_if3(self):
        input = """Class A{
        main(){
        Val _x: Boolean = True;
        If (x) {
        If (x) {If (m==6) {m=1000;}}
        }
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_if4(self):
        input = """Class A{
        main(){
        Val _x: Boolean = True;
        If (x) {If (y) {x=False;}}
        Else {x=True;}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_if5(self):
        input = """Class A{
        main(){
        Val _x: Boolean = True;
        If (x) { If(this.m==7) {x=True;}
        Else {io.writeInt(100);}}
        Else {io.writeInt(1);}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_if6(self):
        input = """Class A{
        main(){
        Val m: Float;
        m =  x.m(b[2]);
        Shape::$main();
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_if7(self):
        input = """Class A{
        main(){
        Var m: Float;
        m =   x.m(b[1*3+4-9*1.3]) - this.kd;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_if8(self):
        input = """Class A{
        main(){
        Val x: Boolean = False;
        If (x) {x = Array(3, 4, 5);}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_if9(self):
        input = """Class A{
        main(){
        Val x: Boolean;
        If (x) {io.readInt(x);}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_if10(self):
        input = """Class A{
        main(){
        Var x: String;
        If (x != "Hello") {io.readBool(x);}
        Else {io.writeBool(x);}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))



    def test_stmt1(self):
        input = """Class A{
        ##this is a cmt##
        Val $a: Int;
        main() {
            $a = 4+5;
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_stmt2(self):
        input = """Class A{
        ## cmt contain illegal escape \p ##
        main(){
        io.writeString("legal");
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_stmt3(self):
        input = """Class A{ Var x: Int;
        }
        ##cmt##"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_stmt4(self):
        input = """Class A{
        A(){}
        A(x,y: String; m: Int){}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_stmt5(self):
        input = """Class Shape {
Val length,width: Float;
getArea() {}
Shape(length,width: Float){
this.length = length;
this.width = width;
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_stmt6(self):
        input = """Class Shape {
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
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_stmt7(self):
        input = """Class Example1 {
factorial(n: Int){
If (n == 0) {Return 1;} Else {Return n * this.factorial(n - 1);}
}
main(){
Val x: Int;
x = io.readInt();
io.writeIntLn(this.factorial(x));
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_stmt8(self):
        input = """Class X{
        Val x: Array[Int, 5];
        X(){
        Foreach (i In 1 .. 100) {
io.writeIntLn(i);
x[i] = i + 1;
}
Foreach (x In 5 .. 2) {
io.writeIntLn(x);}
}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_stmt9(self):
        input = """Class A{
        A(){

##start of declaration part##
Var r,s: Float;
Val a,b: Array[Int, 5];
##list of statements##
r=2.0;
s=r*r*this.myPI;
a[0]= s;
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_stmt10(self):
        input = """Class Shape {
Var $numOfShape: Int = 0;
Val $immuAttribute: Int = 0;
Val length,width: Float;
$getNumOfShape() {
Return numOfShape;
}
}
Class Rectangle: Shape {
getArea(){
Return this.length*this.width;
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_literal1(self):
        input = """Class Lit{
        main(){
        Val A: String;
        A ="my name";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_literal2(self):
        input = """Class Lit{
        main(){
        Var A: String;
        A="This is a string containing tab \\t";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_literal3(self):
        input = """Class Lit{
        main(){
        Val A: String;
        A="He asked me: '"Where is John?'"";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_literal4(self):
        input = """Class Lit{
        main(){
        Val A: String;
        A="^^ Huynh Thi Truong Duy^^";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_literal5(self):
        input = """Class Lit{
        main(){
        Val A: String;
        A= "a\\tb\\f\\b%33\\r\\'hello";}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_literal6(self):
        input = """Class Lit{
        main(){
        Val A: Array[String, 1];
        A=Array("\\t\\b\\f");}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_literal7(self):
        input = """Class Lit{
        main(){
        Val A: Array[String, 2];
        A=Array("\\t\\b\\f", "LAST!!! ^_^ \\'_\\' ~_~ @_@ =.= !_!");}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_literal8(self):
        input = """Class Lit{
        main(){
        Val A: Array[String, 2];
        A=Array("\\t\\b\\f", "LAST!!! ^_^ \\'_\\' ~_~ @_@ =.= !_!", 1.e33, "T\\rV");}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_literal9(self):
        input = """Class Lit{
        main(){
        Val A: Array[String, 1];
        A=Array("abc\\ta\\nbc");}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_literal10(self):
        input = """Class Lit{
        main(){
        Val A: Array[Int, 2] = Array(1.2, 6);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_subclass1(self):

        input = """Class A{Var b: Int;}
        Class B: A{ Val d: Int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_subclass2(self):

        input = """Class A{Val b: Int;}
        Class B: A{ Var d:Int;"""
        expect = "Error on line 2 col 30: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_subclass3(self):

        input = """Class A{Val x: Float;}
        Class B{Val c: String;}
        Class C: A,B{ Val d: Int;}"""
        expect = "Error on line 3 col 18: ,"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_subclass4(self):

        input = """Class A{Val x: Float;}
        Class B: A{Val c: String;}
        Class C: B{ Val d: Int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_subclass5(self):

        input = """Class A{x(){}}
        Class B: A{main(){this.x();}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_subclass6(self):

        input = """Class A{x(){}}
        Class B: A{x(){##cmt##}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_subclass7(self):

        input = """Class A{x(){}}
        Class B: A{x(){io.writeInt(a[1][2]);}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_subclass8(self):

        input = """Class A{x(){}}
        Class B: A{print(){io.writeInt(4+5);}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_subclass9(self):

        input = """Class A{x(){}}
        Class B:A {main(){Val a: Int = 7;}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_subclass10(self):

        input = """Class A{x(){}}
        Class B:A {main(){Val a: Int = 7; a = a*6/10;}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_dcl1(self):
        input = """Class School{ Val $longitude,$latitude: Int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_dcl2(self):
        input = """Class School{ Val $longitude,$latitude: Int;"""
        expect = "Error on line 1 col 44: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_dcl3(self):
        input = """Class School{Val id: Float;}
        Class Faculty { Var id: Int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_dcl4(self):
        input = """Class School{
        Val id: Int;
        print(){io.writeInt(this.id);}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_dcl5(self):
        input = """Class School{
        Val 0id: Int;
        void print(){io.writeInt(this.id);}"""
        expect = "Error on line 2 col 12: 0"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_dcl6(self):
        input = """Class School{
        Val id: Float;
        print(){io.writeInt(this.id);}}
        Class Faculty{Var id: String;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_dcl7(self):
        input = """Class School{
        Val id: Int;
        print(){io.writeInt(this.id);}
        }
        Class Faculty{Var id: String; main(){Return 0;}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_dcl8(self):
        input = """Class School{
        Val id: Int;
        print(){
        Val a: Int =100;
        io.writeInt(a);}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_dcl9(self):
        input = """Class School{
        Val _id: Int;
        print(){
        io.writeInt(this.id);
        Var a: Float;}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_dcl10(self):
        input = """Class A{main(){}"""
        expect = "Error on line 1 col 16: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_mixed1(self):
        input = """Class X{
        main(){
  Val arr, n, i: Array[String, 100];
  io.writeString( "Enter number of elements: ");
  io.readInt(n);
  Foreach (i In 0 ..  n) {
    io.readInt(arr[i]);}
  Foreach (i In 0 .. n) {
    Foreach (j In i+1 .. n) {
      If (arr[i] == arr[j]){
        io.writeString("First repeating integer is ");
         io.writeInt(arr[i]);
      }}
      }
}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_mixed2(self):
        input = """Class A{
        main(){
        io.writeInt(io.readInt(x)+io.readInt(x)+io.readInt(x));
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_mixed3(self):
        input = """Class A{
        main(){
        Val x,sum: Int;
        sum=0;
        io.readInt(x);
        Foreach (i In 1 .. x) {sum=sum+i;}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_mixed4(self):
        input = """Class A{
        main(){
        Val x,y: Int;
        io.readInt(x);
        io.readInt(y);
        ## this is a line cmt
        /* and an unterminated cmt##
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_mixed5(self):
        input = """Class A{
        main(){
        Val x,y: Int;
        io.readInt(x);
        io.readInt(y);
        io.writeInt(x+y);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))








