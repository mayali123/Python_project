sites = ["baidu","Google","Python","Taobao"]
for site in sites:
    if site == "Python":
        print("Python教程！")
        break
    print("循环数据"+site)
else:
    print("没有循环数据！")
print("完成循环！")
