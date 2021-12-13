inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

paper = []
numberOfHashes = 0
maxy = 0
maxx = 0

for line in lines:
    if "," in line:
        x, y = line.split(",")
        if int(x) > maxx:
            maxx = int(x)
        if int(y) > maxy:
            maxy = int(y)

for y in range(maxy+1):
    row = []
    for x in range(maxx+1):
        row.append(".")
    paper.append(row)

for line in lines:
    if len(line) == 0:
        pass
    elif "fold" in line:
        temp = line.split()
        axis, pos = temp[2].split("=")
        if axis == "y":
            ycount = 1
            for y in range(int(pos)+1, len(paper)):
                xcount = 0
                for x in paper[y]:
                    mirroredcell = paper[int(pos) - ycount][xcount]
                    if x == "#" or mirroredcell == "#":
                        paper[int(pos) - ycount][xcount] = "#"
                    else:
                        paper[int(pos) - ycount][xcount] = "."
                    xcount += 1
                ycount += 1
            for y in range(int(pos), len(paper)):
                paper.pop()
        elif axis == "x":
            xcount = 1
            for x in range(int(pos)+1, len(paper[0])):
                for y in paper:
                    currentcell = y[x]
                    mirroredcell = y[int(pos) - xcount]
                    if currentcell == "#" or mirroredcell == "#":
                        y[int(pos) - xcount] = "#"
                    else:
                        y[int(pos) - xcount] = "."
                xcount += 1
            for x in range(int(pos), len(paper[0])):
                for y in paper:
                    y.pop()
    else:
        x, y = line.split(",")
        paper[int(y)][int(x)] = "#"

for y in paper:
    for x in y:
        if x == "#":
            numberOfHashes += 1

print(paper)
print("Number of Hashes: {};".format(numberOfHashes))