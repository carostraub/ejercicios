#Ver en la terminal como reacciona una función básica con distintos valores, strings, números decimales, números enteros
def suma(x,y):
    return x+y

""" >>> suma(1,2)
3
>>> suma(2.5,6.3)
8.8
>>> suma("Hola","papa")
'Holapapa'
>>> suma("hola", 4)
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    suma("hola", 4)
    ~~~~^^^^^^^^^^^
  File "<python-input-0>", line 2, in suma
    return x+y
           ~^~
TypeError: can only concatenate str (not "int") to str
>>> suma(4, "holi")
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    suma(4, "holi")
    ~~~~^^^^^^^^^^^
  File "<python-input-0>", line 2, in suma
    return x+y
           ~^~
TypeError: unsupported operand type(s) for +: 'int' and 'str' 
>>> suma(1,3.2)
4.2
>>> suma(1,"3")
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    suma(1,"3")
    ~~~~^^^^^^^
  File "<python-input-0>", line 2, in suma
    return x+y
           ~^~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> suma(1,int("3"))
4
>>> int(3.2)
3
>>> int(3.99)
3
>>> int(-3.99)
-3
>>> round(3.99)
4
"""