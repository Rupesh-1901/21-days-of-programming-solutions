
test_str =str(input("enter the string: "))
n=str(input("enter the string to be replaced: "))
i=str(input("enter the string to be replaced with: "))
 
print("The original string is : " + test_str) 

temp = str.maketrans(n,i) 
test_str = test_str.translate(temp) 


print("The new string is : " + str(test_str)) 
