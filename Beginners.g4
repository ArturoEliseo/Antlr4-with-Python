grammar Beginners;

// Main Rules
programa    : 'inicio:' bloque;
bloque      : instruccion+;
instruccion : mostrar | asignar | si | darvueltas | hacerFuncion | mientras;

// Mostrar texto
mostrar : 'escribe' '(' contenido ')' ';';

// Contenido flexible que combina texto y expresiones
contenido   : elemento (OPERADOR elemento)*;
elemento    : texto | expresion;

// Operadoras de concatenación
OPERADOR    : '+'; // Add more operators if needed

// Asignación de variables
asignar     : tipo ID '=' expresion ';';
tipo        : 'numero' | 'decimal' | 'palabra' | 'si_no';

// Condicionales
si          : 'si' '(' condicion ')' '{' bloque '}' ('sino' '{' bloque '}')?;

// Ciclos
darvueltas  : 'repite' '(' expresion ')' '{' bloque '}';
mientras : 'mientras' '(' condicion ')' '{' bloque '}';

// Funciones
hacerFuncion: 'funcion' ID '(' parametros? ')' '{' bloque '}';
parametros  : ID (',' ID)*;

// Expresiones
expresion   : termino (('+'|'-') termino)*;
termino     : factor (('*'|'/') factor)*;
factor      : '(' expresion ')' | NUMERO | ID | DECIMAL;
condicion   : expresion ('=='|'!='|'<'|'>'|'<='|'>=') expresion;

// Terminales
NUMERO      : [0-9]+;                  // Match digits
DECIMAL     : [0-9]+ '.' [0-9]+;
ID          : [a-zA-Z_][a-zA-Z_0-9]*;  // Valid identifiers

// Definir la regla 'texto' para que coincida con el texto citado 
texto       : ('"' ~'"'* '"') | ('\'' ~'\''* '\'');

// Ignorar espacios y comentarios
WS          : [ \t\r\n]+ -> skip;
COMENTARIO  : '#' ~[\r\n]* -> skip;
