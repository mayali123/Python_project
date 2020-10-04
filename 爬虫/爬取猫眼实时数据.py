# -*- coding: UTF-8 -*-
# @Time :  9:18
# @Author :mayali123
# @File : 尝试爬猫眼.py
# @Software : PyCharm

import urllib.request, urllib.error
import xlwt
import  json

def main():
    url = 'http://piaofang.maoyan.com/dashboard-ajax/movie?orderType=0&uuid=174f0a73224c8-0556c9a340f0bb-7e647b6e-14f6b5-174f0a73224c8&riskLevel=71&optimusCode=10&_token=eJyNT8sKgkAU%2FZe7HkZHU2cGXAhBGLRIrI24GB%2BphI7oIEX0713BFu2CC%2BfB4XDuC6a4AmkTWOoJJDBqUx8ImBkk820WBJ7DbO4JAuWvJxxOoJiue5BZIBjxuZOvRoI6Y57vEh6InGzURers8NZMjBFojRmlZY2d0jc1NLRX%2BqkGWureqtTcFlpNldXrpatxzj9hwOo%2BxWrE%2B4ZqQ%2FPVJ%2FwR%2B%2BauGZDVx0d6aeIoOjRRcg5DeH8APJNNiw%3D%3D'
    save_path = '猫眼实时数据.xls'
    ls = get_data(url)
    save(ls, save_path)
    # show(ls)

def askUrl(url):
    head = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) "+\
        "Chrome / 85.0.4183.121 Safari / 537.36 Edg / 85.0.564.68"
    }
    req = urllib.request.Request(url, headers=head)
    recv = urllib.request.urlopen(req)
    html = recv.read().decode("utf-8")
    #print(html)
    return html
# 电影名称，上映天数，电影总票房，票房占比，排片场次，排片占比，场均人次，上座率
movie_info = ('movieInfo','sumBoxDesc','boxRate','showCount','showCountRate','avgShowView','avgSeatView')
movie_info2 =('movieName','releaseInfo')
Cmovie_info = ("电影名称","上映天数","电影总票房","票房占比","排片场次","排片占比","场均人次","上座率")
def get_data(url):
    dic = askUrl(url)
    datalist = []
    # 将字符串转 为 字典
    dic = json.loads(dic)
    # print(dic)
    lis = dic.get('movieList').get('list')
    #print(lis)
    for it in lis:
        data = []
        for info in movie_info:
            if info == 'movieInfo':
                for i in movie_info2:
                    data.append(it[info][i])
            else:
                data.append(it[info])
        datalist.append(data)
    return datalist

def save(ls, save_path):
    workbook=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet1 = workbook.add_sheet("猫眼实时数据")
    for i in range(len(Cmovie_info)):
        sheet1.write(0, i, Cmovie_info[i])
    for i in range(len(ls)):
        for j in range(len(ls[0])):
            sheet1.write(i+1, j, ls[i][j])
    workbook.save(save_path)
    print("保存成功！！")

def show(ls):
    for i in range(len(Cmovie_info)):
        print("%s  " % Cmovie_info[i], end=' ')
    print('\n', end='')
    for i in range(len(ls)):
        for j in range(len(ls[0])):
            print("%s  " % ls[i][j], end=' ')
        print('\n', end='')

if __name__ == "__main__":
    main()
