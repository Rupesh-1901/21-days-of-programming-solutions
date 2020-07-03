a=int(input("enter the divident: "))
b=int(input("enter the divisor: "))
steps=0
if(a%b==0):
    steps=0
    print(steps)
else:
      q, mod = divmod(a, b)
      a1=(q+1)*b
      #print(a1)
      mod1=a1-a
      #print(mod1)
      if(mod1>mod):
               for i in range(0, mod):
                             steps=steps+1
                            
               print("the least amount of steps needed is :")
               print(steps)

      elif(mod>mod1):
               for i in range(0, mod1):
                             steps=steps+1
    
               print("the least amount of steps needed is: ")
               print(steps)
          
      elif(mod==mod1):
               for i in range(0, mod1):
                             steps=steps+1
    
               print("the least amount of steps needed is: ")
               print(steps)
