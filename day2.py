def pattern(n):
    odd=1
    space=3
    for i in range(1,n):
        k=64
        for j in range(1,space+1):
            print(" ",end="")
        for j in range(1,odd+1):
            if(j<=i):
                k=k+1
            else:
                k=k-1
            ch=chr(k)    
            print(ch,end="")
        print()
        odd=odd+2
        space=space-1
 
n=int(input("enetr the number of rows needed: ")) 
pattern(n)
        
