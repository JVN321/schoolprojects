
#CHESS







# FIND NUMBER
'''
s = list(range(1,50))
m = []
l = []
while True:
     e = len(s)//2
     s = [s[:e],s[e:]]
     h = 0
     if s[0] == [] or s[1] == []:
          break
     for i in range(len(s[0])+len(m)):
          if i % 5 == 0:
               print()
          
          if i >= len(s[0]):
               f = " " + " "*(1//len(str(m[h])))
               print(m[h],end=f)
               h += 1
          else:
               f = " " + " "*(1//len(str(s[0][i])))
               print(s[0][i],end=f)
     print()
     
     g = input("Y or N: ")
     if g in "Yy":
          
          s,l = s[0],s[1]
          m.extend(l)
     elif g in "Nn":
          s,l = s[1],s[0]
          m.extend(l)
if s[0] == []:
     print(s[1][0])
else:
     print(s[0][0])
'''


# CROSSWORD
'''
import time
import os
import random
import re
import math
with open("crossword.txt", "w+") as f:
    f.write("")

a = int(input("size: ") or 20)
size = [a, a]
words = input(
    "Words seperated by space: ") or "TEST VALUES FOR TESTING THE CROSSWORD PUZZLE MAKER"
words = re.sub("^A-Za-z", "", words)
words = words.split()
wordsgotten = []
show = (input("Display: ")) or 'True'
animate = (input("Animate: ")) or 'False'
if animate == 'True':
    hide = 'False'
else:
    hide = (input("Answers: ")) or 'False'
play = input("Play: ") or 'False'
vari = 'False'
if play == 'False':
    vari = input("Variations: ") or 'False'

varic = []
if vari == 'False':
    seed = float(input("Seed: ") or random.random())
    varic.append(seed)
else:
    varic = [random.random() for s in range(int(vari))]


def display(positions):
    if animate == 'False':
        return
    time.sleep(0.1)
    os.system("cls")
    for i in positions:
        for j in i:
            if j == "":
                print(".", end="  ")
                continue
            print(j, end="  ")
        print()


for i in varic:
    seed = i
    random.seed(seed)
    w = words[:]
    random.shuffle(w)
    positions = [["" for x in range(size[0])] for y in range(size[1])]
    c = w.pop(0).upper()
    a = random.choice(range(size[1]))
    b = random.choice(range(size[0]-len(c)))
    cpos = [b, a, 0]
    for i in range(b, b+len(c)):
        positions[a][i] = c[i-b]  # places the first word on a random position
    display(positions)
    wordcords = []

    def check(positions, zeeword, j, i, ran=False):
        z = []
        for m in range(8):
            for h in range(len(zeeword)):
                l = [[j+h, i], [j-h, i], [j, i+h], [j, i-h],
                     [j+h, i+h], [j-h, i-h], [j-h, i+h], [j+h, i-h]]
                k = l[m]
                try:
                    if k[0] < 0 or k[1] < 0:
                        break
                    thel = positions[k[0]][k[1]]
                except:
                    break
            else:
                z.append(m)
        for m in z:
            for h in range(len(zeeword)):
                l = [[j+h, i], [j-h, i], [j, i+h], [j, i-h],
                     [j+h, i+h], [j-h, i-h], [j-h, i+h], [j+h, i-h]]
                k = l[m]
                thel = positions[k[0]][k[1]]
                if ran == False:
                    thef = "" + zeeword[h]
                else:
                    thef = ""
                if thel in thef:
                    if ran == False:
                        positions[k[0]][k[1]] = zeeword[h]

                        display(positions)

                else:
                    break
            else:
                found = True
                return found
        else:
            found = False
            return found

    for i in w:
        zeeword = i.upper()
        found = False
        for e, f in enumerate(zeeword):
            ranpos = []
            if found == True:
                break
            for j, valp in enumerate(positions):
                if found == True:
                    break
                for i, valf in enumerate(valp):
                    if valf == f:
                        found = check(positions, zeeword, j, i)
                        if found == True:
                            break
            if found == False:
                for j, valp in enumerate(positions):
                    if found == True:
                        break
                    for i, valf in enumerate(valp):
                        if valf == "":
                            foundran = check(positions, zeeword, j, i, True)
                            if foundran == True:
                                ranpos.append([i, j])
            if len(ranpos) != 0:
                tpos = random.choice(ranpos)
                found = check(positions, zeeword, tpos[1], tpos[0], False)
                break
            else:
                break

    fpositions = []
    for i in positions:
        for j in i:
            if j == "":
                letters = [chr(i) for i in range(65, 91)]
                if hide == 'False':
                    fpositions.append(random.choice(letters))
                else:
                    fpositions.append(".")
                continue
            fpositions.append(j)
        fpositions.append("\n")

    with open("crossword.txt", "a+") as f:
        for i in fpositions:
            if i == "\n":
                f.write(i)
                continue
            f.write(i+"  ")

        f.write("\n")
        f.write("Words: ")
        for i in words:
            f.write(i+' ')
        f.write(f"\nSeed: {seed}\n")

    os.system("cls")
    maxspaces = [len(str(size[0]))+1, len(str(size[1]))+2]
    seplines = 1
    if show == 'True':

        while True:
            if animate == 'True':
                break

            print()
            print(maxspaces[1]*" ", end="")

            for i in range(size[0]):
                print(i, end=(maxspaces[0]-len(str(i))+1)*" ")

            print("\n", end=maxspaces[1]*" ")

            for i in range(size[0]):
                print("-"*(maxspaces[0]+1), end="")
            print()
            n = 0
            print(str(n) + (maxspaces[1]-len(str(n))-1)*" " + "|", end="")
            if animate == 'False':
                for i in fpositions:
                    if i == "\n":
                        print(i, end="")
                        n += 1
                        print("\n"*seplines, end="")
                        if n == size[1]:
                            break
                        print(
                            str(n) + (maxspaces[1]-len(str(n))-1)*" " + "|", end="")

                        continue
                    print(i, end=maxspaces[0]*" ")

            print()

            print("Words: ")
            for i in words:
                print(i, end=" ")
            print("\nWords gotten: ")
            for i in wordsgotten:
                print(i, end=" ")
            print()
            print(f"\nSeed: {seed}\n")
            if play == 'True':
                print(
                    "format x,y i,j where x,y and i,j are the starting and ending cordoordinates of the word")
                try:
                    ans = input(": ")
                    cords = ans.split(" ")
                    cords = cords[0].split(",") + cords[1].split(",")
                except:
                    print("Invalid format")
                    continue
                ccords = []
                for i in cords:
                    ccords.append(int(i))
                cords = ccords
                x, y, i, j = cords
                wcords = []
                if x == i:
                    a = (y-j)/math.fabs(y-j)
                    for f in range(y, j-int(a), -int(a)):
                        wcords.append((x, f))
                elif y == j:
                    a = (x-i)/math.fabs(x-i)
                    for f in range(x, i-int(a), -int(a)):
                        wcords.append((f, y))
                else:
                    c = [1, 1]
                    if x < i:
                        c[0] = 1
                    if y < j:
                        c[1] = 1
                    while True:
                        if (x, y) == (i, j):
                            break
                        if x == i or y == j:
                            break

                        x, y = x + c[0], y + c[1]
                        wcords.append((x, y))
                l = ""
                for i in wcords:
                    l += positions[i[1]][i[0]]
                if len(words) == 0:
                    print("No more words won \n YOU WON")
                if l in words:
                    words.remove(l)
                    print("You got", l)
                    wordsgotten.append(l)
                else:
                    print("You didn't get anything")
                os.system("cls")
            else:
                break

    print("Done")
'''