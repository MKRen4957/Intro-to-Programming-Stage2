# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

def main:
    #main function to run the game
    game = True
    while game:
        wrongGuessNum = raw_input("Select maximum wrong guesses: ")
        while wrongGuessNum <= 0:
            wrongGuessNum = raw_input("Invalid input, select maximum wrong guesses: ")
        minLevel = 1
        maxLevel = 3
        level = raw_input("Select difficulty level (1 - 3): ")
        while level < minLevel and level > maxLevel:
            level = raw_input("Invalid input, select difficulty level (1 - 3): ")
        print paraGenerator(level)
        curBlank = 1
        wrongGuess = 0
        maxBlank = 4
        while wrongGuess < wrongGuessNum:
            guess = raw_input("Word in the "+str(curBlank)+" blank: ")
            if guess == missedWords(level, curBlank):
                print "Correct!"
                curBlank += 1
            else:
                wrontGuess += 1
            if curBlank == maxBlank:
                print "All blanks correctly filled, good job"
                game = False
                break
        print "Maximum wrong guesses reached, game over"
        game = False

def paraGenerator(index):
    paragraphs = [
        "Voldemort himself created his ---1--- enemy, just as ---2--- everywhere do! \
        Have you any idea how much ---2--- fear the people they oppress? All of them \
        realize that, one day, amongst their many ---3---, there is sure to be one who \
        rises against them and ---4--- back!",
        "There are many Beths in the world, shy and ---1---, sitting in corners till needed, \
        and living for others so ---2--- that no one sees the ---3--- till the little \
        cricket on the hearth stops ---4---, and the sweet, sunshiny presence vanishes, \
        leaving silence and shadow behind.",
        "The rules of the Hunger Games are simple. In ---1--- for the uprising, \
        each of the twelve districts must provide one girl and one boy, called ---2---, \
        to participate. The twenty-four ---2--- will be imprisoned in a vast outdoor \
        arena that could hold anything from a burning desert to a frozen wasteland. \
        Over a period of several ---3---, the competitors must fight to the ---4---. \
        The last ---2--- standing wins."
    ]
    return paragraphs[index]
def missedWords(index1, index2):
    missingWords = [
        ["worst", "tyrants", "victims", "strikes"],
        ["quiet", "cheerfully", "sacrifices", "chirping"],
        ["punishment", "tributes", "weeks", "death"]
    ]
    return missingWords[index1][index2]
