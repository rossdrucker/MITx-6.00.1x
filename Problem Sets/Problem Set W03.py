# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:13:46 2019

@author: rdrucker
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    missing_letters = [l for l in secretWord if l not in lettersGuessed]
    if len(missing_letters) > 0:
        return False
    else:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for l in secretWord:
        if l in lettersGuessed:
            result += l
        else:
            result += '_ '
    return result

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    letters = string.ascii_lowercase
    for l in letters:
        if l in lettersGuessed:
            letters = letters.replace(l, '')
    return letters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    guesses_left = 8
    available_letters = getAvailableLetters([])
    guessed_letters = []
    word_guessed = False
    while guesses_left > 0 and word_guessed == False:
        print('You have ' + str(guesses_left) + ' guesses left.')
        print('Available Letters: ' + str(available_letters))
        guessed_letter = input('Please guess a letter: ')

        if guessed_letter in guessed_letters:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guessed_letters))
            print('-------------')

        elif guessed_letter in secretWord:
            guessed_letters.append(guessed_letter)
            print('Good guess: ' + getGuessedWord(secretWord, guessed_letters))
            available_letters = getAvailableLetters(guessed_letters)
            print('-------------')

        else:
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, guessed_letters))
            print('-------------')
            guessed_letters.append(guessed_letter)
            available_letters = getAvailableLetters(guessed_letters)
            guesses_left -= 1

        word_is_guessed = isWordGuessed(secretWord, guessed_letters)

        if word_is_guessed:
            word_guessed = True

    if word_guessed == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + str(secretWord))

hangman('taxi')