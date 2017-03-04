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
        level = raw_input("Select difficulty level (easy/med/hard): ")
        while level != "easy" and level != "med" and level != "hard":
            level = raw_input("Invalid input, select difficulty level (easy/med/hard): ")
        if level == "easy":
            lvl = 0
        elif level == "med":
            lvl = 1
        else:
            lvl = 2
        selPara = paraGenerator(lvl)
        print selPara
        curBlank = 1
        wrongGuess = 0
        maxBlank = 5
        while wrongGuess < wrongGuessNum:
            guess = raw_input("Word in the ___"+str(curBlank)+"___ blank: ")
            if guess == missingWords(lvl, curBlank):
                print "Correct!"
                selPara = fillPara(selPara, guess, curBlank)
                curBlank += 1
            else:
                print "Try again"
                wrontGuess += 1
            if curBlank == maxBlank:
                print "All blanks correctly filled, good job"
                game = False
                break
        print "Maximum wrong guesses reached, game over"
        game = False

def paraGenerator(diffLvl):
    #a list contains a paragraph for each difficulty level
    paragraphs = [
        "Voldemort himself created his ___1___ enemy, just as ___2___ everywhere do! \
        Have you any idea how much ___2___ fear the people they oppress? All of them \
        realize that, one day, amongst their many ___3___, there is sure to be one who \
        rises against them and ___4___ back!",
        "There are many Beths in the world, shy and ___1___, sitting in corners till needed, \
        and living for others so ___2___ that no one sees the ___3___ till the little \
        cricket on the hearth stops ___4___, and the sweet, sunshiny presence vanishes, \
        leaving silence and shadow behind.",
        "The rules of the Hunger Games are simple. In ___1___ for the uprising, \
        each of the twelve districts must provide one girl and one boy, called ___2___, \
        to participate. The twenty-four ___2___ will be imprisoned in a vast outdoor \
        arena that could hold anything from a burning desert to a frozen wasteland. \
        Over a period of several ___3___ the competitors must fight to the ___4___. \
        The last ___2___ standing wins."
    ]
    return paragraphs[diffLvl]
def missingWords(diffLvl, blankNum):
    #a list of lists contains the missing words
    missingWords = [
        ["worst", "tyrants", "victims", "strikes"],
        ["quiet", "cheerfully", "sacrifices", "chirping"],
        ["punishment", "tributes", "weeks", "death"]
    ]
    return missingWords[diffLvl][blankNum]
def fillPara(paragraph, guess, blankNum):
    #return the filled paragraph
    wordList = []
    wordList = paragraph.split()
    for word in wordList:
        if word.find(str(blankNum)) != -1:
            pos = wordList.index(word)
            word = word.replace("___"+str(blankNum)+"___", guess)
            wordList[pos] = word
    return " ".join(wordList)

a = "Voldemort himself created his ___1___ enemy, just as ___2___ everywhere do! \
Have you any idea how much ___2___ fear the people they oppress? All of them \
realize that, one day, amongst their many ___3___, there is sure to be one who \
rises against them and ___4___ back!"
b = "x"
c = 1
print fillPara(a,b,c)
