from bs4 import BeautifulSoup
import csv
import time
import requests
import sys
import json
import time
import random
# import str
import operator


from urllib.parse import quote

class Main:
    def index(self,i,sleep_count):
        # 岗位
        work_name="技术总监"

        try:
            link="https://search.51job.com/list/030200,000000,0000,00,9,99,"+quote(work_name)+",2,"+str(i)+".html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
            #print(link)
            response = requests.get(link, headers=headers)
            code=response.apparent_encoding
            response.encoding = code
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            in_data = []
            out_data = []
            count=0

            sojob_result = soup.find_all("script", type='text/javascript')

        except BaseException:
            if (sleep_count > 9):
                print("亲，我都试了45分钟了，还是无法请求网络成功，请你稍后重试或寻求专业人士帮助")
                print("亲，抱歉，程序结束")
                sys.exit()
            print("抱歉，爬取异常，原因可能是需要验证操作或您的网络不佳，我先休息五分钟再来试试把")
            print("开始休眠5分钟")
            sleep_count = sleep_count + 1
            sys.stdout.flush()
            time.sleep(300)
            Main().index(i, sleep_count)



        try:
            a = str(sojob_result[2])
            json_str = json.loads(a[60:-9], strict=False)
            list = json_str['engine_search_result']
        except BaseException:
            sys.stdout.flush()
            time.sleep(3)
            self.index(i + 1, sleep_count)
        if (len(list) == 0):
            print("恭喜你,本次爬取数据任务已完成啦")
            sys.exit()
        try:
            for x in range(1,len(list)):
                work= list[x]['job_name']
                company=list[x]['company_name']
                address=list[x]['workarea_text']
                money = list[x]['providesalary_text']
                attribute_text=list[x]['attribute_text']
                public_time = list[x]['issuedate']
                data=[work,company,address,money,attribute_text,public_time]
                print(data)
                self.write(work_name, data)
                in_data = data
                with open("data/qiancheng_data.txt", "r+", encoding="utf-8") as f:
                    out_data = f.read()
                    f.close()
                in_data = str(in_data)
                if (operator.eq(in_data, out_data)):
                    with open("data/qiancheng_data_count.txt", "r+", encoding="utf-8") as f:
                        count = f.read()
                        count = int(count)
                        f.close()

        except BaseException:
            sys.stdout.flush()
            time.sleep(random.randint(3, 7))
            self.index(i + 1,sleep_count)

        sys.stdout.flush()
        time.sleep(random.randint(3, 7))
        if (count > 12):
            print("恭喜你,本次爬取数据任务已完成啦")
            sys.exit()
        sleep_count=0
        with open("data/qiancheng_data.txt", "w+", encoding="utf-8") as f:
            f.write(str(in_data))
            f.close()
        with open("data/qiancheng_data_count.txt", "w+", encoding="utf-8") as f:
            f.write(str(i))
            f.close()
        self.index(i+1,sleep_count)

    def write(self,work_name, data):
        with open('data/qiancheng' +'_'+ time.strftime("%Y-%m-%d", time.localtime()) + '_' + work_name + '.csv', 'a+',
                  encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            print('写入成功')

with open("data/qiancheng_data.txt", "w+", encoding="utf-8") as f:
    f.write(str([]))
    f.close()
with open("data/qiancheng_data_count.txt", "w+", encoding="utf-8") as f:
    f.write(str(0))
    f.close()
Main().index(1,0)

