def pattern():
    import datetime
    import locale
    import requests
    import pprint
    import math
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
        #print(row)

    w_data=[]
    response = requests.get(GET_URL_W)
    data = response.json()
    for row in data:
        w_data.append(row)
        #print(row)

    b_data=[]
    response = requests.get(GET_URL_B)
    data = response.json()
    for row in data:
        b_data.append(row)
        # print(row)
        
    # スマホのデータ        
    start = p_data[0]["time"]
    end = ""
    fix_p_data = []
    for i in range(len(p_data)-1):
        place =p_data[i]["place"]
        if p_data[i+1]["count"]-p_data[i]["count"]>=360 and p_data[i+1]["place"]!="リビング" and p_data[i]["place"]!="リビング":
            end = p_data[i]["time"]
            data = [end,p_data[i+1]["time"],"phone"]
            fix_p_data.append(data)
            start = p_data[i+1]["time"]
        elif p_data[i+1]["count"]-p_data[i]["count"]>=360:
            if place=="圏外":
                data = [end,p_data[i+1]["time"],"phine"]
                fix_p_data.append(data)
        elif p_data[i]["place"]=="圏外"and p_data[i+1]["place"]!="圏外":
            end = p_data[i+1]["time"]
            a=datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
            b=datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
            diff = a-b
            if diff.seconds>360:
                data = [start,end,"phone"]
                fix_p_data.append(data)
            
        if place!=p_data[i+1]["place"]:
            start = p_data[i+1]["time"]


    #財布のデータ
    start = w_data[0]["time"]
    end = ""
    fix_w_data = []
    for i in range(len(w_data)-1):
        place = w_data[i]["place"]
        if w_data[i+1]["count"]-w_data[i]["count"]>=360 and w_data[i+1]["place"]!="リビング" and w_data[i]["place"]!="リビング":
            end = w_data[i]["time"]
            data = [end,w_data[i+1]["time"],"wallet"]
            fix_w_data.append(data)
            start = w_data[i+1]["time"]
        elif w_data[i+1]["count"]-w_data[i]["count"]>=360:
            #print(w_data[i]["time"],w_data[i+1]["time"],place,"b")
            if place=="玄関":
                data = [end,w_data[i+1]["time"],"wallet"]
                fix_w_data.append(data)
        elif w_data[i]["place"]=="圏外"and w_data[i+1]["place"]!="圏外":
            end = w_data[i+1]["time"]
            a=datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
            b=datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
            diff = a-b
            if diff.seconds>360:
                data = [start,end,"wallet"]
                fix_w_data.append(data)
            
        if place!=w_data[i+1]["place"]:
            start = w_data[i+1]["time"]
                
    # 通学用カバンのデータ     
    start = b_data[0]["time"]
    end = ""
    fix_b_data = []
    for i in range(len(b_data)-1):
        place = b_data[i]["place"]
        if b_data[i+1]["count"]-b_data[i]["count"]>=360 and b_data[i+1]["place"]!="リビング" and b_data[i]["place"]!="リビング":
            end = b_data[i]["time"]
            data = [end,b_data[i+1]["time"],"bag"]
            fix_b_data.append(data)
            start = b_data[i+1]["time"]
        elif b_data[i+1]["count"]-b_data[i]["count"]>=360:
            if place=="圏外":
                data = [end,b_data[i+1]["time"],"bag"]
                fix_b_data.append(data)
        elif b_data[i]["place"]=="圏外"and b_data[i+1]["place"]!="圏外":
            end = b_data[i+1]["time"]
            a=datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
            b=datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
            diff = a-b
            if diff.seconds>360:
                data = [start,end,"bag"]
                fix_b_data.append(data)
            
        if place!=b_data[i+1]["place"]:
            start = b_data[i+1]["time"]
            
    go_out_data = [] 
       
    for i in fix_p_data:
        go_out_data.append(i)
    for i in fix_w_data:
        go_out_data.append(i)
    for i in fix_b_data:
        go_out_data.append(i)
        
    std = sorted(go_out_data, key=lambda x: x[0])
    time_range = 120
    obj = []
    time_list = []

    latest=datetime.datetime.strptime(std[0][0], '%Y-%m-%d %H:%M:%S')
    for i in range(len(std)-1):
        start=datetime.datetime.strptime(std[i][0], '%Y-%m-%d %H:%M:%S')
        end=datetime.datetime.strptime(std[i][1], '%Y-%m-%d %H:%M:%S')
        diff = datetime.datetime.strptime(std[i+1][0], '%Y-%m-%d %H:%M:%S')-start
        if diff.seconds<=300:
            obj.append(std[i][2])

        else:
            obj.append(std[i][2])
            locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
            year = start.year
            month = start.month
            day = start.day
            date = datetime.date(year, month, day)
            hour = str(start.hour).zfill(2)
            minute = str(math.floor(0.1*start.minute)*10).zfill(2)
            request_body = {
                "start_time": std[i][0],    
                "end_time": std[i][1],
                "date": date.strftime('%A'),
                "time": hour+":"+minute,
                "object": str(obj) 
                }
            print(request_body)
            response = requests.post(POST_URL,json=request_body)
            obj = []
            time_list= []
    if obj!=[]:
        obj.append(std[len(std)-1][2])
        start = datetime.datetime.strptime(std[len(std)-1][0], '%Y-%m-%d %H:%M:%S')
        end=datetime.datetime.strptime(std[i][1], '%Y-%m-%d %H:%M:%S')
        locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
        year = start.year
        month = start.month
        day = start.day
        date = datetime.date(year, month, day)
        hour = str(start.hour).zfill(2)
        minute = str(math.floor(0.1*start.minute)*10).zfill(2)
        request_body = {
            "start_time": std[i][0],    
            "end_time": std[i][1],
            "date": date.strftime('%A'),
            "time": hour+":"+minute,
            "object": str(obj) 
            }
        print(request_body)
        response = requests.post(POST_URL,json=request_body)
    

if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    pattern()

print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する
        
