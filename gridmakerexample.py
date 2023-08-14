from gridmaker import create_grid

grid = [[0,12],['adada',5656],['dafa','ffffffjjj']]

tilesize=(10, 4)

tablestr = create_grid(grid,tilesize)

print(tablestr)