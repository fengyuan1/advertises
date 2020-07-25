# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:12:30 2019

@author: Administrator
"""

# import urllib.request
import urllib.parse
import re
import csv
import time
from urllib import request

#https://www.zhipin.com/c101130100/d_203/?query=Java&page=1&ka=page-1

class ZhaopinSpyder:
    def __init__(self):
        self.baseurl = "https://www.zhipin.com/c"
        self.headers = {"user-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
        self.name = ""
        self.city = ""
        #self.page = 0
    # 获取页面
    def getPage(self,url):
        # print(self.headers)
        head = request.Request(url, headers=self.headers)
        # print(head)
        response = request.urlopen(head)
        print(response.getheaders())
        cookie = ''
        for header in response.getheaders():
            if header[0] == 'set-cookie':
                cookie = cookie + header[1].split(';')[0] + '; '
        # 去掉最后的空格
        cookie = cookie[:-1]
        print(cookie)


        # req = urllib.request.Request(url,headers=self.headers)
        # res = urllib.request.urlopen(req)
        # html = res.read().decode("utf-8")
        #print(html)
        # print(html)
        # self.parsePage(html)
    # 解析页面
    def parsePage(self, html):
        print(1)
        # p = re.compile(r'<div class="job-primary">.*?<div class="job-title">(.*?)</div>.*?<span class="red">(.*?)</span>.*?<em class="vline"></em>(.*?)<em class="vline">.*?<h3 class="name">.*?target="_blank">(.*?)</a></h3>.*?',re.S)
        # rList = p.findall(html)
        # print(rList)
        # if bool(rList):
        #     #print(rList)
        #     self.writePage(rList)
        
    # 保存数据
    def writePage(self,List):
        
        f = open("boss.csv","a",newline="",encoding="utf-8")
        write = csv.writer(f)
        write.writerow(["职位名称","薪酬","工作经验","公司名称"])
        for rTuple in List:
            write.writerow([rTuple[0],rTuple[1],rTuple[2],rTuple[3]])
        f.close()
    # 主方法
    def workOn(self):
        citycode = {"北京":"101010100","上海":"101020100","天津":"101030100","重庆":"101040100",
"哈尔滨":"101050100","长春":	"101060100","沈阳":"101070100","呼和浩特":"101080100","石家庄":"101090100",
"太原":	"101100100","西安":	"101110100","济南":	"101120100","乌鲁木齐":"101130100","西宁":"101150100",
"兰州":"101160100","银川":"101170100","郑州":"101180100","南京":"101190100","武汉":	"101200100",
"杭州":"101210100","合肥":"101220100","福州":"101230100","南昌":"101240100","长沙":"101250100",
"贵阳":"101260100","成都":"101270100","广州":"101280100","昆明":"101290100","南宁":"101300100",
"海口":"101310100","台湾":"101341100","拉萨":"101140100","香港":"101320300","澳门":"101330100"}
        self.city = "广州"
        self.name = "架构师" 
        city = citycode[self.city]
# 搜索内容进行转码
        query = urllib.parse.urlencode({"query":self.name})
        print("爬取开始")
        for i in range(1,4):
            url = self.baseurl+city+"/d_203/?"+query+"&page%s&ka=page-%s"%(str(i),str(i))
            print("爬取第%d页"%(i))
            self.getPage(url)
            time.sleep(0.5)
        print("爬取完毕")
           
if __name__ == "__main__":
    spyder = ZhaopinSpyder()
    spyder.workOn()