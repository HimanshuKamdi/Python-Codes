data=[]
s=[]   
for _ in range(int(input())):
    name = input()
    score = float(input())
    data.append([name,score])
    s.append(score)
m=sorted(set(s))
n=set[1]   
# n = sorted(set([score for name, score in data]))[1]
print('\n'.join(sorted([name for name, score in data if score == n])))