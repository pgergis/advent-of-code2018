def preProcessPolymer(letter, s):
    s = list(s)
    i = 0
    while i < len(s):
        if s[i].lower() == letter:
            del(s[i])
        else:
            i += 1
    return ''.join(s)

def processPolymer(s):
    s = list(s)
    i = 0
    while i < len(s)-1:
        if abs(ord(s[i+1]) - ord(s[i])) == 32:
            del(s[i+1])
            del(s[i])
            if i > 2:
                i -= 2
            else:
                i = 0
        else:
            i += 1
    return ''.join(s)

f = None
with open('input.txt', 'r') as fileIn:
    f = fileIn.read().rstrip()

# part 1
print(len(processPolymer(f)))

# part 2
print(min([len(res) for res in [processPolymer(s) for s in [preProcessPolymer(l,f) for l in set(f.lower())]]]))
