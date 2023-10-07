"""
● Keywords are also called as Reserved Words.
● All the keywords can be in Lower Case or upper Case.
● We cannot use a keyword as a variable name, function name or any
other identifier.
● They are used to define the syntax and structure of the Python
language. In Python, keywords are case-sensitive.
"""

import  keyword
print(keyword.kwlist)

"""
Commonly used - keywords

['False', 'None', 'True', 'and', 'as', 
'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

"""
Identifieres - Names given to variables, function, class, module or other objects.

● They start with a letter (A-Z or a-z) or an underscore (_) followed by
zero or more letters, underscores, and digits (0-9).
● Python is case-sensitive, so myVariable and myvariable are two
different identifiers.
Rules for writing identifiers:
TheTestingAcademy

Identifiers can be a combination of letters in lowercase (a to z) or
uppercase (A to Z) or digits (0 to 9) or an underscore (_).
● An identifier cannot start with a digit.
● Keywords cannot be used as identifiers.
● We cannot use special symbols like !, @, #, $, %, etc. in our identifier.
● An identifier can be of any length.
Examples of valid identifiers: myVar, var1, _var, _1_var
Examples of invalid identifiers: 1var, my-var, my@, my var, break
(break is a keyword)
"""

