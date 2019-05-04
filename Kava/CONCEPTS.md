Concepts
=========


Parser
------

This module handles lexing and parsing source files into an abstract syntax tree based on grammar files. Each grammar file defines terminal symbols as well as variable nodes that we expect to see. For each terminal token we define its name as well as the regular expression we will match against. For variable nodes we have two types: grammar which is represented as a list of terminal symbols as well as syntax which is represented as a pattern of grammar nodes. 

Grammar files should be of the form:
```
# Comment
@terminal : 'regexp';
_grammar :  terminal1[?*+] [ , ... ];
syntax : grammar1 [?*+] [ , ... ];
```
Where ?*+ are Kleene operators:
    * '?' : matches 0 or 1 instances
    * '*' : matches 0 or more instances
    * '+' : matches 1 or more instances

It should be noted that syntax nodes can match patterns of grammar or syntaxes. To match the empty token use `epsilon` and the pattern matching will start with `global`. In addition if you would like a terminal to be ignored during iteration of tokens end the terminal in '!'. To ignore all whitespace simply write `@whitespace! : '\s+';`. For terminals to be ignored in AST generation end the terminal in '?'. To ignore parentheses in the ast simply write `@lpar?: '('; @rpar?: ')'`. These types
of tokens will still be used to generate the ast but their nodes will not appear. This allows for scoping without unneccessary nodes to appear.



