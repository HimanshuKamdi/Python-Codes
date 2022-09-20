x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
output = [];
abc = [];
for X in range(x+1):
    for Y in range(y+1):
        for Z in range(z+1):
            if X+Y+Z != n:
                abc = [X,Y,Z];
                output.append(abc);
print(output);

#One liner

print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))