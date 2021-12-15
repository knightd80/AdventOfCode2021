import numpy as np

inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

caves = []

for line in lines:
    row = []
    row[:] = line
    caves.append(row)

max_val = len(caves)

map=np.ones((max_val,max_val),dtype=int)*np.Infinity
for index, cave in enumerate(caves):
    for index2, x in enumerate(cave):
        map[index,index2] = x

# Use Dijkstra’s algorithm
#Initialize auxiliary arrays
distmap=np.ones((max_val,max_val),dtype=int)*np.Infinity
distmap[0,0]=0
originmap=np.ones((max_val,max_val),dtype=int)*np.nan
visited=np.zeros((max_val,max_val),dtype=bool)
finished = False
x,y=int(0),int(0)
count=0

#Loop Dijkstra until reaching the target cell
while not finished:
    # move to x+1,y
    if x < max_val-1:
        if distmap[x+1,y]>map[x+1,y]+distmap[x,y] and not visited[x+1,y]:
            distmap[x+1,y]=map[x+1,y]+distmap[x,y]
            originmap[x+1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
    # move to x-1,y
    if x>0:
        if distmap[x-1,y]>map[x-1,y]+distmap[x,y] and not visited[x-1,y]:
            distmap[x-1,y]=map[x-1,y]+distmap[x,y]
            originmap[x-1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
    # move to x,y+1
    if y < max_val-1:
        if distmap[x,y+1]>map[x,y+1]+distmap[x,y] and not visited[x,y+1]:
            distmap[x,y+1]=map[x,y+1]+distmap[x,y]
            originmap[x,y+1]=np.ravel_multi_index([x,y], (max_val,max_val))
    # move to x,y-1
    if y>0:
        if distmap[x,y-1]>map[x,y-1]+distmap[x,y] and not visited[x,y-1]:
            distmap[x,y-1]=map[x,y-1]+distmap[x,y]
            originmap[x,y-1]=np.ravel_multi_index([x,y], (max_val,max_val))

    visited[x,y]=True
    dismaptemp=distmap
    dismaptemp[np.where(visited)]=np.Infinity
    # now we find the shortest path so far
    minpost=np.unravel_index(np.argmin(dismaptemp),np.shape(dismaptemp))
    x,y=minpost[0],minpost[1]
    if x==max_val-1 and y==max_val-1:
        finished=True
    count=count+1

print("The path length is: {}".format(distmap[max_val-1,max_val-1]))