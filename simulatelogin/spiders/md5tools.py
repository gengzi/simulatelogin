# coding:utf-8

import md5


def md5_encrypt(src):
    """
    md5 加密
    :param src: 需要加密的字段
    :return:
    """
    m1 = md5.new()
    m1.update(src.encode(encoding='utf-8'))
    return m1.hexdigest()



# function chkpwd(obj) {
#  if(obj.value!='')
# {    var s=md5(document.all.txt_asmcdefsddsd.value+md5(obj.value).substring(0,30).toUpperCase()+'10479').substring(0,30).toUpperCase();
#     document.all.dsdsdsdsdxcxdfgfg.value=s;} else { document.all.dsdsdsdsdxcxdfgfg.value=obj.value;
# } }


#function chkyzm(obj) {  if(obj.value!='') {  var s=md5(md5(obj.value.toUpperCase()).substring(0,30).toUpperCase()+'10479').substring(0,30).toUpperCase();  document.all.fgfggfdgtyuuyyuuckjg.value=s;} else {    document.all.fgfggfdgtyuuyyuuckjg.value=obj.value.toUpperCase();}}


# username = "xxxx"
# passwd = "xxx"
# yzm = 'gbhg'
#
# #密码加密
# passwd_jiami = md5_encrypt((username+md5_encrypt(passwd)[0:30].upper()+'10479'))[0:30].upper()
# print passwd_jiami
# #验证码加密
# yzm_jiami = md5_encrypt((md5_encrypt(yzm.upper())[0:30].upper()+'10479'))[0:30].upper()
# print yzm_jiami

#4BA1FA2C1C50B8426134086BBC4EB7
#4BA1FA2C1C50B8426134086BBC4EB7


#E721BDDB0D83D4CB86D018D7F096F5
#E721BDDB0D83D4CB86D018D7F096F5