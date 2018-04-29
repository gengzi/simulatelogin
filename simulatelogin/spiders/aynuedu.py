# -*- coding: utf-8 -*-
from _mysql import result

import scrapy
import re
import random
import time
from PIL import Image
from md5tools import md5_encrypt


class AynueduSpider(scrapy.Spider):
    name = 'aynuedu'
    allowed_domains = ['jwglxt.aynu.edu.cn']
    start_urls = ['http://jwglxt.aynu.edu.cn/']

    VIEWSTATE = ''

    #处理第一次请求，提取登陆需要的额外参数
    def parse(self, response):
        #拿到cookie
        headers = response.headers
        newheaders = dict(headers)
        #设置referer
        newheaders['Referer'] = 'http://jwglxt.aynu.edu.cn/'

        yield scrapy.Request(url="http://jwglxt.aynu.edu.cn/_data/home_login.aspx",callback=self.parse_loginurl,method='GET',headers=newheaders)


    def parse_loginurl(self,response):
        """
        访问登陆的网址，拿到额外的参数
        :param response:
        :return:
        """
        headers = response.headers
        newheaders = dict(headers)
        # 设置referer
        newheaders['Referer'] = 'http://jwglxt.aynu.edu.cn/_data/home_login.aspx'
        newheaders['Accept']='image/webp,image/apng,image/*,*/*;q=0.8'

        #使用正则表达式获取数据
        self.VIEWSTATE = re.search(r'<input type="hidden" name="__VIEWSTATE" value="(.*)"', response.text).group(1)
        print self.VIEWSTATE
        url = "http://jwglxt.aynu.edu.cn/sys/ValidateCode.aspx?t=" + str(random.randint(0, 999))
        yield scrapy.Request(url=url, callback=self.parse_yzmurl,method='GET', headers=newheaders)

    def parse_yzmurl(self,response):
        """
        获取验证码
        :param response:
        :return:
        """
        with open("yzm.jpg","wb") as f:
            f.write(response.body)
        time.sleep(1)
        #打开该验证码
        im = Image.open('yzm.jpg')
        im.show()
        yzm = raw_input("please input yzm:")
        #
        print yzm
        print self.VIEWSTATE

        username = str(raw_input("please input username:"))
        print username
        passwd = str(raw_input("please input passwd:"))
        print passwd

        # username = "xxx"
        # passwd = "xxx"
        # 密码加密
        passwd_jiami = md5_encrypt((username + md5_encrypt(passwd)[0:30].upper() + '10479'))[0:30].upper()
        # 验证码加密
        yzm_jiami = md5_encrypt((md5_encrypt(yzm.upper())[0:30].upper() + '10479'))[0:30].upper()


        url = 'http://jwglxt.aynu.edu.cn/_data/home_login.aspx'
        login_data = {
            '__VIEWSTATE': self.VIEWSTATE,
            'pcInfo': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36undefined5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 SN:NULL',
            'typeName': 'ѧ��',
            'dsdsdsdsdxcxdfgfg': passwd_jiami,
            'fgfggfdgtyuuyyuuckjg': yzm_jiami,
            'Sel_Type': 'STU',
            'txt_asmcdefsddsd': username,
            'txt_pewerwedsdfsdff': '',
            'txt_sdertfgsadscxcadsads': '',
        }

        login_headers = {
            'Referer': 'http://jwglxt.aynu.edu.cn/_data/home_login.aspx',
            'Origin': 'http://jwglxt.aynu.edu.cn',
        }

        # 发送请求参数，并调用指定回调函数处理
        #yield scrapy.Request(url=url, callback=self.parse_login,method='POST', headers=login_headers,)
        yield  scrapy.FormRequest(url=url,formdata=login_data,headers=login_headers,callback=self.parse_login,method="POST")

    def parse_login(self,response):
        """

        :param response:
        :return:
        """
        url = "http://jwglxt.aynu.edu.cn/xsxj/Stu_MyInfo_RPT.aspx"
        getinfoheaders = {
            'Referer': 'http://jwglxt.aynu.edu.cn/xsxj/Stu_MyInfo.aspx',
        }
        yield scrapy.Request(url=url,headers=getinfoheaders,callback=self.show_info)

    def show_info(self,response):
        print response.text


