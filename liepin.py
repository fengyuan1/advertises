#!usr/bin/python
from bs4 import BeautifulSoup
import csv
import time
import random
import requests
import sys
import operator

from urllib.parse import quote



class Main:
	def index(self,i,sleep_count):
		# 岗位
		work_name="技术总监"
		link="https://www.liepin.com/zhaopin/?industries=040&subIndustry=&dqs=050020&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=aaa42964a7680110daf82f6e378267d9&d_ckId=ff5c36a41d1d524cff2692be11bbe61f&d_sfrom=search_prime&d_pageSize=40&siTag=_1WzlG2kKhjWAm3Yf9qrog%7EqdZCMSZU_dxu38HB-h7GFA&key="+quote(work_name)+"&curPage="+str(i);
		user_agent_list = [
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
		]
		headers={"User-Agent": random.choice(user_agent_list)}

		try:
			response=requests.get(link,headers=headers)
			response.encoding = 'utf-8'
			html = response.text
			soup=BeautifulSoup(html,'html.parser')
			sojob_result=soup.find("div",class_='sojob-result')
			list_r=sojob_result.find_all("li")
		except BaseException:
			if(sleep_count>9):
				print("亲，我都试了45分钟了，还是无法请求网络成功，请你稍后重试或寻求专业人士帮助")
				print("亲，抱歉，程序结束")
				sys.exit()
			print("抱歉，爬取异常，原因可能是需要验证操作或您的网络不佳，我先休息五分钟再来试试把")
			print("开始休眠5分钟")
			sleep_count=sleep_count+1
			sys.stdout.flush()
			time.sleep(300)
			Main().index(i,sleep_count)


		if (len(list_r) == 0):
			print("恭喜你,本次爬取数据任务已完成啦")
			sys.exit()
		# 岗位
		sleep_count=0
		in_data=[]
		out_data = []

		with open("data/liepin_data.txt", "r+", encoding="utf-8") as f:
			f.close()
		for x in range(0,len(list_r)):
			address = ''
			work=list_r[x].find("a").get_text().strip()
			edu=list_r[x].find("span",class_='edu').get_text().strip()
			year=list_r[x].find("span",class_='edu').find_next_sibling("span").get_text().strip()
			money=list_r[x].find("span",class_='text-warning').get_text().strip()
			company=list_r[x].find("p",class_='company-name').get_text().strip()
			data=[work,edu,money,company,year,address]

			in_data=data
			with open("data/liepin_data.txt", "r+", encoding="utf-8") as f:
				out_data=f.read()
				f.close()
			in_data=str(in_data)
			if(operator.eq(in_data,out_data)):
				with open("data/liepin_data_count.txt", "r+", encoding="utf-8") as f:
					count = f.read()
					count=int(count)
					f.close()
				if(count>12):
					print("恭喜你,本次爬取数据任务已完成啦")
					sys.exit()
			self.write(work_name, data)
			print(data)


		with open("data/liepin_data.txt", "w+", encoding="utf-8") as f:
			f.write(str(in_data))
			f.close()
		with open("data/liepin_data_count.txt", "w+", encoding="utf-8") as f:
			f.write(str(i))
			f.close()

		sys.stdout.flush()
		time.sleep(random.randint(7, 16))
		Main().index(i+1,sleep_count)

	def write(self,work_name,data):
		with open('data/lieping_'+time.strftime("%Y-%m-%d", time.localtime())+'_'+work_name+'.csv', 'a+', encoding='utf-8', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(data)
			f.close()
			print('写入成功')



with open("data/liepin_data.txt", "w+", encoding="utf-8") as f:
	f.write(str([]))
	f.close()
with open("data/liepin_data_count.txt", "w+", encoding="utf-8") as f:
	f.write(str(0))
	f.close()

Main().index(0,0);