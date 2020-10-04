# -*- coding: UTF-8 -*-
# @Time :  20:03
# @Author :麻亚利
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup   # 提取
import re           # 正则表达式
import urllib.request, urllib.error
import xlwt

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 解决 不能输出 utf-8


def main():
    url = "https://maoyan.com/board/7"
    ls = getData(url)
    save_path = '猫眼数据.xls'
    save(ls, save_path)


# 电影排名
movie_num = re.compile('<i class="board-index board-index-(.*?)">')
# 电影名字
movie_name = re.compile('title="(.*?)"')
# 电影的照片
movie_img = re.compile('data-src="(.*?)"')
# 上映时间
movie_time = re.compile('<p class="releasetime">(.*?)</p>')
# 电影主要演员
movie_star = re.compile('<p class="star">(.*?)</p>', re.S)
# 评分
movie_rating = re.compile('<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>')

info = ("电影排名", "电影名字", "电影的照片", "上映时间", "电影主要演员", "评分")


def getData(url):
    datalist = []
    html = askUrl(url)
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all("dd"):
        data = []
        item = str(item)

        # 电影排名
        num = re.findall(movie_num, item)[0]
        data.append(num)

        # 电影名字
        name = re.findall(movie_name, item)[0]
        data.append(name)

        # 电影的照片
        img = re.findall(movie_img, item)[0]
        data.append(img)

        # 上映时间
        time = re.findall(movie_time, item)[0]
        time = time.replace("上映时间：", "")    # 去掉 上映时间 的字样
        data.append(time)

        # 电影主要演员
        star = re.findall(movie_star, item)[0]
        star = star.strip()
        data.append(star)

        # 评分
        rating= re.findall(movie_rating, item)[0]
        data.append(int(rating[0][:-1])+int(rating[1])/10)

        datalist.append(data)
    return  datalist


def askUrl(url):
    head = {
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) "+\
        "Chrome / 85.0.4183.121 Safari / 537.36 Edg / 85.0.564.68"
    }
    req = urllib.request.Request(url, headers=head)
    recv = urllib.request.urlopen(req)
    html = recv.read().decode("utf-8")
    return html


def save(list, save_path):
    workbook = xlwt.Workbook(encoding='utf', style_compression=0)
    sheet1 = workbook.add_sheet("热门口碑")
    for i in range(len(info)):
        sheet1.write(0, i, info[i])
    for i in range(len(list)):
        for j in range(len(list[0])):
            sheet1.write(i+1, j, list[i][j])
    workbook.save(save_path)


if __name__ == "__main__":
    main()
