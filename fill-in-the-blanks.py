def main():
    #main function to run the game
    game = True
    while game:
        wrongGuessNum = raw_input("Select maximum wrong guesses: ")
        while not wrongGuessNum.isdigit() or int(wrongGuessNum) <= 0:
            wrongGuessNum = raw_input("Invalid input, select maximum wrong guesses: ")
        print "You have up to " + wrongGuessNum + " chances for each blank"
        wrongGuessNum = int(wrongGuessNum)
        level = raw_input("Please select difficulty level (easy/medium/hard): ")
        while level != "easy" and level != "medium" and level != "hard":
            level = raw_input("Invalid input, select difficulty level (easy/medium/hard): ")
        if level == "easy":
            lvl = 0
        elif level == "med":
            lvl = 1
        else:
            lvl = 2
        print level + " mode is selected, see the paragraph below"
        selPara = paraGenerator(lvl)
        print selPara
        curBlank = 1
        wrongGuess = 0
        maxBlank = 5
        while wrongGuess < wrongGuessNum:
            guess = raw_input("Word in the ___"+str(curBlank)+"___ blank: ")
            if guess == missingWords(lvl, curBlank-1):
                print "Correct!"
                selPara = fillPara(selPara, guess, curBlank)
                print selPara
                curBlank += 1
                wrongGuess = 0
            else:
                wrongGuess += 1
                print "Try again, "+str(wrongGuessNum-wrongGuess)+" chances left"
                print selPara
            if curBlank == maxBlank:
                print "All blanks correctly filled, good job"
                game = False
                break
        if curBlank != maxBlank:
            print "Maximum wrong guesses reached, game over"
            game = False

def paraGenerator(diffLvl):
    #a list contains a paragraph for each difficulty level
    paragraphs = [
        "Voldemort himself created his ___1___ enemy, just as ___2___ everywhere do!  Have you any idea how much ___2___ fear the people they oppress? All of them realize that, one day, amongst their many ___3___, there is sure to be one who rises against them and ___4___ back!",
        "There are many Beths in the world, shy and ___1___, sitting in corners till needed, and living for others so ___2___ that no one sees the ___3___ till the little cricket on the hearth stops ___4___, and the sweet, sunshiny presence vanishes, leaving silence and shadow behind.",
        "The rules of the Hunger Games are simple. In ___1___ for the uprising, each of the twelve districts must provide one girl and one boy, called ___2___, to participate. The twenty-four ___2___ will be imprisoned in a vast outdoor arena that could hold anything from a burning desert to a frozen wasteland. Over a period of several ___3___ the competitors must fight to the ___4___. The last ___2___ standing wins."
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

main()
