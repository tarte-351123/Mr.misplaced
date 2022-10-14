from __future__ import print_function
import bag_data
import wallet_data
import phone_data
import data_fix
import pattern
import cluster
import time_save
import time
import threading
from calendar import WEDNESDAY
from re import M
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from datetime import datetime as dt
from matplotlib import dates as mdates

def worker():
    print(time.time())
    time.sleep(8)

def scheduler(interval, f, wait = True):
    base_time = time.time()
    next_time = 0
    while True:
        bag_data.bag_data()
        wallet_data.wallet_data()
        phone_data.phone_data()
        data_fix.data_fix()
        data_fix.data_fix()
        pattern.pattern()
        cluster.cluster()
        time_save.time_save()
        t = threading.Thread(target = f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)   


#何秒に一回処理するか
minute = 1000
scheduler(minute, worker, True)