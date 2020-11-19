import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x,y,z=5;"""
        expect = "Program([VarDecl(Id(x)),VarDecl(Id(y)),VarDecl(Id(z),IntLiteral(5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
   
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """
        Function: main
        Parameter: a[5]
        Body:
        Break;
        EndBody.
        """
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_vardeclaration(self):
        input = """int a,b,c[10],d;
                float e;
                string w,q;"""
        # expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(10,IntType())),VarDecl("d",IntType()),VarDecl("e",FloatType()),VarDecl("w",StringType()),VarDecl("q",StringType())]))
        expect="Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,10)),VarDecl(d,IntType),VarDecl(e,FloatType),VarDecl(w,StringType),VarDecl(q,StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_vardeclaration_1(self):
        input = """int a,b,c[10],d;
                float e[23],p;"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,10)),VarDecl(d,IntType),VarDecl(e,ArrayType(FloatType,23)),VarDecl(p,FloatType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))  
    def test_vardeclaration_4(self):
        input = """boolean a[10],b,c[5];
                string p[7],d;"""
        expect = "Program([VarDecl(a,ArrayType(BoolType,10)),VarDecl(b,BoolType),VarDecl(c,ArrayType(BoolType,5)),VarDecl(p,ArrayType(StringType,7)),VarDecl(d,StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    #test function declaration
    def test_funcdeclaration(self):
        input = """int main(){}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_funcdeclaration_1(self):
        input = """int main(float b,string arr[]){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(b,FloatType),VarDecl(arr,ArrayTypePointer(StringType))],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_funcdeclaration_2(self):
        input = """int main(){
            string a[10],b;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(StringType,10)),VarDecl(b,StringType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_funcdeclaration_3(self):
        input = """int main(){
            string x[20],y;
            float k;
            boolean j;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(x,ArrayType(StringType,20)),VarDecl(y,StringType),VarDecl(k,FloatType),VarDecl(j,BoolType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_funcdeclaration_4(self):
        input = """int[] main(){}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_funcdeclaration_5(self):
        input = """float[] main(int a,float x[]){
            string b,z[20];
            boolean r;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(x,ArrayTypePointer(FloatType))],ArrayTypePointer(FloatType),Block([VarDecl(b,StringType),VarDecl(z,ArrayType(StringType,20)),VarDecl(r,BoolType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_funcdeclaration_6(self):
        input = """void main(){}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_funcdeclaration_7(self):
        input = """void main(){
            int r,s,t[10];
            float y;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(r,IntType),VarDecl(s,IntType),VarDecl(t,ArrayType(IntType,10)),VarDecl(y,FloatType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_funcdeclaration_8(self):
        input = """void main(int hello[],float PPL){
            int s,t[10];
            string minh;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(hello,ArrayTypePointer(IntType)),VarDecl(PPL,FloatType)],VoidType,Block([VarDecl(s,IntType),VarDecl(t,ArrayType(IntType,10)),VarDecl(minh,StringType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_funcdeclaration_9(self):
        input = """
        float add(int a,int b){
            int c;
            float result;
        }
        void main(float PPL){
            int s,t[10];
        }"""
        expect = "Program([FuncDecl(Id(add),[VarDecl(a,IntType),VarDecl(b,IntType)],FloatType,Block([VarDecl(c,IntType),VarDecl(result,FloatType)])),FuncDecl(Id(main),[VarDecl(PPL,FloatType)],VoidType,Block([VarDecl(s,IntType),VarDecl(t,ArrayType(IntType,10))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_funcdeclaration_10(self):
        input = """
        string chain(string a,string b){
            string result;
        }
        float add(int a,int b){
            int c;
            float result;
        }
        void main(float PPL){
            int s,t[10];
        }"""
        expect = "Program([FuncDecl(Id(chain),[VarDecl(a,StringType),VarDecl(b,StringType)],StringType,Block([VarDecl(result,StringType)])),FuncDecl(Id(add),[VarDecl(a,IntType),VarDecl(b,IntType)],FloatType,Block([VarDecl(c,IntType),VarDecl(result,FloatType)])),FuncDecl(Id(main),[VarDecl(PPL,FloatType)],VoidType,Block([VarDecl(s,IntType),VarDecl(t,ArrayType(IntType,10))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    #test if statement
    def test_if_statement(self):
        input = """int main(){
            int a,b;
            if(a){
                break;
            }
            else
                a=a+1;
            b>c=d;
            
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),If(Id(a),Block([Break()]),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))),BinaryOp(=,BinaryOp(>,Id(b),Id(c)),Id(d))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_if_statement_1(self):
        input = """int main(){
            int a,b;
            if(a>10){
                a=a+1;
                b>c=a;
                b;
            }
            return;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),If(BinaryOp(>,Id(a),IntLiteral(10)),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,BinaryOp(>,Id(b),Id(c)),Id(a)),Id(b)])),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_if_statement_2(self):
        input = """int main(){
            a[4];
            if(true) return false;
            if(0.5) return z;
            if(1e2) break;
        }"""
        # expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("a"),IntLiteral(4)),If(BooleanLiteral(True),Return(BooleanLiteral(False))),If(FloatLiteral(0.5),Return(Id("z"))),If(FloatLiteral(100.0),Break())]))]))
        expect="Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(Id(a),IntLiteral(4)),If(BooleanLiteral(true),Return(BooleanLiteral(false))),If(FloatLiteral(0.5),Return(Id(z))),If(FloatLiteral(100.0),Break())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_if_statement_3(self):
        input = """string a,b;
        void main(){
            if(true && a > 5) a[foo()]=0;
            if(0.5+a==9) return true;
            if(1e2<=a) break;
        }"""
        # expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",BooleanLiteral(True),BinaryOp(">",Id("a"),IntLiteral(5))),BinaryOp("=",ArrayCell(Id("a"),CallExpr(Id("foo"),[])),IntLiteral(0))),If(BinaryOp("==",BinaryOp("+",FloatLiteral(0.5),Id("a")),IntLiteral(9)),Return(BooleanLiteral(True))),If(BinaryOp("<=",FloatLiteral(100.0),Id("a")),Break())]))]))
        expect="Program([VarDecl(a,StringType),VarDecl(b,StringType),FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(&&,BooleanLiteral(true),BinaryOp(>,Id(a),IntLiteral(5))),BinaryOp(=,ArrayCell(Id(a),CallExpr(Id(foo),[])),IntLiteral(0))),If(BinaryOp(==,BinaryOp(+,FloatLiteral(0.5),Id(a)),IntLiteral(9)),Return(BooleanLiteral(true))),If(BinaryOp(<=,FloatLiteral(100.0),Id(a)),Break())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_if_statement_4(self):
        input = """string a,b;
        int main(){
            if(a>b){ a =a + 1;
            break;
            continue;
            }
            else{
                a=-b;
            }
        }"""
        expect = "Program([VarDecl(a,StringType),VarDecl(b,StringType),FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(a),Id(b)),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Break(),Continue()]),Block([BinaryOp(=,Id(a),UnaryOp(-,Id(b)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_if_statement_5(self):
        input = """string a,b;
        int main(){
            int a[10];
            if(a>b) a=a+1; else if(a<=c) return;
            if(true) a=false; else a>b;
        }"""
        expect = "Program([VarDecl(a,StringType),VarDecl(b,StringType),FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(IntType,10)),If(BinaryOp(>,Id(a),Id(b)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(<=,Id(a),Id(c)),Return())),If(BooleanLiteral(true),BinaryOp(=,Id(a),BooleanLiteral(false)),BinaryOp(>,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_if_statement_6(self):
        input = """string x,y;
        int main(){
            string a[10];
            a[a[5]]=true;
            if(a>b) a=a+1; else if(a<=c) return; else a<=b;
        }"""
        expect = "Program([VarDecl(x,StringType),VarDecl(y,StringType),FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(StringType,10)),BinaryOp(=,ArrayCell(Id(a),ArrayCell(Id(a),IntLiteral(5))),BooleanLiteral(true)),If(BinaryOp(>,Id(a),Id(b)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(<=,Id(a),Id(c)),Return(),BinaryOp(<=,Id(a),Id(b))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_if_statement_7(self):
        input = """string x,y;
        float a(){}
        int main(){
            string a[10];
            a[a[5]]=true;
            if(a>b) a=true; else if((a<=c)>d) return "o"; else a<=(b+5);
        }"""
        expect = "Program([VarDecl(x,StringType),VarDecl(y,StringType),FuncDecl(Id(a),[],FloatType,Block([])),FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(StringType,10)),BinaryOp(=,ArrayCell(Id(a),ArrayCell(Id(a),IntLiteral(5))),BooleanLiteral(true)),If(BinaryOp(>,Id(a),Id(b)),BinaryOp(=,Id(a),BooleanLiteral(true)),If(BinaryOp(>,BinaryOp(<=,Id(a),Id(c)),Id(d)),Return(StringLiteral(o)),BinaryOp(<=,Id(a),BinaryOp(+,Id(b),IntLiteral(5)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_if_statement_8(self):
        input = """string x,y;
        int main(){
            if(c>d/a) return;
            else {
                a=a[a>b-c];
            }
        }"""
        expect = "Program([VarDecl(x,StringType),VarDecl(y,StringType),FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(c),BinaryOp(/,Id(d),Id(a))),Return(),Block([BinaryOp(=,Id(a),ArrayCell(Id(a),BinaryOp(>,Id(a),BinaryOp(-,Id(b),Id(c)))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_if_statement_9(self):
        input = """string x,y;
        float[] PPL(){
            if(c<=d/a) return;
            else {
                a=b[99>g[10]]-a[a>b-c];
            }
        }"""
        expect = "Program([VarDecl(x,StringType),VarDecl(y,StringType),FuncDecl(Id(PPL),[],ArrayTypePointer(FloatType),Block([If(BinaryOp(<=,Id(c),BinaryOp(/,Id(d),Id(a))),Return(),Block([BinaryOp(=,Id(a),BinaryOp(-,ArrayCell(Id(b),BinaryOp(>,IntLiteral(99),ArrayCell(Id(g),IntLiteral(10)))),ArrayCell(Id(a),BinaryOp(>,Id(a),BinaryOp(-,Id(b),Id(c))))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    #test expression
    def test_expression(self):
        input = """int main(){
            a=a+1;
            b+c=d>e;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,BinaryOp(+,Id(b),Id(c)),BinaryOp(>,Id(d),Id(e)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_expression_1(self):
        input = """float foo(string a, int b){
            int a,b[10];
            string str[4];
        }
        int a(){
            a(a+b>c,a[a+b]);
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,StringType),VarDecl(b,IntType)],FloatType,Block([VarDecl(a,IntType),VarDecl(b,ArrayType(IntType,10)),VarDecl(str,ArrayType(StringType,4))])),FuncDecl(Id(a),[],IntType,Block([CallExpr(Id(a),[BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),ArrayCell(Id(a),BinaryOp(+,Id(a),Id(b)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_expression_2(self):
        input = """int test(){
            if(a>4) return;
            i+2;
            i=i+4;
            z>=5+2;
            if(b) return z+2;
        }"""
        expect = "Program([FuncDecl(Id(test),[],IntType,Block([If(BinaryOp(>,Id(a),IntLiteral(4)),Return()),BinaryOp(+,Id(i),IntLiteral(2)),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(4))),BinaryOp(>=,Id(z),BinaryOp(+,IntLiteral(5),IntLiteral(2))),If(Id(b),Return(BinaryOp(+,Id(z),IntLiteral(2))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_expression_3(self):
        input = """int test(){
            int a;
            a=a+4*6+3>5;
            a/2=p/c+3*"hello"-d;
        }"""
        expect = "Program([FuncDecl(Id(test),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(>,BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(*,IntLiteral(4),IntLiteral(6))),IntLiteral(3)),IntLiteral(5))),BinaryOp(=,BinaryOp(/,Id(a),IntLiteral(2)),BinaryOp(-,BinaryOp(+,BinaryOp(/,Id(p),Id(c)),BinaryOp(*,IntLiteral(3),StringLiteral(hello))),Id(d)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_expression_4(self):
        input = """float PPLmain(){
            if( a==b && a!=c){
                a=b>=c;
                a=c;
            }
        }"""
        expect = "Program([FuncDecl(Id(PPLmain),[],FloatType,Block([If(BinaryOp(&&,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(a),Id(c))),Block([BinaryOp(=,Id(a),BinaryOp(>=,Id(b),Id(c))),BinaryOp(=,Id(a),Id(c))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_expression_5(self):
        input = """void main(){
            foo(2)[3+x]=a[b[2]]+3;
            c[d[e+g]]=foo(a[9]+c[9[c-g]]);
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),BinaryOp(+,IntLiteral(3),Id(x))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLiteral(2))),IntLiteral(3))),BinaryOp(=,ArrayCell(Id(c),ArrayCell(Id(d),BinaryOp(+,Id(e),Id(g)))),CallExpr(Id(foo),[BinaryOp(+,ArrayCell(Id(a),IntLiteral(9)),ArrayCell(Id(c),ArrayCell(IntLiteral(9),BinaryOp(-,Id(c),Id(g)))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_expression_6(self):
        input = """void main(int a[],float b,string c){
            array[a[a[c]+b]]=c*b-d/a;
            x<=y || a == b ;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,FloatType),VarDecl(c,StringType)],VoidType,Block([BinaryOp(=,ArrayCell(Id(array),ArrayCell(Id(a),BinaryOp(+,ArrayCell(Id(a),Id(c)),Id(b)))),BinaryOp(-,BinaryOp(*,Id(c),Id(b)),BinaryOp(/,Id(d),Id(a)))),BinaryOp(||,BinaryOp(<=,Id(x),Id(y)),BinaryOp(==,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_expression_7(self):
        input = """void main(int a[],string c){
            x<=y || a == b ;
            rational(g+5*p[20]);
            print("result"+rational);
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(c,StringType)],VoidType,Block([BinaryOp(||,BinaryOp(<=,Id(x),Id(y)),BinaryOp(==,Id(a),Id(b))),CallExpr(Id(rational),[BinaryOp(+,Id(g),BinaryOp(*,IntLiteral(5),ArrayCell(Id(p),IntLiteral(20))))]),CallExpr(Id(print),[BinaryOp(+,StringLiteral(result),Id(rational))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_expression_8(self):
        input = """void PPLmain(int a[],string c){
            x<=y || a == b || a=true && b+c || false;
        }"""
        expect = "Program([FuncDecl(Id(PPLmain),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(c,StringType)],VoidType,Block([BinaryOp(=,BinaryOp(||,BinaryOp(||,BinaryOp(<=,Id(x),Id(y)),BinaryOp(==,Id(a),Id(b))),Id(a)),BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BinaryOp(+,Id(b),Id(c))),BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_expression_9(self):
        input = """void PPLmain(string c){
            true || x >= (y || a=true) && b+c || false;
        }"""
        expect = "Program([FuncDecl(Id(PPLmain),[VarDecl(c,StringType)],VoidType,Block([BinaryOp(||,BinaryOp(||,BooleanLiteral(true),BinaryOp(&&,BinaryOp(>=,Id(x),BinaryOp(=,BinaryOp(||,Id(y),Id(a)),BooleanLiteral(true))),BinaryOp(+,Id(b),Id(c)))),BooleanLiteral(false))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    #test for statement
    def test_for_statement(self):
        input = """int main(){
            for(i=0;i<10;i=i+1){
                if(true) return;
                return;
                a=a+i;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BooleanLiteral(true),Return()),Return(),BinaryOp(=,Id(a),BinaryOp(+,Id(a),Id(i)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_for_statement_1(self):
        input = """float a(){
            int a[9],i;
            for(i=0;i<9;i=i+1){
                a[i]="PPL Lover";
            }
            print("successful");
        }"""
        expect = "Program([FuncDecl(Id(a),[],FloatType,Block([VarDecl(a,ArrayType(IntType,9)),VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(9));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),StringLiteral(PPL Lover))])),CallExpr(Id(print),[StringLiteral(successful)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_for_statement_2(self):
        input = """float a(){
            int a[9],i;
            for(i=0;i<9;i=i+1){
                if(i+1==9){
                    a[i]=a[0];
                    break;
                }
                a[i]=a[i+1];
            }
            print("PPL pass successful");
        }"""
        expect = "Program([FuncDecl(Id(a),[],FloatType,Block([VarDecl(a,ArrayType(IntType,9)),VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(9));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(+,Id(i),IntLiteral(1)),IntLiteral(9)),Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),ArrayCell(Id(a),IntLiteral(0))),Break()])),BinaryOp(=,ArrayCell(Id(a),Id(i)),ArrayCell(Id(a),BinaryOp(+,Id(i),IntLiteral(1))))])),CallExpr(Id(print),[StringLiteral(PPL pass successful)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_for_statement_3(self):
        input = """boolean mainPPL(){
            int a[9],i;
            for(i=8;i>=0;i=i+2){
                if(i==false)
                    return true;
                return false;
            }
        }"""
        expect = "Program([FuncDecl(Id(mainPPL),[],BoolType,Block([VarDecl(a,ArrayType(IntType,9)),VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(8));BinaryOp(>=,Id(i),IntLiteral(0));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(2)));Block([If(BinaryOp(==,Id(i),BooleanLiteral(false)),Return(BooleanLiteral(true))),Return(BooleanLiteral(false))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    #test do while statement
    def test_dowhile_statement(self):
        input = """int main(){
            do a=a+1; while a<10;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_dowhile_statement_1(self):
        input = """int main(){
            int a,b;
            do a=a+1; while a<10;
            return true;
            float c;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(10))),Return(BooleanLiteral(true)),VarDecl(c,FloatType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_dowhile_statement_2(self):
        input = """void main(string args[]){
            do{ 
                a+b=1;
                if(a>b) break;
                else return; 
            }while a<b+c;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([Dowhile([Block([BinaryOp(=,BinaryOp(+,Id(a),Id(b)),IntLiteral(1)),If(BinaryOp(>,Id(a),Id(b)),Break(),Return())])],BinaryOp(<,Id(a),BinaryOp(+,Id(b),Id(c))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_dowhile_statement_3(self):
        input = """void main(string args[]){
            do{ 
                a+b=1;
                if(a>b) break;
                else return; 
            }
            {
                int x,y,z;
                x=y+z;
            }while a[a<b+c];
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([Dowhile([Block([BinaryOp(=,BinaryOp(+,Id(a),Id(b)),IntLiteral(1)),If(BinaryOp(>,Id(a),Id(b)),Break(),Return())]),Block([VarDecl(x,IntType),VarDecl(y,IntType),VarDecl(z,IntType),BinaryOp(=,Id(x),BinaryOp(+,Id(y),Id(z)))])],ArrayCell(Id(a),BinaryOp(<,Id(a),BinaryOp(+,Id(b),Id(c)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_dowhile_statement_4(self):
        input = """void main(string args[]){
            do{ 
                //void var;
                -a+c=d;
            }
            while a>2.4e3;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([Dowhile([Block([BinaryOp(=,BinaryOp(+,UnaryOp(-,Id(a)),Id(c)),Id(d))])],BinaryOp(>,Id(a),FloatLiteral(2400.0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_dowhile_statement_5(self):
        input = """void main(string args[]){
            do{ 
                consolelog("string\\n");
                print(a,b,c);
                if(PPL==pass)
                    print("An mung");
            }
            while (PPL==pass);
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([Dowhile([Block([CallExpr(Id(consolelog),[StringLiteral(string\\n)]),CallExpr(Id(print),[Id(a),Id(b),Id(c)]),If(BinaryOp(==,Id(PPL),Id(pass)),CallExpr(Id(print),[StringLiteral(An mung)]))])],BinaryOp(==,Id(PPL),Id(pass)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_dowhile_statement_6(self):
        input = """void main(string args[]){
            int i;
            i=0;
            do{ 
                dowhilebidao=true;
                return false;
                toPassPPL=true;
                i=i+1;
            }
            while (PPL==pass);
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([VarDecl(i,IntType),BinaryOp(=,Id(i),IntLiteral(0)),Dowhile([Block([BinaryOp(=,Id(dowhilebidao),BooleanLiteral(true)),Return(BooleanLiteral(false)),BinaryOp(=,Id(toPassPPL),BooleanLiteral(true)),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])],BinaryOp(==,Id(PPL),Id(pass)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    #test break statement
    def test_break_statement(self):
        input = """float test(){
            break;
        }"""
        expect = "Program([FuncDecl(Id(test),[],FloatType,Block([Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_break_statement_1(self):
        input = """float test(){
            if(a>b)
                break;
            else
                -a/b+c*1=d;
        }"""
        expect = "Program([FuncDecl(Id(test),[],FloatType,Block([If(BinaryOp(>,Id(a),Id(b)),Break(),BinaryOp(=,BinaryOp(+,BinaryOp(/,UnaryOp(-,Id(a)),Id(b)),BinaryOp(*,Id(c),IntLiteral(1))),Id(d)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_break_statement_2(self):
        input = """float test(){
           for(i=1;i<10;i=i+1){
               a="Principle";
               b="Programming";
               c="Language";
               z=a+b+c;
               if(z==null) break;
               print("rs = " + z);
           }
        }"""
        expect = "Program([FuncDecl(Id(test),[],FloatType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(a),StringLiteral(Principle)),BinaryOp(=,Id(b),StringLiteral(Programming)),BinaryOp(=,Id(c),StringLiteral(Language)),BinaryOp(=,Id(z),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c))),If(BinaryOp(==,Id(z),Id(null)),Break()),CallExpr(Id(print),[BinaryOp(+,StringLiteral(rs = ),Id(z))])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    
    #test continue statement
    def test_continue_statement(self):
        input = """float foo(){
                    if(true) continue;           
                }"""
        expect = "Program([FuncDecl(Id(foo),[],FloatType,Block([If(BooleanLiteral(true),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_continue_statement_1(self):
        input = """float foo(){
                    do{
                        a=a+1;
                        if(a<0) continue;
                    }
                    while (a>10);
                    if(true) continue;           
                }"""
        expect = "Program([FuncDecl(Id(foo),[],FloatType,Block([Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(<,Id(a),IntLiteral(0)),Continue())])],BinaryOp(>,Id(a),IntLiteral(10))),If(BooleanLiteral(true),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_continue_statement_2(self):
        input = """int main(){
            cout((array[i])[j]);
            if(a>c) continue;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(cout),[ArrayCell(ArrayCell(Id(array),Id(i)),Id(j))]),If(BinaryOp(>,Id(a),Id(c)),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_continue_statement_3(self):
        input = """int main(){
            do { 
                continue;
            }
            while((arr[i])[j]);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([Continue()])],ArrayCell(ArrayCell(Id(arr),Id(i)),Id(j)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_expr_19(self):
        input = """Function : main 
Body:
    expr = expr*2*0x123;
EndBody."""

        expect = Program([FuncDecl( name = Id("main"), param = [], 
                   body=([] ,[
                       Assign(lhs=Id(name='expr'),
                       rhs=BinaryOp(
                            '*',
                            BinaryOp('*',Id(name='expr'),IntLiteral(value = 2)),
                            IntLiteral(value = int('0x123',0))
                       ))]
                    )
                )
            ])

        self.assertTrue(TestAST.checkASTGen(input,expect,379))    

    def test_expr_22(self):
        input = """Function : main 
Body:
    expr = 123.E2;
EndBody."""

        expect = Program([FuncDecl( name = Id("main"), param = [], 
                   body=([] ,[
                        Assign(
                            lhs=Id(name='expr'),
                            rhs=FloatLiteral(value=float("123.E2"))
                        )
                        ]
                    )
                )
            ])

        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_expr_23(self):
        input = """Function : main 
Body:
    expr = a[1 + 2][2 + 7];
EndBody."""

        expect = Program([FuncDecl( name = Id("main"), param = [], 
                   body=([],[
                        Assign(
                            lhs=Id(name='expr'),
                            rhs=ArrayCell(
                                arr=Id(name='a'),
                                idx=[
                                    BinaryOp(op='+',left=IntLiteral(1),right=IntLiteral(2)),
                                    BinaryOp(op='+',left=IntLiteral(2),right=IntLiteral(7))
                                ]
                            )
                        )
                        ]
                    )
                )
            ])

        self.assertTrue(TestAST.checkASTGen(input,expect,381)) 


    def test_expr_24(self):
        input = """Function : main 
Body:
    expr = a == b && c;
EndBody."""

        expect = Program([FuncDecl( name = Id("main"), param = [], 
                   body=([],[
                        Assign(
                            lhs=Id(name='expr'),
                            rhs=BinaryOp(op='==',
                            right=BinaryOp(op='&&',left=Id(name='b'),right=Id(name='c')),
                            left=Id(name='a'))
                        )
                        ]
                    )
                )
            ])

        self.assertTrue(TestAST.checkASTGen(input,expect,383)) 

    def test_expr_25(self):
        input = """Function : main 
Body:
    expr = a || b + c;
EndBody."""

        expect = Program([FuncDecl( name = Id("main"), param = [], 
                   body=([],[
                        Assign(
                            lhs=Id(name='expr'),
                            rhs=BinaryOp(op='||',
                            right=BinaryOp(op='+',left=Id(name='b'),right=Id(name='c')),
                            left=Id(name='a'))
                        )
                        ]
                    )
                )
            ])

        self.assertTrue(TestAST.checkASTGen(input,expect,384)) 

    def test_expr_26(self):
        input = """Function : main 
Body:
    expr = a + b * c;
EndBody."""

        expect = Program([FuncDecl( name = Id("main"), param = [], 
                   body=([],[
                        Assign(
                            lhs=Id(name='expr'),
                            rhs=BinaryOp(op='+',
                            right=BinaryOp(op='*',left=Id(name='b'),right=Id(name='c')),
                            left=Id(name='a'))
                        )
                        ]
                    )
                )
            ])

        self.assertTrue(TestAST.checkASTGen(input,expect,385)) 

    def test_expr_27(self):
        input = """Function : main 
Body:
    expr = !-.True;
EndBody."""

        expect = Program([FuncDecl( name = Id("main"), param = [], 
                   body=([],[
                        Assign(
                            lhs=Id(name='expr'),
                            rhs=UnaryOp(
                                op='!',
                                body=UnaryOp(op='-.',body=BooleanLiteral(value=True))
                            )
                        )
                        ]
                    )
                )
            ])

        self.assertTrue(TestAST.checkASTGen(input,expect,386)) 


    def test_expr_28(self):
        input = """Function : main 
Body:
    expr = !func();
EndBody."""

        expect = Program([FuncDecl( name = Id("main"), param = [], 
                   body=([],[
                        Assign(
                            lhs=Id(name='expr'),
                            rhs=UnaryOp(
                                op='!',
                                body=CallExpr(
                                    method=Id(name='func'),
                                    param=[]
                                )
                            )
                        )
                        ]
                    )
                )
            ])

        self.assertTrue(TestAST.checkASTGen(input,expect,387)) 




