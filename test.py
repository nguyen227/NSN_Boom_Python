file = open("./data/maps/level1.txt", "r")
bitmap = []
map = file.readlines()
for i in range(len(map)):
    bitmap.append([int(x) for x in map[i].split()])
