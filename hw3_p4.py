n = list(map(int,input('Enter index x, y, k (seperated by whitespace):').split(" "))) #把它變成數字的串列
x, y, k = n[0], n[1], n[2]
matrix = []

def color(x): #定義函式
    now = []
    for i in x: #跑它的上下左右，一樣的話放進串列
        if i[0]+1 < len(new) and i[1] < len(new):
            if new[i[0]+1][i[1]] == target:
                new[i[0]+1][i[1]] = k
                now.append([i[0]+1,i[1]])

        if i[0] < len(new) and i[1]+1 < len(new):
            if new[i[0]][i[1]+1] == target:
                new[i[0]][i[1]+1] = k
                now.append([i[0],i[1]+1])
                
        if i[0]-1 < len(new) and i[1] < len(new):
            if new[i[0]-1][i[1]] == target:
                new[i[0]-1][i[1]] = k
                now.append([i[0]-1,i[1]])
                
        if i[0] < len(new) and i[1]-1 < len(new):
            if new[i[0]][i[1]-1] == target:
                new[i[0]][i[1]-1] = k
                now.append([i[0],i[1]-1])
    if len(now) == 0: #找不到一樣的時候跳出迴圈
        return 0
    else:
        return  color(now)


print("Enter the matrix by multiple lines")
while True: #讓它可以一次輸入很多行
    n = input()
    if n == 'q': #輸入q的時候跳出迴圈
        break
    else:
        matrix.append(n)
new = [] 
for i in matrix:
    a = list(map(int,i.split(" "))) #把它變成數字的串列
    new.append(a)
first = [[int(x),int(y)]] #製造初始位置的串列
target = new[x][y] #一開始的位置
new[x][y] = k
color(first) #用上面的函式
for i in new: #全部跑一次
    for j in i:
        print(j,end = " ")
    print() #換行