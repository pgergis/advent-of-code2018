def parseLine(line):
    # line: claim-formatted input string
        # input line looks like: "#nnn @ x,y: WxH"
    # returns: claim dictionary
        # claim = {id: #123, start: (x,y), width: w, height: h}

    parts = line.split()
    id = int(parts[0][1:])
    start = tuple(map(int, parts[2][:-1].split(',')))
    height, width = tuple(map(int, parts[3].split('x')))
    return {'id': id, 'start': start, 'height': height, 'width': width}

def processClaim(claim, fabric):
    # overall fabric is 1000x1000 array
    # unclaimed marked by '.', claimed by 1 '#ID', claimed by more 'x'
    # claim starts at array position [x][y] and marks next w in row for h columns
        # claim = {id: #123, start: (x,y), width: w, height: h}

    startX, startY = claim['start']
    for row in range(startX,startX+claim['height']):
        for column in range(startY,startY+claim['width']):
            if fabric[row][column] == '.':
                fabric[row][column] = claim['id']
            else:
                fabric[row][column] = 'x'
    return fabric

def getWholeClaims(claims, fabric):
    whole = []
    for claim in claims:
        occurrences = sum(row.count(claim['id']) for row in fabric)
        if occurrences == claim['width']*claim['height']:
            whole.append(claim['id'])
    return whole

if __name__ == '__main__':
    claims = []
    with open("../inputs/03-input", 'r') as f:
        for line in f:
            claims.append(parseLine(line))

    fabric = [['.' for x in range(1000)] for y in range(1000)]
    for entry in claims:
        fabric = processClaim(entry, fabric)

    overlaps = 0
    for row in fabric:
        for column in row:
            if column == 'x':
                overlaps += 1

    print("overlaps:", overlaps)
    print('claims with no overlaps:', getWholeClaims(claims, fabric))
