from urllib import request
from bs4 import BeautifulSoup
import csv
import random
import json
import requests

class Main:
	def index(self,i,city="101280100",query="java", industry="", position=""):

		link="https://www.zhipin.com/job_detail/?query={}&city={}&page="+str(i)+"&ka=page-"+str(i)
		url = link.format(query, city)
		user_agent_list = [
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
			"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
		]

		head = request.Request(url, headers={
			'User-Agent': random.choice(user_agent_list),
		})

		response = request.urlopen(head)
		print(response.getheaders())
		cookie = ''
		for header in response.getheaders():
			if header[0] == 'set-cookie':
				cookie = cookie + header[1].split(';')[0] + '; '
		# 去掉最后的空格
		cookie = cookie[:-1]
		print(cookie)
		headers = {
			# 'accept':'application/json, text/javascript, */*; q=0.01',
			# 'accept-encoding':'gzip, deflate, br',
			# 'accept-language':'zh-CN,zh;q=0.8',
			"user-agent": random.choice(user_agent_list),
			# 'x-requested-with':'XMLHttpRequest',
			# 'cookie':cookie, # 需要填写
			}



		#组装城市码
		# if city!="":
			# city=self.get_city_code(city)



		param = {"query": "dsf", "city": "101010100", "page": i}
		req=requests.get(url,param,headers=headers)
		# print(url)
		# response = request.urlopen(req)

		# file=open(r'data/1.txt','a',encoding = 'utf-8')

		# html = response.read().decode("utf-8")
		# soup=BeautifulSoup(req,'html.parser')
		print(req.text)
		# sojob_result=soup.find("div",class_='sojob-result')
		# list=sojob_result.find_all("li")
		# # 岗位
		# for x in range(0,len(list)):
		# 	work=list[x].find("a").get_text().strip()
		# 	edu=list[x].find("span",class_='edu').get_text().strip()
		# 	year=list[x].find("span",class_='edu').find_next_sibling("span").get_text().strip()
		# 	money=list[x].find("span",class_='text-warning').get_text().strip()
		# 	company=list[x].find("p",class_='company-name').get_text().strip()
		# 	# print(year)
		# 	# data=[work,edu,money,company];
		# 	# print(data)
		# 	self.write([work,edu,money,company,year])
		# # print(li[2])

	def write(self,data):
		with open('data/result.csv', 'a', encoding='utf-8', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(data)
			print("写入成功")

	# 获取指定城市的编码
	def get_city_code(self,city_name):
		response = urllib.request.Request("https://www.zhipin.com/wapi/zpCommon/data/city.json")
		print(response)
		# contents = json.loads(response)
		# cities = contents["zpData"]["hotCityList"]
		# city_code = contents["zpData"]["locationCity"]["code"]
		# for city in cities:
		# 	if city["name"] == city_name:
		# 		city_code = city["code"]
		return 1

# for i in range(0,200):
Main().index(2);