ASCII_SIZE = 256

def getMax(str): 
	
	count = [0] * ASCII_SIZE 

	max = -1
	c = '' 

	for i in str: 
		count[ord(i)]+=1; 

	for i in str: 
		if max < count[ord(i)]: 
			max = count[ord(i)] 
			c = i 

	return c 
 
str = str(input("enter the string to be checked: "))
print ("Max occurring character is " + getMax(str)) 


