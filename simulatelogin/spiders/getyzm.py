# coding:utf-8

import requests
import time
from getCookie import getCookieByRequestUrl


def getYZMImage(url,cookie):
    """
    请求验证码的网址，下载验证码信息
    :param url: 验证码的链接
    :param cookie: cookie信息
    :return:
    """
    cookievalue =  'ASP.NET_SessionId='+str(cookie)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie':cookievalue,
        'Referer': 'http://jwglxt.aynu.edu.cn/_data/home_login.aspx',
        'Connection':'keep-alive',
        'Accept-Language':'zh-CN,zh;q=0.9',
        #'Accept-Encoding':' gzip, deflate',
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'Host':'jwglxt.aynu.edu.cn',
    }
    response = requests.get(url=url,headers =headers)
    captcha(response.content)



def captcha(data):
    """
    保存验证码图片到本地
    :param data:
    :return:
    """
    with open('captcha.jpg','wb') as fp:
        fp.write(data)
    time.sleep(1)



# headers ={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
# }
#
# cookie = getCookieByRequestUrl("http://jwglxt.aynu.edu.cn/",headers=headers)
#
# url = "http://jwglxt.aynu.edu.cn/sys/ValidateCode.aspx?t=121"
# getYZMImage(url=url,cookie=cookie)