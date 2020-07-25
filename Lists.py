#Are defined like this [1,2,3]
#Lists can store duplicate values
#Lists can contain different types of elements
#Lists are ordered, each element has a fixed position in the list
#Lists are iterable, you can get their elements one by one

#Negative indices
if __name__ == '__main__':
    a = [1,2,3,'mere']
    print(a[-1])  #prints the last element of the list
    print(a[-2])  #prints the second to last element from the list

    print('--------------------------------')

    #String slicing: a_list[start:stop]  will return all elements from the start index until the stop - 1 index
    a = [123,4223,9382,234,982]
    print(a[1:3])
    #Using slicing you can select all the elements excluding the first and the last like this:
    print(a[1:-1])
    #Both start and stop indexes are optional
    print(a[2:]) #prints all elements from the list starting from index 2
    print(a[:2]) #prints all elements from the list starting from index 0 to 1
    print(a[:])  #prints all elements from the list

    print('--------------------------------')

    #Lists support repetition like this:
    print([0] * 3) #will create a list containing the element 0 three times

    print('--------------------------------')

    # .index() returns the index of the element in the list. If it dosent find it return an error
    a = [12,34,354]
    print(a.index(12))

    print('--------------------------------')

    # in and not in methods return a boolean value based on if it finds the element in the list or not
    print(12 in a)
    print(12 not in a)

    print('--------------------------------')

    # del deletes and element from the list by index
    print(a)
    del a[2]
    print(a)

    print('--------------------------------')

    # to add new items to the list use .insert(index, newItem) method.
    print(a)
    a.insert(2, 'something')
    print(a)

    # list reverse
    a = [1,2,3]
    print(a.reverse())

    # list sort
    a = [1,4,23,2,100,3]
    a.sort()
    print(a)

    # to sort a list you can pass a callable object and will sort the list based on that
    a = "Something strange is happening in the world".split()
    a.sort(key=len) #will sort the content of the list based on the length of each element
    print(a)

    #reversing and sorting into copies
    x = [3,4,1,2]
    y = sorted(x) # sorted() returns a sorted copy of x
    q = reversed(x) # reversed() return a reverseiterator object
    list(q) # to use the reversediterator object you need to apply the list constructor on that object
    

    