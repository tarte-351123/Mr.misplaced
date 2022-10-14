
# 平日と休日に分けて分析

from __future__ import print_function
from calendar import WEDNESDAY
import csv
from importlib.abc import TraversableResources
from re import M
import math
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
filename = 'ble関連プログラム/csv/go_out.csv'

pattern = []
# 配列のコピー
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        pattern.append(row)


time_count_h = [0]*24 #休日
time_count_d = [0]*24 #平日
time_count_h_p1 = [0]*24 #スマホ財布
time_count_h_p2 = [0]*24 #財布カバン
time_count_h_p3 = [0]*24 #スマホカバン
time_count_d_p1 = [0]*24 #スマホ財布
time_count_d_p2 = [0]*24 #財布カバン
time_count_d_p3 = [0]*24 #スマホカバン

data_h = []
data_d = []

data_h_p1 = []
data_h_p2 = []
data_h_p3 = []
data_d_p1 = []
data_d_p2 = []
data_d_p3 = []
#曜日と時間の関係を表示

for i in pattern:
    # ◯◯時の部分
    for j in range(24):
        if int(i[3][0:2]) == j:
            if i[2][0:1] == "土" or i[2][0:1] == "日":
                time_count_h[j]+=1
                if "phone" in i[4] and "wallet" in i[4]:
                    time_count_h_p1[j]+=1
                if "wallet" in i[4] and "bag" in i[4]:
                    time_count_h_p2[j]+=1
                if "phone" in i[4] and "bag" in i[4]:
                    time_count_h_p3[j]+=1
            else :
                time_count_d[j]+=1
                if "phone" in i[4] and "wallet" in i[4]:
                    time_count_d_p1[j]+=1
                if "wallet" in i[4] and "bag" in i[4]:
                    time_count_d_p2[j]+=1
                if "phone" in i[4] and "bag" in i[4]:
                    time_count_d_p3[j]+=1

time_list_h = []    
time_list_d = []    
with open("ble関連プログラム/csv/time_h.csv", "w", newline="", encoding="utf8") as f:
        writer = csv.writer(f) 
with open("ble関連プログラム/csv/time_d.csv", "w", newline="", encoding="utf8") as f:
        writer = csv.writer(f) 

for i in range(24):
    
    data_list = [i,time_count_h[i]]
    if time_count_h[i]!=0:
        data_h.append(data_list)

    data_list = [i,time_count_h_p1[i]]
    if time_count_h_p1[i]!=0:
        data_h_p1.append(data_list)

    data_list = [i,time_count_h_p2[i]]
    if time_count_h_p2[i]!=0:
        data_h_p2.append(data_list)

    data_list = [i,time_count_h_p3[i]]
    if time_count_h_p3[i]!=0:
        data_h_p3.append(data_list)

    data_list = [i,time_count_d[i]]
    if time_count_d[i]!=0:
        data_d.append(data_list)

    data_list = [i,time_count_d_p1[i]]
    if time_count_d_p1[i]!=0:
        data_d_p1.append(data_list)

    data_list = [i,time_count_d_p2[i]]
    if time_count_d_p2[i]!=0:
        data_d_p2.append(data_list)

    data_list = [i,time_count_d_p3[i]]
    if time_count_d_p3[i]!=0:
        data_d_p3.append(data_list)

    data_list = [i,time_count_h[i]]
    if(time_count_h[i]!=0):
        with open("ble関連プログラム/csv/time_h.csv", "a", newline="", encoding="utf8") as f:
            writer = csv.writer(f) 
            writer.writerow(data_list)
        time_list_h.append(data_list)

    data_list = [i,time_count_d[i]]
    if(time_count_d[i]!=0):
        with open("ble関連プログラム/csv/time_d.csv", "a", newline="", encoding="utf8") as f:
            writer = csv.writer(f) 
            writer.writerow(data_list)
        time_list_h.append(data_list)

n_clusters_0 = 3
pred_0 = KMeans(n_clusters_0).fit_predict(data_h)
n_clusters_1 = 5
pred_1 = KMeans(n_clusters_1).fit_predict(data_d)

