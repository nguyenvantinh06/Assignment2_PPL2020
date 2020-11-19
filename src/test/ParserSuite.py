import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    
    def test_201(self):
        """ test var """
        input = """Var: m=5;""" ;     
        expect = "successful";
        self.assertTrue(TestParser.checkParser(input,expect,201));
    def test_202(self):
        """test var"""
        input ="""Var: c, d = 6, e, f;""";
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_203(self):
        """test var"""
        input=""" Var: a = 0.5, b = 72.e2, c = "HCMUT", d = 52, e; """;
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_204(self):
        """test function"""
        input="""
        Function: main
        Body:
        x = 10;
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_205(self):
        """test_if"""
        input ="""
        Function: main
        Body:
        If a==2 Then
        
        EndIf.
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_206(self):
        input ="""
        Function: main
        Body:
        If (a==2) Then
        Var: a=1;
        EndIf.
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_207(self):
        input ="""
        Function: main
        Body:
        If (a==2) Then
        Var: a=1;
        y = foo(2 + x, 4. \. y);
        EndIf.
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_208(self):
        input ="""
        Function: foo
        Body:
        If (a==2) Then
        Var: a=1;
        y = foo(2 + x, 4. \. y)+a;
        EndIf.
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_209(self):
        input ="""
        Function: foo
        Body:
      
        While (n<10) && (m<10) && (check!=False)  Do 
        y = foo(2 + x, 4. \. y)+a;
        EndWhile.
       
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_210(self):
        input ="""
        Function: foo
        Body:
      
        While (n<10) && (m<10) && (check!=False)  Do 
        
        EndWhile.
       
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_211(self):
        input ="""
       Var: x;
    Function: fact
    Parameter: n
    Body:
    If n == 0 Then
    Return 1;
    Else
    Return n * fact (n - 1);
    EndIf.
    EndBody.
    Function: main
    Body:
    x = 10;
    fact (x);   
    EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_212(self):
        input ="""
        Function: abc
        Body:
        Var: r = 10., v;
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.
        """
        output="successful"
        self.assertTrue(TestParser.checkParser(input,output,212))
    def test_213(self):
        input ="""
        Var: a = 3, b=1,c,d,e="abc";
        Function: main
        Body:
        While a<1 Do b=b+1; EndWhile.
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
        
    def test_214(self):
        input ="""
        Var: a = 3, b;
        Function: main
        Body:
        foo (2 + x, 4. \. y);
        goo ();
        While a<1 Do b=b+1; EndWhile.
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_215(self):
        input ="""
        Var: x;
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 1;
Else
Return n * fact (n - 1);
EndIf.
EndBody.
Function: main
Body:
x = 10;
fact (x);
EndBody.
"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_216(self):
        input ="""
        Var: x;
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 1;
Else
Return n * fact (n - 1);
EndIf.
EndBody.
Function: main
Body:
x = 10;
fact (x);
EndBody.
"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
   
    def test_217(self):
        input ="""
Function: foo
Parameter: a[5]
Body:
Var: i = 0,b={1,2,3};
While (i < 5) Do
a[5] = b +. 1.0;
i = i + 1;
EndWhile.
EndBody.

"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_218(self):
        input ="""
Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return True;
    EndIf.
EndBody.    
    """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_219(self):
        input ="""
Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return True;
    EndIf.
EndBody.    
    """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_220(self):
        input ="""
Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return True;
    EndIf.
EndBody.    
    """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_221(self):
        input ="""
Function: test
Parameter: n
Body:
    If n > 10 Then
        Return 5;
    Else
        Return True;
    EndIf.
