import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.cluster import KMeans

# データセットのインポート
file1=pd.read_csv('csv/time_h.csv')
file2=pd.read_csv('csv/time_d.csv')

# データの割り振り
X=file1.iloc[:,0:2]

# SSEの算出
SSE=[]
for i in range(1,9):
    model = KMeans(n_clusters=i,
               init='k-means++',
               n_init=5,
               max_iter=10,
               random_state=0)
    model.fit(X)
    SSE.append(model.inertia_)

# グラフの描画
plt.plot(range(1,9), SSE, marker='o')
plt.xticks(np.arange(1,11,1))
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.show()

# データの割り振り
X=file2.iloc[:,0:2]

# SSEの算出
SSE=[]
for i in range(1,9):
    model = KMeans(n_clusters=i,
               init='k-means++',
               n_init=5,
               max_iter=10,
               random_state=0)
    model.fit(X)
    SSE.append(model.inertia_)

# グラフの描画
plt.plot(range(1,9), SSE, marker='o')
plt.xticks(np.arange(1,11,1))
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.show()