for i in range(n_clusters_0):
    data_x = []
    data_y = []
    center_x = 0
    center_y = 0
    count = 0
    for j in range(len(pred_0)):
        if(pred_0[j]==i):
            data_x.append(data_h[j][0])
            data_y.append(data_h[j][1])
            if data_h[j][1] != 0:
                center_x +=j
                center_y +=time_count_h[j]
                count +=1
    if(count>=2):    
        print(data_x,data_y)
        print("平均"+str(mean(data_x)))
        print("中央値"+str(median(data_x)))
        print("分散"+str(variance(data_x)))
        print("標準偏差"+str(stdev(data_x)))
        print(" ⏬ ")

        start = (mean(data_x)-stdev(data_x))
        if start<0:
            start =24+start 
        end = (mean(data_x)+stdev(data_x))
        if end >23:
            end = end-24
        print("68%区間："+(str('{0:02}'.format(int(start//1))))+"時"+(str('{0:02}'.format(int((start - start//1)*60))))+"分〜"+(str('{0:02}'.format(int(end//1))))+"時"+(str('{0:02}'.format(int((end - end//1)*60))))+"分")

        start = (mean(data_x)-stdev(data_x)*2)
        if start<0:
            start =24+start 
        end = (mean(data_x)+stdev(data_x)*2)
        if end >23:
            end = end-24
        print("90%区間："+(str('{0:02}'.format(int(start//1))))+"時"+(str('{0:02}'.format(int((start - start//1)*60))))+"分〜"+(str('{0:02}'.format(int(end//1))))+"時"+(str('{0:02}'.format(int((end - end//1)*60))))+"分")

        end = mean(data_x)+stdev(data_x)
        print()
        plt.scatter(mean(data_x), mean(data_y), marker="*", c = "black", s = 500)

    plt.bar(data_x,data_y)
    data_x = []
    data_y = []
plt.title("休日")
plt.show()

print("休日：スマホと財布")
for i in range(n_clusters_0):
    for j in range(24):
        data_x.append(j)
        data_y.append(time_count_h_p1[j])
plt.bar(data_x,data_y,color = "red")
plt.title("スマホと財布")
plt.show()

print("休日：財布とカバン")
data_x = []    
data_y = []
for i in range(n_clusters_0):
    for j in range(24):
        data_x.append(j)
        data_y.append(time_count_h_p2[j])
plt.bar(data_x,data_y,color = "blue")
plt.title("財布とカバン")
plt.show()

print("休日：カバンとスマホ")
data_x = []    
data_y = []
for i in range(n_clusters_0):
    for j in range(24):
        data_x.append(j)
        data_y.append(time_count_h_p3[j])
plt.bar(data_x,data_y,color = "green")
plt.title("カバンとスマホ")
plt.show()
print(pred_1)
for i in range(n_clusters_1):
    data_x = []
    data_y = []
    count = 0
    for j in range(len(pred_1)):
        if(pred_1[j]==i):
            data_x.append(data_d[j][0])
            data_y.append(data_d[j][1])
            count +=1
    
    if(count>=2):
        print(data_x, data_y)    
        print("平均"+str(mean(data_x)))
        print("中央値"+str(median(data_x)))
        print("分散"+str(variance(data_x)))
        print("標準偏差"+str(stdev(data_x)))
        print(" ⏬ ")

        start = (mean(data_x)-stdev(data_x))
        if start<0:
            start =24+start 
        end = (mean(data_x)+stdev(data_x))
        if end >23:
            end = end-24
        print("68%区間："+(str('{0:02}'.format(int(start//1))))+"時"+(str('{0:02}'.format(int((start - start//1)*60))))+"分〜"+(str('{0:02}'.format(int(end//1))))+"時"+(str('{0:02}'.format(int((end - end//1)*60))))+"分")

        start = (mean(data_x)-stdev(data_x)*2)
        if start<0:
            start =24+start 
        end = (mean(data_x)+stdev(data_x)*2)
        if end >23:
            end = end-24
        print("90%区間："+(str('{0:02}'.format(int(start//1))))+"時"+(str('{0:02}'.format(int((start - start//1)*60))))+"分〜"+(str('{0:02}'.format(int(end//1))))+"時"+(str('{0:02}'.format(int((end - end//1)*60))))+"分")

        end = mean(data_x)+stdev(data_x)
        print()
        plt.scatter(mean(data_x), mean(data_y), marker="*", c = "black", s = 500)

    plt.bar(data_x,data_y)
    data_x = []
    data_y = []
plt.title("平日")
plt.show()

print("平日：スマホと財布")
for i in range(n_clusters_0):
    for j in range(24):
        data_x.append(j)
        data_y.append(time_count_d_p1[j])
plt.bar(data_x,data_y,color = "red")
plt.title("スマホと財布")
plt.show()

print("平日：財布とカバン")
data_x = []    
data_y = []
for i in range(n_clusters_0):
    for j in range(24):
        data_x.append(j)
        data_y.append(time_count_d_p2[j])
plt.bar(data_x,data_y,color = "blue")
plt.title("財布とカバン")
plt.show()

print("平日：カバンとスマホ")
data_x = []    
data_y = []
for i in range(n_clusters_0):
    for j in range(24):
        data_x.append(j)
        data_y.append(time_count_d_p3[j])

plt.bar(data_x,data_y,color = "green")
plt.title("カバンとスマホ")
plt.show()

