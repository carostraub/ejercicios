""" Ejercicio 1 - Suma de números pares en un Rango:
Escribe una función llamada sumar_pares_en_rango que
reciba dos números enteros, inicio y fin, y devuelva 
la suma de todos los números pares dentro de ese rango 
(inclusive inicio y fin).

Ejemplo:
    Entrada: inicio = 1, fin = 10
    Salida esperada: 30 (2 + 4 + 6 + 8 + 10)

    Entrada: inicio = 3, fin = 7
    Salida esperada: 10 (4 + 6) """

def sumar_pares_en_rango(min, max):
    sum=0
    for num in range(min, max +1):
        if num %2==0:
            sum = sum +num
        return sum