EndBody.    
    """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_222(self):
        input = """
            Var: x=12,b=12346;
            Function: main 
                Parameter: k,l,m,n 
                Body: 
                    If n == 0 Then 
                        Return 1; 
                    Else 
                        Return n * fact (n - 1); 
                    EndIf. 
                EndBody.
            Function: main1
                Body: 
                    x = 123.123;  
                EndBody.
            Function: foo
              Body:
                 Var: a,value,ass[1][1];
                 a=a+123+123+aas+s1234-1-3-2\\123\\1*22;
             EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_223(self):
        input = """
            Var: x=12,b=12346;
            Function: main 
                Parameter: k,l,m,n 
                Body: 
                    If n == 0 Then 
                        Return 1; 
                    Else 
                        Return n * fact (n - 1); 
                    EndIf. 
                EndBody.
            Function: main1
                Body: 
                    x = 123.123;  
                EndBody.
            Function: foo
              Body:
                 Var: a,value,ass[1][1];
                 a=a+123+123+aas+s1234-1-3-2\\123\\1*22;
             EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223)) 
    def test_224(self):
        input = """
            Var: x=12,b=12346;
            Function: main 
                Parameter: k,l,m,n 
                Body: 
                    If n == 0 Then 
                        Return 1; 
                    Else 
                        Return n * fact (n - 1); 
                    EndIf. 
                EndBody.
            Function: main1
                Body: 
                    x = 123.123;  
                EndBody.
            Function: foo
              Body:
                 Var: a,value,ass[1][1];
                 a=a+123+123+aas+s1234-1-3-2\\123\\1*22;
             EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))    
    
    def test_225(self):
        
        input = """
Function: foo
    Body:
        Var: a,value,ass[1][1];
        a=a+123+123+aas+s1234-1-3-2\\123\\1*22;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
        
    def test_226(self):
   
        input = """
        Function:main
        Body:
        Var: a,b,c[10],d;
        d = -. 1050.001e-19 +. 1123.56 +. 14512.2131e-10 *. 10.2132 \\. 0.01e19 ;
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
        
    def test_227(self):
        """ test assignment statement """
        input = """
        Function: foo
        Body:
        a[1.3+45+foo(123)]=abcd-123+123-123 \\ 123 *123 +. 123 -. 123 ;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
        
    def test_228(self):
        """ test assignment statement """
        input = """
        Function: main
        Body:
            Var: a,c,s[10],v;
            test = (check==food);
            v = 12. +. 10.1e-10 *. 10. \\. 0.01e19 -. 1000000.00001e-19999999;
            If ( (a==2) && (a==3)) Then
            foo(n%i-a[foo(i\\4)]);
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_229(self):
        """ test assignment statement """
        input = """
        Function: main
        Body:
            Var: a,c,s[10],v;
            test = (check==food);
            v = 12. +. 10.1e-10 *. 10. \\. 0.01e19 -. 1000000.00001e-19999999;
            If ( (a==2) && (a==3)) Then
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_230(self):
        """ test assignment statement """
        input = """
        Function: main
        Body:
            Var: a,c,s[10],v;
            test = (check==food);
            v = 12. +. 10.1e-10 *. 10. \\. 0.01e19 -. 1000000.00001e-19999999;
            If ( (a==2) && (a==3)) Then
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_231(self):
        """ test assignment statement """
        input = """
        Function: main
        Body:
         i =foo_5(foo_2(foo_1(abc)\\.foo_3(a[123]-foo_4(123))));     
          If ( (a==2) && (a==3)) Then
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_232(self):
        """ test assignment statement """
        input = """
        Function: main
        Body:
         i =foo_5(foo_2(foo_1(abc)\\.foo_3(a[123]-foo_4(123))));     
          If ( (a==2) && (a==3)) Then
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            EndIf.
        EndBody.
        Function: foo
        Body:
         i =foo_5(foo_2(foo_1(abc)\\.foo_3(a[123]-foo_4(123))));     
          If ( (a==2) && (a==3)) Then
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            EndIf.
        EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_233(self):
        """ test assignment statement """
        input = """
        Function: main
        Body:
        i =foo_5(foo_2(foo_1(abc)\\.foo_3(a[123]-foo_4(123))));     
          While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            EndWhile.
        EndBody.
        Function: foo
        Body:
         i =foo_5(foo_2(foo_1(abc)\\.foo_3(a[123]-foo_4(123))));     
          If ( (a==2) && (a==3)) Then
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            EndIf.
        EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_234(self):
        """ test assignment statement """
        input = """
    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        Var: r = 10., v;
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_235(self):
        """ test assignment statement """
        input = """
                    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_236(self):
        input = """
    Function: main
    Parameter: a,b,c[1][2]
    Body: 
        If (i==0) Then Break;
        Else Return foo4(i) * foo4(i+1);
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    
    def test_237(self):
        input=""" 
            Var: a = 3, b;
                Function: main
                    Body:
                    While (a < True) > 5  Do b=b+1; EndWhile.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_238(self):
        input=""" 
            Var: a = 3, b;
                Function: main
                    Body:
                    While (a ==1) > 5  Do b=b+1; EndWhile.
                    EndBody.
                 Function: main2
                    Body:
                    While (a == True) > 5  Do b=b+1; EndWhile.
                    EndBody.
                Function: main1
                    Body:
                    While (a < True) >( 5>5)  Do b=b+1; EndWhile.
                    EndBody.
                     Function: main3
                    Body:
                    While (a < True) > (5==5)  Do b=b+1; EndWhile.
                    EndBody.
                Function: main12
    Body: 
       ** this is a comment**
    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_239(self):
        input=""" 
            Var: a = 3, b;
                Function: main
                    Body:
                    While (a ==1) > 5  Do b=b+1; EndWhile.
                    EndBody.
                 Function: main2
                    Body:
                    For (j=foo(123),j<=a,1) Do
                     If (a[i]>a[j]) Then
                         temp = a[j];
                         a[j]=a[i];
                        a[i]=temp;
                        
                         EndIf.
                    EndFor.
                    EndBody.
                Function: main1
                    Body:
                    While (a < True) >( 5>5)  Do b=b+1; EndWhile.
                    EndBody.
                     Function: main3
                    Body:
                    While (a < True) > (5==5)  Do b=b+1; EndWhile.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_240(self):
        input=""" 
            Var: a = 3, b;
                Function: main
                    Body:
                    While (a ==1) > 5  Do 
                    b=b+1;
                    temp = a[j];
                    a[j]=a[i];
                    a[i]=temp;
                    EndWhile.
                    EndBody.
                 Function: main2
                    Body:
                    For (j=foo(123)*foo(123),j<=(a+1),1+1+1) Do
                     If (a[i]>a[j]) Then
                         temp = a[j];
                         a[j]=a[i];
                            a[i]=temp;
                        Return a=/=1;
                         EndIf.
                    EndFor.
                    EndBody.
                Function: main1
                    Body:
                    While (a < True) >( 5>5)  Do b=b+1; EndWhile.
                    EndBody.
                     Function: main3
                    Body:
                    While (a < True) > (5==5)  Do b=b+1; EndWhile.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_241(self):
        input=""" 
            Var: a = 3, b;
                Function: main
                    Body:
                    While (a ==1) > 5  Do 
                    b=b+1;
                    temp = a[j];
                    a[j]=a[i];
                    a[i]=temp;
                    EndWhile.
                    EndBody.
                 Function: main2
                    Body:
                    For (j=foo(123)*foo(123),j<=(a+1),1+1+1) Do
                     If (a[i]>a[j]) Then
                         temp = a[j];
                         a[j]=a[i];
                            a[i]=temp;
                        Return a=/=1;
                         EndIf.
                    EndFor.
                    EndBody.
                Function: main1
                    Body:
                    While (check!=False) && (i*-foo1(a[i])) Do
                     If (!check) &&(a==5123*123) Then Break; 
                     EndIf.            
                     EndWhile.
                    EndBody.
                     Function: main3
                    Body:
                    While (a < True) > (5==5)  Do b=b+1; EndWhile.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_242(self):
        input=""" 
            Var: a = 3, b;
                Function: main
                    Body:
                    While (a ==1) > 5  Do 
                    b=b+1;
                    temp = a[j];
                    a[j]=a[i];
                    a[i]=temp;
                    EndWhile.
                    EndBody.
                 Function: main2
                    Body:
                    For (j=foo(123)*foo(123),j<=(a+1),1+1+1) Do
                     If (a[i]>a[j]) Then
                         temp = a[j];
                         a[j]=a[i];
                            a[i]=temp;
                        Return a=/=1;
                         EndIf.
                    EndFor.
                    EndBody.
                Function: main1
                    Body:
                    While (check!=False) && (i*-foo1(a[i])) Do
                     If (!check) &&(a==5123*123) Then Break; 
                     EndIf.            
                     EndWhile.
                    EndBody.
                     Function: main3
                    Body:
                    While (a < True) > (5==5)  Do b=b+1; EndWhile.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_243(self):
        """ test while """
        input = """
Function: main  
    Body:
        
        While abc Do 
            
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_244(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    
    def test_245(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))    
    def test_246(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))    
    def test_247(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))    
    def test_248(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))    
    def test_249(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))    
    def test_250(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))    
    def test_251(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))    
    def test_252(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))    
    def test_253(self):
        input = """
    Function: main
    Parameter: a
    Body: 
        
        While ( (a==2) && (a==3)) Do
            foo(n%i-a[foo(i\\4)]);
            a[i]=a[j];
            Break;
            Return;
        EndWhile.
    EndBody.
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))        
    def test_254(self):
        """ test while """
        input = """
Function: main
    Body:
        While (abcd>1) Do
            While (ghik>1) Do
                While (ijmn<foo(a[b])) Do
                   a=b+c-d*e+f-x +.123\\.123-.123+.123;
        EndWhile.
        EndWhile.
        EndWhile.
        
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
        
    def test_255(self):
        """ test while """
        input = """
