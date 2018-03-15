import random
import time
f = open("shakespeare.txt","r")
r = open("shuffled.txt","a+")

def shuffle(s):
    import random
    l = s.split(" ")
    m = []
    for i in range(0,len(l)):
        x = random.randint(0,len(l)-1)
        y = l.pop(x)
        m.append(y)
    return m

randlist = shuffle(f.read())
for i in randlist:
    r.write(i)
print ("done")
f.close()
r.close()
