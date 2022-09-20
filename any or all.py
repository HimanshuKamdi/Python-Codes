# def isPositive(i):
#     if i > 0:
#         return True
#     return False

# def isPalindrome(i):
#     if int(str(i)[::-1]) is i:
#         return True
#     return False

N = int(input())
storage = map(int, input().split())
print(storage)
storage = sorted(storage)
print(storage)

# if all([isPositive(i) for i in storage]):
#     if any([isPalindrome(i) for i in storage]):
#         print("True")
#     else:
#         print("False")
# else:
#     print("False")

# using any or all
# any([1>0,1==0,1<0])   TRue
# any([1<0,2<1,3<2])    false


# N,n = int(input()),input().split()
# print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))