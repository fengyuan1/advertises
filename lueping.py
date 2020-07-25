#!usr/bin/python
from bs4 import BeautifulSoup
import csv
import time
import requests
from urllib.parse import quote

class Main:
	def index(self,i):
		# 岗位
		work_name="java"
		link="https://www.liepin.com/zhaopin/?industries=040&subIndustry=&dqs=050020&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=aaa42964a7680110daf82f6e378267d9&d_ckId=ff5c36a41d1d524cff2692be11bbe61f&d_sfrom=search_prime&d_pageSize=40&siTag=_1WzlG2kKhjWAm3Yf9qrog%7EqdZCMSZU_dxu38HB-h7GFA&key="+quote(work_name)+"&d_curPage="+str(i);
		headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0"}

		response=requests.get(link,headers=headers)
		response.encoding = 'utf-8'
		html = response.text
		soup=BeautifulSoup(html,'html.parser')
		sojob_result=soup.find("div",class_='sojob-result')
		list=sojob_result.find_all("li")
		# 岗位
		try:
			for x in range(0,len(list)):
				address = list[x].find("a", class_='area').get_text().strip()
				work=list[x].find("a").get_text().strip()
				edu=list[x].find("span",class_='edu').get_text().strip()
				year=list[x].find("span",class_='edu').find_next_sibling("span").get_text().strip()
				money=list[x].find("span",class_='text-warning').get_text().strip()
				company=list[x].find("p",class_='company-name').get_text().strip()

				self.write([work,edu,money,company,year,address])
				print([work,edu,money,company,year,address])
		except Exception as e:
			Main().index(i+1)

	def write(self,data):
		with open('data/lieping'+time.strftime("%Y-%m-%d", time.localtime())+'.csv', 'a', encoding='utf-8', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(data)
			print(data)

for i in range(0,200):
	Main().index(i);