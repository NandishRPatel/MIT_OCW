import random
import string
import re

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    secret_word_list = []
    letters_guessed_list = []
    secret_word_list.extend(secret_word)
    secret_word_list = list(set(secret_word_list))
    
    for i in letters_guessed:
        if i in secret_word_list:
            letters_guessed_list.append(i)

    if len(secret_word_list) == len(letters_guessed_list) :
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    underscored_string = [i for i in '_' * len(secret_word)]
    for i in letters_guessed:
        if i in secret_word:
            if secret_word.count(i) > 1:
                list_index = [x for x, y in enumerate(secret_word) if i == y]
                for j in list_index:
                    underscored_string[j] = i
            else:underscored_string[secret_word.index(i)] = i
    return ''.join(underscored_string)




def get_available_letters(letters_guessed):
    s = ""
    for i in string.ascii_lowercase:
        if not i in letters_guessed:
            s+=i
    return s
    

def hangman(secret_word):
    print("\n")
    print("Welcome to the game Hangman")
    print("I'm thinking of a word that is "+str(len(secret_word))+" letters long.")
    guesses = 6
    warnings = 3
    flag = False
    letters_guessed = []
    vowels = 'aeiou'
    available_letters = string.ascii_lowercase

    while guesses > 0:
        print('\n')
        print("--------------------------------------------------------------------------")
        print('\n')
        print("You have "+str(warnings)+" warnings left.")
        print("You have "+str(guesses)+" guesses left.")
        print("Available letters : ",get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter : ")
        if guessed_letter.isalpha():
            if len(guessed_letter) == 1:
                guessed_letter = guessed_letter.lower()
                if guessed_letter in letters_guessed : 
                    if warnings > 0:
                        warnings -= 1
                    else:
                        guesses -= 1
                    print("Oops! You've already guessed that letter. You have "+str(warnings)+" warnings left : ", get_available_letters(letters_guessed)) 
                else:
                    letters_guessed.append(guessed_letter)
                    if guessed_letter in secret_word :
                        print("Good guess : ", get_guessed_word(secret_word,letters_guessed))
                        if is_word_guessed(secret_word,letters_guessed):
                            flag = True
                            break
                    else:
                        if guessed_letter in vowels:
                            guesses -= 2
                        else:
                            guesses -= 1
                        print("OOOOOps! That letter is not in my word! : ", get_guessed_word(secret_word,letters_guessed))
            else:
                if warnings > 0:
                    warnings -= 1
                else:
                    guesses -= 1

                print("Oops! You've already guessed that letter. You have "+str(warnings)+" warnings left : ",get_guessed_word(secret_word,letters_guessed))        
        else:
            if warnings > 0:
                warnings -= 1
            else:
                guesses -= 1
            print("Oops! That is not a valid letter. You have "+str(warnings)+" warnings left : ",get_guessed_word(secret_word,letters_guessed))

    if flag:
        print("Congratulations! You have won the game!")
        temp = []
        temp.extend(secret_word)
        print("Your total score for this game is : ", guesses * len(set(temp)))
    else:
        print("Sorry, you ran out of guesses. The word was "+secret_word+".")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    flag = True
    if len(my_word) == len(other_word):
        for i in my_word:
            for j in other_word:
                if i != '_':
                    if i == j and my_word.count(i) == other_word.count(j):flag = flag and True
                    else:flag = flag and False
        return flag

    else:
        return False
    



def show_possible_matches(my_word):
    new_possible_matches = []
    count_dict = {}
    s = ""
    word_list = ''.join(wordlist)
    for i in my_word:
        if i != '_' :
            if not i in s:
                count_dict[i] = my_word.count(i)
            s+=i
        else:
            s+=("\\w")
    s = r'%s'%s
    possible_matches = list(set(re.findall(s,word_list)))
    for i in possible_matches:
        flag = True
        for key, value in count_dict.items():
            if i.count(key) == value:
                flag = flag and True
            else:
                flag = flag and False
        if flag:
            new_possible_matches.append(i)
    return sorted(new_possible_matches)


def hangman_with_hints(secret_word):
    print("\n")
    print("Welcome to the game Hangman")
    print("I'm thinking of a word that is "+str(len(secret_word))+" letters long.")
    guesses = 6
    warnings = 3
    flag = False
    letters_guessed = []
    vowels = 'aeiou'
    available_letters = string.ascii_lowercase

    while guesses > 0:
        print('\n')
        print("--------------------------------------------------------------------------")
        print('\n')
        print("You have "+str(warnings)+" warnings left.")
        print("You have "+str(guesses)+" guesses left.")
        print("Available letters : ",get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter : ")
        if guessed_letter.isalpha():
            if len(guessed_letter) == 1:
                guessed_letter = guessed_letter.lower()
                if guessed_letter in letters_guessed : 
                    if warnings > 0:
                        warnings -= 1
                    else:
                        guesses -= 1
                    print("Oops! You've already guessed that letter. You have "+str(warnings)+" warnings left : ", get_available_letters(letters_guessed)) 
                else:
                    letters_guessed.append(guessed_letter)
                    if guessed_letter in secret_word :
                        print("Good guess : ", get_guessed_word(secret_word,letters_guessed))
                        if is_word_guessed(secret_word,letters_guessed):
                            flag = True
                            break
                    else:
                        if guessed_letter in vowels:
                            guesses -= 2
                        else:
                            guesses -= 1
                        print("OOOOOps! That letter is not in my word! : ", get_guessed_word(secret_word,letters_guessed))
            else:
                if warnings > 0:
                    warnings -= 1
                else:
                    guesses -= 1

                print("Oops! You've already guessed that letter. You have "+str(warnings)+" warnings left : ",get_guessed_word(secret_word,letters_guessed))        
        elif guessed_letter == '*':
            print("possible matches are :")
            print(' '.join(show_possible_matches(get_guessed_word(secret_word,letters_guessed))))

        else:
            if warnings > 0:
                warnings -= 1
            else:
                guesses -= 1
            print("Oops! That is not a valid letter. You have "+str(warnings)+" warnings left : ",get_guessed_word(secret_word,letters_guessed))

    if flag:
        print("Congratulations! You have won the game!")
        temp = []
        temp.extend(secret_word)
        print("Your total score for this game is : ", guesses * len(set(temp)))
    else:
        print("Sorry, you ran out of guesses. The word was "+secret_word+".")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    
    #secret_word = choose_word(wordlist)
    secret_word = "ample"
    hangman_with_hints(secret_word)
