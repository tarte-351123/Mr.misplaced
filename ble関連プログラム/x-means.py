import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster, preprocessing
from pyclustering.cluster.xmeans import xmeans
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer

x_1 = np.random.normal(50, 10, 20)
x_1 = x_1.reshape([x_1.shape[0], 1])
x_2 = np.random.normal(150, 10, 20)
x_2 = x_2.reshape([x_2.shape[0], 1])
y_1 = np.random.normal(50, 10, 20)
y_1 = y_1.reshape([y_1.shape[0], 1])
y_2 = np.random.normal(150, 10, 20)
y_2 = y_2.reshape([y_2.shape[0], 1])
data1 = np.concatenate([x_1, y_1], axis=1)

x = np.concatenate([data1])
print(x)
plt.scatter(x[:, 0], x[:, 1], alpha=0.5)
plt.show()

xm_c = kmeans_plusplus_initializer(x, 2).initialize()
xm_i = xmeans(data=x, initial_centers=xm_c, kmax=20, ccore=True)
xm_i.process()

classes = len(xm_i._xmeans__centers)
predict = xm_i.predict(x)

for i in range(classes):
    batch_predict = x[predict==i]
    plt.scatter(batch_predict[:, 0], batch_predict[:, 1], alpha=0.5, label="class="+str(i))

centers = np.array(xm_i._xmeans__centers)
plt.scatter(centers[:, 0], centers[:, 1], label="centroids", marker='*', color="red")
plt.show()