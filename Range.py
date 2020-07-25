#Sequence representing an arithmetic progression of integers

#Range determines what arguments mean by counting them
#   range(stop) - only one element
#   range(start,stop) - two elements
#   range(start,stop,step) - three elements

range(5) #the value provided as argument is the end of the range but is not included

range(1,5) #you can also give as argument a starting value. The starting value is included

range(1,5,2) #you can also provide a step with which to increment

#example using enumerate:
if __name__ == '__main__':
    t = [6,45,32,12]
    for p in enumerate(t): #generates a tuple for each element in the list (index,element)
        print(p)

    #you can use tuple unpacking to access the element + index in the list like this:

    for p in enumerate(t):
        print(f'')
