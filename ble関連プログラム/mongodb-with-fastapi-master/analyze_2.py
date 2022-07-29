
# 10分ごとの外出

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
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from datetime import datetime as dt
from sklearn import cluster
from sklearn.cluster import KMeans
import japanize_matplotlib
from sympy import I, true
filename = 'csv/go_out.csv'

pattern = []
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        pattern.append(row)

# サンプルデータ
# 2022-06-13 12:24:21,2022-06-13 16:51:18,月曜日,12:20,"['phone', 'wallet']"

time_count= [[0] * 6 for i in range(24)]
time = [[""] * 6 for i in range(24)]

for i in range(len(pattern)):
    #時間の部分
    for j in range(24):
        #分の部分
        for k in range(6):
            if(int(pattern[i][3][0:2])==j and int(pattern[i][3][3])==k):
                time_count[j][k] +=1
            time[j][k] = str(f'{(j):02}')+":"+str(f'{(k*10):02}')
                
# print(time_count)
# print()
# print(time)
time_stamp = [[""] * 6 for i in range(24)]
x_tick = []
for i in range(24):
    for j in range(6):
        time_stamp[i][j] = str(time[i][j][0:2])+":"+str(time[i][j][3:5])
        x = dt.strptime(time_stamp[i][j],'%H:%M')
        y = time_count[i][j]
        if y!=0:
            ax = plt.subplot()
            ax.bar(x,y,width=0.005)     
            ax.xaxis.set_major_locator(mdates.HourLocator())
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
            ax.set_xlim([dt.strptime('00:00','%H:%M'), dt.strptime('23:59','%H:%M')])
            x_tick.append(str(f'{(i):02}')+":"+str(f'{(j*10):02}'))
            plt.xticks(rotation=90)
plt.show()