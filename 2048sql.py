
import random

tilesize = (7, 4)
gridsize = (4, 4)  # y,x
pad = 40
gamescene = ""

color = "Ñ%@#W$?|!;:+=-,._ "[::-1]
#color = "⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿"
startchoice = [[2, 2], [2, 2], [4], [4, 2]]
choicies = [[2],[2],[2],[2],[4]]
score = 0

def createtile(value,tilesize=tilesize):
    value = str(value)
    tile = ''
    n = 0
    p = 1
    try:
        while True:
            if p >= int(value):
                break
            n += 1
            p += p
    except:
        n = 0

    spacestr = color[n]
    spaces = (tilesize[0] - 1 - len(value))//2
    valueformated = spacestr*spaces + value
    addspaces = tilesize[0] - 1 - len(valueformated)
    valueformated = valueformated + spacestr * addspaces
    for j in range(tilesize[1]):
        for i in range(tilesize[0]):
            if i in (0,) and j in (0,):
                tile += '+'
            elif i in range(0, tilesize[0]+1) and j in (0,):
                tile += '-'
            elif i in (0,) and j in range(0, tilesize[1]+1):
                tile += '|'
            elif j == tilesize[1]//2:
                tile += valueformated[i-j+1]
            else:
                tile += spacestr
        tile += '\n'
    return tile


def combinetiles(grouptiles,gridsize,tilesize):
    finalgrid = ''
    for j in range(len(grouptiles)):
        for i in range(len(grouptiles[j])):
            grouptiles[j][i] = grouptiles[j][i].split('\n')

    for g in range(len(grouptiles)):
        tiles = grouptiles[g]
        for i in range(len(tiles[0])):
            for j in range(len(tiles)):
                finalgrid += tiles[j][i]

            if i == 0:
                finalgrid += '+'
            else:
                finalgrid += '|'
            finalgrid += '\n'
        finalgrid = finalgrid.rstrip('|\n')
        finalgrid += '|\n'
    finalgrid += '+'
    for i in range(gridsize[1]):
        for j in range(tilesize[0]-1):
            finalgrid += '-'
        finalgrid += '+'
    return finalgrid


def addrandomvalue(grid):
    curchoice = random.choice(choicies)
    for k in curchoice:
        popablepoints = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    popablepoints.append((i, j))
        point = random.choice(popablepoints)
        grid[point[0]][point[1]] = k
    return grid

def addscore(value):
    global score
    score += value

def displaygrid(pad,grid,gridsize=gridsize,tilesize=tilesize):
    global gridtiles
    clearscreen()
    for i in range(len(grid)):
        gridtiles.append([])
        for j in range(len(grid[i])):
            gridtiles[i].append(createtile(grid[i][j],tilesize))
    print(combinetiles(gridtiles,gridsize,tilesize))
    gridtiles = []

def compresgrid(move):
    
    def compupdown(jtupe):
        for i in range(0, len(grid[0]),1):
            for j in range(jtupe[0],jtupe[1],jtupe[2]):
                if grid[j][i] != 0 and j != jtupe[3]:
                    k = j - jtupe[4]
                    while grid[k][i] == 0:
                        if k == jtupe[3]:
                            break
                        k -= jtupe[4]
                    else:
                        k += jtupe[4] 
                    if grid[k][i] == grid[j][i]:
                        continue
                    else:
                        grid[k][i] = grid[j][i]
                        grid[j][i] = 0
    if move == "w":
        compupdown((0, len(grid),1,0,1))
    elif move == "s":
        compupdown((len(grid)-1,-1,-1,len(grid)-1,-1))


    def compleftright(itupe):
        for j in range(0, len(grid),1):
            for i in range(itupe[0],itupe[1],itupe[2]):  
                if grid[j][i] != 0 and i != itupe[3]:
                    k = i - itupe[4]
                    while grid[j][k] == 0:
                        if k == itupe[3]:
                            break
                        k -= itupe[4]
                    else:
                        k += itupe[4]
                    if grid[j][k] == grid[j][i]:
                        continue
                    else:
                        grid[j][k] = grid[j][i]
                        grid[j][i] = 0

    if move == "a":
        compleftright((0, len(grid[0]),1,0,1))
    elif move == "d":
        compleftright((len(grid[0])-1,-1,-1,len(grid[0])-1,-1))

def mergegrid(move):
    def mergeupdown(jtupe):
        justmerged = []
        for i in range(0, len(grid[0]),1):
            for j in range(jtupe[0],jtupe[1],jtupe[2]):
                if grid[j][i] != 0 and j != jtupe[3]:
                    k = j - jtupe[4]
                    while grid[k][i] == 0 and k != jtupe[3]:
                        k -= jtupe[4]
                    if grid[k][i] == grid[j][i] and (k,i) not in justmerged:
                        grid[k][i] += grid[j][i]
                        addscore(grid[k][i])
                        grid[j][i] = 0
                        justmerged.append((k,i))

    if move == "w":
        mergeupdown((0, len(grid),1,0,1))
    elif move == "s":
        mergeupdown((len(grid)-1,-1,-1,len(grid)-1,-1))

    def mergeleftright(itupe):
        justmerged = []
        for j in range(0, len(grid),1):
            for i in range(itupe[0],itupe[1],itupe[2]):
            
                if grid[j][i] != 0 and i != itupe[3]:
                    k = i - itupe[4]
                    while grid[j][k] == 0 and k != itupe[3]:
                        k -= itupe[4]
                    if grid[j][k] == grid[j][i] and (j,k) not in justmerged:
                        grid[j][k] += grid[j][i]
                        addscore(grid[j][k])
                        grid[j][i] = 0
                        justmerged.append((j,k))

    if move == "a":
        mergeleftright((0, len(grid[0]),1,0,1))
    elif move == "d":
        mergeleftright((len(grid[0])-1,-1,-1,len(grid[0])-1,-1))
    compresgrid(move)


