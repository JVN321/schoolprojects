from gridmaker import create_grid

grid = [[0,12],['adada',5656],['dafa','ffffffjjj']]

tilesize=(10, 4) #First value is for x axis specify the max length of the tiles , second is y for the height

tablestr = create_grid(grid,tilesize)

print(tablestr)