grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: classdecl_list EOF;
classdecl_list: classdecl classdecl_list | classdecl;

//////////////////////////////// PROGRAM STRUCTURE //////////////////////////////
classdecl:
	CLASS ID LP members RP
	| CLASS ID CL ID LP members RP;
members: (attribute | method) members | attribute | method |;
// attribute: (VAL | VAR) (idlist | idulist) CL mptype SM | (VAL | VAR) (idlist | idulist) CL mptype
// ASSIGN exp_list SM;

attribute: (VAL | VAR) idglist CL mptype SM
	| (VAL | VAR) idglist CL mptype ASSIGN exp_list SM;
method: (ID | IDUSD | CONSTRUCTOR | DESTRUCTOR) param_list block_stmt;
param_list: LB params_decl RB | LB RB;
params_decl: param_decl SM params_decl | param_decl;
param_decl: idlist CL mptype;
idglist: (ID | IDUSD) CM idglist | ID | IDUSD;
idlist: ID CM idlist | ID;
idulist: IDUSD CM idulist | IDUSD;
mptype:
	INTTYPE
	| FLOATTYPE
	| BOOLTYPE
	| STRINGTYPE
	| array_type
	| class_type;
class_type: exp10;
array_type: ARRAY LS (mptype | ARRAY) CM INTLIT RS;
//expression
exp: exp1 (ADDT | ET) exp1 | exp1;
exp1: exp2 (EQ | NEQ | LT | GT | LE | GE) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: exp7 index_list | exp8;
exp8:
	exp8 DOT ID LB exp_list RB
	| exp8 DOT ID
	| exp8 DOT ID LB RB
	| exp9;
exp9:
	exp9 STA IDUSD LB exp_list RB
	| exp9 STA IDUSD
	| exp9 STA IDUSD LB RB
	| exp10;
exp10: NEW ID LB exp_list RB | NEW ID LB RB | exp11;
exp11: LB exp RB | exp12;
exp12: literals | ID | IDUSD;
exp_list: exp CM exp_list | exp;
index_list: LS exp RS index_list | LS exp RS;

//statements
block_stmt: LP stmt_list RP | LP RP;
stmt_list: stmt stmt_list | stmt;
stmt:
	decl_stmt
	| assign_stmt
	| if_stmt
	| loop_stmt
	| break_stmt
	| cont_stmt
	| return_stmt
	| method_stmt;
decl_stmt:
	(VAL | VAR) idlist CL mptype SM
	| (VAL | VAR) idlist CL mptype ASSIGN exp_list SM;
assign_stmt: exp7 ASSIGN exp SM;

if_stmt:
	IF LB exp RB block_stmt else_list
	| IF LB exp RB block_stmt;
else_list: elseif_stmt else_list | elseif_stmt | else_stmt;
elseif_stmt: ELSEIF LB exp RB block_stmt;
else_stmt: ELSE block_stmt;

loop_stmt: FOREACH LB loop_condition RB block_stmt;
loop_condition:
	ID IN exp DOT DOT exp
	| ID IN exp DOT DOT exp BY exp;

break_stmt: BREAK SM;
cont_stmt: CONTINUE SM;
return_stmt: RET exp SM | RET SM;

method_stmt: instance SM | static SM;
instance:
	exp DOT ID LB exp_list RB
	| exp DOT ID
	| exp DOT ID LB RB;
static:
	exp STA IDUSD LB exp_list RB
	| exp STA IDUSD
	| exp STA IDUSD LB RB;

arraylit: ARRAY LB exp_list RB;
//indexed_array: ARRAY LB exp_list RB; indexed_array_list: indexed_array CM indexed_array_list |
// indexed_array; multi_array: ARRAY LB indexed_array_list RB;

/////////////////////////////////////////////////////////

/////////////////////// LEXICAL STRUCTURE /////////////////////////////

//comment//
CMT: '##' .*? '##' -> skip;

//keywords//
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INTTYPE: 'Int';
FLOATTYPE: 'Float';
BOOLTYPE: 'Boolean';
STRINGTYPE: 'String';
RET: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
SELF: 'Self';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';

//operators//
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
ASSIGN: '=';
NEQ: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
ET: '==.';
ADDT: '+.';
STA: '::';
DOT: '.';
// OBJ: 'New';

//separtors//
LB: '(';
RB: ')';
LS: '[';
RS: ']';
LP: '{';
RP: '}';
CM: ',';
SM: ';';
CL: ':';

//identifers//
fragment DIGITS: [1-9] | '0';
fragment LETTERS: [A-Za-z];

ID: (LETTERS | '_') (LETTERS | '_' | DIGITS)*;
IDUSD: '$' (LETTERS | '_' | DIGITS)+;

//literals//
literals:
	INTLIT
	| FLOATLIT
	| STRINGLIT
	| arraylit
	| boolit
	| SELF
	| NULL;

INTLIT:
	INT {self.text = self.text.replace("_", "")}
	| OCT {self.text = self.text.replace("_", "")}
	| HEX {self.text = self.text.replace("_", "")}
	| BIN {self.text = self.text.replace("_", "")};
fragment INT: '0' | [1-9] [0-9]* ('_' [0-9]+)* EXP?;
fragment OCT: '0' ([0-7]+ ('_' [0-7]+)*);
fragment HEX: '0' ('x' | 'X') ([0-9A-F]+ ('_' [0-9A-F]+)*);
fragment BIN: '0' ('b' | 'B') ([0-1]+ ('_' [0-1]+)*);

FLOATLIT:
	INT DEC? {self.text = self.text.replace("_", "")}
	| INT? DEC {self.text = self.text.replace("_", "")};
fragment EXP: ('e' | 'E') ('-' | '+')? DIGITS+;
fragment DEC: '.' DIGITS* EXP?;

boolit: TRUE | FALSE;
STRINGLIT:
	'"' STR_CHAR* '"' {
	temp = self.text
	self.text = temp[1:-1]
};
fragment STR_CHAR: ~[\b\f\r\n\t'"\\] | ESC_SEQ | '\'"';
fragment ESC_SEQ: '\\' [bfrnt'\\];

//////////////////////////////////////////////////////////////////////////

// skip spaces, tabs, newlines
WS: [ \t\r\n\b\f]+ -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING:
	'"' STR_CHAR* ([\b\t\n\f\r'\\] | EOF) {
y = str(self.text)
p = ['\b', '\t', '\n', '\f', '\r', "'", '\\']
if y[-1] in p:
    raise UncloseString(y[1:-1])
else:
    raise UncloseString(y[1:])
};

ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
};
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | ~'\\';
