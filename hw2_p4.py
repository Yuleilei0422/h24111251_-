def print_tree(numberoflayer, lengthoftop, growthoflayer, trunkwidth, trunkheight):
    # 三角形部分
    bottom_length = lengthoftop + (numberoflayer - 1) * growthoflayer  # 底層三角形的邊長
    print(" "*(int(bottom_length))+"#")
    for i in range(numberoflayer):
        length = lengthoftop + i * growthoflayer
        for j in range(1,length):
            if j == length - 1:  # 最後一行只印'#'
                print(' ' * (bottom_length - j) + '#'*(2*j+1))
            else:  
                print(' ' * (bottom_length - j) + '#' + '@' * ((2 * j)-1) + '#')  # 在每一行的開頭添加額外的空格
    # 計算底層三角形寬度
    bottom_width = 2 * (lengthoftop + (numberoflayer - 1) * growthoflayer) - 1

    # 樹幹
    for i in range(trunkheight):
        print(' ' * ((bottom_width - trunkwidth) // 2+1) + '|' * trunkwidth)

numberoflayer = int(input("Please input the number of layers:(2-5)"))
lengthoftop = int(input("Please input the length of the top layer:"))
growthoflayer = int(input("Please input the growth of each layer:"))
trunkwidth = int(input("Please input the width of the trunk(odd number 3 to 9):"))
trunkheight = int(input("Please input the height of the trunk(4 to 10):"))

print_tree(numberoflayer, lengthoftop, growthoflayer, trunkwidth, trunkheight)