from urllib.request import urlopen
import sys
import random
"""
Contains a bunch of functions and exercises from the Pluralsight tutorial

Usage:
    python words.py

    or 

    from the repl: import words
"""

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def  print_words(item):
    for word in item:
        print(word)

def main():
    words = fetch_words()
    print(words)

if __name__ == '__main__':
    main()

def random_color(i):
    switcher = {
        0:'red',
        1:'green',
        2:'magenta',
        3:'brown',
    }
    return switcher.get(i,"Invalid color")

def start_game(newGame = "Yes",delimiter = '-'):

    """Selects a random color and ask for user input until it guesses right!

        Args:
            newGame: A boolean value that determines if a new game should be played or not.
        Returns:
            Nothing
    """

    if newGame in ['yes','YES','Y','y','Yes']:
        print('I am thinking at a random color.Can you guess it?')
        seed = random.randrange(0,4,1)
        randomColor = random_color(seed)

        colorGuess = input('Your guess is:\n')
        tryAgain = True

        while tryAgain:
            if check_right(colorGuess,randomColor) == True:
                print('You got it! The color I was thinking of was: ' + randomColor)
                newGame = input('Want to play again?\n')
                print(16 * delimiter)                                                   #if you multiply an int with a string that string will be printed int times 
                start_game(newGame)
                tryAgain = False
            else:
                print('Try again!')
                colorGuess = input('Your guess is:\n')
    else:
        print('Thanks for playing!')

def check_right(choice,randomColor):
    """Checks if the color inputed by the user is the same as the randomColor selected

        Args:
            choice: A string value represeting the user inputed color
            randomColor: A string value that represents the randomly selected color
        Reuturns:
            True: if colors match
            False: if color do not match
    """
    if choice == randomColor:
        return True
    else:
        return False

def random_test():
    i = 0
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0

    while i <= 100:
        x = random.randrange(0,4,2)
        print(i) 
        if x == 0:
            count0 += 1
        elif x == 1:
            count1 += 1
        elif x == 2:
            count2 += 1
        else:
            count3 += 1
        i += 1

    print(str(count0) + '\n' + str(count1) +'\n' + str(count2) +'\n'+ str(count3) +'\n')

def build_pyramid(levels = 8,material = '*'):
    """Prints a pyramid with the number of levels defined by the input input argument

       INPUT:   
                levels(int): the number of levels the pyramid will have
                material(char): the char the pyramid will be build from
        OUTPUT:
                printed pyramid   
    """
    currentLength = 1
    while levels != 0:
        print(" " * (levels - 1) + material * (currentLength - 1) + material * currentLength)
        currentLength += 1
        levels -= 1
    

#num = sys.argv[1]
#for i in range(int(num)):
#    print(i)
