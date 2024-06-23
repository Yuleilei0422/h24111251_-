poly = input("Input polynomial:") # 輸入多項式
x = input("Input the value of X:") # 輸入一個值為x

poly = " ".join(poly)  # 將字符用空格連接
po = poly.split(" ") # 將字符用空格分割

new_po = [] 
str_po = ""
for elem in po:
    if elem.isdigit(): # 若元素是數字字符則添加至此
        str_po += elem
    elif elem == "X": # 若元素是x則將其值轉換為整數並添加至此
        new_po.append(int(x))
    else: # 將str_po中存的數字字符轉換為整數並添加到new_po中
        if str_po:
            new_po.append(int(str_po))
        str_po = "" # 清空
        new_po.append(elem)

if str_po: # 乘法運算
    new_po.append(int(str_po))
if new_po[0] == "-":
    new_po[0] = -1
    new_po.insert(1, "*")

i = 0
while i < len(new_po): # 指數運算
    if new_po[i] == "^":
        new_po[i-1] **= new_po[i+1]
        del new_po[i]
        del new_po[i]
        i -= 1
    i += 1
i = 0
while i < len(new_po): # 加法運算
    if new_po[i] == "*":
        new_po[i-1] *= new_po[i+1]
        del new_po[i]
        del new_po[i]
        i -= 1
    i += 1
i = 0
while i < len(new_po):
    if new_po[i] == "-": # 減法運算
        new_po[i-1] -= new_po[i+1]
        del new_po[i]
        del new_po[i]
        i -= 1
    i += 1
i = 0
while i < len(new_po):
    if new_po[i] == "+":
        new_po[i-1] += new_po[i+1]
        del new_po[i]
        del new_po[i]
        i -= 1
    i += 1
print("Evaluated Result: %d" % new_po[0]) # 輸出

