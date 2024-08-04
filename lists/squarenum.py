num=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]

for i in num:
    sq=i*i

    if sq%2==0:
        even.append(sq)
    else:
        odd.append(sq)

print(even)
print(odd)