from itertools import groupby
n=input()
for i,j in groupby(map(int,list(n))):
    print(tuple([len(list(j)), i]) ,end = " ")

#Equivalent To

# S=input()
# i=1
# a=[]
# count=1
# while i<len(S):
#     if S[i]==S[i-1]:
#         count+=1
#         i+=1
#     else:
#         a.append((count,int(S[i-1])))
#         i+=1
#         count=1
# a.append((count,int(S[i-1])))
# for i in a:
#     print(i,end=' ')