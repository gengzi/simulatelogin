# coding:utf-8

import requests

def getCookieByRequestUrl(response):
    """
    根据请求的响应获取cookie信息
    :param response: 请求网站后的响应
    :return:
    """
    cookiejar = response.cookies

    # 8. 将CookieJar转为字典：
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

    return cookiedict['ASP.NET_SessionId']

    # print cookiejar
    #
    # print cookiedict

def getCookieByRequestSession(url,headers):
    """
    发送请求获取cookie信息
    :param url: 请求的网站的网址
    :param headers: 请求头
    :return:
    """
    session = requests.session()
    response = session.get(url=url,headers=headers)
    cookiedict = requests.utils.dict_from_cookiejar(response.cookies)
    return cookiedict['ASP.NET_SessionId']


headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}

# print getCookieByRequestUrl("http://jwglxt.aynu.edu.cn/",headers=headers)
#print getCookieByRequestSession("http://jwglxt.aynu.edu.cn/",headers=headers)