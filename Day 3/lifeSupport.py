inputFile = open('input.txt', 'r')
lines = inputFile.read().splitlines()

onCount = 0
offCount = 0
oxygenRating = []
scrubberRating = []

def get_on_off_counts(ratingList, position):
    offCount = 0
    onCount = 0
    for rating in ratingList:
        items = list(rating)
        if int(items[position]) == 0:
            offCount += 1
        if int(items[position]) == 1:
            onCount += 1
    return onCount, offCount

for line in lines:
    oxygenRating.append(line)
    scrubberRating.append(line)

position = 0
while len(oxygenRating) > 1:
    onCount, offCount = get_on_off_counts(oxygenRating, position)
    
    maxCount = 0 if offCount > onCount else 1

    tempRating = []
    for rating in oxygenRating:
        # Do work to remove items from list
        if int(rating[position]) == maxCount:
            tempRating.append(rating)
        oxygenRating = tempRating.copy()

    # Reset onCount and offCount to 0 and increment position indicator
    onCount = 0
    offCount = 0
    position += 1

position = 0
while len(scrubberRating) > 1:
    onCount, offCount = get_on_off_counts(scrubberRating, position)
    
    minCount = 1 if onCount < offCount else 0

    tempRating = []
    for rating in scrubberRating:
        # Do work to remove items from list
        if int(rating[position]) == minCount:
            tempRating.append(rating)
        scrubberRating = tempRating.copy()

    # Reset onCount and offCount to 0 and increment position indicator
    onCount = 0
    offCount = 0
    position += 1
    
print("Oxygen Rating: {}; CO2 Scrubber Rating: {}; Life Support Rating: {};".format(int(oxygenRating[0],2), int(scrubberRating[0],2), int(oxygenRating[0],2) * int(scrubberRating[0],2)))