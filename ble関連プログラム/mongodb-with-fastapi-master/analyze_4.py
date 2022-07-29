
# 平日と休日に分けて

from __future__ import print_function
from calendar import WEDNESDAY
import csv
from importlib.abc import TraversableResources
from re import M
import math
from turtle import width
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn import cluster
import sklearn
from sklearn.cluster import KMeans
from datetime import datetime as dt
from matplotlib import dates as mdates
import japanize_matplotlib
from sympy import I, true
from statistics import mean, median,variance,stdev
from datetime import datetime
filename = 'csv/go_out.csv'

pattern = []
# 配列のコピー
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        pattern.append(row)

time_count_h = [[0] * 6 for i in range(24)]# 休日
time_stamp_h = [[""] * 6 for i in range(24)]
time_count_d = [[0] * 6 for i in range(24)]# 平日
time_stamp_d = [[""] * 6 for i in range(24)]
time_count_h_p1 = [[0] * 6 for i in range(24)] #スマホ財布
time_count_h_p2 = [[0] * 6 for i in range(24)] #財布カバン
time_count_h_p3 = [[0] * 6 for i in range(24)] #スマホカバン
time_count_d_p1 = [[0] * 6 for i in range(24)] #スマホ財布
time_count_d_p2 = [[0] * 6 for i in range(24)] #財布カバン
time_count_d_p3 = [[0] * 6 for i in range(24)] #スマホカバン

data_h = []
data_d = []

data_h_p1 = []
data_h_p2 = []
data_h_p3 = []
data_d_p1 = []
data_d_p2 = []
data_d_p3 = []
#曜日と時間の関係を表示


sample_data= "木曜日,13:20"
sample_date = sample_data[0:1]
sample_time = int(sample_data[4:6])*60+int(sample_data[7:9])
print(sample_date)
print(sample_time)
print()

for i in (pattern):
    #時間の部分
    if i[2][0:1] == "土" or i[2][0:1] == "日":
        for j in range(24):
            #分の部分
            for k in range(6):
                if(int(i[3][0:2])==j and int(i[3][3])==k):
                    time_count_h[j][k] +=1
                    if "phone" in i[4] and "wallet" in i[4]:
                        time_count_h_p1[j][k]+=1
                    if "wallet" in i[4] and "bag" in i[4]:
                        time_count_h_p2[j][k]+=1
                    if "phone" in i[4] and "bag" in i[4]:
                        time_count_h_p3[j][k]+=1
                time_stamp_h[j][k] = str(f'{(j):02}')+":"+str(f'{(k*10):02}')
    else:
        for j in range(24):
            #分の部分
            for k in range(6):
                if(int(i[3][0:2])==j and int(i[3][3])==k):
                    time_count_d[j][k] +=1
                    if "phone" in i[4] and "wallet" in i[4]:
                        time_count_d_p1[j][k]+=1
                    if "wallet" in i[4] and "bag" in i[4]:
                        time_count_d_p2[j][k]+=1
                    if "phone" in i[4] and "bag" in i[4]:
                        time_count_d_p3[j][k]+=1
                time_stamp_d[j][k] = str(f'{(j):02}')+":"+str(f'{(k*10):02}')

time_list_h = []    
time_list_d = []    
with open("csv/time_h.csv", "w", newline="", encoding="utf8") as f:
        writer = csv.writer(f) 
with open("csv/time_d.csv", "w", newline="", encoding="utf8") as f:
        writer = csv.writer(f) 

time = [[""] * 6 for i in range(24)]
#休日
n_clusters_0 = 3

x_tick_h = []
for i in range(24):
    for j in range(6):
        time[i][j] = str(time_stamp_h[i][j][0:2])+":"+str(time_stamp_h[i][j][3:5])
        data_list = [int(time_stamp_h[i][j][0:2])*60+int(time_stamp_h[i][j][3:5]),time_count_h[i][j]]
        with open("csv/time_h.csv", "a", newline="", encoding="utf8") as f:
            writer = csv.writer(f) 
            writer.writerow(data_list)
        if time_count_h[i][j]!=0:
            data_h.append(data_list)
        x = dt.strptime(time[i][j],'%H:%M')
        y = time_count_h[i][j]
