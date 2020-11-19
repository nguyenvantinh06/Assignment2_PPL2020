from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        listDeclare=[]
        for i in ctx.declaration():
            listDeclare=listDeclare+ self.visit(i)
        return Program(listDeclare)

    def visitDeclaration(self,ctx:BKITParser.DeclarationContext):
        list_variabledeclare=[]
        list_functiondeclare=[]
        if ctx.variable_declare():
            for i in ctx.variable_declare():
                list_variabledeclare=list_variabledeclare+self.visit(i)
        if ctx.function_declare():
            for j in ctx.function_declare():
                list_functiondeclare= list_functiondeclare+self.visit(j)
        list_program=list_variabledeclare+list_functiondeclare
        return list_program
        
    def visitVariable_declare(self,ctx:BKITParser.Variable_declareContext):
        return self.visit(ctx.variable_list())

    def visitVariable_list(self,ctx:BKITParser.Variable_listContext):
        list_variable=[]
        for i in ctx.variable():
            list_variable=list_variable+[self.visit(i)]
        return list_variable

    def visitVariable(self,ctx:BKITParser.VariableContext):
        if ctx.scalar_variable():
            return self.visit(ctx.scalar_variable())
        else: return self.visit(ctx.composite())
    
    def visitScalar_variable(self,ctx:BKITParser.Scalar_variableContext):
        if ctx.ID():
            variable=Id(ctx.ID().getText())
        if ctx.DECIMAL():
            init=IntLiteral(int(ctx.DECIMAL().getText(),0))
        elif ctx.OCTAL():
            init=IntLiteral(int(ctx.OCTAL().getText(),0))
        elif ctx.HEXA():
            init=IntLiteral(int(ctx.HEXA().getText(),0))
        elif ctx.FLOAT():
            init=FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.STRING():
            init=StringLiteral(ctx.STRING().getText())
        elif ctx.BOOL():
            init=BooleanLiteral(ctx.BOOL().getText())
        else:
            init=None
        return VarDecl(variable,[],init)

    def visitComposite(self,ctx:BKITParser.CompositeContext):
        if ctx.ID():
            variable=Id(ctx.ID().getText())
        dimen=[]
        for i in ctx.int_assignment():
            dimen=dimen + [self.visit(i)]
        if ctx.type_assignment():
            init=self.visit(ctx.type_assignment())
        else: init=None
        return VarDecl(variable,dimen,init)

    def visitInt_assignment(self,ctx:BKITParser.Int_assignmentContext):
        if ctx.DECIMAL():
            init=int(ctx.DECIMAL().getText(),0)
        elif ctx.OCTAL():
            init=int(ctx.OCTAL().getText(),0)
        elif ctx.HEXA():
            init=int(ctx.HEXA().getText(),0)
        return init

    def visitType_assignment(self,ctx:BKITParser.Type_assignmentContext):
        if ctx.DECIMAL():
            return IntLiteral(int(ctx.DECIMAL().getText(),0))
        elif ctx.OCTAL():
            return IntLiteral(int(ctx.OCTAL().getText(),0))
        elif ctx.HEXA():
            return IntLiteral(int(ctx.HEXA().getText(),0))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.BOOL():
            return BooleanLiteral(ctx.BOOL().getText())
        elif ctx.array_list():
            return self.visit(ctx.array_list())

    def visitArray_list(self,ctx:BKITParser.Array_listContext):
        list_array=[]
        for i in ctx.array():
            list_array=list_array + [self.visit(i)]
        return ArrayLiteral(list_array)

    def visitArray(self,ctx:BKITParser.ArrayContext):
        if ctx.DECIMAL():
            return IntLiteral(int(ctx.DECIMAL().getText(),0))
        elif ctx.OCTAL():
            return IntLiteral(int(ctx.OCTAL().getText(),0))
        elif ctx.HEXA():
            return IntLiteral(int(ctx.HEXA().getText(),0))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.BOOL():
            return BooleanLiteral(ctx.BOOL().getText())
        elif ctx.array_list():
            return self.visit(ctx.array_list())

    def visitFunction_declare(self,ctx:BKITParser.Function_declareContext):
        name=Id(ctx.ID().getText())
        parameter=[]
        if ctx.parameter_list():
            parameter=self.visit(ctx.parameter_list())
        body=[]
        if ctx.body():
            body=self.visit(ctx.body())
        return [FuncDecl(name,parameter,body)]

    def visitParameter_list(self,ctx:BKITParser.Parameter_listContext):
        listparameter=[]
        for i in ctx.parameter_id():
            listparameter=listparameter+ [self.visit(i)]
        return listparameter

    def visitParameter_id(self,ctx:BKITParser.Parameter_idContext):
        parameter_id=Id(ctx.ID().getText())
        dimen=[]
        for i in ctx.intnew():
            dimen=dimen+ [self.visit(i)]
        return VarDecl(parameter_id,dimen,None)
       
    def visitBody(self,ctx:BKITParser.BodyContext):
        return self.visit(ctx.statement_list())

    def visitStatement_list(self,ctx:BKITParser.Statement_listContext):
        list_variabledeclare=[]
        list_functiondeclare=[]
        for i in ctx.variable_declare():
            list_variabledeclare=list_variabledeclare+self.visit(i)
        for i in ctx.function_list():
            list_functiondeclare=list_functiondeclare+self.visit(i)
        return tuple(list_variabledeclare,list_functiondeclare)

    def visitFunction_list(self,ctx:BKITParser.Function_listContext):
        if ctx.assignmentstatement():
            return self.visit(ctx.assignmentstatement())    
        elif ctx.ifstatement():
            return self.visit(ctx.ifstatement())
        elif ctx.forstatement():
            return self.visit(ctx.forstatement())
        elif ctx.whilestatement():
            return self.visit(ctx.whilestatement())
        elif ctx.dowhilestatement():
            return self.visit(ctx.dowhilestatement())
        elif ctx.breakstatement():
            return self.visit(ctx.breakstatement())
        elif ctx.continuestatement():
            return self.visit(ctx.continuestatement())
        elif ctx.callstatement():
            return self.visit(ctx.callstatement())
        elif ctx.returnstatement():
            return self.visit(ctx.returnstatement())
    def visitIfstatement(self,ctx:BKITParser.IfstatementContext):
        listif=[]
        expr1=self.visit(ctx.exp())
        var_declare=[]
        func_declare=[]
        var_declare,func_declare=self.visit(ctx.statement_list())
        if1=(expr1,var_declare,func_declare)
        listif.append(if1)
        if ctx.statement_list():
            for i in ctx.statement_list():
                listif.append(self.visit(i))
        else_stmt=[],[]
        if ctx.statement_list():
            else_stmt=self.visit(ctx.statement_list())
        
        return If(listif,(else_stmt))
    def visitForstatement(self,ctx:BKITParser.ForstatementContext):
        for_id=Id(ctx.ID().getText())
        expr1=self.visit(ctx.exp(0))
        expr2=self.visit(ctx.exp(1))
        expr3=self.visit(ctx.exp(2))
        loop=self.visit(ctx.statement_list())
        return For(for_id,expr1,expr2,expr3,loop)

    def visitWhilestatement(self,ctx:BKITParser.WhilestatementContext):
        if ctx.exp():
            expr=self.visit(ctx.exp())
        statement_list1=self.visit(ctx.statement_list())
        return While(expr,statement_list1)
   
    def visitDowhilestatement(self,ctx:BKITParser.DowhilestatementContext):
        list_statement=([],[])
        stmt=self.visit(ctx.statement_list())
        list_statement=stmt
        expr=self.visit(ctx.exp())
        return Dowhile(list_statement,expr)

    def visitAssignmentstatement(self,ctx:BKITParser.AssignmentstatementContext):
        if (ctx.ID()):
            return Assign(Id(ctx.ID().getText()), self.visit(ctx.exp()))
        elif (ctx.exp6()):
            return Assign(self.visit(ctx.exp6()),self.visit(ctx.exp()))
 
    def visitReturnstatement(self,ctx:BKITParser.ReturnstatementContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else: 
            return Return(None)

    def visitContinuestatement(self,ctx:BKITParser.ContinuestatementContext):  
        return Continue()

    def visitBreakstatement(self,ctx:BKITParser.BreakstatementContext):
        return Break()
    
    def visitFunctioncall(self,ctx:BKITParser.Function_callContext):
        method=Id(ctx.ID().getText())
        list_exp=[]
        for i in ctx.exp():
            list_exp=list_exp+ self.visit(i)
        return CallExp(method,list_exp)
    
    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:
            if ctx.ASSIGN():
                return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.NOTEQ():
                return BinaryOp(ctx.NOT_EQUAL().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.LESS_THAN():
                return BinaryOp(ctx.LT().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.GREATER_THAN():
                return BinaryOp(ctx.GT().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.LTOE():
                return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.GTOE():
                return BinaryOp(ctx.GET().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.ASSIGNFLOAT():
                return BinaryOp(ctx.ASSIGNFLOAT().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.LTOEFLOAT():
                return BinaryOp(ctx.LETFLOAT().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.GTOEFLOAT():
                return BinaryOp(ctx.GETFLOAT().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.LESS_THAN_FLOAT():
                return BinaryOp(ctx.LTFLOAT().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.GREATER_THAN_FLOAT():
                return BinaryOp(ctx.GTFLOAT().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))

    def visitExp1(self,ctx:BKITParser.Exp1Context):
        if ctx.getChildCount() == 3:
            if ctx.AND():
                return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2()))
            elif ctx.OR():
                return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2()))
        else: 
            return self.visit(ctx.exp2())

    def visitExp2(self,ctx:BKITParser.Exp2Context):
        if ctx.getChildCount() == 3:
            if ctx.SUB():
                return BinaryOp(ctx.SUB().getText(),self.visit(ctx.exp2(),self.visit(ctx.exp3())))
            elif ctx.SUBFLOAT():
                return BinaryOp(ctx.SUBFLOAT().getText(),self.visit(ctx.exp2(),self.visit(ctx.exp3())))
            elif ctx.ADD():
                return BinaryOp(ctx.ADD().getText(),self.visit(ctx.exp2(),self.visit(ctx.exp3())))
            elif ctx.ADDFLOAT():
                return BinaryOp(ctx.ADDFLOAT().getText(),self.visit(ctx.exp2(),self.visit(ctx.exp3())))
        else: return ctx.exp3()

    def visitExp3(self,ctx:BKITParser.Exp3Context):
        if ctx.getChildCount()==3:
            if ctx.MUL():
                return BinaryOp(ctx.MUL().getText(),self.visit(ctx.exp3(),self.visit(ctx.exp4())))
            elif ctx.MULFLOAT():
                return BinaryOp(ctx.MULFLOAT().getText(),self.visit(ctx.exp3(),self.visit(ctx.exp4())))
            elif ctx.DIV():
                return BinaryOp(ctx.DIV().getText(),self.visit(ctx.exp3(),self.visit(ctx.exp4())))
            elif ctx.DIVFLOAT():
                return BinaryOp(ctx.DIVFLOAT().getText(),self.visit(ctx.exp3(),self.visit(ctx.exp4())))
            elif ctx.PERCENT():
                return BinaryOp(ctx.PERCENT().getText(),self.visit(ctx.exp3(),self.visit(ctx.exp4())))
        else:
            return ctx.exp4()
    def visitExp4(self,ctx:BKITParser.Exp4Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp4))
        else: 
            return self.visit(ctx.exp5)
    
    def visitExp5(self,ctx:BKITParser.Exp6Context):
        if ctx.SUB():
            return UnaryOp(ctx.SIGN().getText(),self.visit(ctx.exp5))
        elif ctx.SUBFLOAT():
            return UnaryOp(ctx.SIGNFLOAT().getText(),self.visit(ctx.exp5))
        else: 
            return self.visit(ctx.exp6())
    
    def visitExp6(self,ctx:BKITParser.Exp6Context):
        if ctx.getChildCount()>1:
            expr=self.visit(ctx.exp7())
            listexp=[]
            for i in ctx.exp():
                listexp=listexp+[self.visit(i)]
            return ArrayCell(expr,listexp)
    
    def visitExp7(self,ctx:BKITParser.Exp7Context):
        if ctx.function_call:
            return self.visit(ctx.function_call())
        else: 
            return self.visit(ctx.exp8())
    
    def visitExp8(self,ctx:BKITParser.Exp8Context):
        if ctx.exp():
            return self.visit(ctx.exp())
        else: 
            return self.visit(ctx.exp9())
    
    def visitExp9(self,ctx:BKITParser.Exp9Context):
        if ctx.DECIMAL():
            return IntLiteral(int(ctx.DECIMAL().getText()))
        elif ctx.OCTAL():
            return IntLiteral(int(ctx.OCTAL().getText(),0))
        elif ctx.HEXA():
            return IntLiteral(int(ctx.HEXA().getText(),0))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.BOOL():
            return BooleanLiteral(ctx.BOOL().getText())
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.array_list():
            return self.visit(ctx.array_list())   
    
  
    


