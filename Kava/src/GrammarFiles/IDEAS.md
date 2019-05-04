Kavascript
===========

Kavascript is a language that lets you do everything. Compiled yet has the versatility of python; kavascript is the perfect tool for everything.




Terminals
----------

String : `"this is a string literal"` Will result in string with an internal char array with these exact characters. Can contain escaped characters.
Format : `\`x * 4+2\`` Equivalent to eval() but results in a string. Evaluates an expression and returns the result as a string. Can contain escaped characters.
Script : `"""
    This is a script
"""`    Exactly equivalent to a string, however whitespace at the beginning of each line is truncated to the smallest indentation (or none if you start on the same line as """). Cannot contain escaped characters. All newlines and tabs will be stored as internal escaped chars.

Char : `'c'` Results in a single char. Can be an escaped character.

Integer : Any normal decimal number. Underscores are allowed between any two digits. Can be prefixed with `0b`, `0o`, or `0x` to treated as binary, octal or hexadecimal literals.
Float : Any normal floating point number. Scientific notation coerces to a float.
Complex : Anynumber followed by `i` or `j` or `k` will be converted to a complex number. Combining these three into a single number will result in a quaternion.

Expressions
------------

Collections
------------

Statements
-----------




Functionality
-------------

Function :
```
functype FunctionName( args ) {

}
```
functype can be any of `{ def, func, oper, prefix, postfix }`


Structures
-----------

Classes : 
```
class ClassName(ParentClass) {
    def init(self) {

    }
    ...
}
```

Enum :
```
enum EnumName(ParentEnum) {
    ident(args), ident2(args), ident3(args);

    def init(self) {

    }
}
```

Struct :
```
struct StructName {
    type member1;
    type member2;
    ...
}
```
