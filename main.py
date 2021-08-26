# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:28:58 2021

@author: Regan Yue
"""
import requests
from bs4 import BeautifulSoup
from send_mail import sendMail
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def main():
    Room = "15-303"  #寝室号
    URL = "http://111.177.117.104:8080/admin/sys!chaxun.action"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    formData = {'fjmc': Room.encode("utf-8")}
    session=requests.session()
    
    response=session.post(URL,data=formData,headers=headers)
    
    if response.status_code==200:
        print("查询成功！")
        response.encoding=response.apparent_encoding
        soup = BeautifulSoup(response.text,"html.parser")
        #td0 = soup.find('table').find_all("tr")[0].find_all('td')
        #td1 = soup.find('table').find_all("tr")[1].find_all('td')
        td2 = soup.find('table').find_all("tr")[2].find_all('td')
        #td3 = soup.find('table').find_all("tr")[3].find_all('td')
        #td4 = soup.find('table').find_all("tr")[4].find_all('td')
        
        list2_str = []
        for i in range(len(td2)):
            list2_str.append(td2[i].getText().strip())
            
        print(list2_str[0],list2_str[1])
        print(list2_str[2],list2_str[3])
        print(list2_str[4],list2_str[5])
        
        fee = list2_str[5].replace("元","")
        if float(fee)<30.0:
            ret = sendMail("1131625869@qq.com")  # 要发送的邮箱
            if ret:
                print("邮件发送成功")
            else:
                print("邮件发送失败")        
        

scheduler = BlockingScheduler()
# 修改定时任务，这里是设置每天下午14点7分进行查询
scheduler.add_job(main, 'cron', day_of_week='0-6', hour=14, minute=7)
scheduler.start()























