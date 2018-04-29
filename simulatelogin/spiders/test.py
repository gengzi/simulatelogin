# -*- coding: utf-8 -*-


newheaders = {
    'X-Aspnet-Version': ['1.1.4322'],
    'Set-Cookie': ['ASP.NET_SessionId=rywtsp554x5pfx45pknxw145; path=/'],
    'X-Powered-By': ['ASP.NET'],
    'Server': ['none'],
    'Cache-Control': ['private'],
    'Date': ['Sat, 28 Apr 2018 05:29:43 GMT'],
    'Content-Type': ['text/html; charset=gb2312']
}

newheaders['Referer'] = 'http://jwglxt.aynu.edu.cn/'

print newheaders['Set-Cookie'][0]

print newheaders

from  PIL import Image

# im = Image.open('captcha.jpg')
# im.show()