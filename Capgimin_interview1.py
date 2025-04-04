Input = "abcd"
output = "aabbccdd"
list1=[]
b=""
for i in range(len(Input)):
    a=Input[i]+Input[i]
    b+=a
print(b)