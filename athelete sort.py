def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

# cars.sort(key=myFunc)
# print(cars)
cars.sort(reverse=True)
print(cars)





import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())

    # Athlete Sort in python - Hacker Rank Solution START   
    arr.sort(key = lambda x : x[k])
    for i in arr:
        print(*i,sep=' ')
    # Athlete Sort in python - Hacker Rank Solution END


