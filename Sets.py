#   Unordered collection of unique elements
#   Sets are mutable
#   Elements in a set are immutable

if __name__ == "__main__":
    setTest = {6,26,422,5839}
    print(setTest)

    #   Using the set constructor to create an empty set
    emptySet = set()
    print(emptySet)

    #   Set constructor can construct a set from any iterable object
    randomList = [12,12,123,54,12,7]
    print(randomList)
    setTest = set(randomList) #    the constructed set will remove any duplicates
    print(setTest)

    # Set iteration: the order in which elements appear are random
    for i in {2,34,52434,1}:
        print(i)

    #   Membership test
    q = {12,343,12566,7,8}
    print(q)
    print(12 in q)
    print(1 not in q)

    #   Adding elements to a set
    print(q)
    q.add(99)
    print(q)
    #adding multiple elements at once can be done using .update() method
    q.update([2133,5,6])
    print(q)

    #   Removing elements from a set
    q.remove(12)
    q.discard(5)
    #trying to remove an element that dosent exist in a set will throw an error
    print(q)

    # Copying a set: performs a shallow copy, copying the reference not the object
    copiedSet = q.copy()
    print(copiedSet)

    #
    #   SET ALGEBRA
    #   

def setAlgebraOperations():
    blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
    blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
    smell_hcn = {'Harry','Amelia'}
    taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
    o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
    a_blood = {'Harry'}

    #   UNION operation: returns the elements contained in both sets and removes all duplicates
    print(blue_eyes.union(blond_hair))

    #   INTERSECTION operation: returns the common elements from both sets
    print(blue_eyes.intersection(blond_hair))

    #   DIFFERENCE operation: finds all elements that are present in the first set and not in the second set
    print(blond_hair.difference(blue_eyes))

    #   SYMMETRIC DIFFERENCE operation: returns the elements that are in the first set and not in the second set 
    #                                   and all elements that are in the second set and not in the first set
    print(blond_hair.symmetric_difference(blue_eyes))

    #   ISSUBSET: returns true if the first set is a subset of the second set. False otherwise
    print(smell_hcn.issubset(blond_hair))

    # ISSUPERSET: returns true if the first set contains all elements from the second set. False otherwise
    print(taste_ptc.issuperset(smell_hcn))

    # ISDISJOINT: tests if two sets have no members in common. True if they have no members in common. False otherwise
    print(a_blood.isdisjoint(o_blood))

