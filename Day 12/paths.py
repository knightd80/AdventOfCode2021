inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

tunnels = {}
paths = []
countOfPaths = 0

for line in lines:
    src, dst = line.split("-")
    if src in tunnels:
        if dst not in tunnels[src]:
            tunnels[src].append(dst)
    else:
        tunnels[src] = [dst]
    if dst in tunnels:
        if src not in tunnels[dst]:
            tunnels[dst].append(src)
    else:
        if dst != "end":
            tunnels[dst] = [src]

# Need to traverse paths from start to end
for cave in tunnels["start"]:
    paths.append(["start", cave])

all_paths_tested = False
while not all_paths_tested:
    all_paths_tested = True
    temp_paths = []
    for path in paths:
        if path[len(path)-1] != "end":
            all_paths_tested = False
            for cave in tunnels[path[len(path)-1]]:
                temp_path = path.copy()
                if (cave.islower() and cave not in path) or cave.isupper():
                    temp_path.append(cave)
                    temp_paths.append(temp_path)
        else:
            temp_paths.append(path)
                
    paths = temp_paths.copy()

print("Count of Paths: {};".format(len(paths)))