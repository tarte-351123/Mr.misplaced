import requests
import pprint
import datetime
from datetime import datetime

POST_URL = "http://localhost:8000/cluster/"


# リクエストボディを定義する
request_body = {
    "dateType": "平日",
    "normalDistribution": {
        "mean": "",
        "std": "",
        "range": [{
        "from_": "",
        "to_": ""
        },
        {
        "from": "",
        "to": ""
        }, 
        {
        "from": "",
        "to": ""
        }, ]
    },
    "model": [{
        "object": "スマホと財布",
        "percentage": "%"
        },
        {
        "object": "財布とカバン",
        "percentage": "%" 
        },
        {
        "object": "カバンとスマホ",
        "percentage": "%"
        },
    ]
}


# POSTリクエストを、リクエストボディ付きで送信する
response = requests.post(POST_URL, json=request_body)

# レスポンスボディを出力する
pprint.pprint(response.json())