thickness = 1
c='T'

# for i in range(0,thickness*2,2):
#     print((c*i).rjust(thickness*2)+c)
#     # if i>=6:
#     #     print((c*thickness).ljust(thickness*6))
    
# for i in range(thickness*2+1,0,-2):
#     print((c*i).rjust(thickness*2+1))


for i in range(thickness):
    print(c*(thickness*10))
for i in range(thickness*5):
    print((c*(thickness*2)).center(thickness*10)) 
# for i in range(thickness,0,-1):
    
#         # for j in range(0,n-i):
#         #     print(' '.end=' ')
#     for j in range(thickness+2,0,-1):
#         print('T'.center(thickness*10),end=' ')
#     print()
for i in range(thickness,0,-1):
    print(((c*(thickness-i)).rjust(thickness)+c+(c*(thickness-i)).ljust(thickness)).center(thickness*10))
