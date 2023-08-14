
def createtile(value,tilesize):
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

    spacestr = ' '
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

def displaygrid(grid,gridsize,tilesize):
    gridtiles = []
    for i in range(len(grid)):
        gridtiles.append([])
        for j in range(len(grid[i])):
            gridtiles[i].append(createtile(grid[i][j],tilesize))
    return (combinetiles(gridtiles,gridsize,tilesize))

def create_grid(grid,tilesize=(7, 4)):
    gridsize = (len(grid),len(grid[0]))
    return displaygrid(grid,gridsize,tilesize)