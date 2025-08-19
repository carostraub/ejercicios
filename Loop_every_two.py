#Change the loop, so it loops two by two instead of one by one.
mySampleArray = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]
for i in range(0, len(mySampleArray), 2):
    print(mySampleArray[i], end=" ")