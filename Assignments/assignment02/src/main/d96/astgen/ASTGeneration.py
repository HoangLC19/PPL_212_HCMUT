from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    # decl: list[ClassDecl] => Program(decl)
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        decl = self.visit(ctx.classdecl_list())
        return Program(decl)

    # => list[ClassDecl]
    def visitClassdecl_list(self, ctx: D96Parser.Classdecl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.classdecl())]
        return [self.visit(ctx.classdecl())] + self.visit(classdecl_list())

    # classname: Id, memlist: list[MemDecl], parentname: Id => Classdecl
    def visitClassdecl(self, ctx: D96Parser.ClassdeclContext):
        className = Id(ctx.ID(0).getText())
        memList = self.visit(ctx.members())
        if ctx.CL():
            parentName = Id(ctx.ID(1).getText())
            return ClassDecl(className, memList, parentName)
        return ClassDecl(className, memList)

    # => list[MemDecl]
    def visitMembers(self, ctx: D96Parser.MembersContext):
        if ctx.getChildCount() == 0:
            return []
        elif not ctx.members():
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(0)) + self.visit(ctx.members())

    # kind: SIKind, decl: StoreDecl => list[AttributeDecl]
    def visitAttribute(self, ctx: D96Parser.AttributeContext):
        kind = Static() if ctx.idulist() else Instance()
        typ = self.visit(ctx.mptype())
        value = self.visit(ctx.exp_list()) if ctx.ASSIGN() else None
        result = []
        if ctx.VAL():  # -> ConstDecl
            constlist = self.visit(ctx.getChild(1))
            i = 0
            for ids in constlist:
                result += [ConstDecl(ids, typ, value[i]
                                     if value != None else None)]
                i += 1
        else:  # -> VarDecl
            varlist = self.visit(ctx.getChild(1))
            i = 0
            for ids in varlist:
                result += [VarDecl(ids, typ, value[i]
                                   if value != None else None)]
                i += 1

        return list(map(lambda decl: AttributeDecl(kind, decl), result))

    # kind: SIKind, name: Id, param: List[VarDecl], body: block => [MethodDecl]
    def visitMethod(self, ctx: D96Parser.MethodContext):
        kind = Static() if ctx.IDUSD() else Instance()
        if ctx.CONSTRUCTOR():
            name = Id('Constructor')
        elif ctx.DESTRUCTOR():
            name = Id('Destructor')
        else:
            name = Id(ctx.getChild(0).getText())

        param = self.visit(ctx.param_list())  # -> list[VarDecl]
        body = self.visit(ctx.block_stmt())
        return [MethodDecl(kind, name, param, body)]

    # => list[VarDecl]
    def visitParam_list(self, ctx: D96Parser.Param_listContext):
        if ctx.getChildCount() == 2:
            return []
        return self.visit(ctx.params_decl())

    # => list[VarDecl]
    def visitParams_decl(self, ctx: D96Parser.Params_declContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param_decl())
        return self.visit(ctx.param_decl()) + self.visit(params_decl())

    # => [VarDecl]
    def visitParam_decl(self, ctx: D96Parser.Param_declContext):
        varlist = self.visit(ctx.idlist())  # -> list[Id]
        typ = self.visit(ctx.mptype())
        return list(map(lambda var: VarDecl(var, typ), varlist))

    # => list[id]
    def visitIdlist(self, ctx: D96Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())

    # => lisd[idu]
    def visitIdulist(self, ctx: D96Parser.IdulistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.IDUSD().getText())]
        return [Id(ctx.IDUSD().getText())] + self.visit(ctx.idulist())

    def visitMptype(self, ctx: D96Parser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLTYPE():
            return BoolType()
        elif ctx.STRINGTYPE():
            return StringType()
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        elif ctx.class_type():
            return self.visit(ctx.class_type())

    def visitClass_type(self, ctx: D96Parser.Class_typeContext):
        return self.visit(ctx.epx10())

    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        size = ctx.INTLIT().getText()
        eleType = self.visit(ctx.mptype())
        return ArrayType(size, eleType)

    # BinaryOp
    def visitExp(self, ctx: D96Parser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp1(0), ctx.exp1(1))

    # BinaryOp
    def visitExp1(self, ctx: D96Parser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp2(0), ctx.exp2(1))

    # BinaryOp
    def visitExp2(self, ctx: D96Parser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        return BinaryOp(ctx.getChild(1), ctx.exp2(), ctx.exp3())

    # BinaryOp
    def visitExp3(self, ctx: D96Parser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        return BinaryOp(ctx.getChild(1), ctx.exp3(), ctx.exp3())

    # BinaryOp
    def visitExp4(self, ctx: D96Parser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        return BinaryOp(ctx.getChild(1), ctx.exp4(), ctx.exp5())

    # UnaryOp
    def visitExp5(self, ctx: D96Parser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        return UnaryOp(ctx.getChild(0).getText(), ctx.exp5())

    # UnaryOp
    def visitExp6(self, ctx: D96Parser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        return UnaryOp(ctx.getChild(0).getText(), ctx.exp6())

    # ArrayCell
    def visitExp7(self, ctx: D96Parser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp8())
        return ArrayCell(ctx.exp7(), self.visit(ctx.index_list()))

    # Field access : Instance access
    def visitExp8(self, ctx: D96Parser.Exp8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp9())
        return FieldAccess(ctx.exp8(), Id(ctx.ID().getText()))

    # Field access : Static access
    def visitExp9(self, ctx: D96Parser.Exp9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp10())
        return FieldAccess(ctx.exp9(), Id(ctx.IDUSD().getText()))

    # NewExpr Classname: Id, param: list[Expr]
    def visitExp10(self, ctx: D96Parser.Exp10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp11())
        return NewExpr(Id(ctx.ID().getText()), self.visit(exp_list) if ctx.exp_list() else [])

    def visitExp11(self, ctx: D96Parser.Exp11Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp12())
        return self.visit(ctx.exp())

    def visitExp12(self, ctx: D96Parser.Exp12Context):
        return self.visit(ctx.getChild(0))

    # => list[Expr]
    def visitExp_list(self, ctx: D96Parser.Exp_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        return [self.visit(ctx.exp())] + self.visit(ctx.exp_list())

    # => list[Expr]
    def visitIndex_list(self, ctx: D96Parser.Index_listContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.exp())]
        return [self.visit(ctx.exp())] + self.visit(ctx.index_list())

    # inst: list[inst] => Block(list[inst])
    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        inst = self.visit(ctx.stmt_list())
        return Block(inst)

    # => list[inst]
    def visitStmt_list(self, ctx: D96Parser.Stmt_listContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stmt())
        return self.visit(ctx.stmt()) + self.visit(ctx.stmt_list())

    def visitStmt(self, ctx: D96Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    # VarDecl, constant: Id, typ, value => list[decl]
    def visitDecl_stmt(self, ctx: D96Parser.Decl_stmtContext):
        typ = self.visit(ctx.mptype())
        value = self.visit(ctx.exp_list()) if ctx.ASSIGN() else None
        result = []
        idlist = self.visit(ctx.getChild(1))
        if ctx.VAL():  # -> ConstDecl
            result = [ConstDecl(ids, typ, value) for ids in idllist]
        else:  # -> VarDecl
            result = list(map(lambda ids: VarDecl(ids, typ, value), idlist))
        return result

    # lhs: expr, exp: expr => [Assign(stmt)]
    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        lhs = self.visit(ctx.exp7())
        exp = self.visit(ctx.exp())
        return [Assign(lhs, exp)]

    # epxr: epxr, thenStmt: Stmt, elseStmt: Stmt or None => [If(Stmt)]
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        expr = self.visit(ctx.exp())
        thenStmt = self.visit(self.block_stmt())
        elseStmt = self.visit(ctx.self_list()) if ctx.self_list() else None
        return [If(expr, thenStmt, elseStmt)]

    # => elseStmt: Stmt
    def visitElse_list(self, ctx: D96Parser.Else_listContext):
        if ctx.getChildCount() == 2:
            elseIf = self.visit(ctx.elseif_stmt())
            elseStmt = self.visit(ctx.else_list())  # => stmt_list
            return If(elseIf[0], elseIf[1], elseStmt)
        elif ctx.else_stmt():
            return self.visit(ctx.else_stmt())
        else:
            elseIf = self.visit(ctx.elseif_stmt())
            return If(elseIf[0], elseIf[1], None)

    def visitElseif_stmt(self, ctx: D96Parser.Elseif_stmtContext):
        expr = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.block_stmt())
        return (expr, thenStmt)

    def visitElse_stmt(self, ctx: D96Parser.Else_stmtContext):
        return self.visit(ctx.block_stmt())

    # id: Id, expr1: Expr, expr2: Expr, loop: Stmt, expr3: expr => [For(stmt)]
    def visitLoop_stmt(self, ctx: D96Parser.Loop_stmtContext):
        loop = self.visit(ctx.block_stmt())
        condition = self.visit(ctx.loop_condition())
        return [For(condition[0], condition[1], condition[2], loop, condition[3])]

    # => [ids, expr1, expr2, expr3]
    def visitLoop_condition(self, ctx: D96Parser.Loop_conditionContext):
        ids = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2)) if ctx.BY() else None
        return [ids, expr1, expr2, expr3]

    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return [Break()]

    def visitCont_stmt(self, ctx: D96Parser.Cont_stmtContext):
        return [Continue()]

    # expr = Expr => [Return(stmt)]
    def visitReturn_stmt(self, ctx: D96Parser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return()

    # obj: Expr, method: Id, param: list[Expr] => [CallStmt(Stmt)]
    def visitMethod_stmt(self, ctx: D96Parser.MethodContext):
        return [self.visit(ctx.getChild(0))]

    def visitInstance(self, ctx: D96Parser.InstanceContext):
        obj = self.visit(ctx.exp())
        ids = self.visit(Id(ctx.ID().getText()))
        param = self.visit(ctx.exp_list()) if ctx.exp_list() else []
        return CallStmt(obj, ids, param)

    def visitStatic(self, ctx: D96Parser.StaticContext):
        obj = self.visit(ctx.exp())
        ids = self.visit(Id(ctx.IDUSD().getText()))
        param = self.visit(ctx.exp_list()) if ctx.exp_list() else []
        return CallStmt(obj, ids, param)

    # value: list[Expr]
    def visitArraylit(self, ctx: D96Parser.ArraylitContext):
        value = self.visit(ctx.exp_list())
        return ArrayLiteral(value)

    def visitLiterals(self, ctx: D96Parser.LiteralsContext):
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.boolit():
            return self.visit(ctx.boolit())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.SELF():
            return SelfLiteral()
        return NullLiteral()

    def visitBoolit(self, ctx: D96Parser.BoolitContext):
        return BooleanLiteral(ctx.getChild(0).getText())
