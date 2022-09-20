class fun:
    def __init__(self,n) :
        self.n=n
    def __add__(self,x):
        s=self.n*x.n
        return s

        
a=fun(2)
b=fun(3)
x=a+b
print(x)