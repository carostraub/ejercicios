def str_to_int(digitos):
    valor=0
    for digito in digitos:
        valor=valor*10+ int(digito)
    return valor

print(str_to_int("283"))

x= str_to_int((1,2,3))
print(x)
