binary_num =list(input("Input a binary no. ="))
v=0
for i in range(len(binary_num)):
      d = binary_num.pop()
      if d == '1':
           v= v + pow(2,i)
print(chr(v))
