#Day 02 (a)

def set2dict(s):
    #'3 b, 4 r, 6 g'
    gbag = {
        'blue': 0,
        'green': 0,
        'red': 0
    }
    aset = [i.split() for i in s.split(', ')]
    for i in aset:
        gbag[i[1]] = int(i[0])
    return gbag

bag = {
    'blue': 14,
    'green': 13,
    'red': 12
}
pgames = 0
while True:
    try:
        gn, sets = input().split(':')
        gn = gn.split()[1]
        sets = sets.strip().split('; ')
        # print(gn, sets)
        possible = True
        for i in sets:
            gbag = set2dict(i)
            # print(gbag)
            if gbag['blue'] > bag['blue'] or gbag['green'] > bag['green'] or gbag['red'] > bag['red']:
                possible = False
                break
        pgames += int(gn) if possible else 0
        # print(pgames, gn, possible)      
    except:
        break
print(pgames)
  
    
#Day 02 (b)

# def set2dict(s):
#     #'3 b, 4 r, 6 g'
#     gbag = {
#         'blue': 0,
#         'green': 0,
#         'red': 0
#     }
#     aset = [i.split() for i in s.split(', ')]
#     for i in aset:
#         gbag[i[1]] = int(i[0])
#     return gbag

pgames = 0
while True:
    try:
        now = {"red":0, "green":0, "blue":0}
        sets = input().split(':')[1].strip().split('; ')
        pnow = 1
        # print(sets)
        for i in sets:
            minbag = set2dict(i)
            for color in minbag:
                now[color] = max(now[color], minbag[color])
        # print(now)
        for v in now.values():
            pnow *= v
        pgames += pnow
    except:
        break
print(pgames)