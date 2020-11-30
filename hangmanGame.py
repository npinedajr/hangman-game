from random import*
from queue import PriorityQueue

def main():
    wordCollection = readFile()
    print("==========Welcome to the Hangman game!==========")
    categoryOptions = ["category","Adjectives","Animals","Foods","Holidays","States","Progress","Quit the program"]
    difficultyOptions = ["difficulty","Easy","Medium","Hard","Go back","Quit the program"]
    wordsResults = {}
    wins = 0
    match = 0
    while True:
        category = menu(categoryOptions)
        if category == 6:
            printProgress(match,wins,wordsResults)
        elif category == 7:
            break
        else:
            difficulty = menu(difficultyOptions)
            if difficulty == 4:
                continue 
            elif difficulty == 5:
                break 
            else:
                word = obtainWord(category,difficulty,wordCollection)
                if word != -1:
                    won = playGame(word)
                    if won:
                        wordsResults[word] = True
                        match += 1
                        wins += 1
                    else:
                        wordsResults[word] = False
                        match += 1
                else:
                    print("Uh oh! There is no more new words that fit the parameters you have chosen. Please enter different parameters.")
    print("==========Thank you for playing!==========") 
    printProgress(match,wins,wordsResults)

def readFile():
    """
    Inputs: Nothing
    Returns: A list of dictionaries, where each dictionary represents a category of words. 
    Purpose: Read from the words.txt file, which holds all of the words that can be guessed, and
             store each word based on their category and their difficulty rating. Each dictionary holds three
             items, where the keys represent a difficulty and the value is a list of the words that fit both the
             difficulty and category.  
    """
    Adjectives = {
        "Easy" : [],
        "Medium" : [],
        "Hard": []
    }
    Animals = {
        "Easy" : [],
        "Medium" : [],
        "Hard": []
    }
    Foods = {
        "Easy" : [],
        "Medium" : [],
        "Hard": []
    }
    Holidays = {
        "Easy" : [],
        "Medium" : [],
        "Hard": []
    }
    States = {
        "Easy" : [],
        "Medium" : [],
        "Hard": []
    }
    words = [Adjectives,Animals,Foods,Holidays,States]
    with open('words.txt') as fp:
        wordInfo = []
        lineNumber = 0
        for line in fp:
            lineNumber += 1
            wordInfo = line.split()
            if wordInfo[0] == "Adjectives" :
                if wordInfo[1] == "Easy" :
                    words[0]["Easy"].append(wordInfo[2])
                elif wordInfo[1] == "Medium":
                    words[0]["Medium"].append(wordInfo[2])
                elif wordInfo[1] == "Hard":
                    words[0]["Hard"].append(wordInfo[2])
                else:
                    raise FileError("Line number ",lineNumber," in the words.txt file does not have a valid difficulty")
            elif wordInfo[0] == "Animals" :
                if wordInfo[1] == "Easy" :
                    words[1]["Easy"].append(wordInfo[2])
                elif wordInfo[1] == "Medium":
                    words[1]["Medium"].append(wordInfo[2])
                elif wordInfo[1] == "Hard":
                    words[1]["Hard"].append(wordInfo[2])
                else:
                    raise FileError("Line number ",lineNumber," in the words.txt file does not have a valid difficulty")
            elif wordInfo[0] == "Foods" :
                if wordInfo[1] == "Easy" :
                    words[2]["Easy"].append(wordInfo[2])
                elif wordInfo[1] == "Medium":
                    words[2]["Medium"].append(wordInfo[2])
                elif wordInfo[1] == "Hard":
                    words[2]["Hard"].append(wordInfo[2])
                else:
                    raise FileError("Line number ",lineNumber," in the words.txt file does not have a valid difficulty")
            elif wordInfo[0] == "Holidays" :
                if wordInfo[1] == "Easy" :
                    words[3]["Easy"].append(wordInfo[2])
                elif wordInfo[1] == "Medium":
                    words[3]["Medium"].append(wordInfo[2])
                elif wordInfo[1] == "Hard":
                    words[3]["Hard"].append(wordInfo[2])
                else:
                    raise FileError("Line number ",lineNumber," in the words.txt file does not have a valid difficulty")   
            elif wordInfo[0] == "States" :
                if wordInfo[1] == "Easy" :
                    words[4]["Easy"].append(wordInfo[2])
                elif wordInfo[1] == "Medium":
                    words[4]["Medium"].append(wordInfo[2])
                elif wordInfo[1] == "Hard":
                    words[4]["Hard"].append(wordInfo[2])
                else:
                    raise FileError("Line number ",lineNumber," in the words.txt file does not have a valid difficulty")
            else:
                raise FileError("Line number ",lineNumber," in the words.txt file does not have a valid category")
    return words

