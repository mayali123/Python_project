def isOdd(num):
    if num % 2:
        return True
    else:
        return False

def isNum(st):
    try:
        eval(st)
        return True
    except:
        return False
from datetime import datetime
def main():
    now_time = datetime.now()
    now_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
    print(now_time)
    st = input("请输入：")
    print("{}".format(isNum(st)))
    st1 = input("请输入：")
    print("{}".format(isOdd(int(st1))))

if  __name__ == "__main__":
    main()
