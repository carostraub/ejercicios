#crear una funcion que reciba un número natural y devuelve true ssi el número es primo
def is_prime(num):
    if num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

print(is_prime(100000))
print(is_prime(10000019))
