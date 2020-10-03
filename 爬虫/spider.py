# -*- coding = utf-8 -*-
# @Time :  7:50
# @Author :麻亚利
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup   # 提取
import re           # 正则表达式
import urllib.request, urllib.error
import xlwt
import sqlite3

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 解决 不能输出 utf-8

def main():
    # print('hello')
    url = "https://movie.douban.com/top250?start="
    save_path ="豆瓣电影排名TOP25.xls"
    #
    save(get_data(url), save_path)


# 正则表达式
# 链接
movie_Link = re.compile('<a href="(.*?)">')
# 图片
movie_img = re.compile('<img.*src="(.*?)"', re.S)
# 名字
movie_name = re.compile(r'<span class="title">(.*)</span>')
# 评分
movie_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
movie_num = re.compile(r'<span>(.*)人评价</span>')
# 概况
movie_info = re.compile(r'<span class="inq">(.*?)</span>')
# 信息
movie_bd = re.compile(r'<p class="">(.*?)</p>', re.S)

def ask_url(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/" +
                      "537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63"
    }
    req = urllib.request.Request(url, headers=head)
    receive = urllib.request.urlopen(req)
    html = receive.read().decode("utf-8")
    return html

# 获取数据
def get_data(Baseurl):
    dataList = []
    for i in range(10):
        url = Baseurl + str(i*25)
        html = ask_url(url)
        #  解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            # file = open("豆瓣电影排行榜TOP250.html", "w", encoding="utf-8")
            # file.write(str(item))
            # file.close()
            data = []
            # 链接
            link = re.findall(movie_Link, str(item))[0]
            data.append(link)

            # 图片
            img = re.findall(movie_img,str(item))
            data.append(img)

            # 名字
            name = re.findall(movie_name, str(item))
            if len(name) == 2:
                data.append(name[0])
                data.append(name[1].replace("/", ""))
                # print(data)
            else:
                data.append(name[0])
                data.append(" ")

            # 评分
            rating = re.findall(movie_rating, str(item))[0]
            data.append(rating)

            # 评价人数
            num = re.findall(movie_num, str(item))[0]
            data.append(num)

            # 概况
            info = re.findall(movie_info, str(item))
            if len(info) == 1:
                data.append(info[0])
            else:
                data.append(" ")

            # 信息
            bd = re.findall(movie_bd, str(item))[0]

            data.append(bd.replace("<br/>", "").replace("\n", "").strip())
            dataList.append(data)
    return dataList


def save(dataList,save_path):
    print("save...")
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet("豆瓣电影排名TOP250")
    info = ("链接", "图片", "中文名", "外国名", "评分", "评价人数", "概况", "信息")
    for i in range(8):
        worksheet.write(0, i, info[i])
    for i in range(250):
        for j in range(8):
            worksheet.write(i+1, j, dataList[i][j])

    workbook.save(save_path)


if __name__ == "__main__":
    main()
    print("保存成功")
