
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    # decl: List[ClassDecl]
    def visitProgram(self, ast, c):
        c = [{}]  # list of scopes
        for decl in ast.decl:
            self.visit(decl, c)

    # classname: Id, memlist: List[MemDecl], parentname: Id = None
    def visitClassDecl(self, ast, c):
        pass

    def visitAttributeDecl(self, ast, c):
        pass

    def visitVarDecl(self, ast, c):
        pass

    def visitConstDecl(self, ast, c):
        pass

    def visitMethodDecl(self, ast, c):
        pass

    def visitInstance(self, ast, c):
        pass

    def visitStatic(self, ast, c):
        pass

    # Expression
    def visitBinaryOp(self, ast, c):
        pass

    def visitUnaryOp(self, ast, c):
        pass

    def visitCallExpr(self, ast, c):
        pass

    def visitNewExpr(self, ast, c):
        pass

    # stmt
    def visitBlock(self, ast, c):
        pass

    def visitCallStmt(self, ast, c):
        pass

    def visitReturn(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitBreak(self, ast, c):
        pass

    def visitFor(self, ast, c):
        pass

    def visitIf(self, ast, c):
        pass

    def visitAssign(self, ast, c):
        pass

    # Literals

    def visitSelfLiteral(self, ast, c):
        return ClassType()

    def visitNullLiteral(self, ast, c):
        return NullType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitArrayLiteral(self, ast, c):
        return ArrayType()

    # Type

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitClassType(self, ast, c):
        return ClassType()

    def visitArrayType(self, ast, c):
        return ArrayType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitBoolType(self, ast, c):
        return BoolType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitIntType(self, ast, c):
        return IntType()

    # LHS
    def visitArrayCell(self, ast, c):
        pass

    def visitFieldAccess(self, ast, c):
        pass

    def visitId(self, ast, c):
        pass
