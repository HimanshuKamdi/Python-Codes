# #crown
# thickness=7
# c='*'
# for i in range(thickness):
#     print((c*i).ljust(thickness-1)+c+(c*i).rjust(thickness-1))

# def func(n):
#     def func1():
#         return "edureka"
#     def func2():
#         return "Python"    
#     if n==1:
#         return func1
#     else: 
#         return func2
# a= func(1)
# b=func(2)
# print(a()) 
# print(b())

# import re
# a='d'
# n=input()
# m=re.compile(n)
# b=m.search(a)
# print(b)

# arr=[1,1,1,2,2,3]
# s=set(arr)
# max=0
# a=0
# for i in s:
#     if arr.count(i)>max and a<i:
#         max=arr.count(i)
#         a=i
#         print(a)
# print(a) 
# l=[1,2,3,4]
# m=[2,1]
# print(set(l)-set(m))
# print(sorted(l)==sorted(m))

# def recur(n):
#     if n<=1:
#         return n
#     else:
#         return(recur(n-1)+recur(n-2))
# n=10
# for i in range(n):
#     print(recur(i))

# name1=["M","B",",C"]
# name2=name1
# name3=name1[:]
# # print(name1)
# # print(name2)
# # print(name3)
# # name2[0]="Orange"
# # name3[1]="Grapes"
# # print(name1)
# # print(name2)
# # print(name3)
# # sum=0
# # for ls in (name1,name2,name3):
# #     print(ls)


# # print('a'<'A')
# # a="s"
# # b="c"
# # print(b is a)
# # print(b == a)
# # print(id(a))
# # print(id(b))
# # print(2%1)

# def repeatedSubstringPattern( s: str) -> bool:
#   for i in range(len(s)//2+1,0,-1):
#     if len(s)%i==0:
#       c=s.count(s[0:i])
#       print(c)
#       if len(s)//i-1==c:
#         return True
#   return False
# # def repeatedSubstringPattern( s) :
# #   for i in range(1,len(s)//2+1):
# #     j=0
# #     c=0
# #     if len(s)%i==0:
# #     #   ans=all(s[j:j+i]==s[j+i:j+i+i] for j in range(0,len(s)-i-i,i) )
# #     # if ans:
# #     #   return True
# #       for j in range(0,len(s)-i-i+1,i):
        
# #         if s[j:j+i]==s[j+i:j+i+i] :
# #           c+=1
# #         else:
# #           break
# #       if len(s)//i-1==c:
# #         return True
# #   return False

# print(repeatedSubstringPattern('abab'))

# def threeSum( nums) :
#   l1=[]
#   for i in range(len(nums)-2):
#     if nums[i]!=nums[i+1] and nums[i]!=nums[i+2] and [nums[i],nums[i+1],nums[i+2]] not in l1:
#       l1.append([nums[i],nums[i+1],nums[i+2]])
#   return l1
# print(threeSum([-1,0,1,2,-1,-4]))

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(intervals(0))