Function: main
    Body:
        While (n>1) Do
            While (m>1) Do
                While (k<foo(a[n][b])) Do
                    While (f!= 11-k) Do
                        i=(i+1)-(2*abc) ||(a==a123) ||(a!=123) ;
                    EndWhile.
            EndWhile.
        EndWhile.
    EndBody.
        """
        expect = "Error on line 12 col 4: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,255))
   
    def test_256(self):
        """ test while """
        input = """
Function: main
    Body:
        If (n>1) Then
            a=a+1;
        ElseIf (a==5) Then
                While (k<foo(a[n][b])) Do
                    While (f!= 11-k) Do
                        i=i-1;
                    EndWhile.
                EndWhile.
        
        ElseIf (a==6) Then i=i-1;
        Else i=i+2;
        EndIf.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def testcase_257(self):
        input = """
            Function: main1
	        Body:
		        Return a + b-c+d;
	        EndBody.
            Function: main
	        Body:
		        Var: c = 10,d=11,e=123;
		        For (i = 0, i < 10, 1123) Do
			        If s <=1 Then Break;
                    Else a=a+1;
                    a=foo(12-13)+foo(123+a[1][2]);
			        EndIf.;
		        EndFor.
	        EndBody.
            """
        expect = "Error on line 13 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def testcase_258(self):
        input = """
            Function: test
            Parameter: x, y, z
            Body:
            For (b[2] = 0, i > 0, i + 1) Do
                x = a + b +. x;
                y = a + 12000.;
                z = b || x && c;
            EndFor.
            EndBody.
            """
        expect = "Error on line 5 col 18: ["
        self.assertTrue(TestParser.checkParser(input, expect, 258))
    def testcase_259(self):
        input = """
            Var: i=1;
            Function: foo     
                Body:
                Var: a=0;
                While (x = 1 *. 2 +.3 ) Do
                 
                EndWhile.
                EndBody.
            """
        expect = "Error on line 6 col 16: While"
        self.assertTrue(TestParser.checkParser(input, expect, 259))
    def test_260(self):
        input=""" Var:c = 5, a; 
        Function:nhuiuiuiuiuiu
        Body:
        iu=iu+1;
        EndBody.
        """;
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_261(self):
        input = """
             Function: main
                Parameter: a[10][10], b 
                Body: 
                    If bool_of_string Then 
                        i=i+1;
                    EndIf.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_262(self):
       
        input = """
