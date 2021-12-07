inputFile = open('sample.txt', 'r')
lines = inputFile.read().splitlines()

NUMOFDAYS = 256
lanternFish = []

for fish in lines[0].split(","):
    lanternFish.append(int(fish))

#print("Initial state: {};".format(lanternFish))

for day in range(NUMOFDAYS):
    lanternFishTemp = lanternFish.copy()
    for index, fish in enumerate(lanternFishTemp):
        if fish == 0:
            fish = 6
            lanternFish.append(8)
        else:
            fish -= 1
        lanternFish[index] = fish
    #print("After {} days: {};".format(day + 1, lanternFish))

print("Count of Lantern Fish after {} days: {};".format(NUMOFDAYS, len(lanternFish)))