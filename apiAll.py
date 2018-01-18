#coding=utf-8

import requests

class ApiRes(object):
    def __init__(self):
        self.headers = {
            'platformtype': "IOS",
            'cookie': "loanMarketVisitorId=e41662c5-5bc1-4422-bbaa-94bdb9c8ba00",
            'deviceid': "F8B61417-4975-4C26-A46A-92DE4C964801",
        }
    def getBanner(self):
        url = "https://66qianzhuang-api-test.yangqianguan.com/api/home/banner"
        response = requests.request("GET", url, headers=self.headers)
        res = response.text
        return res

    def getCard(self):
        url = "https://66qianzhuang-api-test.yangqianguan.com/api/home/card"
        response = requests.request("GET", url, headers=self.headers)
        res = response.text
        return res

    def getScroll(self):
        url = "https://66qianzhuang-api-test.yangqianguan.com/api/home/scroll"
        response = requests.request("GET", url, headers=self.headers)
        res = response.text
        return res
    def getHomeconf(self):
        url = "https://66qianzhuang-api-test.yangqianguan.com/api/home/config"
        response = requests.request("GET", url, headers=self.headers)
        res = response.text
        return res

# a =ApiRes()
# print(a.getHomeconf())



