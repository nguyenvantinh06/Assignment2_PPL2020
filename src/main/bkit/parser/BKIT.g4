//MSSV:1814356
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
    language=Python3;
}
program: declaration EOF;

declaration: variable_declare* function_declare*;
//Parser

variable_declare: VAR CL variable_list SEMI;

variable_list: variable (COMMA variable)* ;
variable : scalar_variable|composite;

scalar_variable: ID ('='(DECIMAL|OCTAL|HEXA|FLOAT|STRING|BOOL|array_list))? ;
composite:ID (LSB int_assignment RSB)+ ('='(type_assignment))?;
int_assignment:DECIMAL|OCTAL|HEXA;
type_assignment:DECIMAL|OCTAL|HEXA|FLOAT|STRING|BOOL|array_list;

function_declare:(FUNCTION CL ID (PARAMETER CL parameter_list)? body);

parameter_list: parameter_id (COMMA parameter_id)*;
parameter_id:ID('['(intnew)']')*;
intnew: DECIMAL|OCTAL|HEXA; 
body: BODY CL statement_list ENDBODY DOT;
statement_list: (variable_declare)*(function_list)*;
function_list:assignmentstatement|ifstatement|forstatement|whilestatement|dowhilestatement|breakstatement|continuestatement|callstatement|returnstatement;

ifstatement:IF exp THEN statement_list (ELSEIF exp THEN statement_list)* (ELSE statement_list)? ENDIF DOT ;
forstatement:FOR LP scalar_variable EQ exp COMMA exp COMMA exp RP DO statement_list ENDFOR DOT;
whilestatement:WHILE exp DO statement_list ENDWHILE DOT;
dowhilestatement:DO statement_list WHILE exp ENDDO DOT;

breakstatement:BREAK SEMI;
continuestatement:CONTINUE SEMI;
callstatement:ID LB ( exp ( COMMA exp )*)? RB SEMI;
returnstatement:RETURN exp? SEMI;

assignmentstatement:(ID|exp6) EQ exp SEMI;
function_call: ID LP  (exp (COMMA exp)*)? RP;

exp:exp1 (ASSIGN|NOT_EQUAL|LESS_THAN|GREATER_THAN|LTOE|GTOE|ASSIGNFLOAT|LTOEFLOAT|GTOEFLOAT|LESS_THAN_FLOAT|GREATER_THAN_FLOAT) exp1|exp1;
exp1:exp1 (AND|OR) exp2|exp2;
exp2:exp2 (SUB|SUBFLOAT|ADD|ADDFLOAT) exp3|exp3;
exp3:exp3 (MUL|MULFLOAT|DIV|DIVFLOAT|PERCENT) exp4|exp4;
exp4: '!' exp4|exp5;
exp5:(SUB|SUBFLOAT) exp5|exp6;
exp6: exp7 (LSB exp RSB)+ |exp7 ;
exp7:function_call|exp8;
exp8: LP exp RP|exp9;
exp9:DECIMAL|OCTAL|HEXA|FLOAT|ID|STRING|BOOL|array_list;


//Array
array: DECIMAL|OCTAL|HEXA|STRING|BOOL|FLOAT| array_list;
array_list: '{' (array (',' array)*)? '}';

//Lexer
COMMENT:('**' ('\n' '*')* .*? '**')->skip;
ID: [a-z][a-zA-Z0-9_]* ;

//Integer
DECIMAL:([0-9]+);
INT:HEXA|ID|OCTAL;
HEXA:'0'([Xx])([A-F] | [0-9])+;
OCTAL:'0'([Oo])[0-7]+;

//Float

FLOAT:([0-9]+) ('.'[0-9]*)? (('e'|'E')('+'|'-'|)[1-9]+)?;

//Boolean
TRUE:'True';
FALSE:'False';
fragment LETTER:[a-zA-Z];
fragment DIGIT:[0-9];
BOOL:TRUE|FALSE;

//String

STRING: '"' ((~('\\'|'"'))| ('\\' ('t'| 'n'| 'b'| 'f'| 'r'| '\''|'\\'))| ('\'"') )* '"'
{
        self.text = self.text[1:-1]
};

//Key_word
BODY:'Body'; 
BREAK:'Break';
CONTINUE:'Continue';
DO: 'Do';
ELSE:'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR:'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF:'If'; 
PARAMETER:'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR:'Var';
WHILE: 'While';
ENDDO:'EndDo';

//Seperators
LB: '{';
RB: '}';
LSB:'[';
RSB:']';
LP: '(';
RP: ')';
DOT:'.';
SEMI: ';';
COMMA: ',';
EQ:'=';
CL:':';

//Arithmetic operators
MUL:'*';
MULFLOAT:'*.';
SUB:'-';
SUBFLOAT:'-.';
ADD:'+';
ADDFLOAT:'+.';
DIV:'\\';
DIVFLOAT:'\\.';
PERCENT:'%';
//Boolean_Operator

NOT:'!';

//Relation operators

ASSIGN:'==';
NOT_EQUAL:'!=';
LESS_THAN:'<';
GREATER_THAN:'>';
LTOE:'<=';
GTOE:'>=';
ASSIGNFLOAT:'=/=';
LESS_THAN_FLOAT:'<.';
GREATER_THAN_FLOAT:'>.';
LTOEFLOAT:'<=.';
GTOEFLOAT:'>=.';
AND:'&&';
OR:'||';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment LEGAL_ESCAPE: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\"' | '\\''\\';

UNCLOSE_STRING:'"' (~[\n\r\b\f\t\\"] | LEGAL_ESCAPE)* ;
ILLEGAL_ESCAPE: UNCLOSE_STRING '\\' ~[nrbft"\\] ;
UNTERMINATED_COMMENT: '**' ('*' ~'*' | ~'*')*? EOF;
ERROR_CHAR:.;





