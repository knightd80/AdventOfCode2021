from math import floor

inputFile = open('sample.txt', 'r')
lines = inputFile.read().splitlines()

def fishProduced(countOfDays, totalFish):
    if countOfDays < 0:
        print(totalFish)
        return totalFish
    else:
        totalFish += floor((countOfDays) / 6)
        return fishProduced(countOfDays - 7, totalFish)

NUMOFDAYS = 18
lanternFish = []
lanternFishCount = 0

for fish in lines[0].split(","):
    lanternFish.append(int(fish))

for index, fish in enumerate(lanternFish):
    for day in range(NUMOFDAYS):
        if fish == 0:
            print("day: {}; index: {};".format(day, index))
            for remainingDays in range(NUMOFDAYS - day, 0, -7):
                lanternFishCount += fishProduced(remainingDays - 1, 0)
            lanternFishCount += 1
            break
        else:
            fish -= 1
        lanternFish[index] = fish
print(lanternFish)

print("Count of Lantern Fish after {} days: {};".format(NUMOFDAYS, lanternFishCount))