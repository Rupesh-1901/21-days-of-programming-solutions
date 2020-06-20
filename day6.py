def frequency_calculator(x):
    freq = dict()   
    while(x):       
        unit_dig = x%10    
        if (unit_dig in freq):    
            freq[unit_dig] = (freq[unit_dig] + 1) 
        else:
            freq[unit_dig] = 1    
        x = int(x/10)
    print(freq)
x=int(input("enter the number: "))   
frequency_calculator(x)
 
 
