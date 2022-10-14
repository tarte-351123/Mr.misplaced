import schedule
from time import sleep
import requests
import datetime

def task():
    print("タスク実行中")
    GET_URL1 = "http://localhost:8000/cluster/"
    GET_URLp = "http://localhost:8000/phone/"
    GET_URLw = "http://localhost:8000/wallet/"
    GET_URLb = "http://localhost:8000/bag/"
    
    response = requests.get(GET_URLp)
    data = response.json()
    data.reverse()
    latest=""
    data_list=[]
    for i in range(20):
        if i<=19 and data[i]["time"]==data[i+1]["time"]:
            a_data=[data[i]["time"],data[i]["hostname"],data[i]["rssi"],data[i+1]["hostname"],data[i+1]["rssi"]]
            data_list.append(a_data)
            latest=data[i]["time"]
        elif latest!=data[i]["time"]:
            a_data=[data[i]["time"],data[i]["hostname"],data[i]["rssi"]]
            data_list.append(a_data)
    latest=""
    time_list_p=[]
    # 簡単な修正プログラム
    for i in range(len(data_list)-2):
        if latest!= data_list[i][0]:
            if  "ohashi01" not in data_list[i]:
                host="ohashi01"
            elif "ohashi02" not in data_list[i]:
                host="ohashi02"
            data = [data_list[i][0],data_list[i][1],data_list[i+1][2],host,-110]
            time_list_p.append(data)
        if "ohashi01" in data_list[i] and "ohashi01" not in data_list[i+1] and "ohashi01" in data_list[i+2]:
            ave = (data_list[i][2]+data_list[i+2][2])/2
            data = [data_list[i+1][0],data_list[i+1][1],data_list[i+1][2],"ohashi01",int(ave)]
            time_list_p.append(data)
            latest=data_list[i+1][0]
        elif "ohashi02" in data_list[i] and "ohashi02" not in data_list[i+1] and "ohashi02" in data_list[i+2]:
            ave = (data_list[i][2]+data_list[i+2][2])/2
            data=[data_list[i+1][0],data_list[i+1][1],data_list[i+1][2],"ohashi02",int(ave)]
            time_list_p.append(data)
            latest=data_list[i+1][0]
            
    response = requests.get(GET_URLw)
    data = response.json()
    data.reverse()
    latest=""
    data_list=[]
    for i in range(10):
        if i<=9 and data[i]["time"]==data[i+1]["time"]:
            a_data=[data[i]["time"],data[i]["hostname"],data[i]["rssi"],data[i+1]["hostname"],data[i+1]["rssi"]]
            data_list.append(a_data)
            latest=data[i]["time"]
        elif latest!=data[i]["time"]:
            a_data=[data[i]["time"],data[i]["hostname"],data[i]["rssi"]]
            data_list.append(a_data)
    latest=""
    time_list_w=[]
    # 簡単な修正プログラム
    for i in range(len(data_list)-2):
        if latest!= data_list[i][0]:
            if  "ohashi01" not in data_list[i]:
                host="ohashi01"
            elif "ohashi02" not in data_list[i]:
                host="ohashi02"
            data = [data_list[i][0],data_list[i][1],data_list[i+1][2],host,-110]
            time_list_w.append(data)
        if "ohashi01" in data_list[i] and "ohashi01" not in data_list[i+1] and "ohashi01" in data_list[i+2]:
            ave = (data_list[i][2]+data_list[i+2][2])/2
            data = [data_list[i+1][0],data_list[i+1][1],data_list[i+1][2],"ohashi01",int(ave)]
            time_list_w.append(data)
            latest=data_list[i+1][0]
        elif "ohashi02" in data_list[i] and "ohashi02" not in data_list[i+1] and "ohashi02" in data_list[i+2]:
            ave = (data_list[i][2]+data_list[i+2][2])/2
            data=[data_list[i+1][0],data_list[i+1][1],data_list[i+1][2],"ohashi02",int(ave)]
            time_list_w.append(data)
            latest=data_list[i+1][0]
            
    response = requests.get(GET_URLb)
    data = response.json()
    data.reverse()
    latest=""
    data_list=[]
    for i in range(10):
        if i<=9 and data[i]["time"]==data[i+1]["time"]:
            a_data=[data[i]["time"],data[i]["hostname"],data[i]["rssi"],data[i+1]["hostname"],data[i+1]["rssi"]]
            data_list.append(a_data)
            latest=data[i]["time"]
        elif latest!=data[i]["time"]:
            a_data=[data[i]["time"],data[i]["hostname"],data[i]["rssi"]]
            data_list.append(a_data)
    latest=""
    time_list_b=[]
    # 簡単な修正プログラム
    for i in range(len(data_list)-2):
        if latest!= data_list[i][0]:
            if  "ohashi01" not in data_list[i]:
                host="ohashi01"
            elif "ohashi02" not in data_list[i]:
                host="ohashi02"
            data = [data_list[i][0],data_list[i][1],data_list[i+1][2],host,-110]
            time_list_b.append(data)
        if "ohashi01" in data_list[i] and "ohashi01" not in data_list[i+1] and "ohashi01" in data_list[i+2]:
            ave = (data_list[i][2]+data_list[i+2][2])/2
            data = [data_list[i+1][0],data_list[i+1][1],data_list[i+1][2],"ohashi01",int(ave)]
            time_list_b.append(data)
            latest=data_list[i+1][0]
        elif "ohashi02" in data_list[i] and "ohashi02" not in data_list[i+1] and "ohashi02" in data_list[i+2]:
            ave = (data_list[i][2]+data_list[i+2][2])/2
            data=[data_list[i+1][0],data_list[i+1][1],data_list[i+1][2],"ohashi02",int(ave)]
            time_list_b.append(data)
            latest=data_list[i+1][0]
            
    place_list =""
    for i in time_list_p:
        if i[1]=="ohashi02":
            tmp1=i[1]
            i[1]=i[3]
            i[3]=tmp1
            tmp2=i[2]
            i[2]=i[4]
            i[4]=tmp2
        
            
        if i[2]>=i[4]:
            place = "リビング"
            place_list+="0"
        elif i[2]<i[4]:
            place = "玄関"
            place_list+="1"
        elif i[2]==-110 and i[4]==-110:
            place = "圏外"
            place_list+="2"
        print(i[0],place)
    print()
    print(time_list_p[0][0],place,"phone")
    i =time_list_w[0]
    if i[1]=="ohashi02":
        tmp1=i[1]
        i[1]=i[3]
        i[3]=tmp1
        tmp2=i[2]
        i[2]=i[4]
        i[4]=tmp2
    if i[2]>=i[4]:
        place = "リビング"
    elif i[2]<i[4]:
        place = "玄関"
    elif i[2]==-110 and i[4]==-110:
        place = "圏外"
    print(i[0],place,"wallet")
    i =time_list_b[0]
    if i[1]=="ohashi02":
        tmp1=i[1]
        i[1]=i[3]
        i[3]=tmp1
        tmp2=i[2]
        i[2]=i[4]
        i[4]=tmp2
    if i[2]>=i[4]:
        place = "リビング"
    elif i[2]<i[4]:
        place = "玄関"
    elif i[2]==-110 and i[4]==-110:
        place = "圏外"
    print(i[0],place,"bag")
    
    if "1111100" in place_list:
        print("お前外出直前だろ")
        
         
    
schedule.every(5).seconds.do(task)
while True:
    schedule.run_pending()
    sleep(1)