Function: main
    Body:
        Do 
           While i!=1 Do 
            
            a=special(g)+letranquynhnhu(102);
            i=123*345;
            m=foo(a[i]);
           EndWhile.
        While (a>b) && (b<foo[j]) EndDo.
        Return abc_tinh(abc);
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_263(self):
        """ test do while """
        input = """
Function: foo
    Body:
        While (i<3) Do
            While (i>6) Do
                While (abc+d123) Do
                    a=a+1;
                EndWhile.
            EndWhile.
        EndWhile.
    EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_264(self):
        input= """  Var: a = 5, b=1;
                    Function:main
                    Body:
                    a=a+1;
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_265(self):
        input="""
                Var: a=c, b=5;
                    Function: main
                    Body:
                    If(i==i+1) Then 
                        While imp != 5 Do
                            For( index = 5123 ,ind < 20,8+1-4) Do 
                            a= 1+2-3
                            EndFor.
                        EndWhile.
                    EndIf.
                    EndBody.
        """
        expect = "Error on line 2 col 22: ="
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_266(self):
        input = """
            Var: x;
            Function: fact 
                Parameter: n, a
                Body: 
                    For (a=2, a[1]<10, 2) Do
                        x=n;
                    EndFor.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_267(self):
        input = """
            ** This is a single-line comment. **
            Var: a[10] = {1,2,3,24,13,12,10,13,123,123}; 
            Var: b[2][3]={{5,6,3},{1,2,6}};
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_268(self):
        input = """
             Function: foo 
                Parameter: a[5], b 
                Body: 
                    Var: i = 0; 
                    While (i < 5) Do
                        a[i] = b +. 1.0; 
                        i = i + 1; 
                    EndWhile. 
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_269(self):
        input="""
        Var: x=5,m=10,n={1,2,3},k,t,i,n,h[102]={1,2,3,"This is a string"};
        Function: main
        Parameter:a[3],b
        Body:
        While (i==a) Do
        For (i=5,i<5,foo(3)) Do
            i=i+1;
        For (i=6,i<a,foo(foo(3*foo(3)))) Do
        For (i=5+6,i<10*10-10.,foo(3)*foo(4)*.foo(4)) Do
            i=10;
            print("x");
            print(asdfasdfs);
        EndFor.
        EndFor.
        EndFor.
        EndWhile.
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_270(self):
        
        input = """
             Function: foo 
                Parameter: a[0x10][0X123][0o123], b[0o123][0O123] 
                Body:
                    For (i=5,a==1+2+4+4,6) Do
                    i=13213123;
                    EndFor. 
                    Do c = a[i+foo(5)] - b[a[b[8+a[7+b[8]]]]];
                    c = foo(n)[3] - 2;
                    While (c < 25) || (d > 9)
                    EndDo.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_271(self):
        
        input = """
             Function: foo 
                Parameter: a[0x10][0X123], b[0o123][0O123] 
                Body:
                    For (i=5,i==6,6) Do
                    i=13213123;
                    EndFor. 
                    Do c = a[{1,2,3}] - b[a[b[8+a[7+b[8]]]]];
                    c = foo({1,2,3})*foo(1)*foo[1][2] - 2;
                    Break;
                    Return;

                    While (c < 25) || (d > 9)
                    EndDo.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))            
    def test_272(self):
        
        input = """
             Function: foo 
                Parameter: a[0x10][0X123], b[0o123][0O123] 
                Body:
                    For (i=5,i==6,6+123) Do
                    i=13213123;
                    i=13123;
                    EndFor. 
                    Do c = a[{1,2,3}] - b[a[b[8+a[7+b[8]]]]];
                    c = foo({1,2,3},{123}) - 2;
                    While ((c < 25) || (d > 9))
                    EndDo.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))   

    def test_273(self):
        
        input = """
             Function: foo 
                Parameter: a[0x10][0X123], b[0o123][0O123] 
                Body:
                    print(toni_kross,"chuyen",bcc);
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))            
    def test_274(self):
        input="""
        Function:foo
        Parameter:b
        Body:
        For (i=5,m==123,10) Do
            For (abc_5=123,m==123*123-asdf[foo(f12[123]*foo(1))],i+.1*.21) Do
                While (i==i+foo(123*123.+.foo[1])) Do
                    string=string+"1";
                EndWhile.
            EndFor.
        EndFor.

        EndBody.
        """ 
        output="successful"
        self.assertTrue(TestParser.checkParser(input,output,274))      
    def test_275(self):
        input="""
        Function:foo
        Parameter:b
        Body:
        For (i=5,m==123,10) Do
            For (abc_5=123,m==123*123-asdf[foo(f12[123]*foo(1))],i+.1*.21) Do
                While (i==i+foo(123*123.+.foo[1])) Do
                    string=string+"1";
                EndWhile.
            EndFor.
        EndFor.

        EndBody.
        Function:main
        Parameter:b[10][123]
        Body:
        For (i=5,m==123-213+213213*213-12-.1+.1.+1.,10) Do
            For (abc_5=123,m==123*123-asdf[foo(f12[123]*foo(1))],i+.1*.21) Do
                While (i==i+foo(123*123.-.foo[1])) Do
                    string=string+"1";
                    a=25[25];
                EndWhile.
            EndFor.
        EndFor.

        EndBody.
        """    
        output="successful"
        self.assertTrue(TestParser.checkParser(input,output,275))   
    def test_276(self):
        input="""
        Function:main
        Body:
        str1="\\b\\t\\nasdf\\rasdf\\fadfasdf\\' asdfdsfasdfstring";
        str2=str1*10+ foo(4,a[2][123][123][a[2][3]]);
        EndBody."""
        output="successful"
        self.assertTrue(TestParser.checkParser(input,output,276))
    def test_277(self):
        input ="""
        Var: a = 2;
        Function: main
        Body:
        Break;
        While (a==1) Do x=1;
        EndWhile.
        Continue;
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_278(self):
        input ="""
        Var: a = 1232132;
        Function: foo
        Body:
        a=1;
        b=2;
        c=3[3][3];
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_279(self):
        input ="""
        Var: a = 2;
        Function: main
        Body:
        a = 6;
        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_280(self):
        input ="""
        Var: a = 2,b=3,c=4,d=5;
        Function: main
        Parameter: n,m,l[2]
        Body:
        a = 6;

        EndBody.
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def testcase_281(self):
        input = """
            Var: parser = 1810814;
            Function: foo
                Parameter: count, x, y, z
                Body:
                While ((x_13 == 1.0-8+.765 *. 2.098) || False) Do
                While (x==123) Do
                EndWhile.
                EndWhile.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))
    def testcase_282(self):
        input = """
            Function: main
	        Parameter: a,b,c,d,e
	        Body:
		        Break;
                Return;
	        EndBody.
            
            Function: main
	        Body:
		        Var: s = 0;
		        For (i = 0, i < 10, 1) Do
			        If s >= 40 Then Continue;
                    Break;
                    Continue;
			        EndIf.
		        EndFor.
	        EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))
    def testcase_283(self):
        input = """
            Function: main
            
            Body:
            For (b[1][2][3][4] = 123, i <= 0.123, i + 10123) Do
                x = a + b +. x;
                y = a + 12000.23+.123;
                z = (b || x) && c-123;
            While (i==1)
            Do
            EndWhile.
            EndFor.
            EndBody.
            """
        expect = "Error on line 5 col 18: ["
        self.assertTrue(TestParser.checkParser(input, expect, 283))
    def test_284(self):
        input= """  Var: a = 3, b;
                    Function: tinhasf
                    Body:
                    If(a==1) Then 
                        While e != 5 Do
                            For( id = 1235 ,id < 20,8) Do
                            For (i=1,i<213,123) Do
                            EndFor.
                              EndFor.
                        EndWhile.
                    EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_285(self):
        input = """
            Var: x;
            Function: fact 
                Parameter: n, a
                Body: 
                    Var: temp123;
                    temperature=n+123;
                    x=temp+213;
                    foo(123+foo(123+foo(123+foo())));
                EndBody.
             Function: fact123
                Parameter: n
                Body: 
                    Var: temp;
                    temp=n;
                
                    x=temp+a;
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_286(self):
        input = """
            Var: x;
            Function: fact 
                Parameter: n, a
                Body: 
                    For (i=2+2, i<10+123, 2-123+123) Do
                        While (i==2) Do a=a+1;
                        EndWhile.
                    EndFor.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_287(self):
        input = """
            Var: x;
            Function: fact 
                Parameter: n, a
                Body: 
                    For (i[1123]=1232, abc[1213]<12310*.12+.123., a+2) Do
                        For (i=1,i==b,i+3) Do
                            EndFor.

                    EndFor.
                EndBody.
            """
        expect = "Error on line 6 col 26: ["
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_288(self):
        """ test assignment statement """
        input = """
                    Var: r,a,b,c,d,e,f;
                    Function: abc_def_123_ABC_DEF
                    
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        While (a+1) Do
                        EndWhile.
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_289(self):
        """ test assignment statement """
        input = """
                    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        a[3][4][3+foo(2)[123]]=a[2][3]+4;
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_290(self):
        """ test assignment statement """
        input = """
                    Var: r = 10,i=213;
                    Function: main
                    Parameter: n, a[1][3][5][7][9], abc
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        a="<TABLE>";
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        i="HoangvuTinh";
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_291(self):
        """ test assignment statement """
        input = """
                    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_292(self):
        """ test assignment statement """
        input = """
                    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_293(self):
        """ test assignment statement """
        input = """
                    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_294(self):
        """ test assignment statement """
        input = """
                    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_295(self):
     
        input = """
                    Var: r = 1110;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                   
                    Function: a_b_c
                    Parameter:t,i,n,h
                    Body:
                        a[3+a[3] + foo(1)] = a[10][10] + 4.e5;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        While (a==a-7) Do
                        EndWhile.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_296(self):
        
        input = """
                    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                       
                        Break;
                        Return 1;
                        
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_297(self):
        """ test assignment statement """
        input = """
                    Var: r = 10.;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_298(self):
        """ test assignment statement """
        input = """
                 Function: main
                    Body:
                    While (a ==1) > 5  Do b=b+1; EndWhile.
                    EndBody.
                 Function: main2
                    Body:
                    For (j=foo(123),j<=a,1) Do
                     If (a[i]>a[j]) Then
                         temp = a[j];
                         a[j]=a[i];
                        a[i]=temp;
                        
                         EndIf.
                    EndFor.
                    EndBody.
                Function: main1
                    Body:
                    While (a < True) >( 5>5)  Do b=b+1; EndWhile.
                    EndBody.
                     Function: main3
                    Body:
                    While (a < True) > (5==5)  Do b=b+1; EndWhile.
                    EndBody.
                    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_299(self):
        """ test assignment statement """
        input = """
                    Var: r = 10;
                    Function: abc
                    Parameter: n, a[5][7], bcd[9]
                    Body:
                        a[3 + foo(2)] = a[b[2][3]] + 4;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                     Function: main
                    Body:
                        
                        If (a==a-7)Then
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_300(self):
        
        input = """
                    Var: r = 10;
                    Function: abcdcfghijklm_gh_213_ba12Acbmain
                    Parameter:  a[1][1][1][2], bcd[9][123]
                    Body:
                        a[1 + main(main(main()))] = k[h[123][1233]] + 4.;
                        
                        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                        If (a+.a-7)Then
                        EndIf.
                    For (i=1,i==3,i+1) Do
                    a=a+1;
                    EndFor.

                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))