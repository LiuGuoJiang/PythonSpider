import lxml as lxml
import requests
from lxml import etree
from pymongo import MongoClient
client = MongoClient()
db = client.TuhuInfo
TuhuInfo = db.Info
#print(response.text)

if __name__=='__main__':
    urlTemp = 'https://item.tuhu.cn/Tires/1/au1-f0-a55-r16-w205-vVE_LSG_EXCELLEGX.html'
    responseTemp = requests.get(urlTemp)
    sTemp = etree.HTML(responseTemp.text)
    page = sTemp.xpath('//div[@class="pager"]/a/text()')
    trArray = sTemp.xpath('//*[@id="Products"]/table/tbody/tr')
    print(len(trArray))  # 获取页面上每页加载多少条：20
    print(len(page))  # 获取到当前页面有多少页数据
    for pIndex in range(len(page)-2):
        url = 'https://item.tuhu.cn/Tires/{0}/au1-f0-a55-r16-w205-vVE_LSG_EXCELLEGX.html'.format(pIndex+1)
        response = requests.get(url)
        s = etree.HTML(response.text)
        for index in range(len(trArray)):
            dic_tuhu = {}
            imgHref = s.xpath('//*[@id="Products"]/table/tbody/tr[{0}]/td[1]/a/@href'.format(index+1))
            pid = s.xpath('//*[@id="Products"]/table/tbody/tr[{0}]/td[2]/a/text()'.format(index+1))
            price=s.xpath('//*[@id="Products"]/table/tbody/tr[{0}]/td[3]/div/strong/text()'.format(index+1))
            tireType=s.xpath('//*[@id="Products"]/table/tbody/tr[{0}]/td[2]/div[1]/label[1]/span/text()'.format(index+1))
            tireWeight = s.xpath('//*[@id="Products"]/table/tbody/tr[{0}]/td[2]/div[1]/label[2]/span/text()'.format(index+1))
            tirePattern=s.xpath('//*[@id="Products"]/table/tbody/tr[{0}]/td[2]/div[1]/label[3]/span/text()'.format(index+1))
            tireSpeed = s.xpath('//*[@id="Products"]/table/tbody/tr[{0}]/td[2]/div[1]/label[4]/span/text()'.format(index + 1))
            Scord=s.xpath('//*[@id="Products"]/table/tbody/tr[{0}]/td[2]/div[2]/div/div/label[2]/text()'.format(index+1))
            PingLunCount=s.xpath('//*[@id="Products"]/table/tbody/tr[{0}]/td[2]/div[2]/div/div/a/em[1]/text()'.format(index+1))
            dic_tuhu['Tuhu_ImgHref']=imgHref[0]
            dic_tuhu['Tuhu_ProductName']=pid[0].strip()
            dic_tuhu['Tuhu_ProductPrice']=price[0]
            dic_tuhu['Tuhu_TireType']=tireType[0].strip()
            dic_tuhu['Tuhu_TireWeight']=tireWeight[0].strip()
            dic_tuhu['Tuhu_TirePattern']=tirePattern[0].strip()
            dic_tuhu['Tuhu_TireSpeed']=tireSpeed[0].strip()
            dic_tuhu['Tuhu_Score']=Scord[0].strip()
            dic_tuhu['Tuhu_PingLunCount']=PingLunCount[0].strip()
            TuhuInfo.insert(dic_tuhu)
            print(dic_tuhu['Tuhu_ImgHref'])
            print(dic_tuhu['Tuhu_ProductName'])
            print(dic_tuhu['Tuhu_ProductPrice'])
#//*[@id="Products"]/table/tbody/tr[1]/td[2]/a/text()
#//*[@id="Products"]/table/tbody
#//*[@id="Products"]/table/tbody/tr[1]/td[1]/a/href
#//*[@id="Products"]/table/tbody/tr[1]/td[2]/a/text()
#//*[@id="Products"]/table/tbody/tr
#//*[@id="Products"]/table/tbody/tr[1]/td[2]/a/text()
#//*[@id="Products"]/table/tbody/tr[1]/td[3]/div/strong/text()
#//*[@id="Products"]/div[2]
#//*[@id="Products"]/div[2]/a[1]
#//*[@id="Products"]/table/tbody/tr
#//*[@id="Products"]/table/tbody/tr[1]/td[2]/div[1]/label[1]
#//*[@id="Products"]/table/tbody/tr[1]/td[2]/div[1]/label[1]/span
#//*[@id="Products"]/table/tbody/tr[2]/td[2]/div[2]/div/div/label[2]/text()
#//*[@id="Products"]/table/tbody/tr[1]/td[2]/div[2]/div/div/label[2]
#//*[@id="Products"]/table/tbody/tr[1]/td[2]/div[2]/div/div/a/text()
#//*[@id="Products"]/table/tbody/tr[1]/td[2]/div[2]/div/div/a/em[1]/text()