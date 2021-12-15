inputFile = open('sample.txt', 'r')
lines = inputFile.read().splitlines()

STEPS = 40
polymer = ""
polymerpairs = []

def getPolymerCharacterCount():
    polymerCharCount = {}
    mostCommon = 0
    leastCommon = 999999999
    for char in polymer:
        if char in polymerCharCount:
            polymerCharCount[char] += 1
        else:
            polymerCharCount[char] = 1
    print(polymerCharCount)
    for key in polymerCharCount:
        if int(polymerCharCount[key]) > mostCommon:
            mostCommon = int(polymerCharCount[key])
        if int(polymerCharCount[key]) < leastCommon:
            leastCommon = int(polymerCharCount[key])
    return mostCommon - leastCommon

for line in lines:
    if "->" in line:
        polymerpairs.append(line)
    elif len(line) > 0:
        polymer = line

#print("Initial Polymer: {};".format(polymer))
for step in range(STEPS):
    temppolymer = "o".join(polymer[i:i+1] for i in range(0,len(polymer))) + "o"
    paircount = {}
    for polymerpair in polymerpairs:
        pair, insert = polymerpair.split(" -> ")
        if pair in polymer:
            if pair in paircount:
                paircount[pair] += polymer.count(pair)
            else:
                paircount[pair] = polymer.count(pair)
            #print("pair: {};".format(pair))
            pair2 = pair[:1] + "o" + pair[1:] + "o"
            triple = pair[:1] + "o" + insert + "n" + pair[1:] + "o"
            #print("triple: {};".format(triple))
            replacedall = False
            while not replacedall:
                polymerLength = len(temppolymer)
                temppolymer = temppolymer.replace(pair2, triple)
                if (len(temppolymer) - polymerLength) == 0:
                    replacedall = True
    polymer = temppolymer.replace("o", "").replace("n", "")
    #print(polymer)
    #print(paircount)
    #print("After Step {}: {};".format(step+1, polymer))
    print("After Step {}: Polymer most common - least common = {};".format(step+1, getPolymerCharacterCount()))

print("Polymer most common - least common: {};".format(getPolymerCharacterCount()))