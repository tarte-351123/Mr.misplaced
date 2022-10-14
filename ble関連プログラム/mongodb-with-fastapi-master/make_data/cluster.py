from time import strptime

from requests import request

def cluster():
    import requests
    from datetime import datetime as dt
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn import cluster, preprocessing
    from matplotlib import dates as mdates
    from pyclustering.cluster.xmeans import xmeans
    from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
    from statistics import mean, median,variance,stdev
    
    GET_URL = "http://localhost:8000/pattern/"
    POST_URL = "http://localhost:8000/cluster/"
    
    response = requests.get(POST_URL)
    data = response.json()
    
    for i in range(len(data)):
        requests.delete(POST_URL)
    
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
    
    response = requests.get(GET_URL)
    data = response.json()
    x_h = []
    y_h = []
    y_h_p1 = []
    y_h_p2 = []
    y_h_p3 = []
    x_d = []
    y_d = []
    y_d_p1 = []
    y_d_p2 = []
    y_d_p3 = []
    
    for i in (data):
        if i["date"][0:1] == "土" or i["date"][0:1] == "日":
            # 休日
            for j in range(24):
                for k in range(6):
                    if(int(i["time"][0:2])==j and int(i["time"][3])==k):
                        time_count_h[j][k] +=1
                        if "phone" in i["object"] and "wallet" in i["object"]:
                            time_count_h_p1[j][k]+=1
                        if "wallet" in i["object"] and "bag" in i["object"]:
                            time_count_h_p2[j][k]+=1
                        if "phone" in i["object"] and "bag" in i["object"]:
                            time_count_h_p3[j][k]+=1
                    time_stamp_h[j][k] = str(f'{(j):02}')+":"+str(f'{(k*10):02}')
        else:
            # 平日
            for j in range(24):   
                for k in range(6):
                    if(int(i["time"][0:2])==j and int(i["time"][3])==k):
                        time_count_d[j][k] +=1
                        if "phone" in i["object"] and "wallet" in i["object"]:
                            time_count_d_p1[j][k]+=1
                        if "wallet" in i["object"] and "bag" in i["object"]:
                            time_count_d_p2[j][k]+=1
                        if "phone" in i["object"] and "bag" in i["object"]:
                            time_count_d_p3[j][k]+=1
                    time_stamp_d[j][k] = str(f'{(j):02}')+":"+str(f'{(k*10):02}')
    time_stamp_h_sub = []
    time_stamp_d_sub = []
    for i in range(24):
        for j in range(6):
            if int(time_count_h[i][j])!=0:
                x_h.append([int(time_stamp_h[i][j][0:2])*60+int(time_stamp_h[i][j][3:5])])
                time_stamp_h_sub.append([time_stamp_h[i][j]])
                y_h.append([time_count_h[i][j]])
                y_h_p1.append(time_count_h_p1[i][j])
                y_h_p2.append(time_count_h_p2[i][j])
                y_h_p3.append(time_count_h_p3[i][j])
                
            if int(time_count_d[i][j])!=0:
                x_d.append([int(time_stamp_d[i][j][0:2])*60+int(time_stamp_d[i][j][3:5])])
                time_stamp_d_sub.append([time_stamp_d[i][j]])
                y_d.append([time_count_d[i][j]])
                y_d_p1.append(time_count_d_p1[i][j])
                y_d_p2.append(time_count_d_p2[i][j])
                y_d_p3.append(time_count_d_p3[i][j])
                
    x_tick_h = []
    
    data1 = np.concatenate([x_h, y_h], axis=1)
    h = np.concatenate([data1])
    xm_c = kmeans_plusplus_initializer(h, 2).initialize()
    xm_i = xmeans(data=h, initial_centers=xm_c, kmax=20, ccore=True)
    xm_i.process()
    
    n_clusters_0 = len(xm_i._xmeans__centers)
    pred_0 = xm_i.predict(h)

    for i in range(n_clusters_0):
        batch_predict = h[pred_0==i]

    centers = np.array(xm_i._xmeans__centers)
    
    data2 = np.concatenate([x_d, y_d], axis=1)
    d = np.concatenate([data2])
    xm_c = kmeans_plusplus_initializer(d, 2).initialize()
    xm_i = xmeans(data=d, initial_centers=xm_c, kmax=20, ccore=True)
    xm_i.process()
    
    n_clusters_1 = len(xm_i._xmeans__centers)
    pred_1 = xm_i.predict(d)

    for i in range(n_clusters_1):
        batch_predict = d[pred_1==i]

    centers = np.array(xm_i._xmeans__centers)
    
    #休日
    print("休日")
    print()
    data_x = []
    data_y = []
    p1=[]
    p2=[]
    p3=[] 
    for i in range(n_clusters_0):
        count = 0
        for j in range(len(pred_0)):
            
            if(pred_0[j]==i):
                if y_h[j][0]!=0:
                    data_x.append(x_h[j])
                    data_y.append(y_h[j])
                    count +=1   
                p1.append(y_h_p1[j])   
                p2.append(y_h_p2[j])   
                p3.append(y_h_p3[j])
                           
        if(count>=2):
            all = 0
            add_p1 = 0
            add_p2 = 0
            add_p3 = 0
            for i in range (len(data_y)):
                all+=data_y[i][0]
            for i in range(len(p1)):
                add_p1+=p1[i]
            print("スマホと財布: "+str(int(add_p1/all*100))+"%")
            
            for i in range(len(p2)):
                add_p2+=p2[i]
            print("財布とカバン: "+str(int(add_p2/all*100))+"%")

            for i in range(len(p3)):
                add_p3+=p3[i]
            print("カバンとスマホ: "+str(int(add_p3/all*100))+"%")
            print()
            index_x=[]
            for i in range (len(data_x)):
                index_x.append(data_x[i][0])
            mean_x = (mean(index_x))
            print("平均"+(str('{0:02}'.format(int(mean_x/60))))+":"+str('{0:02}'.format(int(mean_x%60))))
            print("標準偏差"+str(int(stdev(index_x))))
            print(" ⏬ ")
            start = mean_x-stdev(index_x)
            if start<0:
                start =24+start 
            end = mean_x+stdev(index_x)
            if end >23:
                end = end-24
            a = (str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))
            aa = (str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60))))
            print("68%区間："+a+"~"+aa)

            start = mean_x-stdev(index_x)*2
            if start<0:
                start =24+start 
            end = mean_x+stdev(index_x)*2
            if end >23:
                end = end-24
            b = (str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))
            bb = (str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60))))
            print("90%区間："+b+"~"+bb)
            
            start = mean_x-stdev(index_x)*3
            if start<0:
                start =24+start 
            end = mean_x+stdev(index_x)*3
            if end >23:
                end = end-24
            c = (str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))
            cc = (str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60))))
            print("99%区間："+c+"~"+cc)
            print("------------")
            request_body = {
                "dateType": "休日",
                "normalDistribution": {
                    "mean": str('{0:02}'.format(int(mean_x/60)))+":"+str('{0:02}'.format(int(mean_x%60))),
                    "sd": str(int(stdev(index_x))),
                    "range": [{
                    "from_": a,
                    "to_": aa
                    },
                    {
                    "from_": b,
                    "to_": bb
                    }, 
                    {
                    "from_": c,
                    "to_": cc
                    }, ]
                },
                "model": [{
                    "object": "スマホと財布",
                    "percentage": str(int(add_p1/all*100))+"%"
                    },
                    {
                    "object": "財布とカバン",
                    "percentage": str(int(add_p2/all*100))+"%" 
                    },
                    {
                    "object": "カバンとスマホ",
                    "percentage": str(int(add_p3/all*100))+"%"
                    },
                ]
            }
            response = requests.post(POST_URL,json=request_body)
            data_x = []
            data_y = []
            p1=[]
            p2=[]
            p3=[] 
            
        #     # plt.scatter(mean_x, mean_y, marker="*", c = "black", s = 500)
        # time_list = []
        # for i in range(len(data_x)):
        #     fix_data = dt.strptime(str(int(data_x[i]/60))+":"+str(int(data_x[i]%60)),'%H:%M')
        #     time_list.append(fix_data)
        # ax = plt.subplot()
        # print(data_y)
        # ax.bar(time_list,data_y,width=0.005)     
        # ax.xaxis.set_major_locator(mdates.HourLocator())
        # ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        # ax.set_xlim([dt.strptime('00:00','%H:%M'), dt.strptime('23:59','%H:%M')])
        # x_tick_h.append(str(f'{(i):02}')+":"+str(f'{(j*10):02}'))
        # plt.xticks(rotation=90)
        
        
    print("平日")
    print()
    data_x = []
    data_y = []
    p1=[]
    p2=[]
    p3=[] 
    for i in range(n_clusters_1):
        count = 0
        for j in range(len(pred_1)):
            
            if(pred_1[j]==i):
                if y_d[j][0]!=0:
                    data_x.append(x_d[j])
                    data_y.append(y_d[j])
                    count +=1   
                p1.append(y_d_p1[j])   
                p2.append(y_d_p2[j])   
                p3.append(y_d_p3[j])
                           
        if(count>=2):
            all = 0
            add_p1 = 0
            add_p2 = 0
            add_p3 = 0
            for i in range (len(data_y)):
                all+=data_y[i][0]
            for i in range(len(p1)):
                add_p1+=p1[i]
            print("スマホと財布: "+str(int(add_p1/all*100))+"%")
            
            for i in range(len(p2)):
                add_p2+=p2[i]
            print("財布とカバン: "+str(int(add_p2/all*100))+"%")

            for i in range(len(p3)):
                add_p3+=p3[i]
            print("カバンとスマホ: "+str(int(add_p3/all*100))+"%")
            print()
            index_x=[]
            for i in range (len(data_x)):
                index_x.append(data_x[i][0])
            mean_x = (mean(index_x))
            print("平均"+(str('{0:02}'.format(int(mean_x/60))))+":"+str('{0:02}'.format(int(mean_x%60))))
            print("標準偏差"+str(int(stdev(index_x))))
            print(" ⏬ ")
            start = mean_x-stdev(index_x)
            if start<0:
                start =24+start 
            end = mean_x+stdev(index_x)
            if end >23:
                end = end-24
            a = (str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))
            aa = (str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60))))
            print("68%区間："+a+"~"+aa)

            start = mean_x-stdev(index_x)*2
            if start<0:
                start =24+start 
            end = mean_x+stdev(index_x)*2
            if end >23:
                end = end-24
            b = (str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))
            bb = (str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60))))
            print("90%区間："+b+"~"+bb)
            
            start = mean_x-stdev(index_x)*3
            if start<0:
                start =24+start 
            end = mean_x+stdev(index_x)*3
            if end >23:
                end = end-24
            c = (str('{0:02}'.format(int(start/60))))+":"+(str('{0:02}'.format(int(start%60))))
            cc = (str('{0:02}'.format(int(end/60))))+":"+(str('{0:02}'.format(int(end%60))))
            print("99%区間："+c+"~"+cc)
            print("------------")
            request_body = {
                "dateType": "平日",
                "normalDistribution": {
                    "mean": str('{0:02}'.format(int(mean_x/60)))+":"+str('{0:02}'.format(int(mean_x%60))),
                    "sd": str(int(stdev(index_x))),
                    "range": [{
                    "from_": a,
                    "to_": aa
                    },
                    {
                    "from_": b,
                    "to_": bb
                    }, 
                    {
                    "from_": c,
                    "to_": cc
                    }, ]
                },
                "model": [{
                    "object": "スマホと財布",
                    "percentage": str(int(add_p1/all*100))+"%"
                    },
                    {
                    "object": "財布とカバン",
                    "percentage": str(int(add_p2/all*100))+"%" 
                    },
                    {
                    "object": "カバンとスマホ",
                    "percentage": str(int(add_p3/all*100))+"%"
                    },
                ]
            }
            response = requests.post(POST_URL,json=request_body)
            data_x = []
            data_y = []
            p1=[]
            p2=[]
            p3=[] 
        
            
    
if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    cluster()

print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する