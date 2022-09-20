m,n=input().split()
l=[]
for i in range(int(n)):
    l1=list(map(float,input().split()))
    l.append(l1)
print(l)
print(*l)
for _ in zip(*l):
    print(sum(_)/len(_))