gridtiles = []
grid = []

for i in range(gridsize[0]*gridsize[1]):
    grid.append(0)


curchoice = random.choice(startchoice)
popablepoints = list(range(len(grid)))
for i in curchoice:
    point = random.choice(popablepoints)
    popablepoints.remove(point)
    grid[point] = i
tempgrid = list(grid)
grid = []
c = 0
for i in range(0, len(tempgrid), gridsize[1]):
    i += gridsize[1]
    grid.append(tempgrid[c:i])
    c = i


def clearscreen(n=40):
    print("\n"*40)

def startgame():
    global grid
    while True:
        tempgrid = []
        for i in range(len(grid)):
            tempgrid.append([])
            for j in grid[i]:
                tempgrid[i].append(j)
        displaygrid(pad,grid)
        print("Score:",score)
        move = input(':').lower()
        if move == "exit":
            print("\nGame over","\nYour Score: ",score,sep='')
            return score
        if move not in "wasd":
            continue
        mergegrid(move)

        if tempgrid == grid:
            try:
                addrandomvalue(tempgrid)
            except:
                print("\nGame over","\nYour Score: ",score,sep='')
                return score
            continue
        grid = addrandomvalue(grid)

def showoptions(opt):
    s = ""
    choices = []
    for i in range(len(opt)):
        s += f"({i}): {opt[i]} \n"
        choices.append(str(i))
    while True:
        print(s)
        out = input("Choose: ")
        if out in choices:
            return int(out)
        else:
            print("Invalid Choice\n")

options = ["New game","High Scores","Help","Exit"]

import mysql.connector as sql

while True:
    user = input("Sql Username (Default is root): ")
    if user == "": user = "root"
    try:
        password = input("Sql Password (Default is root): ")
        if password == "": password = "root"
        con = sql.connect(host="localhost",password = password,user=user)
    except sql.errors.ProgrammingError:
        print("Wrong password")
    except Exception as e:
        print("Could not connect to mysql")
        print("Error Details: " + str(e))
    else:
        break

cur = con.cursor()
try:
    cur.execute("use 2048database")
except:
    cur.execute("create database 2048database")
    cur.execute("use 2048database")

try:
    cur.execute("insert into data values('test','test',0)")
    cur.execute("delete from data where username = 'test' and password = 'test' and highscore = 0")
except:
    cur.execute("create table data(username varchar(20) primary key,password varchar(20),highscore int)")


loginoptions = ["New User","Login"]
choice = showoptions(loginoptions)
if choice == 0:
    while True:
        
        newuser = input("User Name with no spaces or special characters of 10 characters: ")
        if len(newuser) > 10:
            print("Username too long")
            continue
        try:
            cur.execute(f"select * from data where username = '{newuser}'")
            if len(cur.fetchall()) > 0: 
                print("User name already exists")
                continue
            else:
                while True:
                    password = input("Password with no spaces: ")
                    if password == input("Retype password: "):
                        break
                    else:
                        print("Passwords dont match")
                        continue
                cur.execute(f"insert into data values('{newuser}','{password}',0)")
                con.commit()
                user = newuser
                break
        except Exception as e:
            print("Wrong username format")
            print("More error details: " + str(e))
        
elif choice == 1:
    while True:
        try:
            username = input("Username: ")
            password = input("Password: ")
            cur.execute(f"select * from data where username='{username}' and password='{password}'")
            if len(cur.fetchall()) == 1: 
                user = username 
                break
            else: print("Wrong password of username \n")
        except Exception as e:
            print("Error Details: " + str(e))
            pass
while True:
    clearscreen()
    choice = showoptions(options)

    if choice == 3:
        print("Exiting")
        exit()
    if choice == 2:
        print("Use w,a,s,d to move by inserting the key and pressing enter\nType exit to end game")
        input("Press enter to go back to main menu")
    if choice == 0:
        score = startgame()
        try:
            cur.execute(f"select * from data where username = '{user}'")
            data = list(cur.fetchall())
            highscore = data[0][-1]
            if score > highscore:
                print("New Highscore")
                cur.execute(f"update data set highscore = {score} where username = '{user}'")
                con.commit()
            input("Press enter to go back to main menu")
        except Exception as e:
            print("Error details: " + str(e))
            input("Press enter to go back to main menu")
    if choice == 1:
        clearscreen()
        try:
            cur.execute(f"select username,highscore from data order by highscore desc")
            highscores = cur.fetchall()
            maxlen = 0
            highscores.insert(0,("Names","High Scores"))
            for i in highscores:
                if len(i[0]) > maxlen:
                    maxlen = len(i[0])
                if len(str(i[1])) > maxlen:
                    maxlen = len(str(i[1]))
            
            displaygrid(pad,highscores,gridsize=(0,2),tilesize=(maxlen + 3 , 4))
            input("Press enter to go back to main menu")
        except Exception as e:
            print("Error Details: ",e)