
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

sample_data= "月曜日,13:45"
sample_date = sample_data[0:1]
sample_time = int(sample_data[4:6])*60+int(sample_data[7:9])

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

pred_0 = KMeans(n_clusters_0).fit_predict(data_h)

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

pred_1 = KMeans(n_clusters_1).fit_predict(data_d)
data_y_all = []
data_y_p1 = []
data_y_p2 = []
data_y_p3 = []
range_list_h= []
range_list_d = []

if sample_date == "土" or sample_date == "日":
    flag = False
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
            mean_x = (mean(data_x))
            mean_y = (mean(data_y))
            
            start_1 = mean_x-stdev(data_x)
            if start_1<0:
                start_1 =24+start_1
            end_1 = mean_x+stdev(data_x)
            if end_1 >23:
                end_1 = end_1-24
            start_time_1 = (str('{0:02}'.format(int(start_1/60))))+":"+(str('{0:02}'.format(int(start_1%60))))
            end_time_1 = (str('{0:02}'.format(int(end_1/60))))+":"+(str('{0:02}'.format(int(end_1%60))))
            
            start_2 = mean_x-stdev(data_x)*2
            if start_2<0:
                start_2 =24+start_2
            end_2 = mean_x+stdev(data_x)*2
            if end_2 >23:
                end_2 = end_2-24
            start_time_2 = (str('{0:02}'.format(int(start_2/60))))+":"+(str('{0:02}'.format(int(start_2%60))))
            end_time_2 = (str('{0:02}'.format(int(end_2/60))))+":"+(str('{0:02}'.format(int(end_2%60))))

            start_3 = mean_x-stdev(data_x)*3
            if start_3<0:
                start_3 =24+start_3
            end_3 = mean_x+stdev(data_x)*3
            if end_3 >23:
                end_3 = end_3-24
            start_time_3 = (str('{0:02}'.format(int(start_3/60))))+":"+(str('{0:02}'.format(int(start_3%60))))
            end_time_3 = (str('{0:02}'.format(int(end_3/60))))+":"+(str('{0:02}'.format(int(end_3%60))))
            
            range_list_h.append(str(int(start_3))+"〜"+str(int(end_3)))
            if (int(start_time_3[0:2])*60+int(start_time_3[3:5])<=sample_time and sample_time <=int(end_time_3[0:2])*60+int(end_time_3[3:5])):
                print()
                print("平均"+(str('{0:02}'.format(int(mean_x/60))))+":"+str('{0:02}'.format(int(mean_x%60))))
                print("標準偏差"+str(int(stdev(data_x))))
                print("68%区間："+start_time_1+"〜"+end_time_1)
                print("90%区間："+start_time_2+"〜"+end_time_2)
                print("99%区間："+start_time_3+"〜"+end_time_3)
                
                print(" ⏬ ")
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
                print("-------------")
                flag = True
        
        data_x = []
        data_y = []

    if flag==False:
        print(sample_time)
        print(range_list_h)
        min=9999
        near = []
        for i in range(len(range_list_h)):
            spr_time = range_list_h[i].split('〜')
            if (int(spr_time[0])-sample_time < min):
                min = int(spr_time[0])-sample_time
                near = [range_list_h[i]]
            if (int(spr_time[0])+1440) - sample_time< min:
                min = int(spr_time[0])+1440 - sample_time
                near = [range_list_h[i]]
            if (sample_time+1440-int(spr_time[1])<min):
                min = sample_time+1440 - int(spr_time[1])
                near = [range_list_h[i]]
            if (sample_time - int(spr_time[1])<min):
                min = sample_time-int(spr_time[1])
                near = [range_list_h[i]]
            
        print(near)
        aaaa = int(near[0].split('〜')[0])
        start_time = str('{0:02}'.format(int(aaaa/60)))+":"+str('{0:02}'.format(int(aaaa%60)))
        
        print(start_time)
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
                mean_x = (mean(data_x))
                mean_y = (mean(data_y))

                start_1 = mean_x-stdev(data_x)
                if start_1<0:
                    start_1 =24+start_1
                end_1 = mean_x+stdev(data_x)
                if end_1 >23:
                    end_1 = end_1-24
                start_time_1 = (str('{0:02}'.format(int(start_1/60))))+":"+(str('{0:02}'.format(int(start_1%60))))
                end_time_1 = (str('{0:02}'.format(int(end_1/60))))+":"+(str('{0:02}'.format(int(end_1%60))))

                start_2 = mean_x-stdev(data_x)*2
                if start_2<0:
                    start_2 =24+start_2
                end_2 = mean_x+stdev(data_x)*2
                if end_2 >23:
                    end_2 = end_2-24
                start_time_2 = (str('{0:02}'.format(int(start_2/60))))+":"+(str('{0:02}'.format(int(start_2%60))))
                end_time_2 = (str('{0:02}'.format(int(end_2/60))))+":"+(str('{0:02}'.format(int(end_2%60))))

                start_3 = mean_x-stdev(data_x)*3
                if start_3<0:
                    start_3 =24+start_3
                end_3 = mean_x+stdev(data_x)*3
                if end_3 >23:
                    end_3 = end_3-24
                start_time_3 = (str('{0:02}'.format(int(start_3/60))))+":"+(str('{0:02}'.format(int(start_3%60))))
                end_time_3 = (str('{0:02}'.format(int(end_3/60))))+":"+(str('{0:02}'.format(int(end_3%60))))

                range_list_h.append(str(int(start_3))+"〜"+str(int(end_3)))
                if (start_time == start_time_3):
                    print("平均"+(str('{0:02}'.format(int(mean_x/60))))+":"+str('{0:02}'.format(int(mean_x%60))))
                    print("標準偏差"+str(int(stdev(data_x))))
                    print("68%区間："+start_time_1+"〜"+end_time_1)
                    print("90%区間："+start_time_2+"〜"+end_time_2)
                    print("99%区間："+start_time_3+"〜"+end_time_3)
                    print(" ⏬ ")
                    print("確率は修正してあります。")  
                    p1=0
                    p2=0
                    p3=0
                    all = 0
                    for i in range (len(data_y_all)):
                        all+=data_y_all[i]

                    for i in range(len(data_y_p1)):
                        p1+=data_y_p1[i]
                    print("スマホと財布: "+str(int(p1/all*50))+"%")

                    for i in range(len(data_y_p2)):
                        p2+=data_y_p2[i]
                    print("財布とカバン: "+str(int(p2/all*50))+"%")

                    for i in range(len(data_y_p3)):
                        p3+=data_y_p3[i]
                    print("カバンとスマホ: "+str(int(p3/all*50))+"%")
                    print("-------------")
