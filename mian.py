##润扬选场地
#author：chark
#仅供学习使用，请勿传播
import json
import requests
import datetime
now_time = datetime.datetime.now()
ntime=datetime.datetime.now()+datetime.timedelta(days=6)#更新是days=6
nntime=ntime.strftime('%Y-%m-%d')
changdi_url = "http://reservation.ruichengyunqin.com/api/blade-app/qywx/saveOrder?userid=12132700"
headers = {
        "Content-Type" : 'application/json',
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63060012)"
}
kg=" "
#data里好像有不需要的参数
#改gymId，groundId，……和startTime，endTime
def pa8(start_time,end_time):
 data = {

        "customerEmail":"null",
        "customerId":"1429608770295611394",
        "customerName":"邱恒康",
        "customerTel":"15190699198",
        "userNum":"2",
        "gymId":"1297443858304540673",
        "gymName":"8号场",
        "groundId":"1298273265650819073",
        "gymName":"润杨羽毛球馆",
        "groundType":"0",
        "messagePushType":"0",
        "isIllegal":"0",
        "orderDate":"2022-06-08 20:22:00",
        "tmpOrderDate":"2022-06-08 20:22:00",
        "tmpStartTime":"2022-06-08 13:00:00",
        "tmpEndTime":"2022-06-08 13:30:00",
        "startTime":start_time,
        "endTime":end_time,#2022-06-08 19:30:00
}

 response=requests.post(url=changdi_url,headers=headers,data=json.dumps(data) )
 if '成功' in response.text:
  print('8号成了')
 else:
  print('8号失败')

def pa1(start_time,end_time):
 data = {

        "customerEmail":"null",
        "customerId":"1429608770295611394",
        "customerName":"邱恒康",
        "customerTel":"15190699198",
        "userNum":"2",
        "gymId":"1297443858304540673",
        "gymName":"1号场",
        "groundId":"1298272433186332673",
        "gymName":"润杨羽毛球馆",
        "groundType":"0",
        "messagePushType":"0",
        "isIllegal":"0",
        "orderDate":"2022-06-08 20:22:00",
        "tmpOrderDate":"2022-06-08 20:22:00",
        "tmpStartTime":"2022-06-08 13:00:00",
        "tmpEndTime":"2022-06-08 13:30:00",
        "startTime":start_time,
        "endTime":end_time,#2022-06-08 19:30:00
}

 response=requests.post(url=changdi_url,headers=headers,data=json.dumps(data) )
 if '成功' in response.text:
  print('1号成了')
 else:
  print('1号失败')

pa8(nntime+kg+'18:00:00',nntime+kg+'19:00:00')
pa8(nntime+kg+'19:00:00',nntime+kg+'20:00:00')
pa8(nntime+kg+'20:00:00',nntime+kg+'21:00:00')
pa8(nntime+kg+'21:00:00',nntime+kg+'22:00:00')

#print(nntime +kg+"19:00:00")
pa1(nntime+kg+'18:00:00',nntime+kg+'19:00:00')
pa1(nntime+kg+'19:00:00',nntime+kg+'20:00:00')
pa1(nntime+kg+'20:00:00',nntime+kg+'21:00:00')
pa1(nntime+kg+'21:00:00',nntime+kg+'22:00:00')