from bs4 import BeautifulSoup
import csv
import time
import requests
from urllib.parse import quote

class Main:
    def index(self,i):
        # 岗位
        work_name="运营总监"
        link="https://search.51job.com/list/030200,000000,0000,00,9,99,"+quote(work_name)+",2,"+str(i)+".html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

        response = requests.get(link, headers=headers)
        code=response.apparent_encoding
        response.encoding = code
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        sojob_result = soup.find("div", id='resultList')
        list = sojob_result.find_all("div" , class_='el')
        for x in range(1,len(list)):
            # print(list[x])
            work=list[x].find("p",class_='t1').find("span").get_text().strip()
            company=list[x].find("span",class_='t2').get_text().strip()
            address=list[x].find("span",class_='t3').get_text().strip()
            money = list[x].find("span", class_='t4').get_text().strip()
            public_time=list[x].find("span",class_='t5').get_text().strip()
            self.write([work,company,address,money,public_time])

    def write(self, data):
        with open('data/qiancheng' + time.strftime("%Y-%m-%d", time.localtime()) + '.csv', 'a+', encoding='utf-8',
                  newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            print(data)

for i in range(0,200):
    Main().index(i)

print('恭喜你，爬取数据成功')
