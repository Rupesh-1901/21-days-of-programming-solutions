n=int(input("Enter total numbers in the gp series: "))
a=int(input("Enter first term of the series: "))
r=int(input("Enetr common ratio of the series: "))
print("the geometric series is\n")
print(a)
next_term=1
prev_term=1
temp=a
sum=0
for i in range(n):
    prev_term=temp
    next_term=prev_term*r
    print(next_term)
    temp=next_term
    sum+=temp
    
print(sum+a)    
      
      
