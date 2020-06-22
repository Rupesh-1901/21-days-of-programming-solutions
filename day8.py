
from array import *
array_num = array('i',[])
n=int(input("number of elements: "))
for x in range(0,n):
    a=int(input("enter element : "))
    array_num.append(a)
    
print("SCORES: "+str(array_num))


for i in range(0, len(array_num)):    
    for j in range(i+1, len(array_num)):    
        if(array_num[i] > array_num[j]):    
            temp = array_num[i]   
            array_num[i] = array_num[j]   
            array_num[j] = temp    
     
print()
    
print("The runners up score is: ");    
print(array_num[-2])
