from segments import Segment


tup = [(111,222),(333,444),(333,444)]

stopscreens = {}
for t in tup:
    stopscreens.setdefault(t, Segment())
    stopscreens[t][None:None]=True


tes = [(111,222),(333,'444'),(333,444),(111,111)]

for te in tes:
    mc = stopscreens.get(te, Segment())
    print(mc[2017])
    if mc[1]:
        print('te',mc[1])
