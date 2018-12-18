from collections import Counter

input = "inputs/01-input"

freqTable = Counter([0])
with open(input, 'r') as f:
    freq = 0
    iterations = 0
    while max(list(freqTable.values())) < 2:
        for shift in f:
            op = shift[0]
            val = int(shift[1:])
            if op == '+':
                freq += val
            elif op == '-':
                freq -= val
            else:
                print("Input error!")
                break
            freqTable[freq] += 1
            if freqTable[freq] == 2:
                print(freq, "hit twice!")
                break
        if iterations == 0:
            print("first result:",freq)
        f.seek(0)
        iterations += 1
print("ran {} iterations".format(iterations))
