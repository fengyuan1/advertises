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
import requests
from urllib import request

#https://www.zhipin.com/c101130100/d_203/?query=Java&page=1&ka=page-1
class ZhaopinSpyder:
    def __init__(self):
        self.baseurl = "https://www.zhipin.com/c"
        self.headers = {
            "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "cookie":"__zp__pub__=; _bl_uid=bOk4b6U6sv0yaehChrgt610q4d9X; lastCity=101280100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1595564075,1595606820,1595606820,1595831896; __c=1595831898; __g=-; __l=l=%2Fwww.zhipin.com%2Fc101280100%2Fd_203%2F%3Fquery%3D%25E6%259E%25B6%25E6%259E%2584%25E5%25B8%2588%26page1%3D%26ka%3Dpage-1&r=&friend_source=0&friend_source=0; t=bhAXzzvVTh5wEw7h; wt=bhAXzzvVTh5wEw7h; __zp_stoken__=7cd5aWDNuRz12KWMibwcLLmgLTQJiI0AoUH4eLytYEFtAZRQ9KkYhER0gFSJ2GSZMLUdCQGU1IjZVZGFnRxEpTA1VHwoiY3loCzY4cQsgCj5ZIFg5RBQhPnBKZCgjYEkub34HP2BOXT9Lfh0%3D; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1595840422; __a=14270550.1564480289.1595606823.1595831898.98.10.16.45",
            "upgrade-insecure-requests":1,
            "cache-control":"max-age=0",
            "accept-language":"zh-CN,zh;q=0.9",
            "accept-encoding":"gzip, deflate, br",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "scheme":"https",
            "path":"/job_detail/?ka=header-job",
            "method":"GET",
            "authority":"www.zhipin.com"

         }
        self.name = ""
        self.city = ""
        #self.page = 0
    # 获取页面
    def getPage(self,url):
        # print(self.headers)
        head = request.Request(url, headers=self.headers)
        # print(head)
        response = request.urlopen(head)
        cookie = ''
        # print(response.getheaders())
        for header in response.getheaders():
            if header[0] == 'set-cookie':
                cookie = cookie + header[1].split(';')[0] + '; '
        # 去掉最后的空格
        cookie = cookie[:-1]
        # print(cookie)
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            'x-requested-with': 'XMLHttpRequest',
            'cookie': cookie,  # 需要填写
        }

        # print(self.headers)
        req = requests.get(url,headers=headers)

        print(req)
        # html = res.read().decode("utf-8")
        # print(html)
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