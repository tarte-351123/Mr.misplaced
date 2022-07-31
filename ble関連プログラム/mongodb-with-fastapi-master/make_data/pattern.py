def pattern():
    import csv
    import datetime
    import locale
    import requests
    import pprint
    import pandas as pd

    GET_URL_P = "http://localhost:8000/result_phone/"
    GET_URL_W = "http://localhost:8000/result_wallet/"
    GET_URL_B = "http://localhost:8000/result_bag/"
    GET_URL_T = "http://localhost:8000/date/"
    POST_URL = "http://localhost:8000/pattern/"

    response = requests.get(GET_URL_T)
    
    
    
    #データのこぴー
    p_data=[]
    response = requests.get(GET_URL_P)
    data = response.json()
    for row in data:
        p_data.append(row)

    w_data=[]
    response = requests.get(GET_URL_W)
    data = response.json()
    for row in data:
        w_data.append(row)

    b_data=[]
    response = requests.get(GET_URL_B)
    data = response.json()
    for row in data:
        b_data.append(row)

    # スマホのデータ        
    start = p_data[0]["time"]
    end = ""
    fix_p_data = []
    for i in range(len(p_data)-1):
        place = p_data[i]["place"]
        if(int(p_data[i+1]["count"])-int(p_data[i]["count"])>3):
            if(p_data[i+1]["place"]=="圏外" and place=="圏外"):
                end = p_data[i+1]["time"]
            else:
                data = [str(start) ,str(p_data[i]["time"]),place]
                fix_p_data.append(data)
            start = p_data[i+1]["time"]

        if place != p_data[i+1]["place"]:
            data = [str(start), str(p_data[i+1]["time"]), place]
            fix_p_data.append(data)
            start = p_data[i+1]["time"]

        if int(i) == int(len(p_data)-2):
            end = p_data[i+1]["time"]
            # print(start,end)
            if start !=end:
                data = [str(start) ,str(end),place]
                fix_p_data.append(data)

    for i in range (len(fix_p_data)+2):
        if fix_p_data[i][1] != fix_p_data[i+1][0] and fix_p_data[i+1][2]=="圏外":
            data = [str(fix_p_data[i][1]),str(fix_p_data[i+1][1]),place]
            del fix_p_data[i+1]
            fix_p_data.insert(i,data)

        if fix_p_data[i][1] != fix_p_data[i+1][0]:
            data = [str(fix_p_data[i][1]),str(fix_p_data[i+1][0]),"圏外"]
            fix_p_data.insert(i+1,data)

    #財布のデータ
    start = w_data[0]["time"]
    end = ""
    fix_w_data = []
    for i in range(len(w_data)-1):
        place = w_data[i]["place"]

        # print(w_data[i],start)

        if(int(w_data[i+1]["count"])-int(w_data[i]["count"])>3):
            data = [str(start), str(w_data[i]["time"]), place]
            fix_w_data.append(data)

            start = w_data[i+1]["time"]

        if place != w_data[i+1]["place"]:
            data = [str(start), str(w_data[i+1]["time"]), place]
            fix_w_data.append(data)
            start = w_data[i+1]["time"]
        
        if int(i) == int(len(w_data)-2):
            end = w_data[i+1]["time"]
            # print(start,end)
            data = [str(start) ,str(end),place]
            fix_w_data.append(data)

    for i in range (len(fix_w_data)+2):
        if fix_w_data[i][1] != fix_w_data[i+1][0]:
            data = [str(fix_w_data[i][1]),str(fix_w_data[i+1][0]),"圏外"]
            fix_w_data.insert(i+1,data)


    # 通学用カバンのデータ        
    start = b_data[0]["time"]
    end = ""
    fix_b_data = []
    for i in range(len(b_data)-1):
        place = b_data[i]["place"]
        if(int(b_data[i+1]["count"])-int(b_data[i]["count"])>3):
            if(b_data[i+1]["place"]=="圏外" and place=="圏外"):
                end = b_data[i+1]["time"]
            else:
                data = [str(start) ,str(b_data[i]["time"]),place]
                fix_b_data.append(data)

            start = b_data[i+1]["time"]
        
        if place != b_data[i+1]["place"]:
            data = [str(start), str(b_data[i+1]["time"]), place]
            fix_b_data.append(data)
            start = b_data[i+1]["time"]

        if int(i) == int(len(b_data)-2):
            end = b_data[i+1]["time"]
            # print(start,end)
            data = [str(start) ,str(end),place]
            fix_b_data.append(data)
    print(fix_b_data)
        
    for i in range (len(fix_b_data)+2):
        if fix_b_data[i][1] != fix_b_data[i+1][0]:
            data = [str(fix_b_data[i][1]),str(fix_b_data[i+1][0]),"圏外"]
            fix_b_data.insert(i+1,data)

    # print("This is phone data.")
    # for i in (fix_p_data):
    #     print(i)
    # print("---------")
    # print("This is wallet data.")
    # for i in (fix_w_data):
    #     print(i)
    # print("-------------")
    # print("This is bag data.")
    # for i in (fix_b_data):
    #     print(i)


    # print()
    # 何が一緒にいたかを出力する
    # print("スマホ")

    pattern_wallet_data = []
    time_p=0
    for i in fix_p_data:
        day = int(i[0][8:10])*3600*24
        hour = int(i[0][11:13])*3600
        minute = int(i[0][14:16])*60
        second = int(i[0][17:20])
        start_time_p = day+hour + minute +second
        day = int(i[1][8:10])*3600*24
        hour = int(i[1][11:13])*3600
        minute = int(i[1][14:16])*60
        second = int(i[1][17:20])
        end_time_p = day+hour + minute +second
        
        for j in fix_w_data:
            
            day = int(j[0][8:10])*3600*24
            hour = int(j[0][11:13])*3600
            minute = int(j[0][14:16])*60
            second = int(j[0][17:20])
            start_time_w = day+hour + minute +second
            day = int(j[1][8:10])*3600*24
            hour = int(j[1][11:13])*3600
            minute = int(j[1][14:16])*60
            second = int(j[1][17:20])
            end_time_w = day+hour + minute +second 

            #print(start_time_p,start_time_w,end_time_p)
            if start_time_p <= start_time_w and start_time_w<=end_time_p :
                start_time = start_time_w
                start_stamp = j[0]
                place = i[2]
            elif start_time_p <= start_time_w and start_time_w<=end_time_p:
                start_time = start_time_p
                start_stamp = i[0]
            elif start_time_w <=start_time_p:
                start_time = start_time_p
                start_stamp = i[0]
                place = i[2]
                
            if end_time_w <= end_time_p and start_time_p<=end_time_w :
                end_time = end_time_w
                end_stamp = j[1]
                place = i[2]
            elif end_time_w <= end_time_p and start_time_p<=end_time_w:
                end_time = end_time_p
                end_stamp = i[1]
                place = i[2]
            elif end_time_p <= end_time_w:
                end_time = end_time_p
                end_stamp = i[1]

        # print(start_time,end_time,place)
        data = [start_stamp,end_stamp,place]
        pattern_wallet_data.append(data)
        # print(data)        
        place =""

    # print()

    # 各項目の外出履歴を出力

    go_out = 0
    go_out_data = []
    # print()
    for i in range (len(fix_p_data)):
        start = int(fix_p_data[i][0][11:13])*3600+int(fix_p_data[i][0][14:16])*60+int(fix_p_data[i][0][17:19])
        end = int(fix_p_data[i][1][11:13])*3600+int(fix_p_data[i][1][14:16])*60+int(fix_p_data[i][1][17:19])
        if(fix_p_data[i][2]=="圏外" and end!=start and end-start>=10):
            go_out += 1 
            #print(fix_p_data[i][1])
            year = int(fix_p_data[i][0][0:4])
            month = int(fix_p_data[i][0][5:7])
            day = int(fix_p_data[i][0][8:10])
            hour = (fix_p_data[i][0][11:13])

            date = datetime.date(year, month, day)
            locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
            #print(date.strftime('%Y-%m-%d'))
            #print(date.strftime('%A')+hour+"時")
            day = int(fix_p_data[i+1][0][8:10])*3600*24
            hour = int(fix_p_data[i+1][0][11:13])*3600
            minute = int(fix_p_data[i+1][0][14:16])*60
            second = int(fix_p_data[i+1][0][17:20])
            start_time = day+hour + minute +second
            data_list = [fix_p_data[i][0],fix_p_data[i][1],start_time ,"phone"]
            # print(data_list)
            go_out_data.append(data_list)
            

    # print("スマホは"+str(go_out)+"回外出を検知しました。")
    # print("------------")

    go_out = 0
    # print()
    for i in range (len(fix_w_data)):
        start = int(fix_w_data[i][0][11:13])*3600+int(fix_w_data[i][0][14:16])*60+int(fix_w_data[i][0][17:19])
        end = int(fix_w_data[i][1][11:13])*3600+int(fix_w_data[i][1][14:16])*60+int(fix_w_data[i][1][17:19])
        if(fix_w_data[i][2]=="圏外" and end!=start and end-start>=10):
            go_out += 1 
            #print(fix_w_data[i][1])
            year = int(fix_w_data[i][0][0:4])
            month = int(fix_w_data[i][0][5:7])
            day = int(fix_w_data[i][0][8:10])
            hour = (fix_w_data[i][0][11:13])

            date = datetime.date(year, month, day)
            locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
            #print(date.strftime('%Y-%m-%d'))
            #print(date.strftime('%A')+hour+"時") 
            day = int(fix_w_data[i+1][0][8:10])*3600*24
            hour = int(fix_w_data[i+1][0][11:13])*3600
            minute = int(fix_w_data[i+1][0][14:16])*60
            second = int(fix_w_data[i+1][0][17:20])

            start_time = day+hour + minute +second
            
            data_list = [fix_w_data[i][0],fix_w_data[i][1],start_time, "wallet"]
            # print(data_list)
            go_out_data.append(data_list)
                

    # print("財布は"+str(go_out)+"回外出を検知しました。")
    # print("------------")
    go_out = 0
    # print()
    for i in range (len(fix_b_data)):
        start = int(fix_b_data[i][0][11:13])*3600+int(fix_b_data[i][0][14:16])*60+int(fix_b_data[i][0][17:19])
        end = int(fix_b_data[i][1][11:13])*3600+int(fix_b_data[i][1][14:16])*60+int(fix_b_data[i][1][17:19])
        if(fix_b_data[i][2]=="圏外" and end!=start and end-start>=60):
            go_out += 1 
            #print(fix_b_data[i][1])
            year = int(fix_b_data[i][0][0:4])
            month = int(fix_b_data[i][0][5:7])
            day = int(fix_b_data[i][0][8:10])
            hour = (fix_b_data[i][0][11:13])

            date = datetime.date(year, month, day)
            locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
            #print(date.strftime('%Y-%m-%d'))
            #print(date.strftime('%A')+hour+"時") 

            day = int(fix_b_data[i+1][0][8:10])*3600*24
            hour = int(fix_b_data[i+1][0][11:13])*3600
            minute = int(fix_b_data[i+1][0][14:16])*60
            second = int(fix_b_data[i+1][0][17:20])
            start_time = day+hour + minute +second 
            data_list = [fix_b_data[i][0],fix_b_data[i][1],start_time, "bag"]
            # print(data_list)
            go_out_data.append(data_list)
            

    # print("カバンは"+str(go_out)+"回外出を検知しました。")
    # print("------------")

    # 何が一緒にいたかを出力するgesu
    # print("複数持ち歩いての外出")

    pattern_data = []
    time=0

        
    # print()
    std = sorted(go_out_data, key=lambda x: x[0])

    time_range = 120
    obj = []
    time_list = []
    data_list = []
    for i in range(len(std)-2):
       # print(std[i])
        obj.append(std[i][3])
        time_list.append(std[i][1])
        time_list.sort
        if std[i+1][2]-std[i][2]>time_range:
            year = int(std[i][0][0:4])
            month = int(std[i][0][5:7])
            day = int(std[i][0][8:10])
            hour = str(std[i][0][11:13])
            minute = int(std[i][0][14:16])
            minute = (int(minute/10))

            minute = f'{(minute*10):02}'  # 0埋めで4文字
            date = datetime.date(year, month, day)
            
            locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
            # print("          ⏬            ")
            
            request_body = {
                "start_time": std[i][0],    
                "end_time": time_list[0],
                "date": date.strftime('%A'),
                "time": hour+":"+minute,
                "object": str(obj) 
                }
            response = requests.post(POST_URL,json=request_body)
            obj = []
            time_list= []
    

if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    pattern()

print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する
        
