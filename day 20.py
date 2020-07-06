L = [1, 3, 2, 8, 4]
sum = 7

count=0
for i in range(len(L) ):
    if L[i]<=sum:
        count+=1
        
        
for i in range(len(L)-1):
    for j in range(i + 1, len(L)):
        if L[i]+L[j]<=sum:
                count+=1
                
for i in range(len(L )-2):
    for j in range(i+1, len(L)-1):
        for k in range(j+1,len(L)):
            if L[i] + L[j] +L[k]<=sum:
                count+=1
                
print(count)
