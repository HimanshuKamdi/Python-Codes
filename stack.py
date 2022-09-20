n=0
Library=[1,2,3]
def Push(stk,item):
    a=int(input("Enter Book Number"))
    Library.append(a)
    print(Library)

def Pop(Library):
    if Library==[]:
        print("Underflow case.Can't delete ")
    else:
        Library.pop()
        print(Library)

Push(Library,n)
Pop(Library)
    