def menu(options):
    """
    Inputs: A list, which contains the options that a user will be choosing from.
    Returns: An integer, which represents the option chosen by the user.
    Purpose: Take input from the user and verify that the input is valid option 
             allowed based on the options list entered. Will continue to ask a user for
             a valid option if the user entered something that is not allowed.
    """
    valid = False
    while not valid:
        print("")
        print("What",options[0],"would you like to chose for your word?")
        for i in range(len(options)-1):
            print(i+1,"-",options[i+1])
        choice = input("Option: ")
        if choice.isnumeric():
            if int(choice)<=0 or int(choice)>(len(options)-1):
                print("Invalid range. Please try again.")
            else:
                valid = True
        else:
            print("Invalid choice. Please try again.") 
    return int(choice) 

def printProgress(match,wins,wordsResults):
    """
    Inputs: The integer with the name match, which represents the number of matches played during this session.
            The integer with the name wins, which represents the number of matches won by the user during this session.
            The dictionary with the name wordsResults, where each key in an item pair represents the word attempted to guess
            and the value stores a boolean, where True means they successfuly guessed and False means they failed to guess the word.
    Returns: Nothing. This function only prints.
    Purpose: To print the current progress of the user, which consists of the number of matches and wins, and which words they did and 
             did not solve.
    """
    print("You have played",match,"matches and won",wins,"times.")
    wordsPlayed = list(wordsResults.keys())
    for i in range(len(wordsPlayed)):
        if "_" in wordsPlayed[i]:
            if wordsResults.get(wordsPlayed[i]) == False:
                print(wordsPlayed[i].replace('_',' '),"was not solved.")
            else:
                print(wordsPlayed[i].replace('_',' '),"was solved!")
        else:
            if wordsResults.get(wordsPlayed[i]) == False:
                print(wordsPlayed[i],"was not solved.")
            else:
                print(wordsPlayed[i],"was solved!")


def obtainWord(category,difficulty,wordsCollection):
    """
    Inputs: The integer named caregory, which will select the category in wordsCollection.
            The integer named difficulty, which will determine the key that is pulled.
            The list named wordsCollection, where each element contains a dictionary representing a different
            category.
    Returns: Can return an integer of -1, which represents that the user has already guessed all
             available words with the specific category and difficulty entered.
             If user has not used all available words, will randomly return a word that fits the 
             caregory and difficulty entered by the user.
    Purpose: To randomly obtain a word based on the category and difficulty entered by the user. If no more 
             words are available under the same category and difficulty, return -1.
    """
    if difficulty == 1:
        if len(wordsCollection[category-1]["Easy"]) == 0:
            return -1
        x = randrange(len(wordsCollection[category-1]["Easy"]))
        return wordsCollection[category-1]["Easy"].pop(x)
    elif difficulty == 2:
        if len(wordsCollection[category-1]["Medium"]) == 0:
            return -1
        x = randrange(len(wordsCollection[category-1]["Medium"]))
        return wordsCollection[category-1]["Medium"].pop(x)
    else:
        if len(wordsCollection[category-1]["Hard"]) == 0:
            return -1
        x = randrange(len(wordsCollection[category-1]["Hard"]))
        return wordsCollection[category-1]["Hard"].pop(x)

