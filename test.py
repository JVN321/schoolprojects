





grid = []



def updown(jtup,ktup):

    for i in range(len(grid[0])):
            for j in range(jtup[0],jtup[1],jtup[2]):
                if grid[j][i] == 0 or j == jtup[3]:continue
                comb = grid[j][i]
                grid[j][i] = 0
                pval = j
                for k in range(j+ktup[0],ktup[1],ktup[2]):
                    if grid[k][i] != 0:
                        pval = k
                        break
                if grid[k][i] == comb:
                    comb = grid[k][i] + comb
                    grid[k][i] = 0
                    grid[j][i] = 0
                
                pval = j
                for k in range(j+ktup[0],ktup[1],ktup[2]):
                    if grid[k][i] != 0:
                        break
                    pval = k
                grid[pval][i] = comb

#w
updown((0,len(grid),1,0,),(-1,-1,-1))
#s
updown((len(grid)-1,-1,-1,len(grid)-1,),(1,len(grid),1))


'''
if move == 'w':
    for i in range(len(grid[0])):
        for j in range(0,len(grid),1):
            if grid[j][i] == 0 or j == 0:continue
            comb = grid[j][i]
            grid[j][i] = 0
            pval = j
            for k in range(j-1,-1,-1):
                if grid[k][i] != 0:
                    pval = k
                    break
            if grid[k][i] == comb:
                comb = grid[k][i] + comb
                grid[k][i] = 0
                grid[j][i] = 0
            
            pval = j
            for k in range(j-1,-1,-1):
                if grid[k][i] != 0:
                    break
                pval = k
            grid[pval][i] = comb
if move == 's':
    for i in range(len(grid[0])):
        for j in range(len(grid)-1,-1,-1):
            if grid[j][i] == 0 or j == len(grid)-1:continue
            comb = grid[j][i]
            grid[j][i] = 0
            pval = j
            for k in range(j+1,len(grid),1):
                if grid[k][i] != 0:
                    pval = k
                    break
            if grid[k][i] == comb:
                comb = grid[k][i] + comb
                grid[k][i] = 0
                grid[j][i] = 0
            
            pval = j
            for k in range(j+1,len(grid),1):
                if grid[k][i] != 0:
                    break
                pval = k
            grid[pval][i] = comb
'''


def updown(jtup, ktup, grid1, dir=False):
    for i in range(grid1):
        for j in range(jtup[0], jtup[1], jtup[2]):
            j1, i1 = j, i
            if dir == True:
                j1, i1 = i, j
            if grid[j1][i1] == 0 or j == jtup[3]:
                continue
            comb = grid[j1][i1]
            grid[j1][i1] = 0
            pval = j

            for k in range(j+ktup[0], ktup[1], ktup[2]):
                if dir == True:
                    k1, i2 = i, k
                else:
                    k1, i2 = k, i
                if grid[k1][i1] != 0:
                    pval = k
                    break
            if grid[k1][i2] == comb:
                comb = grid[k1][i2] + comb
                grid[k1][i2] = 0
                grid[j1][i1] = 0

            pval = j
            for k in range(j+ktup[0], ktup[1], ktup[2]):
                if dir == True:
                    k2, i3 = i, k
                else:
                    k2, i3 = k, i
                if grid[k2][i3] != 0:
                    break
                pval = k
            if dir == True:
                pval1, i3 = i, pval
            else:
                pval1, i3 = pval, i
            grid[pval1][i3] = comb

if move == 'w':
    updown((0, len(grid), 1, 0,), (-1, -1, -1), len(grid[0]))
elif move == 's':
    updown((len(grid)-1, -1, -1, len(grid)-1,),
            (1, len(grid), 1), len(grid[0]))

elif move == 'a':
    updown((0, len(grid[0]), 1, 0,), (-1, -1, -1), len(grid), True)
