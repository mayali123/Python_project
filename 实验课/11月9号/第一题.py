def is_leap(year):
    if (year%4==0 and year%100!=0)or (year%100==0 and year%400 != 0):
        return True
    return False
year=int(input("请输入一个年份:"))
if is_leap(year):
    print("{}是一个闰年".format(year))
else:
    print("{}不是一个闰年".format(year))