def playGame(word):
    """
    Inputs: A string, which represents the word that the user is solving for.
    Returns: A boolean, where True represents that the user successfully guessed the word, 
             and False means the user failed to solve the word.
    Purpose: To allow users to guess the word entered into the function. They can only make 
             a maxium of 6 mistakes. If they would like to give up, the user can just press enter.
    """
    mystery = makeMystery(word)
    mistakes = 6
    lettersGuessed = PriorityQueue()
    print("")
    print("==========Good Luck!==========")
    while True:
        lettersGuessedList = []
        for i in range(lettersGuessed.qsize()):
            temporary = lettersGuessed.get()
            lettersGuessedList.append(temporary)
        print("The word you are trying to solve is the following:")
        print(mystery)
        print("Letters Guessed: "), print("".join(lettersGuessedList))
        if mistakes == 1:
            print("You can make 1 more mistake.")
        else:
            print("You can make",mistakes,"more mistakes.")
        letter = inputLetter(lettersGuessedList)
        if letter == "":
            if "_" in word:
                print("Nice try! The answer was:",word.replace('_',' '))
                return False
            else:
                print("Nice try! The answer was:",word)
                return False
        lettersGuessed.put(letter.upper())
        for i in range(len(lettersGuessedList)):
            lettersGuessed.put(lettersGuessedList[i].upper())
        if letter.upper() in word.upper():
            print("Nice! This letter is indeed in the word!")
            print("")
            mystery = updateMystery(letter,word,mystery)
            if mystery == word:
                print("Congratulations! You have found the word!")
                if "_" in word:
                    print("The answer was:",word.replace('_',' '))
                    return True
                else:
                    print("The answer was:",word)
                    return True
        else:
            print("Oops! This letter is not found in the word!")
            print("")
            mistakes -= 1
            if mistakes == 0:
                if "_" in word:
                    print("Nice try! The answer was:",word.replace('_',' '))
                    return False
                else:
                    print("Nice try! The answer was:",word)
                    return False

def makeMystery(word):
    """
    Inputs: A string, which represents the word that the user is solving for
    Returns: A string, which represents the user's current progress in solving the word.
    Purpose: Create a new string, which has the same length as the word entered and converts 
             all letters into asteriks, allowing the user to guess for the letter contained in 
             the word.
    """
    accum = ""
    for i in range(len(word)):
        if word[i] == "_":
            accum += " "
        elif ord("Z")>=ord(word[i])>=ord("A") or ord("a")<=ord(word[i])<=ord("z"):
            accum += "?"
        else:
            accum += word[i]
    return accum 

def inputLetter(lettersGuessed):
    """
    Inputs: A list, which contains all the letters already guessed by the user for this current word.
    Returns: A string, which can either be empty, representing that the user would like to give up, or a 
             valid letter.
    Purpose: To ask the user for a valid letter they believe might be in the word. 
    """
    valid = False
    while not valid:
        print("What letter would you like to guess? If you would like to stop playing, just press enter.")
        letter = input("Letter: ")
        if letter == "":
            return ""
        else: 
            if letter.isalpha() and len(letter) == 1:
                if letter.upper() in lettersGuessed:
                    print("You have already guessed this letter before. Please enter a different letter.")
                    print("")
                else:
                    return letter.upper()
            else:
                print("Invalid entry. Please enter a single letter.")
                print("")

def updateMystery(letter,word,mystery):
    """
    Inputs: A string named letter, which represents the letter the user guessed 
            A string named word, which is the word the user is guessing for.
            A string named mystery, which represents the user's progress in solving the word.
    Returns: A string, which represents the updated progress for the user solving the word.
    Purpose: To update the user's progress in solving the word by finding where the letter they guessed
             is found in the word. 
    """
    accum = ""
    for j in range(len(word)):
        if letter.upper() == word[j].upper():
            accum += word[j]
        else:
            accum += mystery[j]
    return accum
        
main()