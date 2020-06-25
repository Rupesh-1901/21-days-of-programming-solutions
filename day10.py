def swapList(lst): 
	size = len(lst) 
	
	 
	temp = lst[0] 
	lst[0] = lst[size - 1] 
	lst[size - 1] = temp 
	
	return lst 

lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
	element = int(input()) 

	lst.append(element) 
	
print(lst)
print(swapList(lst)) 


