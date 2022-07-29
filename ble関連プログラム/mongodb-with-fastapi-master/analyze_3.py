
# 曜日ごとに

from __future__ import print_function
from calendar import WEDNESDAY
import csv
from re import M
import math
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from datetime import datetime as dt
from matplotlib import dates as mdates
import japanize_matplotlib

filename = 'csv/go_out.csv'

pattern = []
# 配列のコピー
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        pattern.append(row)


time_count_sun = [0]*24 
time_count_mon = [0]*24 
time_count_tue = [0]*24 
time_count_wed = [0]*24 
time_count_thu = [0]*24 
time_count_fri = [0]*24 
time_count_sat = [0]*24 

data_x_sun = []
data_y_sun = []
data_x_mon = []
data_y_mon = []
data_x_tue = []
data_y_tue = []
data_x_wed = []
data_y_wed = []
data_x_thu = []
data_y_thu = []
data_x_fri = []
data_y_fri = []
data_x_sat = []
data_y_sat = []

data_sun = []
data_mon = []
data_tue = []
data_wed = []
data_thu = []
data_fri = []
data_sat = []

#曜日と時間の関係を表示

for i in pattern:
    # ◯◯時の部分
    print(i)
    for j in range(24):
        if int(i[2][3:5]) == j:
            if i[2][0:1] == "日":
                time_count_sun[j]+=1
            elif i[2][0:1] == "月":
                time_count_mon[j]+=1
            elif i[2][0:1] == "火":
                time_count_tue[j]+=1
            elif i[2][0:1] == "水":
                time_count_wed[j]+=1
            elif i[2][0:1] == "木":
                time_count_thu[j]+=1
            elif i[2][0:1] == "金":
                time_count_fri[j]+=1
            elif i[2][0:1] == "土":
                time_count_sat[j]+=1
        
for i in range(24):

    data_y_sun.append(time_count_sun[i])
    data_x_sun.append(i)
    data_list = [i,time_count_sun[i]]
    data_sun.append(data_list)

    data_y_mon.append(time_count_mon[i])
    data_x_mon.append(i)
    data_list = [i,time_count_mon[i]]
    data_mon.append(data_list)

    data_y_tue.append(time_count_tue[i])
    data_x_tue.append(i)
    data_list = [i,time_count_tue[i]]
    data_tue.append(data_list)

    data_y_wed.append(time_count_wed[i])
    data_x_wed.append(i)
    data_list = [i,time_count_wed[i]]
    data_wed.append(data_list)

    data_y_thu.append(time_count_thu[i])
    data_x_thu.append(i)
    data_list = [i,time_count_thu[i]]
    data_thu.append(data_list)

    data_y_fri.append(time_count_fri[i])
    data_x_fri.append(i)
    data_list = [i,time_count_fri[i]]
    data_fri.append(data_list)

    data_y_sat.append(time_count_sat[i])
    data_x_sat.append(i)
    data_list = [i,time_count_sat[i]]
    data_sat.append(data_list)

# plt.scatter(data_x,data_y)
# plt.show()
n_clusters_sun = 5
pred_sun = KMeans(n_clusters_sun).fit_predict(data_sun)
print(data_sun)
print(pred_sun)

n_clusters_mon = 5
pred_mon = KMeans(n_clusters_mon).fit_predict(data_mon)
print(data_mon)
print(pred_mon)

n_clusters_tue = 5
pred_tue = KMeans(n_clusters_tue).fit_predict(data_tue)
print(data_tue)
print(pred_tue)

n_clusters_wed = 5
pred_wed = KMeans(n_clusters_wed).fit_predict(data_wed)
print(data_wed)
print(pred_wed)

n_clusters_thu = 5
pred_thu = KMeans(n_clusters_thu).fit_predict(data_thu)
print(data_thu)
print(pred_thu)

n_clusters_fri = 5
pred_fri = KMeans(n_clusters_fri).fit_predict(data_fri)
print(data_fri)
print(pred_fri)

n_clusters_sat = 5
pred_sat = KMeans(n_clusters_sat).fit_predict(data_sat)
print(data_sat)
print(pred_sat)

for i in range(n_clusters_sun):
    data_x = []
    data_y = []
    for j in range(24):
        if(pred_sun[j]==i):
            data_x.append(j)
            data_y.append(time_count_sun[j])

    plt.bar(data_x,data_y)

plt.title("日曜日")
plt.show()

for i in range(n_clusters_mon):
    data_x = []
    data_y = []
    for j in range(24):
        if(pred_mon[j]==i):
            data_x.append(j)
            data_y.append(time_count_mon[j])

    plt.bar(data_x,data_y)
plt.title("月曜日")
plt.show()

for i in range(n_clusters_tue):
    data_x = []
    data_y = []
    for j in range(24):
        if(pred_tue[j]==i):
            data_x.append(j)
            data_y.append(time_count_tue[j])

    plt.bar(data_x,data_y)
plt.title("火曜日")
plt.show()

for i in range(n_clusters_wed):
    data_x = []
    data_y = []
    for j in range(24):
        if(pred_wed[j]==i):
            data_x.append(j)
            data_y.append(time_count_wed[j])

    plt.bar(data_x,data_y)
plt.title("水曜日")
plt.show()

for i in range(n_clusters_thu):
    data_x = []
    data_y = []
    for j in range(24):
        if(pred_thu[j]==i):
            data_x.append(j)
            data_y.append(time_count_thu[j])

    plt.bar(data_x,data_y)
plt.title("木曜日")
plt.show()

for i in range(n_clusters_fri):
    data_x = []
    data_y = []
    for j in range(24):
        if(pred_fri[j]==i):
            data_x.append(j)
            data_y.append(time_count_fri[j])

    plt.bar(data_x,data_y)
plt.title("金曜日")
plt.show()

for i in range(n_clusters_sat):
    data_x = []
    data_y = []
    for j in range(24):
        if(pred_sat[j]==i):
            data_x.append(j)
            data_y.append(time_count_sat[j])

    plt.bar(data_x,data_y)
plt.title("土曜日")
plt.show()