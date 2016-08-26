#!/usr/bin/python3.4
#HW1Q1.py
#Python 3.4 
#Ice bucket challenge stat calculator

print("#icebucketchallenge vs #alsicebucketchallenge, percentage change")

#The two lists
icebucketchallenge = [200, 500, 2000, 12000, 24000, 65000, 70000]
alsicebucketchallenge = [100, 300, 1500, 13000, 25000, 105000, 85000]


def topz(sweg):
    memes = len(sweg)
    x= 0
    putz = []
    while (memes-1) > x:
        y = x + 1
        noob = ((((sweg[y] - sweg[x]) / sweg[x])) * 100)
        x += 1
        #print(x)
        putz.append(round(noob))
    return putz

ice=topz(icebucketchallenge)

als=topz(alsicebucketchallenge)
memdfasd=len(icebucketchallenge) -1

for x in range(0, memdfasd):
    print(ice[x], "vs", als[x])


#Numbers are a bit off because I'm using python 3 for this. I could print out the exact value by removing the round() but I like the integers.
