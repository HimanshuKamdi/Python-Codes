n=int(input("Enter a number"))

l1=list(map(chr,range(97,123)))
x=l1[n-1::-1]+l1[1:n]
m=len('-'.join(x))
for i in range(1,n):
    print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))
print('-'.join(x))
for i in range(n,0,-2):
    print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))

