# a global dictionary of dictionaries containing a paragraph and a list of answers
# for the missing blanks for each difficulty level, input argument will determine
# which paragrah and the corresponding answers
game_data = {
    'easy': {
        'paragrah': "Voldemort himself created his ___1___ enemy, just as ___2___ "\
        "everywhere do! Have you any idea how much ___2___ fear the people they oppress? "\
        "All of them realize that, one day, amongst their many ___3___, there is sure "\
        "to be one who rises against them and ___4___ back!",
        'answers': ["worst", "tyrants", "victims", "strikes"]
    },
    'medium': {
        'paragrah': "There are many Beths in the world, shy and ___1___, sitting "\
        "in corners till needed, and living for others so ___2___ that no one sees "\
        "the ___3___ till the little cricket on the hearth stops ___4___, and the "\
        "sweet, sunshiny presence vanishes, leaving silence and shadow behind.",
        'answers': ["quiet", "cheerfully", "sacrifices", "chirping"]
    },
    'hard': {
        'paragrah': "The rules of the Hunger Games are simple. In ___1___ for the "\
        "uprising, each of the twelve districts must provide one girl and one boy, "\
        "called ___2___, to participate. The twenty-four ___2___ will be imprisoned "\
        "in a vast outdoor arena that could hold anything from a burning desert to "\
        "a frozen wasteland. Over a period of several ___3___ the competitors must "\
        "fight to the ___4___. The last ___2___ standing wins.",
        'answers': ["punishment", "tributes", "weeks", "death"]
    }
}

def main():
    # main function to run the game, check user input and determine game result
    max_wrong_guess = wrong_guess_input()
    level = level_input()
    run_game(max_wrong_guess, level)

def run_game(max_wrong_guess, level):
    # compare user input with the corresponding result from game_data, if user input
    # does not match, a wrong guess counter will increase, elsewise the program will
    # move to the next blank and reset the wrong guess counter back to zero. The game
    # will stop either when the wrong guess reaches maximum defined by the user or
    # the user correctly fills all the blanks.
    game = True
    cur_blank = 1
    wrong_guess = 0
    max_blank = 5
    sel_para = game_data[level]['paragrah']
    print sel_para
    while wrong_guess < max_wrong_guess and cur_blank < max_blank:
        guess = raw_input("Word in the ___"+str(cur_blank)+"___ blank: ")
        if guess == game_data[level]['answers'][cur_blank-1]:
            print "Correct!"
            sel_para = fill_blank(sel_para, guess, cur_blank)
            print sel_para
            cur_blank += 1
            wrong_guess = 0
        else:
            wrong_guess += 1
            print "Try again, "+str(max_wrong_guess-wrong_guess)+" chances left"
            print sel_para
    if cur_blank == max_blank:
        print "All blanks correctly filled, good job"
    else:
        print "Maximum wrong guesses reached, game over"

def wrong_guess_input():
    # check the user input on the maximum wrong guess, a valid input is a
    # positive number, the function will return the valid maximum wrong guess
    # as an interger
    max_wrong_guess = raw_input("Select maximum wrong guesses: ")
    while not max_wrong_guess.isdigit() or int(max_wrong_guess) <= 0:
        max_wrong_guess = raw_input("Invalid input, select maximum wrong guesses: ")
    print "You have up to " + max_wrong_guess + " chances for each blank"
    return int(max_wrong_guess)

def level_input():
    # check the user inut on the game difficulty, a valid input is one of the
    # three key word "esay", "medium" and "hard", the function will return the
    # the valid difficulty selection as a string
    level = raw_input("Please select difficulty level (easy/medium/hard): ")
    while level != "easy" and level != "medium" and level != "hard":
        level = raw_input("Invalid input, select difficulty level (easy/medium/hard): ")
    print level + " mode is selected, see the paragraph below"
    return level

def fill_blank(paragraph, guess, blank_num):
    # fill the blank defined from input argument blank_num with the input argument
    # guess, and return the filled paragraph as defined by the input argument
    word_list = []
    word_list = paragraph.split()
    for word in word_list:
        if word.find(str(blank_num)) != -1:
            pos = word_list.index(word)
            word = word.replace("___"+str(blank_num)+"___", guess)
            word_list[pos] = word
    return " ".join(word_list)

main()
