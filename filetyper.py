
import random
words = open("words.txt",'r').read().split()
#words = open("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt",'r').read().split()
dsize = 47
points = 0
toffset = 50
timerend = 10

def displayout(word,timer):
    
    print("WORD: " + word + "\n" + "Points: " + str(points) + "\n" + "#"*timer + " "*(timerend-timer-1) + "|| " + str(timerend-timer) + "\n"*dsize)


def readinput():
    with open("input.txt",'r') as f: 
        lines = f.readlines()
        try:
            if ' ' in lines[-1]:
                lwords = lines[-1].strip().split(' ')
                for i in range(len(lwords)-1,-1,-1):
                    if lwords[i] != '':
                        return lwords[i]
                else:
                    return ''
            else:
                return lines[-1].strip()
        except:
            return ''

start = input("Type Enter to start: ")


while True:
    done = False
    previousword = ''
    while True:
        newword = random.choice(words)
        if previousword == newword:
            continue
        else:break
    prog = 1
    for timer in range(timerend):
        #displayout(newword,timer)
        for i in range(toffset):
            inputword = readinput() 
            if inputword == newword:
                points += len(newword)*((timerend*toffset)+1-prog)/(toffset*10)
                done = True
                break
            prog += 1
            displayout(newword,timer)
        if done == True:
            break
    else:
        points = points - 10
        