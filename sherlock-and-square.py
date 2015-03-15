import math

def sherlock(n):
    return (pow(2,n+1,(pow(10,9)+7))+ 2)%(pow(10,9)+7)

a = int(raw_input())

l=[]
for i in range(0,a):
    b = input()
    l.append(b)


for x in l:
    print sherlock(x)
