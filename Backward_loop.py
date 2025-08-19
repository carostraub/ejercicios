#Without using the reverse() method, please reverse loop (from the end to the beginning) the whole array and print all the items on the console as you go.
#Then do it with while and compare both methods.
mySampleArray = ['Esmeralda', 'Kiko', 'Ruth', 'Lebron', 'Pedro', 'Maria', 'Lou', 'Fernando', 'Cesco', 'Bart', 'Annie'];
""" for i in range(len(mySampleArray)-1, -1, -1):
    print(mySampleArray[i], end=" ") """
index = len(mySampleArray) -1
while index >= 0:
    print(mySampleArray[index])
    index -= 1

"""Tiene más sentido usar reversed() o reverse() y si es solo while o for prefiero for que while"""