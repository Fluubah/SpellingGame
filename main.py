import random
import os
import time
word=False
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
        if score>wrong:
            return(score)
        elif wrong>score:
            return("l")
score=0
timetosleep=3
input("In this game, you will see a word for a decreasing amount of time and you have to try to respell it the best you can.\nEach letter youhave in the correct spot will give you an extra point, and a word spelled fully corrected has a 2x multiplier\nThe game continues until you get less than 50 percent accuracy on a word\nPress enter to begin")
clear()
while True:
    if not word:
        word = chooseword()
    print(word)
    time.sleep(timetosleep)
    clear()
    print(f"score:{score}")
    guess=input("What was the word: ")
    grade=checkguess(guess, word)
    if grade=="l":
        break
    else:
        score+=grade
    word = False
    timetosleep*=0.75
    clear()
print(f"Your total score was {score}")