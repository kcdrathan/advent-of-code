# Day 01 (a)
res = 0
while (True):
    try:
        tres = ''
        s1 = input()
        s2 = s1[::-1]
        for i in s1:
            if i.isdigit():
                tres += i
                break
        for j in s2:
            if j.isdigit():
                tres += j
                break
        print(tres)
        res += int(tres)
    except:
        break
print(res)


# Day 01 (b)
dwords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

ep1 = {
    'one': 0,
    'two': 0,
    'thr': 2,
    'fou': 1,
    'fiv': 1,
    'six': 0,
    'sev': 2,
    'eig': 2,
    'nin': 1
}

ep2 = {
    'eno': 0,
    'owt': 0,
    'eer': 2,
    'ruo': 1,
    'evi': 1,
    'xis': 0,
    'nev': 2,
    'thg': 2,
    'eni': 1
}

def reverse(s):
    s = s[::-1]
    return s

res = 0
while (True):
    try:
        tres = ''
        w = 3
        s1 = input()
        for i in range(len(s1)):
            if s1[i].isdigit():
                tres += s1[i]
                break
            else:
                # print(s1[i:i+w])
                if s1[i:i+w] in ep1:
                    if s1[i:i+w+ep1[s1[i:i+w]]] in dwords:
                        tres += str(dwords.index(s1[i:i+w+ep1[s1[i:i+w]]])+1)
                        break
        s2 = s1[::-1]
        # print(s2)
        for j in range(len(s2)):
            if s2[j].isdigit():
                tres += s2[j]
                break
            else:
                # print(s2[j:j+w])
                if s2[j:j+w] in ep2:
                    if reverse(s2[j:j+w+ep2[s2[j:j+w]]]) in dwords:
                        tres += str(dwords.index(reverse(s2[j:j+w+ep2[s2[j:j+w]]]))+1)
                        break
        print(tres)
        res += int(tres)
    except Exception as e:
        # print(e)
        break
print(res)

