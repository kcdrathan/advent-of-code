
# # Day 04 (a)
# res = 0
# while True:
#     try:
#         # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#         wn, n = input().split(':')[1].strip().split('|')
#         wn = wn.strip().split()
#         n = n.strip().split()
#         print(wn, n)
#         wc = 0
#         tres = 0
#         for i in n:
#             if i in wn:
#                 print(i)
#                 wc += 1
#                 if wc == 1:
#                     tres = 1
#                 else:
#                     tres *= 2
#         print('tres: ', tres)
#         res += tres
#     except:
#         break
# print(res)
# print()
        

# Day 04 (b)

def addsc(s):
    ret = 0
    cn = s.split(':')[0].split()[1]
    wn, n = s.split(':')[1].strip().split('|')
    wn = wn.strip().split()
    n = n.strip().split()
    # print(wn, n)
    for i in n:
        if i in wn:
            ret += 1
    return cn, ret

file = open('in.txt', 'r')
res = 0
mdict = {}
x = 0
while x<1:
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    for _ in file:
        cn, nwn = addsc(_)
        mdict[int(cn)] = nwn
    x += 1

    fl = {i: 1 for i in mdict}
    for i in range(1, len(mdict)+1):
        for j in range(i+1, mdict[i]+i+1):
            fl[j] += fl[i]
        # print(fl)
    print(sum(fl.values()))
