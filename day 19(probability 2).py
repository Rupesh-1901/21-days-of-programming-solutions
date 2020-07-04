import random
def probability(a,b):
    i=random.randint(a,b+1)
    for x in range(n):
        count=0
        for i in range(a,b+1):
            j=1
            while j*j<=i:
                if j*j==i:
                    count=count+1
                j=j+1
        
    total=b-a+1
    probability=count/total
    print(probability)
    
L = int(input("enter the lower range: "))
U = int(input("enter the upper range: "))
n=  int(input("enter the number of iterations: "))
probability(L,U)
