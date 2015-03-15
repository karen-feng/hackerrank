import math

a = int(raw_input())

l=[]
for i in range(0,a):
    b = input()
    l.append(b)

for x in l:
    c = x*x
    print c%(pow(10,9)+7)