elif move == 'd':
    updown((len(grid[0])-1, -1, -1, len(grid[0])-1),
            (1, len(grid[0]), 1), len(grid[0]), True)












    def updown(jtup,ktup):
        for i in range(len(grid[0])):
                for j in range(jtup[0],jtup[1],jtup[2]):
                    if grid[j][i] == 0 or j == jtup[3]:continue
                    comb = grid[j][i]
                    grid[j][i] = 0
                    pval = j
                    for k in range(j+ktup[0],ktup[1],ktup[2]):
                        if grid[k][i] != 0:
                            pval = k
                            break
                    if grid[k][i] == comb:
                        comb = grid[k][i] + comb
                        grid[k][i] = 0
                        grid[j][i] = 0
                    
                    pval = j
                    for k in range(j+ktup[0],ktup[1],ktup[2]):
                        if grid[k][i] != 0:
                            break
                        pval = k
                    grid[pval][i] = comb

    if move == 'w':
        updown((0,len(grid),1,0,),(-1,-1,-1))
    elif move == 's':
        updown((len(grid)-1,-1,-1,len(grid)-1,),(1,len(grid),1))

    elif move == 'a':

        for i in range(len(grid)):
            for j in range(0,len(grid[0]),1):
                if grid[i][j] == 0 or j == 0:continue
                comb = grid[i][j]
                grid[i][j] = 0
                pval = j
                for k in range(j-1,-1,-1):
                    if grid[i][k] != 0:
                        pval = k
                        break
                if grid[i][k] == comb:
                    comb = grid[i][k] + comb
                    grid[i][k] = 0
                    grid[i][j] = 0
                
                pval = j
                for k in range(j-1,-1,-1):
                    if grid[i][k] != 0:
                        break
                    pval = k
                grid[i][pval] = comb
    elif move == 'd':

        for i in range(len(grid)):
            for j in range(len(grid[0])-1,-1,-1):
                if grid[i][j] == 0 or j == len(grid[0])-1:continue
                comb = grid[i][j]
                grid[i][j] = 0
                pval = j
                for k in range(j+1,len(grid[0]),1):
                    if grid[i][k] != 0:
                        pval = k
                        break
                if grid[i][k] == comb:
                    comb = grid[i][k] + comb
                    grid[i][k] = 0
                    grid[i][j] = 0
                
                pval = j
                for k in range(j+1,len(grid[0]),1):
                    if grid[i][k] != 0:
                        break
                    pval = k
                grid[i][pval] = comb




move = ''


'''
if move == "w":
    for i in range(0, len(grid[0]),1):
        for j in range(0, len(grid),1):
            if grid[j][i] != 0 and j != 0:
                k = j - 1
                while grid[k][i] == 0 and k != 0:
                    k -= 1
                if grid[k][i] == grid[j][i] and (k,i) not in justmerged:
                    grid[k][i] += grid[j][i]
                    grid[j][i] = 0
                    justmerged.append((k,i))
if move == "s":
    for i in range(0, len(grid[0]),1):
        for j in range(len(grid)-1,-1,-1):
            if grid[j][i] != 0 and j != len(grid)-1:
                k = j + 1
                while grid[k][i] == 0 and k != len(grid)-1:
                    k += 1
                if grid[k][i] == grid[j][i] and (k,i) not in justmerged:
                    grid[k][i] += grid[j][i]
                    grid[j][i] = 0
                    justmerged.append((k,i))
'''

'''
    if move == "a":
        for j in range(0, len(grid),1):
            for i in range(0, len(grid[0]),1):
            
                if grid[j][i] != 0 and i != 0:
                    k = i - 1
                    while grid[j][k] == 0 and k != 0:
                        k -= 1
                    if grid[j][k] == grid[j][i] and (j,k) not in justmerged:
                        grid[j][k] += grid[j][i]
                        grid[j][i] = 0
                        justmerged.append((j,k))
    if move == "d":
        for j in range(0, len(grid),1):
            for i in range(len(grid[0])-1,-1,-1):
                if grid[j][i] != 0 and i != len(grid[0])-1:
                    k = i + 1
                    while grid[j][k] == 0 and k != len(grid[0])-1:
                        k += 1
                    if grid[j][k] == grid[j][i] and (j,k) not in justmerged:
                        grid[j][k] += grid[j][i]
                        grid[j][i] = 0
                        justmerged.append((j,k))
'''

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
                    grid[j][i] = 0
                    justmerged.append((j,k))

if move == "a":
    mergeupdown((0, len(grid[0]),1,0,1))
elif move == "d":
    mergeupdown((len(grid[0])-1,-1,-1,len(grid[0])-1,-1))
