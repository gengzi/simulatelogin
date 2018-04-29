# coding:utf-8


import requests
from md5tools import md5_encrypt
from getyzm import getYZMImage
from getCookie import getCookieByRequestUrl
import random
from lxml import etree
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}


def login(username,passwd,yzm,cookie,viewstate):
    #组拼 data
    login_data  = {
        '__VIEWSTATE':viewstate,
        'pcInfo':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36undefined5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 SN:NULL',
        'typeName':'ѧ��',
        'dsdsdsdsdxcxdfgfg': passwd,
        'fgfggfdgtyuuyyuuckjg':yzm,
        'Sel_Type': 'STU',
        'txt_asmcdefsddsd':username,
        'txt_pewerwedsdfsdff':'',
        'txt_sdertfgsadscxcadsads':'',
    }

    cookievalue = 'ASP.NET_SessionId=' + str(cookie)
    login_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie':cookievalue,
        'Referer': 'http://jwglxt.aynu.edu.cn/_data/home_login.aspx',
        'Origin': 'http://jwglxt.aynu.edu.cn',
    }

    loginurl = "http://jwglxt.aynu.edu.cn/_data/home_login.aspx"

    session = requests.session()
    response = session.post(url=loginurl,data=login_data,headers=login_headers)

    getinfoheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie': cookievalue,
        'Referer': 'http://jwglxt.aynu.edu.cn/xsxj/Stu_MyInfo.aspx',
    }
    response1 = session.get(url="http://jwglxt.aynu.edu.cn/xsxj/Stu_MyInfo_RPT.aspx",headers=getinfoheaders)
    print response1.text



if __name__ == "__main__":
    #访问教务主网页获取cookie信息
    response = requests.get(url="http://jwglxt.aynu.edu.cn/", headers=headers)
    cookie = getCookieByRequestUrl(response)

    #拼装新的请求头，访问登陆的链接，获取到额外的参数和对应的值
    loginhomeheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie': cookie,
        'Referer': 'http://jwglxt.aynu.edu.cn/',
        #'Referer': 'http://jwglxt.aynu.edu.cn/default.new.aspx',

    }
    loginhomeurl = 'http://jwglxt.aynu.edu.cn/_data/home_login.aspx'
    response = requests.get(loginhomeurl,headers=loginhomeheaders)

    VIEWSTATE = re.search(r'<input type="hidden" name="__VIEWSTATE" value="(.*)"',response.text).group(1)
    print VIEWSTATE

    #根据cookie信息，访问验证码链接，保存验证码图片到本地
    url = "http://jwglxt.aynu.edu.cn/sys/ValidateCode.aspx?t="+str(random.randint(0,999))
    getYZMImage(url=url, cookie=cookie)

    #等待用户输入，将密码和验证码进行加密处理
    username = str(raw_input("请输入账号:"))
    print username
    passwd = str(raw_input("请输入密码:"))
    print passwd
    yzm = str(raw_input("请输入验证码:"))
    print yzm

    # username = "xxx"
    # passwd = "xxx"
    # 密码加密
    passwd_jiami = md5_encrypt((username + md5_encrypt(passwd)[0:30].upper() + '10479'))[0:30].upper()
    # 验证码加密
    yzm_jiami = md5_encrypt((md5_encrypt(yzm.upper())[0:30].upper() + '10479'))[0:30].upper()


    viewstate = VIEWSTATE

    #模拟登陆
    login(username,passwd_jiami,yzm_jiami,cookie,viewstate)


