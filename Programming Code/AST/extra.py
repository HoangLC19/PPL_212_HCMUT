# In CSEL, a program consists of many declarations: variable declation (vardecl), constant declaration (constdecl), function declaration (funcdecl). Given the grammar of CSEL as follows:

# and AST classes as follows:

# class Program(ABC): # decl: List[Decl]

# class Type(ABC): pass

# class IntType(Type)

# class FloatType(Type)

# class BooleanType(Type)

# class LHS(ABC): pass

# class Id(LHS): # name: str

# class Decl(ABC): pass

# class VarDecl(Decl): # id: Id, typ: Type

# class ConstDecl(Decl): # id: Id, typ: Type, value: Expr

# class FuncDecl(Decl): # name: Id, param: List[VarDecl]

# class Exp(ABC): pass

# class IntLit(Exp): # value: int


# class FloatLit(Exp): # value: float

# class BooleanLit(Exp): # value: bool

# Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a CSEL input?

class ASTGenerator(CSELVisitor):

    # Visit a parse tree produced by CSELParser#program.
    # Let a: Int; Program([VarDecl(Id(a), IntType)])
    def visitProgram(self, ctx: CSELParser.ProgramContext):
        decls = ctx.decl()
        result = []
        for decl in decls:
            result += self.visit(decl)
        return Program(result)

    # Visit a parse tree produced by CSELParser#cseltype.
    # Let a: Int; => IntType
    def visitCseltype(self, ctx: CSELParser.CseltypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        return BooleanType()

    # Visit a parse tree produced by CSELParser#decl.
    # Let a: Int; => [VarDecl(Id(a), IntType)]
    def visitDecl(self, ctx: CSELParser.DeclContext):
        return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(1))

    # Visit a parse tree produced by CSELParser#decltail.
    # Let a: Int; => []
    def visitDecltail(self, ctx: CSELParser.DecltailContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(1))

    # Visit a parse tree produced by CSELParser#vardecl.
    # Let a: Int; single_vardecls: [[Id(a), IntType]] => [VarDecl(Id(a), IntType)]
    def visitVardecl(self, ctx: CSELParser.VardeclContext):
        decls = self.visit(ctx.single_vardecls())
        return list(map(lambda decl: VarDecl(decl[0], decl[1]), decls))

    # Visit a parse tree produced by CSELParser#single_vardecls.
    # Let a: Int; single_vardecls: [[Id(a), IntType]], single_vardecltail: [] => [[Id(a), IntType]]
    def visitSingle_vardecls(self, ctx: CSELParser.Single_vardeclsContext):

        return [self.visit(ctx.single_vardecl())] + self.visit(ctx.single_vardecltail())

    # Visit a parse tree produced by CSELParser#single_vardecl.
    # Let a: Int; => [Id(a), IntType]
    def visitSingle_vardecl(self, ctx: CSELParser.Single_vardeclContext):
        typ = self.visit(ctx.cseltype())
        ids = Id(ctx.ID().getText())
        return [ids, typ]

    # Visit a parse tree produced by CSELParser#single_vardecltail.
    # Let a: Int; => []
    def visitSingle_vardecltail(self, ctx: CSELParser.Single_vardecltailContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.single_vardecl())] + self.visit(ctx.single_vardecltail())

    # Visit a parse tree produced by CSELParser#constdecl.

    def visitConstdecl(self, ctx: CSELParser.ConstdeclContext):
        decl = self.visit(ctx.single_constdecl())
        return [ConstDecl(decl[0], decl[1], decl[2])]

    # Visit a parse tree produced by CSELParser#single_constdecl.

    def visitSingle_constdecl(self, ctx: CSELParser.Single_constdeclContext):
        ids = ctx.ID().getText()
        typ = self.visit(ctx.cseltype())
        value = self.visit(ctx.expr())
        return [ids, typ, value]

    # Visit a parse tree produced by CSELParser#expr.

    def visitExpr(self, ctx: CSELParser.ExprContext):
        if ctx.INTLIT():
            return IntLit(ctx.INTLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLit(ctx.FLOATLIT().getText())
        return BooleanLit(ctx.BOOLEANLIT().getText())

    # Visit a parse tree produced by CSELParser#funcdecl.

    def visitFuncdecl(self, ctx: CSELParser.FuncdeclContext):
        return [FuncDecl(Id(ctx.ID().getText(), self.visit(ctx.paramlist())))]

    # Visit a parse tree produced by CSELParser#paramlist.

    def visitParamlist(self, ctx: CSELParser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        decls = self.visit(ctx.single_vardecls())
        return list(map(lambda decl: VarDecl(decl[0], decl[1]), decls))
