#Create a function that recives a value, an array and a new value. If the value we are searching for is in the array sustitude that value with the new value. if the original value is more than once in the array just change it the first time. 
#This function has to return true if it modified the array and false in case everything stayed the same. 
bands = ['BTS', 'Twenty One Pilots', 'Tomorrow x Together', 'Stray Kids', 'Daft Punk', 'Queen', 'BTS', 'Genesis', 'YES', 'Coldplay']
value = 'BTS'
new_value = 'BangTan Sonyeondan'

def substitude(value, new_value, group):
    for i, band in enumerate(group):
        if band == value:
            group[i] = new_value
            return True
    return False
    
result = substitude('BTS', 'BangTan Sonyeondan', bands)
print(result)
print(bands)