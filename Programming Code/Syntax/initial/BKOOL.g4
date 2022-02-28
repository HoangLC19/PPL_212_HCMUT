grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// program  : mptype 'main' LB RB LP body? RP EOF ;

// mptype: INTTYPE | VOIDTYPE ;

// body: funcall SEMI;

// exp: funcall | INTLIT ;

// funcall: ID LB exp? RB ;

// INTTYPE: 'int' ;

// VOIDTYPE: 'void'  ;

// ID: [a-zA-Z]+ ;

// INTLIT: [0-9]+;

// LB: '(' ;

// RB: ')' ;

// LP: '{';

// RP: '}';

// SEMI: ';' ;

// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// ERROR_CHAR: .; UNCLOSE_STRING: .; ILLEGAL_ESCAPE: .;

/////// 1 /////////

program: (vardecl | funcdecl)+ EOF;

vardecl: 'vardecl';

funcdecl: 'funcdecl';

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};

//////// 2 ///////

// program: decls EOF; decls: decl decls | decl; decl: vardecl | funcdecl;

// //And some other rules for variable declaration, function declaration and other rules

// funcdecl: mptype ID paramdecl body; paramdecl: LP paralist RP | LP RP; paralist: param SM
// paralist | param; param: mptype idlist;

// vardecl: mptype idlist SM; idlist: ID CM idlist | ID;

// mptype: INTTYPE | FLOATTYPE; body: 'body'; INTTYPE: 'int'; FLOATTYPE: 'float'; LP: '('; RP: ')';
// LB: '{'; RB: '}'; SM: ';'; CM: ','; ID: [a-zA-Z]+; WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

//////// 3 /////////

// program: decls EOF;

// decls: decl decls | decl; decl: vardecl | funcdecl;

// //And some other rules for variable declaration, function declaration and other rules

// funcdecl: mptype ID paramdecl body; paramdecl: LP paralist RP | LP RP; paralist: param SM
// paralist | param; param: mptype idlist; body: LB bodydecls RB; bodydecls: bodydecl bodydecls |
// bodydecl; bodydecl: vardecl | stmts; stmts: assign | call | ret; assign: ID EQ expr SM; call: ID
// LP exprlist RP SM; exprlist: expr CM exprlist | expr; ret: RETURN expr SM;

// vardecl: mptype idlist SM; mptype: INTTYPE | FLOATTYPE; idlist: ID CM idlist | ID; expr: 'expr';
// INTTYPE: 'int'; FLOATTYPE: 'float'; RETURN: 'return'; EQ: '='; LP: '('; RP: ')'; LB: '{'; RB:
// '}'; SM: ';'; CM: ','; ID: [a-zA-Z]+; WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

////// 4 ////// 

// program: decls EOF;

// decls: decl decls | decl; decl: vardecl | funcdecl;

// funcdecl: mptype ID paramdecl body; paramdecl: LP paralist RP | LP RP; paralist: param SM
// paralist | param; param: mptype idlist; body: LB bodydecls RB; bodydecls: bodydecl bodydecls |
// bodydecl; bodydecl: vardecl | stmts; stmts: assign SM | call SM | ret SM; assign: ID EQ expr;
// call: ID LP exprlist RP; exprlist: expr CM exprlist | expr; ret: RETURN expr; expr: expr1 ADD
// expr | expr1; expr1: expr2 SUB expr2 | expr2; expr2: expr2 MUL expr3 | expr2 DIV expr3 | expr3;
// expr3: operands | LB expr RB; operands: ID | INTLIT | FLOATLIT | call;

// vardecl: mptype idlist SM; idlist: ID CM idlist | ID;

// mptype: INTTYPE | FLOATTYPE; INTTYPE: 'int'; FLOATTYPE: 'float'; RETURN: 'return'; EQ: '='; LP:
// '('; RP: ')'; LB: '{'; RB: '}'; SM: ';'; CM: ','; ADD: '+'; SUB: '-'; MUL: '*'; DIV: '/'; ID:
// [a-zA-Z]+; INTLIT: [1-9]+ | '0'; fragment INTPART: [1-9]+ | '0'; fragment FRACPART: '.' [0-9]+;
// FLOATLIT: INTPART FRACPART; WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

