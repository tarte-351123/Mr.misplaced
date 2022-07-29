import requests
import pprint
import datetime
from datetime import datetime
import csv

POST_URL = "http://localhost:8000/result_phone/"
filename = '../csv/result_phone.csv'

pattern = []
# 配列のコピー
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        pattern.append(row)

for i in pattern:
    print(i)
    # リクエストボディを定義する
    request_body = {
        
    }


# POSTリクエストを、リクエストボディ付きで送信する
# response = requests.post(POST_URL, json=request_body)

# レスポンスボディを出力する
pprint.pprint(response.json())