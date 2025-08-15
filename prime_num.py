#crear una funcion que reciba un número natural y devuelve true ssi el número es primo
def is_prime(num):
    if num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True




def prime_list(num):
    for n in range(1, num+1):
        if is_prime(n):
            print(n)
        


prime_list(5)

        