else:
    flag = False
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
            mean_x = (mean(data_x))
            mean_y = (mean(data_y))

            start_1 = mean_x-stdev(data_x)
            if start_1<0:
                start_1 =24+start_1
            end_1 = mean_x+stdev(data_x)
            if end_1 >23:
                end_1 = end_1-24
            start_time_1 = (str('{0:02}'.format(int(start_1/60))))+":"+(str('{0:02}'.format(int(start_1%60))))
            end_time_1 = (str('{0:02}'.format(int(end_1/60))))+":"+(str('{0:02}'.format(int(end_1%60))))

            start_2 = mean_x-stdev(data_x)*2
            if start_2<0:
                start_2 =24+start_2
            end_2 = mean_x+stdev(data_x)*2
            if end_2 >23:
                end_2 = end_2-24
            start_time_2 = (str('{0:02}'.format(int(start_2/60))))+":"+(str('{0:02}'.format(int(start_2%60))))
            end_time_2 = (str('{0:02}'.format(int(end_2/60))))+":"+(str('{0:02}'.format(int(end_2%60))))

            start_3 = mean_x-stdev(data_x)*3
            if start_3<0:
                start_3 =24+start_3
            end_3 = mean_x+stdev(data_x)*3
            if end_3 >23:
                end_3 = end_3-24
            start_time_3 = (str('{0:02}'.format(int(start_3/60))))+":"+(str('{0:02}'.format(int(start_3%60))))
            end_time_3 = (str('{0:02}'.format(int(end_3/60))))+":"+(str('{0:02}'.format(int(end_3%60))))

            range_list_d.append(str(int(start_3))+"〜"+str(int(end_3)))
            if (int(start_time_3[0:2])*60+int(start_time_3[3:5])<=sample_time and sample_time <=int(end_time_3[0:2])*60+int(end_time_3[3:5])):
                print("平均"+(str('{0:02}'.format(int(mean_x/60))))+":"+str('{0:02}'.format(int(mean_x%60))))
                print("標準偏差"+str(int(stdev(data_x))))
                print("68%区間："+start_time_1+"〜"+end_time_1)
                print("90%区間："+start_time_2+"〜"+end_time_2)
                print("99%区間："+start_time_3+"〜"+end_time_3)
                print(" ⏬ ")
                print()  
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
                print("-------------")
                flag = True

        data_x = []
        data_y = []

    if flag==False:
        print(sample_time)
        print(range_list_d)
        min=9999
        near = []
        for i in range(len(range_list_d)):
            spr_time = range_list_d[i].split('〜')
            if (int(spr_time[0])-sample_time < min):
                min = int(spr_time[0])-sample_time
                near = [range_list_d[i]]
                print(min)
            if (int(spr_time[0])+1440 - sample_time)< min:
                min = int(spr_time[0])+1440 - sample_time
                near = [range_list_d[i]]
                print(min)
            if (sample_time+1440-int(spr_time[1])<min):
                min = sample_time+1440 - int(spr_time[1])
                near = [range_list_d[i]]
            if (sample_time - int(spr_time[1])<min):
                min = sample_time-int(spr_time[1])
                near = [range_list_d[i]]
            
        print(near)
        aaaa = int(near[0].split('〜')[0])
        start_time = str('{0:02}'.format(int(aaaa/60)))+":"+str('{0:02}'.format(int(aaaa%60)))
        
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
                mean_x = (mean(data_x))
                mean_y = (mean(data_y))

                start_1 = mean_x-stdev(data_x)
                if start_1<0:
                    start_1 =24+start_1
                end_1 = mean_x+stdev(data_x)
                if end_1 >23:
                    end_1 = end_1-24
                start_time_1 = (str('{0:02}'.format(int(start_1/60))))+":"+(str('{0:02}'.format(int(start_1%60))))
                end_time_1 = (str('{0:02}'.format(int(end_1/60))))+":"+(str('{0:02}'.format(int(end_1%60))))

                start_2 = mean_x-stdev(data_x)*2
                if start_2<0:
                    start_2 =24+start_2
                end_2 = mean_x+stdev(data_x)*2
                if end_2 >23:
                    end_2 = end_2-24
                start_time_2 = (str('{0:02}'.format(int(start_2/60))))+":"+(str('{0:02}'.format(int(start_2%60))))
                end_time_2 = (str('{0:02}'.format(int(end_2/60))))+":"+(str('{0:02}'.format(int(end_2%60))))

                start_3 = mean_x-stdev(data_x)*3
                if start_3<0:
                    start_3 =24+start_3
                end_3 = mean_x+stdev(data_x)*3
                if end_3 >23:
                    end_3 = end_3-24
                start_time_3 = (str('{0:02}'.format(int(start_3/60))))+":"+(str('{0:02}'.format(int(start_3%60))))
                end_time_3 = (str('{0:02}'.format(int(end_3/60))))+":"+(str('{0:02}'.format(int(end_3%60))))

                range_list_d.append(str(int(start_3))+"〜"+str(int(end_3)))
                if (start_time == start_time_3):
                    print("平均"+(str('{0:02}'.format(int(mean_x/60))))+":"+str('{0:02}'.format(int(mean_x%60))))
                    print("標準偏差"+str(int(stdev(data_x))))
                    print("68%区間："+start_time_1+"〜"+end_time_1)
                    print("90%区間："+start_time_2+"〜"+end_time_2)
                    print("99%区間："+start_time_3+"〜"+end_time_3)
                    print(" ⏬ ")
                    print("確率は修正してあります。")  
                    p1=0
                    p2=0
                    p3=0
                    all = 0
                    for i in range (len(data_y_all)):
                        all+=data_y_all[i]

                    for i in range(len(data_y_p1)):
                        p1+=data_y_p1[i]
                    print("スマホと財布: "+str(int(p1/all*50))+"%")

                    for i in range(len(data_y_p2)):
                        p2+=data_y_p2[i]
                    print("財布とカバン: "+str(int(p2/all*50))+"%")

                    for i in range(len(data_y_p3)):
                        p3+=data_y_p3[i]
                    print("カバンとスマホ: "+str(int(p3/all*50))+"%")
                    print("-------------")