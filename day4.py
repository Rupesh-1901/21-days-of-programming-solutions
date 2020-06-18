def function():
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    for i in range(a,b+1):
        if i>1:
            for x in range(2,i):
                if (i % x)==0:
                    break
                else:
                    print(i)
                    print("\n")
                    
                    
        else:
            print("try again")
            break
                    
function()
