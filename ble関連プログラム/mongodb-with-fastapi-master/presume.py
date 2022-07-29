import requests
from datetime import datetime

GET_URL1 = "http://localhost:8000/result_phone/"
GET_URL2 = "http://localhost:8000/cluster/"

response = requests.get(GET_URL2)
data = response.json()

sample_data_type = "平日"
sample_time_data = "19:20"
sample_time = int(sample_time_data[0:2])*60+int(sample_time_data[3:5])
print(sample_time_data)
data_list = []
for i in data:
    list = i["dateType"],int(i["normalDistribution"]["range"][2]["from_"][0:2])*60+int(i["normalDistribution"]["range"][2]["from_"][3:5]),int(i["normalDistribution"]["range"][2]["to_"][0:2])*60+int(i["normalDistribution"]["range"][2]["to_"][3:5])
    if sample_data_type == list[0] and list[1]<=sample_time and sample_time<=list[2]:
        print("cluster!")
        print(i["dateType"])
        print(i["normalDistribution"]["range"][2])
        for i in i["model"]:
            print(i)

