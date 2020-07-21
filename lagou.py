# import urllib.request
from urllib import parse
from urllib import request
from bs4 import BeautifulSoup
import csv
import ssl
import json
import time
class Main:
	def index(self,i):
		# 去掉全局安全校验
		ssl._create_default_https_context = ssl._create_unverified_context
		# 先爬取首页python职位的网站以获取Cookie
		url = 'https://www.lagou.com/jobs/list_%E6%9E%B6%E6%9E%84%E5%B8%88?city=%E5%B9%BF%E5%B7%9E&labelWords=&fromSearch=true&suginput='
		# print(url)
		req = request.Request(url, headers={
		    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
		})
		response = request.urlopen(req)
		# print(response)
		# 从响应头中提取Cookie
		cookie = ''
		for header in response.getheaders():
		    if header[0] == 'Set-Cookie':
		        cookie = cookie + header[1].split(';')[0] + '; '
		# 去掉最后的空格
		cookie = cookie[:-1]
		# print(cookie)
		# 爬取职位数据
		url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
		# 构造请求头，将上面提取到的Cookie添加进去
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
			'Cookie': cookie,
			'Referer': 'https://www.lagou.com/jobs/list_%E6%9E%B6%E6%9E%84%E5%B8%88?city=%E5%B9%BF%E5%B7%9E&labelWords=&fromSearch=true&suginput='
		}
		data = {
			'first': 'true',
			'pn': i,
			'kd': '运营总监'
		}

		req = request.Request(url, data=parse.urlencode(data).encode('utf-8'), headers=headers,method='POST')
		# print(req)
		response = request.urlopen(req)
		# print(response.read().decode('utf-8'))
		result=response.read().decode('utf-8')
		result=json.loads(result);
		# print(result['content']['positionResult'])

# 岗位
		try:
			# print(result)
			for x in range(0,result['content']['positionResult']['resultSize']):
				district=result['content']['positionResult']['result'][x]['city']
				work=result['content']['positionResult']['result'][x]['positionName']
				edu=result['content']['positionResult']['result'][x]['education']
				year=result['content']['positionResult']['result'][x]['workYear']
				money=result['content']['positionResult']['result'][x]['salary']
				company=result['content']['positionResult']['result'][x]['companyFullName']
				create_time=result['content']['positionResult']['result'][x]['createTime']
				data=[work,edu,money,company];
				print(data)
				if district=="广州" or district=="深圳":
					self.write([district,work,edu,money,company,year,create_time])
		except IOError:
			print('chenggong')


	def write(self,data):
		with open('data/lagou_guangdong'+time.strftime("%Y-%m-%d", time.localtime())+'.csv', 'a', encoding='utf-8', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(data)
			print("写入成功")

for i in range(0,200):
	Main().index(i);
	time.sleep(15)
print("写入完成")