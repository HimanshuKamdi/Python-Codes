from itertools import combinations
from itertools import combinations_with_replacement
a,n=input().split()

l=int(n)

# for i in range (1,l+1):
#     for j in combinations(sorted(a),i):
#         print(''.join(j))

for j in combinations(sorted(a),l):
        print(''.join(j))

for j in combinations_with_replacement(sorted(a),l):
        print(''.join(j))