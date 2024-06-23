n=int(input("The Total number of students:"))
list=[]
for i in range(1,n+1):
    list.append(i)


index = 0
while len(list) > 1:
    index = (index + 2) % len(list)  # 跳過每三個學生

    list.pop(index)


# 最後留下的學生就是列表中唯一剩餘的學生
print("The last ID is:",list[0])