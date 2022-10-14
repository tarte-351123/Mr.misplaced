def wallet_data():
    import re
    from pymongo import MongoClient
    import requests
    import datetime
    from datetime import datetime

    GET_URL = "http://localhost:8000/wallet/"
    GET_DATE_URL = "http://localhost:8000/date/"
    POST_URL = "http://localhost:8000/result_wallet/"

    response = requests.get(POST_URL)
    data = response.json()
    
    for i in range (len(data)):
        requests.delete(POST_URL)

    # POSTリクエストを、リクエストボディ付きで送信する
    response = requests.get(GET_URL)

    # dataというList型変数に全てのデータを格納
    data = response.json()
    #data.reverse()

    #より近いラズパイの hostname を格納

    day = int(data[0]["time"][8:10])*3600*24
    hour = int(data[0]["time"][11:13])*3600
    minute = int(data[0]["time"][14:16])*60
    second = int(data[0]["time"][17:20])
    start_time = day+hour + minute +second
    n1=0
    n2=0
    count = 1
    ohashi01 = []
    ohashi02 = []

    for i in data:
        day = int(i["time"][8:10])*3600*24
        hour = int(i["time"][11:13])*3600
        minute = int(i["time"][14:16])*60
        second = int(i["time"][17:20])
        now = day+hour+minute+second
        time_diff = now-start_time
        last_time_diff = 0
        
        #　次のデータと時間が同じ場合
        if i["time"] == data[count]["time"]:

            if i["rssi"]>data[count]["rssi"]:
                    near = i["hostname"]
            elif i["rssi"]<data[count]["rssi"]:
                    near = data[count]["hostname"]
            else :
                near = "中間地点"
        # 次のデータと時間が違う場合
        elif i["time"] != data[count]["time"]:
            near = i["hostname"]


        last_time = i["time"]

        if i["hostname"]=="ohashi01":
            data_list = [i["hostname"], time_diff, i["time"], i["rssi"]]
            ohashi01.append(data_list)

        elif i["hostname"]=="ohashi02":
            data_list = [i["hostname"], time_diff, i["time"], i["rssi"]]
            ohashi02.append(data_list)
            
        if count < len(data)-3:
                count +=1
                
    l_sec = int(re.split('[- /:]', ohashi01[1][2])[5])
    l_min = int(re.split('[- /:]', ohashi01[1][2])[4])*60
    l_hou = int(re.split('[- /:]', ohashi01[1][2])[3])*3600
    l_day = int(re.split('[- /:]', ohashi01[1][2])[2])*24*3600
    l_start = (l_sec+l_min+l_hou+l_day)

    g_sec = int(re.split('[- /:]', ohashi02[1][2])[5])
    g_min = int(re.split('[- /:]', ohashi02[1][2])[4])*60
    g_hou = int(re.split('[- /:]', ohashi02[1][2])[3])*3600
    g_day = int(re.split('[- /:]', ohashi02[1][2])[2])*24*3600
    g_start = (g_sec+g_min+g_hou+g_day)
    g_start = (g_sec+g_min+g_hou+g_day)

    living_data=[]
    for i in range(1,len(ohashi01)-1):
        #print(l_data[i])
        living_data.append(ohashi01[i])
        diff = int(ohashi01[i+1][1])-int(ohashi01[i][1])

         #値が取れなかった間隔
        if(diff<3600):
            while diff > 3:
                diff -= 3
                add = l_start+int(ohashi01[i+1][1])-diff
                day = add//(24*3600)
                if(day<=9):
                    day = str("0"+str(day))
                else:
                    day = str(day)
                add = add%(24*3600)

                hou = add//3600
                if(hou<=9):
                    hou = str("0"+str(hou))
                else:
                    hou = str(hou)
                add = add%3600

                min = add//60
                if(min<=9):
                    min = str("0"+str(min))
                else:
                    min = str(min)
                sec = add%60
                if(sec<=9):
                    sec = str("0"+str(sec))
                else:
                    sec = str(sec)
                
                date = ohashi01[i][2][0:8] + str(day)+ " "+str(hou)+":"+str(min)+":"+str(sec)
                data = ["ohashi01",int(ohashi01[i+1][1])-diff,date,"-110"]
                living_data.append(data)

            
    genkan_data=[]
    for i in range(1,len(ohashi02)-1):
        #print(l_data[i])
        genkan_data.append(ohashi02[i])
        diff = int(ohashi02[i+1][1])-int(ohashi02[i][1])

        #値が取れなかった間隔
        if(diff<3600):
            while diff > 3:
                diff -= 3
                add = g_start+int(ohashi02[i+1][1])-diff
                day = add//(24*3600)
                if(day<=9):
                    day = str("0"+str(day))
                else:
                    day = str(day)
                add = add%(24*3600)

                hou = add//3600
                if(hou<=9):
                    hou = str("0"+str(hou))
                else:
                    hou = str(hou)
                add = add%3600

                min = add//60
                if(min<=9):
                    min = str("0"+str(min))
                else:
                    min = str(min)
                sec = add%60
                if(sec<=9):
                    sec = str("0"+str(sec))
                else:
                    sec = str(sec)
                
                date = ohashi02[i][2][0:8] + str(day)+ " "+str(hou)+":"+str(min)+":"+str(sec)
                data = ["ohashi02",str(int(ohashi02[i+1][1])-diff),date,"-110"]
                genkan_data.append(data)

    response = requests.get(GET_DATE_URL)
    date = response.json()
    date.reverse()
    latest = datetime.strptime(date[0]["time"], '%Y-%m-%d %H:%M:%S')
    last_time = latest
    for i in range(len(living_data)):
        # print(living_data,last_time)
        for j in range(len(genkan_data)):
            if living_data[i][1]==genkan_data[j][1]:
                place=""
                num=0
                if i<=len(genkan_data) and genkan_data[j][3] :
                    if living_data[i][3]=='-110' and genkan_data[j][3]=='-110':
                        place = "圏外" # 0は圏外（外出）
                    elif int(living_data[i][3])>int(genkan_data[j][3]):
                        place = "リビング" # 2はリビング
                        num=2
                    elif int(living_data[i][3])<=int(genkan_data[j][3]):
                        place = "玄関" # 1は玄関
                        num=1
                else :
                    place = ""
                
                #print(living_data[i][1],living_data[i][2],living_data[i][3],genkan_data[j][3],place)


                request_body = {"count": living_data[i][1] ,
                "time": living_data[i][2],    
                "rssi1": living_data[i][3],
                "rssi2": genkan_data[j][3],
                "place": place,
                "place_num": num 
                }
                
                date = datetime.strptime(list(request_body.items())[1][1], '%Y-%m-%d %H:%M:%S')
                if (last_time<date):
                    last_time = date
                    response = requests.post(POST_URL, json=request_body)
        j+=1
    print("-------------------")

if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    wallet_data()

print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する