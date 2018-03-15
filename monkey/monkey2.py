#this one generates a random number corresponding to an ASCII character, checks it against the first character of shakespeare,
#and if they match, adds it to a text file. it then moves onto the next character, and does the same again until done.
import random
f = open('shakespeare.txt','r')
def ranChr():
  "generate a random 8bit character, simulates the monkey's keypress."
  x = random.randint(0,255)
  x = chr(x)
  return x

def check(s,r):
  "checks against text to see if the monkey has typed a bit of shakespeare"
  if s == r:
    return True
  return False


for i in f.read():
  a = open("copy.txt",'a+')
  t = False
  while T == False:
    r = ranChr()
    t = check(i,r)
  a.write(r)
print("done")
f.close()
a.close()
