import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e ;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1;
}
float goo (float a, b) {
   return foo(1, a, b);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 202))

    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input, expect, 203))
