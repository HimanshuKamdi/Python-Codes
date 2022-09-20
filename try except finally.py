# for i in range(int(input())):
#     try:
#         a,b=map(int,input().split())
#         print(a//b)
#     except Exception as e:
#         print("Error Code:",e)
#     finally:
#         print("code run succesfully")

rsc="RSC"
try: #try requires a excepr of finally after it
    print(int(rsc),end="")
    print(rsc,end="")
except:
    print("RSC1",end="")
else:  #requires a another function i.e try , if before it
    print("RSC2",end="")

finally: 
    print("RSC3",end="")