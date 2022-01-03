Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nombre=roberto
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    nombre=roberto
NameError: name 'roberto' is not defined
>>> nombre="roberto"
>>> nombre.count(o)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    nombre.count(o)
NameError: name 'o' is not defined
>>> nombre.count("o")
2
>>> nombre.find("j")
-1
>>> nombre.find("r")
0
>>> nombre.find("j")
-1
>>> nombre.find("b")
2
>>> nombre.rfind("o")
6
>>> nombre.upper()
'ROBERTO'
>>>  nombre.capitalize()
 
SyntaxError: unexpected indent
>>>  nombre.capitalize()
 
SyntaxError: unexpected indent
>>>  nombre.title()
 
SyntaxError: unexpected indent
>>> nombre="maria victoria"
>>>  nombre.capitalize()
 
SyntaxError: unexpected indent
>>> nombre.title()
'Maria Victoria'
>>> nombre_completo.capitalize()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    nombre_completo.capitalize()
NameError: name 'nombre_completo' is not defined
>>> nombre_completo.capitalize()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    nombre_completo.capitalize()
NameError: name 'nombre_completo' is not defined
>>> nombre.lower()
'maria victoria'
>>> frase="los zapatitos me dan calor"
>>> frase.split()
['los', 'zapatitos', 'me', 'dan', 'calor']
>>> var="jose;perez;099999999999"
>>> var.split(".")
['jose;perez;099999999999']
>>> metodo.join()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    metodo.join()
NameError: name 'metodo' is not defined
>>> var.join()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    var.join()
TypeError: str.join() takes exactly one argument (0 given)
>>> var=frase.spli()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    var=frase.spli()
AttributeError: 'str' object has no attribute 'spli'
>>> var=frase.split()
>>> class
SyntaxError: invalid syntax
>>> type
<class 'type'>
>>> var
['los', 'zapatitos', 'me', 'dan', 'calor']
>>> ".".join(var)
'los.zapatitos.me.dan.calor'
>>> " ".join(var)
'los zapatitos me dan calor'
>>> var.isnumeric()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    var.isnumeric()
AttributeError: 'list' object has no attribute 'isnumeric'
>>> var="123"
>>> var.isnumeric()
True
>>> var.isdigit()
True
>>> var.isdecimal()
True
>>> 