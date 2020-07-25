import datetime
import math

#When concatenating strings is preferable to use str.join()
#str.join() inserts a separator between a collection of strings


if __name__ == '__main__':
    colors = ';'.join(['red','green','blue'])
    print(colors)
    combine = "".join(['new','found','land'])
    print(combine)


    a = 'partition'
    b = a.partition("tit") #what partition does it split a string in 3 parts inside a tuple. The part before the separator. The separator. The part after the separator
    print(b)

    #example use of tuple unpacking + .partition method
    destination = ('Germany:London')
    a,_,b = destination.partition(":")
    # : is saved in _ and it dosent throw an error showing that the variable is not used
    print(a)
    print(b)

    #f strings - allow embbeding of expressions inside literal strings
    value = 40
    print(f'The value is {value}')
    print(f'The current time is {datetime.datetime.now().isoformat()}.')
    print(f'Math constants: pi = {math.pi:.3f}, e = {math.e:.3f}') # :.3f specifies the precision in decimals of the represented number




