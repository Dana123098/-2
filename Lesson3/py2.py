Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mashin=["bmv","mz","ac"]
>>> print(mashin)
['bmv', 'mz', 'ac']
>>> message = f "(jkg g ffff {mashin[1].title()})"
SyntaxError: invalid syntax
>>> message = f"(jkg g ffff {mashin[1].title()})"
>>> print(message)
(jkg g ffff Mz)
>>> 