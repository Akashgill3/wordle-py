import random
from termcolor import colored

def greeting():
    print("Welcome to Wordle!")
    print("Please Enter a 5-Letter Word")

def getWords(filename):
    words = []
    with open(filename) as f:
        words = f.read().split()
    return words

def getWord(filename):
    words = []
    with open(filename) as f:
        words = f.read().split()

    return random.choice(words)

def prettyPrint(list):
    print("Output: ", end='')
    for x in list:
        print(x, end='')

greeting()
guesses = 1
correctWord = getWord('words.txt')
correctWords = getWords('words.txt')
while guesses < 6:
    try:
        inputWord = input("\nInput: ").lower()
        if len(inputWord) != 5 or inputWord not in correctWords:
            raise ValueError
        else:
            guesses += 1
    except ValueError:
        print("Invalid input. Please try again")
        continue

    inputList = []
    for idx in range(0, 5):
        if correctWord[idx] == inputWord[idx]:
            inputList.append(colored(inputWord[idx], "green"))
        elif inputWord[idx] in correctWord:
            inputList.append(colored(inputWord[idx], "yellow"))
        else:
            inputList.append(colored(inputWord[idx], "white"))

    if inputWord == correctWord:
        prettyPrint(inputList)
        print(f"\nYou got it in {guesses - 1} tries.\n")
        break
    elif inputWord != correctWord and guesses == 6:
        prettyPrint(inputList)
        print("\nWhoops, better luck next time")
        print(f"Answer: {correctWord}")
    else:
        prettyPrint(inputList)


