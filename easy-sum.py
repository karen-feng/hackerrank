def easysum(N,m):
    if N<m:
        return (N*(N+1))/2
    if N==m:
        return (N*(N-1))/2
    else:
        n = N/m
        rem = N%m
        return (n*m*(m-1))/2 + ((rem+1)*rem)/2

a = int(raw_input())

l=[]
for i in range(0,a):
    b = map(int, raw_input().strip().split(" "))
    l.append(b)

for x in l:
    print easysum(x[0],x[1])
