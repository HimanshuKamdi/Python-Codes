import re
for _ in range(int(input())):
    print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)  
pattern=r'^[+-]?[0-9]*\.[0-9]+$'
for i in range(int(input())):
    s=input()     
    print(bool(re.match(pattern,s)))