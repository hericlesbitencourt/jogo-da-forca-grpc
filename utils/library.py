import random
from utils.forca import DRAW_FORCA

def getSecretWord():
    with open("palavras.txt", "rt") as f:
        palavras = f.readlines()
        palavra = random.choice(palavras)
    return palavra.strip().upper()

def getLetterGuess(wrongLetters, correctLetters):
        allLetters = wrongLetters + correctLetters
        while True:
            letter = input('Digite uma letra. \n').upper()
            if len(letter) != 1:
                print('Digite somente 1 (uma) letra')
            elif letter in allLetters:
                print('Essa letra já foi digitada, tente outra letra.')
            elif not 'A' <= letter <= 'Z':
                print('Só é possível digitar letras.')
            else:
                return letter

def printIncompletedWord(word):
    for letter in word:
        print(letter, end='  ')
    print()

def printGame(wrongLetters, correctLetters, secretWord):
    print(DRAW_FORCA[len(wrongLetters)]+'\n')
    print("Letras Erradas: ", end=' ')
    printIncompletedWord(wrongLetters)
    incompleted_word = '_'*len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            incompleted_word = incompleted_word[:i] + secretWord[i] + incompleted_word[i+1:]
    printIncompletedWord(incompleted_word)