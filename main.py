import random
import os
import time
word=False
speedgame=False
memgame=False
typegame=False
smult=1
elapsedtime=0
sentence=[]
wordamt=0
clear = lambda: os.system('cls')
f = open("words.txt", "rt")
wordlist=[]
for i in f.readlines():
    wordlist.append(i[0:-1])
def chooseword():
    return(random.choice(wordlist))
def checkguess(word,guess):
    if guess==word:
        return(len(word) * 2)
    else:
        wrong=0
        score=0
        for i in range(len(guess)):
            try:
                if word[i] == guess[i]:
                    score+=1
                else:
                    wrong+=1
            except:
                wrong+=1
        if score>wrong*smult:
            return(score)
        elif wrong*smult>score:
            return("l")
def checkaccuracy(sentence,retype):
    if retype==sentence:
        return 100
    else:
        correct=0
        for i in range(len(retype)):
            try:
                if sentence[i] == retype[i]:
                    correct+=1
            except:
                pass
    return ((correct/len(sentence))*100)
score=0
timetosleep=3
words=[]
game1="In this game, you will see a word for a decreasing amount of time and you have to try to respell it the best you can.\nEach letter youhave in the correct spot will give you an extra point, and a word spelled fully corrected has a 2x multiplier\nThe game continues until you get less than 50 percent accuracy on a word\nPress enter to begin"
game2="In this game, each round a new word will be added to what you have to type out\n Each correct letter adds one to your score, a perfect recreation gives a 2x multiplier, and the game ends when you have less than 75 percent accuracy"
game3="In this game, you have to retype a sentence and press enter when you're finished. Then the game will calculate your WPM and accuracy."
whichgame=input("Do you want to play game 1 (speed based) or game 2 (memory based) or game 3 (typing test) Type 1, 2 or 3: ")
if whichgame=="1":
    input(game1)
    speedgame=True
elif whichgame=="2":
    input(game2)
    memgame=True
    smult=4
elif whichgame=="3":
    input(game3)
    typegame=True
    wordamt=input("How many words do you want to retype (input an integer): ")
    for i in range(int(wordamt)):
        sentence.append(chooseword())
    sentence=' '.join(i for i in sentence)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("TYPE")
    start=time.time()
else:
    input("invalid response")
clear()
while memgame:
    words.append(chooseword())
    word=' '.join(words)
    print(word)
    time.sleep(timetosleep)
    clear()
    print(f"score:{score}")
    guess=input("What was the word: ")
    grade=checkguess(guess, word)
    if grade=="l":
        print(f"The correct answer was {word}, and you typed {guess}")
        print(f"Your total score was {score}")
        break
    else:
        score+=grade

    clear()
while speedgame:
    if not word:
        word = chooseword()
    print(word)
    time.sleep(timetosleep)
    clear()
    print(f"score:{score}")
    guess=input("What was the word: ")
    grade=checkguess(guess, word)
    if grade=="l":
        print(f"The word was {word}")
        print(f"Your total score was {score}")
        break
    else:
        score+=grade
    word = False
    timetosleep*=0.75
    clear()
while typegame:
    print(sentence)
    retype=input()
    accuracy=checkaccuracy(sentence, retype)
    elapsedtime=time.time()-start
    WPM=(len(sentence)/5)/(elapsedtime/60)
    print(f"You had a WPM of {WPM} with an accuracy of {accuracy}")
    break