print((("+---" * 7) + "+\n" + ("|   " * 7) + "|\n") * 6 + ("+---" * 7) + "+") #畫表格
print("  0   1   2   3   4   5   6")

x = True
done = False
ra = [0, 1, 2, 3, 4, 5, 6]
col = [[" " for i in range(6)] for j in range(7)] #創造一個空的二維陣列
while not done:	
	if x:
		column = input("Player X >>") #x的回合
	else:
		column = input("Player O >>") #y的回合
	if column.isdigit():
		column = int(column)
		if column not in rang: #沒有在範圍裏面
			print("\nOut of range, try again [0-6].\n")
			continue
		elif " " not in col[column]: #那行滿了
			print("\nThis column is full. Try another column.\n")
			continue
	else: #不是輸數字
		print("\nInvalid input, try again [0-6].\n")
		continue
	if x:
		col[column][col[column].index(" ")] = ("X")
	else:
		col[column][col[column].index(" ")] = ("O")
	x = not x
	for i in range(6):
		print(("+---" * 7) + "+")
		for j in range(7):
			print("| " + col[j][5-i] + " ", end="")
		print("|")
	print(("+---" * 7) + "+")
	print("  0   1   2   3   4   5   6")
	for i in range(7):#檢查橫的
		for j in range(3):
			if col[i][j] == col[i][j+1] == col[i][j+2] == col[i][j+3] == "X":
				print("Winner: X")
				done = True
			elif col[i][j] == col[i][j+1] == col[i][j+2] == col[i][j+3] == "O":
				print("Winner: O")
				done = True
	for j in range(6):#檢查直的
		for i in range(4):
			if col[i][j] == col[i+1][j] == col[i+2][j] == col[i+3][j] == "X":
				print("Winner: X")
				done = True
			elif col[i][j] == col[i+1][j] == col[i+2][j] == col[i+3][j] == "O":
				print("Winner: O")
				done = True
	for i in range(0, 4):#檢查斜的
		for j in range(0, 3):
			if col[i][j] == col[i+1][j+1] == col[i+2][j+2] == col[i+3][j+3] =="X":
				print("Winner: X")
				done = True
			elif col[i][j] == col[i+1][j+1] == col[i+2][j+2] == col[i+3][j+3] =="O":
				print("Winner: O")
				done = True
	for i in range(3, 7):
		for j in range(0, 3):
			if col[i][j] == col[i-1][j+1] == col[i-2][j+2] == col[i-3][j+3] =="X":
				print("Winner: X")
				done = True
			elif col[i][j] == col[i-1][j+1] == col[i-2][j+2] == col[i-3][j+3] =="O":
				print("Winner: O")
				done = True
	draw = True			
	for i in range(7):#平手
		for j in range(6):
			if " " in col[i][j]:
				draw = False
				break
	if draw == True:
		print("Draw")
		done = True
