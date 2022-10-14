from requests import request
import datetime

def data_fix():
    import requests
    GET_URL = "http://localhost:8000/result_phone/" 
    POST_URL = "http://localhost:8000/result_phone/" 

    response = requests.get(GET_URL)
    data = response.json()
  
    base_data=[]
    #データのこぴー
    for row in data:
        base_data.append(row)

    for i in range(len(data)):
        requests.delete(POST_URL)
        
    for i in range(len(base_data)-1):
        diff = base_data[i+1]["count"]-base_data[i]["count"]
        if diff!=3 and diff<3600:
            mydate = datetime.datetime.strptime(base_data[i]["time"], '%Y-%m-%d %H:%M:%S')
            td_3s = datetime.timedelta(seconds=3)
            data = {'count': base_data[i]["count"]+3, 'time': str(mydate+td_3s), 'rssi1': -110, 'rssi2': -110, 'place': base_data[i]["place"], 'place_num':0}
            base_data.insert(i+1, data)
          
    count = 0
    for i in range (0,5):
        list = (base_data[0]["place"],base_data[1]["place"],base_data[2]["place"],base_data[3]["place"],base_data[4]["place"],base_data[5]["place"],base_data[6]["place"])
        if list.count("リビング")>=3:
            place ="リビング"
            num=2
        elif list.count("玄関")>=3:
            place ="玄関"
            num=1
        elif list.count("圏外")>=3:
            place ="圏外"
            num=0
        data_list = [base_data[i]["count"],base_data[i]["time"],base_data[i]["rssi1"],base_data[i]["rssi2"],place,num]
        request_body = {"count": base_data[i]["count"] ,
                "time": base_data[i]["time"],    
                "rssi1": base_data[i]["rssi1"],
                "rssi2": base_data[i]["rssi2"],
                "place": place,
                "place_num": num 
                }
        response = requests.post(POST_URL,json=request_body)

    for i in range(6,len(base_data)):
        place = ""
        num = 0
        list = (base_data[i-6]["place"],base_data[i-5]["place"],base_data[i-4]["place"],base_data[i-3]["place"],base_data[i-2]["place"],base_data[i-1]["place"],base_data[i]["place"])
        if list.count("リビング")>=3:
            place ="リビング"
            num=2
        elif list.count("玄関")>=3:
            place ="玄関"
            num=1
        elif list.count("圏外")>=3:
            place ="圏外"
            num=0
        else:
            place = base_data[i]["place"]
            num = base_data[i]["place_num"]

        count +=1
        
        request_body = {"count": base_data[i]["count"] ,
                "time": base_data[i]["time"],    
                "rssi1": base_data[i]["rssi1"],
                "rssi2": base_data[i]["rssi2"],
                "place": place,
                "place_num": num 
                }
        data_list = [base_data[i]["count"],base_data[i]["time"],base_data[i]["rssi1"],base_data[i]["rssi2"],place,num]
        response = requests.post(POST_URL,json=request_body)


    GET_URL = "http://localhost:8000/result_wallet/" 
    POST_URL = "http://localhost:8000/result_wallet/" 

    response = requests.get(GET_URL)
    data = response.json()
  
    base_data=[]
    #データのこぴー
    for row in data:
        base_data.append(row)

    for i in range(len(data)):
        requests.delete(POST_URL)
        
    for i in range(len(base_data)-1):
        diff = base_data[i+1]["count"]-base_data[i]["count"]
        if diff!=3 and diff<3600:
            mydate = datetime.datetime.strptime(base_data[i]["time"], '%Y-%m-%d %H:%M:%S')
            td_3s = datetime.timedelta(seconds=3)
            data = {'count': base_data[i]["count"]+3, 'time': str(mydate+td_3s), 'rssi1': -110, 'rssi2': -110, 'place': base_data[i]["place"], 'place_num':0}
            base_data.insert(i+1, data)
          
    count = 0
    for i in range (0,5):
        list = (base_data[0]["place"],base_data[1]["place"],base_data[2]["place"],base_data[3]["place"],base_data[4]["place"],base_data[5]["place"],base_data[6]["place"])
        if list.count("リビング")>=3:
            place ="リビング"
            num=2
        elif list.count("玄関")>=3:
            place ="玄関"
            num=1
        elif list.count("圏外")>=3:
            place ="圏外"
            num=0
        data_list = [base_data[i]["count"],base_data[i]["time"],base_data[i]["rssi1"],base_data[i]["rssi2"],place,num]
        request_body = {"count": base_data[i]["count"] ,
                "time": base_data[i]["time"],    
                "rssi1": base_data[i]["rssi1"],
                "rssi2": base_data[i]["rssi2"],
                "place": place,
                "place_num": num 
                }
        response = requests.post(POST_URL,json=request_body)

    for i in range(6,len(base_data)):
        place = ""
        num = 0
        list = (base_data[i-6]["place"],base_data[i-5]["place"],base_data[i-4]["place"],base_data[i-3]["place"],base_data[i-2]["place"],base_data[i-1]["place"],base_data[i]["place"])
        if list.count("リビング")>=3:
            place ="リビング"
            num=2
        elif list.count("玄関")>=3:
            place ="玄関"
            num=1
        elif list.count("圏外")>=3:
            place ="圏外"
            num=0
        else:
            place = base_data[i]["place"]
            num = base_data[i]["place_num"]

        count +=1
        
        request_body = {"count": base_data[i]["count"] ,
                "time": base_data[i]["time"],    
                "rssi1": base_data[i]["rssi1"],
                "rssi2": base_data[i]["rssi2"],
                "place": place,
                "place_num": num 
                }
        response = requests.post(POST_URL,json=request_body)
    

    GET_URL = "http://localhost:8000/result_bag/" 
    POST_URL = "http://localhost:8000/result_bag/" 

    response = requests.get(GET_URL)
    data = response.json()
  
    base_data=[]
    #データのこぴー
    for row in data:
        base_data.append(row)

    for i in range(len(data)):
        requests.delete(POST_URL)
        
    for i in range(len(base_data)-1):
        diff = base_data[i+1]["count"]-base_data[i]["count"]
        if diff!=3 and diff<3600:
            mydate = datetime.datetime.strptime(base_data[i]["time"], '%Y-%m-%d %H:%M:%S')
            td_3s = datetime.timedelta(seconds=3)
            data = {'count': base_data[i]["count"]+3, 'time': str(mydate+td_3s), 'rssi1': -110, 'rssi2': -110, 'place': base_data[i]["place"], 'place_num':0}
            base_data.insert(i+1, data)
          
    count = 0
    for i in range (0,5):
        list = (base_data[0]["place"],base_data[1]["place"],base_data[2]["place"],base_data[3]["place"],base_data[4]["place"],base_data[5]["place"],base_data[6]["place"])
        if list.count("リビング")>=3:
            place ="リビング"
            num=2
        elif list.count("玄関")>=3:
            place ="玄関"
            num=1
        elif list.count("圏外")>=3:
            place ="圏外"
            num=0
        data_list = [base_data[i]["count"],base_data[i]["time"],base_data[i]["rssi1"],base_data[i]["rssi2"],place,num]
        request_body = {"count": base_data[i]["count"] ,
                "time": base_data[i]["time"],    
                "rssi1": base_data[i]["rssi1"],
                "rssi2": base_data[i]["rssi2"],
                "place": place,
                "place_num": num 
                }
        response = requests.post(POST_URL,json=request_body)

    for i in range(6,len(base_data)):
        place = ""
        num = 0
        list = (base_data[i-6]["place"],base_data[i-5]["place"],base_data[i-4]["place"],base_data[i-3]["place"],base_data[i-2]["place"],base_data[i-1]["place"],base_data[i]["place"])
        if list.count("リビング")>=3:
            place ="リビング"
            num=2
        elif list.count("玄関")>=3:
            place ="玄関"
            num=1
        elif list.count("圏外")>=3:
            place ="圏外"
            num=0
        else:
            place = base_data[i]["place"]
            num = base_data[i]["place_num"]

        count +=1
        
        request_body = {"count": base_data[i]["count"] ,
                "time": base_data[i]["time"],    
                "rssi1": base_data[i]["rssi1"],
                "rssi2": base_data[i]["rssi2"],
                "place": place,
                "place_num": num 
                }
        response = requests.post(POST_URL,json=request_body)    
    print("--------------")

if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    data_fix()

print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する