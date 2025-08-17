import random
""" Create a variable named theLastOne, and assign to it the LAST element of myStupidArray.

Then, print it on the console. """
def generate_random_array():
    aux_Array = []
    random_length = random.randint(0, 99)
    for i in range(random_length):
        aux_Array.append(random.randint(0, 99))
    return aux_Array

my_stupid_array = generate_random_array()

the_last_one = my_stupid_array[-1]
print(the_last_one)