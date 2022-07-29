def time_save():
    import requests
    from datetime import datetime

    GET_URL = "http://localhost:8000/result_phone/"
    GET_TIME_URL = "http://localhost:8000/date/"
    POST_URL = "http://localhost:8000/date/"
    response = requests.get(GET_URL)
    data = response.json()
    base_data=[]
    #データのこぴー
    for row in data:
        base_data.append(row)

    response = requests.get(GET_TIME_URL)
    data = response.json()
    data.reverse()
    latest = datetime.strptime(data[0]["time"],'%Y-%m-%d %H:%M:%S')
    for i in  base_data:
        dt = datetime.strptime(i["time"],'%Y-%m-%d %H:%M:%S')
        if latest<dt:
            latest = dt
    request_body = {
                "time": str(latest)
                }
    response =  requests.post(POST_URL,json=request_body)

    print(latest)
if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    time_save()

print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する