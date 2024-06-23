def zeller(year, month, day=1):
    if month < 3:
        month += 12
        year -= 1

    h = (day + 2*month + 3*(month+1)//5 + year + year//4 - year//100 + year//400) % 7

    return h

def print_month(year, month):
    # 檢查年份是否是閏年
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap_year = True
    else:
        leap_year = False

    # 決定每個月有多少天
    if month in [4, 6, 9, 11]:
        days = 30
    elif month == 2:
        if leap_year:
            days = 29
        else:
            days = 28
    else:
        days = 31

    # 計算該月的第一天是星期幾
    first_day = zeller(year, month)

    # 輸出日曆
    print("Mon Tue Wed Thu Fri Sat Sun")
    print("    " * first_day, end="")
    for i in range(1, days + 1):
        print(f"{i:3}", end=" ")
        if (i + first_day) % 7 == 0:
            print()

# 讓使用者輸入年份和月份
year = int(input("Please input the year: "))
month = int(input("Please input the month: "))

print_month(year, month)