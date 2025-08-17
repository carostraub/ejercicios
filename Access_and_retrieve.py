myArray = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
# 1. print the 3rd item here
print(myArray[2])
#2. change the 'thursday' value to null here
#myArray[4] = None
#3. print the position of step 2
#print(myArray[4])
#La primera vez que diga 'thursday' cambiarlo por None con una iteración
def change_thursday(myArr):
    for i, day in enumerate(myArr):
        if day == 'thursday':
            myArr[i] = None
    

change_thursday(myArray)

print(myArray)
