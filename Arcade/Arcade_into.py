# Intro 

# The Journey Begins

# Add challange 
def add(param1, param2):
    return param1 + param2
print(add(1,2))

# centuryFromYear challange
def centuryFromYear(year):
    year = year/100
    if year == int(year):
        return year
    else:
        return int(year)+1
            
print(centuryFromYear(1905))


# palindrome challange 
def checkPalindrome(inputString):
    if inputString[::-1] == inputString:
        return True
    else:
        return False

# Edge of the Ocean

# adjacentElementsProduct challange 
def adjacentElementsProduct(inputArray):
	store_result = []
	length = len(inputArray)
	length_after = length-1
	for i in range(length_after):
		store_result.append(inputArray[i]*inputArray[length-len(inputArray[i:length_after])])
	return max(store_result)

adjacentElementsProduct([3, 6, -2, -5, 7, 3])

# shapeArea 

def shapeArea(n):
    return (n-1)**2+n**2

print(shapeArea(5)) # print(shapeArea('print any number you wanted'))
