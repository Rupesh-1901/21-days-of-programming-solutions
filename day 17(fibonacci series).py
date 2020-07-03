def fibo(a,b,n):
   if n>0:
       print(a+b)
       fibo(b,a+b,n-1)  

n = int(input("Enter number of terms: "))
a=int(input("please enter the 1st positive integer:"))
b=int(input("plese enter the 2nd positive integer:"))
if n <= 0:  
   print("Please enter a positive integer")
else:  
   print("Fibonacci sequence:")  
   print(a)
   print(b)
   fibo(a,b,n-2)  
 

