from collections import Counter

def getChecksum(boxIDs):
    twos = 0
    threes = 0
    for box in boxIDs:
        counts = list(Counter(list(box)).values())
        if 3 in counts:
            threes += 1
        if 2 in counts:
            twos += 1
    return twos * threes

def strDiff(str1, str2):
    diff = 0
    common = []
    for a,b in zip(str1,str2):
        if a != b:
            diff += 1
        else:
            common.append(a)
    diff += abs(len(str1)-len(str2))
    return diff, ''.join(common)

def findSimilar(boxIDs):
    for i in range(len(boxIDs)-1):
        for j in range(1,len(boxIDs[i:])):
            diff, common = strDiff(boxIDs[i], boxIDs[i+j])
            if  diff == 1:
                return common
    return "none are similar"

if __name__ == '__main__':
    boxIDs = []
    with open("inputs/02-input", 'r') as f:
        for line in f:
            boxIDs.append(line)
    print("checksum", getChecksum(boxIDs))
    print("common in similar", findSimilar(boxIDs))
