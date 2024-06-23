n=int(input("Please input a number:"))
i=0
while i<=n:
    sum=0
    j=1
    while j<i :
        if i%j==0:
            sum+=j
        j+=1
    if sum==i:
        print("perfect number:",i)
    i+=1