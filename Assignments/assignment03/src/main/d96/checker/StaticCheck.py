
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
# from Utils import Utils
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


class StaticChecker(BaseVisitor):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def infer(self, name, typ, c):
        scope = next(iter(filter(lambda scope: name in scope, c)))
        scope[name] = typ

    # decl: List[ClassDecl]
    def visitProgram(self, ast, c):
        c = [{}]  # list of scope
        for decl in ast.decl:
            self.visit(decl, c)

    # classname: Id, memlist: List[MemDecl], parentname: Id = None

    def visitClassDecl(self, ast, c):
        # check class redeclared
        if ast.classname.name in c[0]:
            raise Redeclared(Class(), ast.classname.name)

        c[0][ast.classname.name] = 0
        env = [{}] + c
        for decl in ast.memlist:
            self.visit(decl, env)

    # kind: SIking, decl: StoreDecl
    def visitAttributeDecl(self, ast, c):
        # check attribute redeclared
        name = ast.decl.variable.name if ast.decl.variable else ast.decl.constant.name
        typ = self.visit(ast.decl.varType, c) if ast.decl.variable else self.visit(
            ast.decl.constType, c)
        if name in c[0]:
            raise Redeclared(Attribute(), name)

        c[0][name] = typ

    # variable: Id, varType: Type, varInit: Expr = None

    def visitVarDecl(self, ast, c):
        # check variable redeclared
        if ast.variable.name in c[0]:
            raise Redeclared(Variable(), ast.variable.name)

        c[0][ast.variable.name] = self.visit(ast.varType, c)

    def visitConstDecl(self, ast, c):
        # check constant redeclared
        if ast.constant.name in c[0]:
            raise Redeclared(Constant(), ast.constant.name)

        c[0][ast.constant.name] = self.visit(ast.constType, c)

    # kind: SIKind, name: Id, param: List[VarDecl], body: Block
    def visitMethodDecl(self, ast, c):
        # check method redeclared
        if ast.name.name in c[0]:
            raise Redeclared(Method(), ast.name.name)

        env = [{}] + c

        # check parameter redeclared
        for param in ast.param:
            if param.variable.name in env[0]:
                raise Redeclared(Parameter(), param.variable.name)
            env[0][param.variable.name] = self.visit(param.varType, env)

        c[0][ast.name.name] = env[0]
        self.visit(ast.body, env)

    def visitInstance(self, ast, c):
        pass

    def visitStatic(self, ast, c):
        pass

    # Expression
    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)

        if ast.op in ['+', '-', '*', '/']:
            if (type(left) is IntType or type(left) is FloatType) and type(right) is NoneType:
                right = left
                self.infer(ast.right.name, left, c)
                return left

            elif (type(right) is IntType or type(right) is FloatType) and type(left) is NoneType:
                left = right
                self.infer(ast.left.name, right, c)
                return right

            elif type(left) is IntType and type(right) is FloatType:
                left = right
                return FloatType()

            elif type(right) is IntType and type(left) is FloatType:
                right = left
                return FloatType()

            elif type(left) is not type(right):
                raise TypeMismatchInExpression(ast)

        elif ast.op == '%':
            if type(left) is IntType and type(right) is NoneType:
                right = left
                self.infer(ast.right.name, left, c)

            elif type(right) is IntType and type(left) is NoneType:
                left = right
                self.infer(ast.left.name, right, c)

            elif type(left) is not IntType or type(right) is not IntType:
                raise TypeMismatchInExpression(ast)

            return IntType()

    def visitUnaryOp(self, ast, c):
        pass

    def visitCallExpr(self, ast, c):
        pass

    def visitNewExpr(self, ast, c):
        pass

    # stmt
    def visitBlock(self, ast, c):
        for inst in ast.inst:
            self.visit(inst, c)

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
        return NoneType()

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
