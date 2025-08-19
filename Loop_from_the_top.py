#Try looping from the end to the beginning.
mySampleArray = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12];
backwards_array= list(reversed(mySampleArray))
#print(backwards_array)
for i in range(len(mySampleArray)-1, -1, -1):
    print(mySampleArray[i], end=" ")
 