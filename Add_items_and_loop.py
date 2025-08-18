#Add 10 random integers to the arr list and print the array on the console.

import random
arr = [4,5,734,43,45];
for i in range(10):
    arr.append(random.randint(0,99))
print(arr)