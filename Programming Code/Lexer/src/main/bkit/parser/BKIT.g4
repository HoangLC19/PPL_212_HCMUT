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

options {
	language = Python3;
}

program: EOF;

///////// 1 ////////// ID: [a-z][a-z0-9]*;

//////// 2 ///////// fragment COMB: '0' | [1-9] | [1-9][0-9] | [1-9][0-9][0-9]; IP: COMB '.' COMB
// '.' COMB '.' COMB;

///// 3 //////// fragment EXP: 'e' '-'? [1-9]+; fragment INT: [0-9]+ EXP?; fragment DEC: [0-9]+
// EXP?; REAL: INT ('.' DEC)?;

// fragment INTPART: [0-9]+; fragment FRACPART: '.' [0-9]+; fragment EXPPART: 'e' '-'? [0-9]+; REAL:
// INTPART (FRACPART EXPPART? | EXPPART);

////// 4 /////// fragment SQ: '\''; fragment DQ: '\'\''; STRING: '\'' (DQ | ~['])* '\'';

// fragment DIGITS: [1-9] | '0';

// PHP: '0' | DIGITS ('_'? DIGITS+)*;

DECIMAL:
	'0'
	| [1-9] [0-9]* ('_' [0-9]+)* {
	self.text = self.text.replace("_", "")
};

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;