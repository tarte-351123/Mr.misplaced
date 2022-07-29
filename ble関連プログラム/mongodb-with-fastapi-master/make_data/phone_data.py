from attr import s


def phone_data():
    import requests
    import csv
    from pymongo import MongoClient
    import requests
    import datetime
    from datetime import datetime

    GET_URL = "http://localhost:8000/phone/"
    POST_URL = "http://localhost:8000/result_phone/"
    GET_DATE_URL = "http://localhost:8000/date/"
    POST_DATE_URL = "http://localhost:8000/date/"

    # for i in range (5):
    #     delete = requests.delete(GET_URL)


    # POSTリクエストを、リクエストボディ付きで送信する
    response = requests.get(GET_URL)

    # dataというList型変数に全てのデータを格納
    data = response.json()
    #data.reverse()


    #より近いラズパイの hostname を格納
    near = ""
    last_time = ""
    with open("csv/ohashi01_phone.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                tag = (["hostname","count", "time","rssi"])
                writer.writerow(tag)
    with open("csv/ohashi02_phone.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                tag = (["hostname","count","time", "rssi"])
                writer.writerow(tag)
    with open("csv/result_phone.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                tag = (["count","time","living_rssi","genkan_rssi","result"])

    day = int(data[0]["time"][8:10])*3600*24
    hour = int(data[0]["time"][11:13])*3600
    minute = int(data[0]["time"][14:16])*60
    second = int(data[0]["time"][17:20])
    start_time = day+hour + minute +second
    n1=0
    n2=0
    result=0

    count = 1

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
            with open("csv/ohashi01_phone.csv", "a", newline="", encoding="utf8") as f:

                writer = csv.writer(f)
                data_list = [i["hostname"], time_diff, i["time"], i["rssi"]]
                writer.writerow(data_list)
                n1 +=3

        elif i["hostname"]=="ohashi02":
            with open("csv/ohashi02_phone.csv", "a", newline="", encoding="utf8") as f:

                writer = csv.writer(f)
                data_list = [i["hostname"], time_diff, i["time"], i["rssi"]]
                writer.writerow(data_list)
                n2 +=3
        if count < len(data)-3:
                count +=1

    f.close()
            

    import csv
    import re
    with open("csv/ohashi01_phone.csv", encoding='utf-8', newline='') as f:
        csvreader = csv.reader(f)
        l_data=[]
        #データのこぴー
        for row in csvreader:
            l_data.append(row)

    with open("csv/ohashi02_phone.csv", encoding='utf-8', newline='') as f:
        csvreader = csv.reader(f)
        g_data=[]
        #データのこぴー
        for row in csvreader:
            g_data.append(row)


    l_sec = int(re.split('[- /:]', l_data[1][2])[5])
    l_min = int(re.split('[- /:]', l_data[1][2])[4])*60
    l_hou = int(re.split('[- /:]', l_data[1][2])[3])*3600
    l_day = int(re.split('[- /:]', l_data[1][2])[2])*24*3600
    l_start = (l_sec+l_min+l_hou+l_day)

    g_sec = int(re.split('[- /:]', g_data[1][2])[5])
    g_min = int(re.split('[- /:]', g_data[1][2])[4])*60
    g_hou = int(re.split('[- /:]', g_data[1][2])[3])*3600
    g_day = int(re.split('[- /:]', g_data[1][2])[2])*24*3600
    g_start = (g_sec+g_min+g_hou+g_day)

    living_data=[]
    for i in range(1,len(l_data)-1):
        #print(l_data[i])
        living_data.append(l_data[i])
        diff = int(l_data[i+1][1])-int(l_data[i][1])

        #値が取れなかった間隔
        if(diff<3600):
            while diff > 3:
                diff -= 3
                add = l_start+int(l_data[i+1][1])-diff
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
                
                date = l_data[i][2][0:8] + str(day)+ " "+str(hou)+":"+str(min)+":"+str(sec)
                data = ["ohashi01",str(int(l_data[i+1][1])-diff),date,"-110"]
                living_data.append(data)

            
    genkan_data=[]
    for i in range(1,len(g_data)-1):
        #print(l_data[i])
        genkan_data.append(g_data[i])
        diff = int(g_data[i+1][1])-int(g_data[i][1])

        #値が取れなかった間隔
        while diff > 3:
            diff -= 3
            add = g_start+int(g_data[i+1][1])-diff
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
            
            date = g_data[i][2][0:8] + str(day)+ " "+str(hou)+":"+str(min)+":"+str(sec)
            data = ["ohashi01",str(int(g_data[i+1][1])-diff),date,"-110"]
            genkan_data.append(data)

    response = requests.get(GET_DATE_URL)
    date = response.json()
    date.reverse()
    latest = datetime.strptime(date[0]["time"], '%Y-%m-%d %H:%M:%S')
    last_time = latest
    for i in range(len(living_data)):
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

                with open("csv/result_phone.csv", "a", newline="", encoding="utf8") as f:

                    writer = csv.writer(f)
                    data_list = [living_data[i][1],living_data[i][2],living_data[i][3],genkan_data[j][3],place,num]
                    writer.writerow(data_list)

                request_body = {"count": living_data[i][1] ,
                "time": living_data[i][2],    
                "rssi1": living_data[i][3],
                "rssi2": genkan_data[j][3],
                "place": place,
                "place_num": num 
                }
                
                date = datetime.strptime(list(request_body.items())[1][1], '%Y-%m-%d %H:%M:%S')
                if (latest<date):
                    latest = date
                    response = requests.post(POST_URL, json=request_body)

        j+=1
    print("-------------------")

if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    phone_data()

print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する
