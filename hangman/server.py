import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost',8089))
serversocket.listen(1)
while(True):
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    word = str(buf,'utf-8')
    word,hint=word.split(',')
    break
word = word.lower()
HANGMANPICS = ['''
+----+
|    |
|
|
|
|
>===== ''','''
+----+
|    |
|    0
|
|
|
>===== ''','''
|    |
|    0
|    |
|
|
>===== ''','''
+----+
|    |
|    0
|  _/|
|
|
>===== ''','''
+----+
|    |
|    0
|  /|\
|
|
>===== ''','''
+----+
|    |
|    0
|  /|\
|   /
|
>===== ''','''
+----+
|    |
|    0
|  /|\
|   / \_
|
>===== ''']
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print("Hint :",end =" ")
    print(hint)
    print("Missed Letters:",end=' ')
    for letter in missedLetters:
        print(letter,end=' ')
    print()
    blanks = '_'*len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter,end=' ')
    print()
def getGuess(alreadyGuessed):
    while(True):
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter, Choose another letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('PLease enter a LETTER')
        else:
            return guess
print("H A N G M A N")
missedLetters = ''
correctLetters = ''
secretWord =word
gameIsDone = False
while(True):
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "'+secretWord+'"!  You Have won!')
            gameIsDone = True
            break
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
            print('You have run out of guesses!')
            gameIsDone = True
            break