pred_0 = KMeans(n_clusters_0).fit_predict(data_h)
data_y_all = []
data_y_p1 = []
data_y_p2 = []
data_y_p3 = []
for i in range(n_clusters_0):
    data_x = []
    data_y = []
    center_x = 0
    center_y = 0
    count = 0
   
    for j in range(len(pred_0)):
        if(pred_0[j]==i):
            if data_h[j][1]!=0:
                data_x.append(data_h[j][0])
                data_y.append(data_h[j][1])
                count +=1
            h = int(data_h[j][0]/60)
            m = int((data_h[j][0]%60)/10)
            data_y_all.append(time_count_h[h][m])
            data_y_p1.append(time_count_h_p1[h][m])
            data_y_p2.append(time_count_h_p2[h][m])
            data_y_p3.append(time_count_h_p3[h][m])    

    if(count>=2):
        p1=0
        p2=0
        p3=0
        all = 0
        for i in range (len(data_y_all)):
            all+=data_y_all[i]

        for i in range(len(data_y_p1)):
            p1+=data_y_p1[i]
        print("スマホと財布: "+str(int(p1/all*100))+"%")

        for i in range(len(data_y_p2)):
            p2+=data_y_p2[i]
        print("財布とカバン: "+str(int(p2/all*100))+"%")

        for i in range(len(data_y_p3)):
            p3+=data_y_p3[i]
        print("カバンとスマホ: "+str(int(p3/all*100))+"%")
        print()
        mean_x = (mean(data_x))
        mean_y = (mean(data_y))
        print("平均"+(str('{0:02}'.format(int(mean_x/60))))+":"+str('{0:02}'.format(int(mean_x%60))))
        print("標準偏差"+str(int(stdev(data_x))))
        print(" ⏬ ")

        start = mean_x-stdev(data_x)
        if start<0:
            start =24+start 
        end = mean_x+stdev(data_x)
        if end >23:
            end = end-24
        print("68%区間："+(str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))+"〜"+(str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60)))))

        start = mean_x-stdev(data_x)*2
        if start<0:
            start =24+start 
        end = mean_x+stdev(data_x)*2
        if end >23:
            end = end-24
        print("90%区間："+(str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))+"〜"+(str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60)))))
        print("------------")
        # plt.scatter(mean_x, mean_y, marker="*", c = "black", s = 500)
    time_list = []
    for i in range(len(data_x)):
        fix_data = dt.strptime(str(int(data_x[i]/60))+":"+str(int(data_x[i]%60)),'%H:%M')
        time_list.append(fix_data)
    ax = plt.subplot()
    print(data_y)
    ax.bar(time_list,data_y,width=0.005)     
    ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax.set_xlim([dt.strptime('00:00','%H:%M'), dt.strptime('23:59','%H:%M')])
    x_tick_h.append(str(f'{(i):02}')+":"+str(f'{(j*10):02}'))
    plt.xticks(rotation=90)
    
    with open("csv/time_h.csv", "a", newline="", encoding="utf8") as f:
        writer = csv.writer(f) 
        writer.writerow(data_list)
    data_x = []
    data_y = []
plt.title("休日")
# plt.show()
plt.show()
data_x = []
data_y = []

#平日
n_clusters_1 = 6

x_tick_d = []
for i in range(24):
    for j in range(6):
        time[i][j] = str(time_stamp_d[i][j][0:2])+":"+str(time_stamp_d[i][j][3:5])
        data_list = [int(time_stamp_d[i][j][0:2])*60+int(time_stamp_d[i][j][3:5]),time_count_d[i][j]]
        with open("csv/time_d.csv", "a", newline="", encoding="utf8") as f:
            writer = csv.writer(f) 
            writer.writerow(data_list)
        if time_count_d[i][j]!=0:
            data_d.append(data_list)
        x = dt.strptime(time[i][j],'%H:%M')
        y = time_count_d[i][j]
pred_1 = KMeans(n_clusters_1).fit_predict(data_d)
data_y_all = []
data_y_p1 = []
data_y_p2 = []
data_y_p3 = []

for i in range(n_clusters_1):
    data_x = []
    data_y = []
    center_x = 0
    center_y = 0
    count = 0
    for j in range(len(pred_1)):
        if(pred_1[j]==i):
            if data_d[j][1]!=0:
                data_x.append(data_d[j][0])
                data_y.append(data_d[j][1])
                count +=1
            h = int(data_d[j][0]/60)
            m = int((data_d[j][0]%60)/10)
            data_y_all.append(time_count_d[h][m])
            data_y_p1.append(time_count_d_p1[h][m])
            data_y_p2.append(time_count_d_p2[h][m])
            data_y_p3.append(time_count_d_p3[h][m])  
    if(count>=2):    
        p1=0
        p2=0
        p3=0
        all = 0
        for i in range (len(data_y_all)):
            all+=data_y_all[i]

        for i in range(len(data_y_p1)):
            p1+=data_y_p1[i]
        print("スマホと財布: "+str(int(p1/all*100))+"%")

        for i in range(len(data_y_p2)):
            p2+=data_y_p2[i]
        print("財布とカバン: "+str(int(p2/all*100))+"%")

        for i in range(len(data_y_p3)):
            p3+=data_y_p3[i]
        print("カバンとスマホ: "+str(int(p3/all*100))+"%")
        print()
        mean_x = (mean(data_x))
        mean_y = (mean(data_y))
        print("平均"+(str('{0:02}'.format(int(mean_x/60))))+":"+str('{0:02}'.format(int(mean_x%60))))
        print("標準偏差"+str(int(stdev(data_x))))
        print(" ⏬ ")

        start = mean_x-stdev(data_x)
        if start<0:
            start =24+start 
        end = mean_x+stdev(data_x)
        if end >23:
            end = end-24
        print("68%区間："+(str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))+"〜"+(str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60)))))

        start = mean_x-stdev(data_x)*2
        if start<0:
            start =24+start 
        end = mean_x+stdev(data_x)*2
        if end >23:
            end = end-24
        print("90%区間："+(str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))+"〜"+(str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60)))))
        print("-------------")
        # plt.scatter(mean_x, mean_y, marker="*", c = "black", s = 500)
    time_list = []
    for i in range(len(data_x)):
        fix_data = dt.strptime(str(int(data_x[i]/60))+":"+str(int(data_x[i]%60)),'%H:%M')
        time_list.append(fix_data)
    ax = plt.subplot()
    ax.bar(time_list,data_y,width=0.005)     
    ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax.set_xlim([dt.strptime('00:00','%H:%M'), dt.strptime('23:59','%H:%M')])
    x_tick_d.append(str(f'{(i):02}')+":"+str(f'{(j*10):02}'))
    plt.xticks(rotation=90)
    
    data_x = []
    data_y = []
plt.title("平日")
# plt.show()
plt.show()
