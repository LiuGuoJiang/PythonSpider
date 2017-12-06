import requests
import pandas
from pymongo import MongoClient
import time
from fake_useragent import UserAgent
def get_job_info(page,kd,url,setName):
    for i in range(page):
        payload={
            'first':'true',
            'pn':i,
            'kd':kd
        }
        ua=UserAgent()
        headers['User-Agent']=ua.random
        response=requests.post(url,data=payload,headers=headers)
        if response.status_code==200:
            job_json_position=response.json()['content']['positionResult']['result']
            if job_json_position:
                setName.insert(job_json_position)
            else:
                break
        else:
            print('Request error!')

        print('Crawling the '+str(i+1)+' page of data')
        time.sleep(1)


if __name__=='__main__':
    stack = ["爬虫",'PHP', ".NET", "JAVA", "AI", "DataAnalysis"]
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchoolJob=0"
    headers = {
        'Cookie': 'JSESSIONID=ABAAABAAADEAAFI645AAE10A3472E699508EA942EEFE028; _gat=1; user_trace_token=20171206145103-d3cce821-da51-11e7-85f8-525400f775ce; PRE_UTM=; PRE_HOST=www.google.co.jp; PRE_SITE=https%3A%2F%2Fwww.google.co.jp%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20171206145103-d3cceae2-da51-11e7-85f8-525400f775ce; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.1084614236.1512543063; _ga=GA1.2.1441577731.1512543063; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512543064; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512543081; LGSID=20171206145103-d3cce95d-da51-11e7-85f8-525400f775ce; LGRID=20171206145121-de842742-da51-11e7-9c2d-5254005c3644; SEARCH_ID=b4d3431dd65842f9967222e12c4d5d47',
        'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput='
    }
    client = MongoClient()
    db = client.lagou
    lagou = db.LagouInfo
    for index in range(len(stack)):
        print(stack[index])
        get_job_info(10, stack[index], url, lagou)