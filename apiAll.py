#coding=utf-8

import requests

def getCard():
    url = "https://66qianzhuang-api-test.yangqianguan.com/api/home/card"
    headers = {
        'platformtype': "ANDROID",
        'cookie': "loanMarketVisitorId=e41662c5-5bc1-4422-bbaa-94bdb9c8ba00",
        'deviceid': "F8B61417-4975-4C26-A46A-92DE4C964801",
        }
    response = requests.request("GET", url, headers=headers)

    print(response.text)