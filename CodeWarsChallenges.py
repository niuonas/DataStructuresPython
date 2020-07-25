def SumOfMultiplesOf3And5(number):
    """Returns the sum of numbers that are lower than the input and are multiples of 3 or 5. If the number is multiple of both it will be added only one time

        Input: 
            number: An int variable that is the upper limit
        Output:
            sum: The sum of the multiples of 3 and 5 that are lower than the input number 
    """
    sum = 0
    for i in range(number):
        if i % 3 == 0.0:
            sum += i
        elif i % 5 == 0.0:
            sum += i
    return sum


def DescendingOrder(number):
    """Reareanges the digits of the number to form the biggest possible number
    
        Input:
            number: the number to be rearanged
        Output:
            rearangedNumber: the biggest number that can be formed using the digits provided   
    """

    digitList = [int(x) for x in str(number)]
    digitList.sort()
    digitList.reverse()
    return int(''.join(str(i) for i in digitList))


def SquareDigits(number):
    """Receives as input a number, squares each of its digit and returns a new number.

        Input:
            number: int containing the initial number
        Output:
            numberSquared: int containing the initial number with each of its digits squared
    """

    digitList = [int(x) for x in str(number)]

    c = []
    for i in digitList:
        c.append(int(i)**2)
    
    return int(''.join(str(i) for i in c))


def HiddenCubic(inputString):
    """Receives as input a string and extracts the hidden cubic numbers. If it dosent find any hidden cubic numbers returns a message

        Input:
            string: A string of charachters that needs to be checked to see if contains any cubic numbers
        Output:
            A list of found hidden numbers
    """

    inputString = inputString.split(' ')
    sumOfDigits = 0
    hiddenCubes = []
    startIndex = 0
    endIndex = 3

    for i in inputString:
        
        for char in i:
                if char.isdigit() == False:
                    i = i.replace(char,'')

        sumOfDigits = 0
        if len(i) <= 3:
            if i.isdigit() == True:
                for j in i:
                    sumOfDigits += int(j)**3
                if sumOfDigits == int(i):
                    hiddenCubes.append(i)
        else:    
            while(len(i) > 0):
                sumOfDigits = 0
                j = i[startIndex:endIndex]
                if j.isdigit() == True:
                    for k in j:
                        sumOfDigits += int(k)**3
                    if sumOfDigits == int(j):
                        hiddenCubes.append(j)
                i = i[3:]

    sumOfCubes = 0

    for i in hiddenCubes:
        sumOfCubes = sumOfCubes + int(i)
    outputString = ''
    if len(hiddenCubes) == 0:
        outputString = 'Unlucky'
    else:
        for i in hiddenCubes:
            outputString = outputString + i + " "
        outputString = outputString + str(sumOfCubes) + ' Lucky'

    return outputString
    

def arrayDifference(a,b):
    """Removes all values from list a which are present in list b
        Input:
            a: list to be removed from
            b: list with elements that need to be removed
        Output:
            c: list containing the elements from a that are not in b
    """               

    for i in a:
        if i in b:
            a = list(filter((i).__ne__, a))
    return a


def isPrime(a):
    """Checks if the given number is a prime number.
        Input:
            a: int that is checked if it is prime or not
        Output:
            True if is prime False otherwise"""
    if a in [0,1]:
        return False
    if a < 0:
        return False
    for i in range(2, int(a / 2) + 1):
        if a % i == 0:
            return False
    return True

def test():
    for i in range(10):
        print(i)
        if i % 2 == 0:
            return i

def split_string(string):

    count = 0
    strSplitted = ''
    strList = list(string)

    if len(string) % 2 != 0:
        string += '_'

    if len(string) == 0:
        return []
    
    for i in range(len(strList)):
        strSplitted += strList[i]
        count = count + 1
