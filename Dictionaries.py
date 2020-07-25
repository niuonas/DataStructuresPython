#dict constructor: dict()
#dict keys need to be unmutable objects
#dict keys must be unique
#dict values dont have to be unique
#dict values can be mutable
#items in dict are not stored in a particular order
#dictionary copying is shallow (copying only the reference to the object not the object itself)


if __name__ == "__main__":
    names_and_ages = [('Alice',32),('Bob',48)]

    #examples of using the dict constructor
    d = dict(names_and_ages)  
    print(d)
    phonetic = dict(a = 'alfa', b = 'omega')
    print(phonetic)

    #examples of copying dictionaries
    d = dict(goldenrod = 0xDAA520, indigo = 0x4B0082, seashell = 0xFFF5EE)
    print(d)
    e = d.copy()
    print(e)
    f = dict(e)
    print(f)

    #   to add entries from one dictionary to another or to modify the existing entrie use dict.update()
    g = dict(wheat = 0xF5DEB3)
    print(f)
    f.update(g) #   dict.update() method is called on the dict we want to add elements and as argument is passed the dict that is to be added
    print(f)
    #   modyfing existing entries in a dicitionary
    stocks = {'GOOG':891, 'APPL':416, 'IBM': 25}
    print(stocks)
    stocks.update({'GOOG':894,'YHOO':25})
    print(stocks)

    #
    #   ITERATING THROUGH A DICTIONARY
    #

    colors = dict(aquamarine='#7FFFD4', burlywood='#DEB887',charturese = '#7FFF00')

    for key in colors:
        print(f"{key} => {colors[key]}")
        #REMAINDER: the keys are returned in an ARBITRARY order. Not in the order they were inputed
    
    #   If we want to iterate through the values of a dictionary:
    for values in colors:
        print(values)

    #   dict.items() allows us to iterate over keys and values in tandem
    #       on each iteration yields a (key, value) tuple
    for i in colors.items():
        print(i)

    #
    #   MEMBERSHIP TESTS
    #       are made with IN and NOT IN operators

    symbols = dict(usd='$', gbp='pound', nzd='$', krw='korean')
    print('usd' in symbols)
    print('lei' in symbols)
    print('gbp' not in symbols)

    #
    #   DELETING ELEMENTS FROM A DICTIONARY
    #       using del

    print(symbols)
    del symbols['usd']
    print(symbols)

    #   only the keys are immutable, the dictionary itself and the values are mutable
    #   Example on how to modify values and add values in a dictionary:

    print(symbols)
    symbols['gbp'] += '*****'
    symbols['lei'] = '12313'
    print(symbols)

    #
    #   Pretty print
    #       to print a dictionary in a more readeable form

    from pprint import pprint as pp 
    pp(symbols)