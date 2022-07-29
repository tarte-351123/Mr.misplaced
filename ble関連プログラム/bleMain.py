# ラズパイで動かしているプログラム
# BLEビーコンをMACアドレスで見分けてサーバーへ送る
import csv
import json
import datetime
import time
import sys
import subprocess
import multiprocessing
import requests
import pprint
import signal
import threading

class DataLogger():
    def __init__(self, fn):
        self.fn = fn

    def append_line(self, line):
        with open(self.fn, "a") as f:
            f.write(line + '\n')

class LeAdvertisingReport():
    global count
    count = 0
    
    def __init__(self):
        self.company = None
        self.type = None
        self.mac_address = None
        self.rssi = None
        self.tx_power = None
        self.timestamp = datetime.datetime.now()

    def set_company(self, line):
        if line.startswith('Company: '):
            self.company = line.split(': ')[1]

    def set_type(self, line):
        if line.startswith('Type: '):
            self.type = line.split(': ')[1]

    def set_mac_address(self, line):
        if line.startswith('Address: '):
            self.mac_address = line.split(' ')[1]

    def set_tx_power(self, line):
        if line.startswith('TX power: '):
            self.tx_power = int(line.split(': ')[1].split(' ')[0])

    def set_rssi(self, line):
        if line.startswith('RSSI: '):
            self.rssi = int(line.split(': ')[1].split(' ')[0])

    def event_detected(self):
        # 使用するビーコンの数だけ調べる
        my_ble_1 = "F8:36:A9:7F:DF:B3" # tag wallet
        my_ble_2 = "D9:7A:A3:C4:80:79" # phone
        ble_id = 'NoID'
        
        # 特定のMacアドレスを含むモノ以外は除外する
        if my_ble_1 != self.mac_address and my_ble_2 !=self.mac_address:
            return
        
        # MacアドレスをビーコンIDに変換
        if my_ble_1 == self.mac_address:
            ble_id = 'wallet'
            
        elif my_ble_2 == self.mac_address:
            ble_id = 'phone'
        
        # 距離の算出
        d = None
        if self.tx_power and self.rssi:
            d = pow(10.0, (self.tx_power - self.rssi) / 20.0)
        
        # 距離計測不十分のため除外
        if d == None:
            return
        
        global count
        count += 1
        
        # global hn
        hn = 'ohashi01'
        
        # 検知レポートを表示


        #ログとしてローカルに書き出す
        tmp = {
                'hostname': hn,
                'timestamp': self.timestamp.isoformat(),
                'count': count,
                'rssi': self.rssi, #電波の強さ
                'tx_power': self.tx_power,
                'distance': d,
                'mac_address': self.mac_address,
                'ble_id': ble_id,
                'company': self.company
        }
#         tmp = {
#             "rssi",self.rssi
#         }
        timedata = str(self.timestamp.isoformat())
        minute = (timedata[17:19])
        
        if int(minute)%3==1:
            minute =str(int(minute)-1)
            if(len(minute)==1):
                minute="0"+minute
        elif int(minute)%3==2:
            minute =str(int(minute)-2)
            if(len(minute)==1):
                minute="0"+minute
        elif int(minute)%3==0:
            minute =str(int(minute))
            if(len(minute)==1):
                minute="0"+minute
            
        day = timedata[0:10]
        time = timedata[11:16]
        
        print("---------------------")
        print(hn)
        print(self.rssi)
        print(ble_id)
        
        print(day+" "+time+":"+minute)
        print("---------------------")

        # リクエストボディを定義する
        request_body = {"hostname": hn,
                        "rssi": self.rssi, 
                        "ble_id": ble_id,
                        "time": day+" "+time+":"+minute
                        }
        if ble_id == "wallet":
            response = requests.post("http://192.168.0.22:8000/wallet/", json=request_body)
            pprint.pprint(response.json())
    
        elif ble_id == "phone":
            response = requests.post("http://192.168.0.22:8000/phone/", json=request_body)
            pprint.pprint(response.json())
        


def run_lescan():
    while True:
        process = subprocess.Popen(['hcitool', 'lescan', '--duplicates'], stdout
=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            output = process.stdout.readline()
            if process.poll() is not None:
                break
            if output:
                #print('lescan >>>', output.strip())
                pass

def run_btmon():
    def _is_new_event(line):
        return '> HCI Event: LE Meta Event' in line
    tmp = None
    while True:
        process = subprocess.Popen(['btmon'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            output = process.stdout.readline()
            if process.poll() is not None:
                break
            if output:
                line = output.decode('utf-8').strip()
                # HCI Eventを拾い上げる
                if _is_new_event(line):
                    if tmp is not None:
                        tmp.event_detected()
                    tmp = LeAdvertisingReport()
                    continue
                # イベントが検知されるまで待つ
                if tmp is None:
                    continue
                # コマンド出力をパースする
                try:
                    tmp.set_company(line)
                    tmp.set_type(line)
                    tmp.set_mac_address(line)
                    tmp.set_tx_power(line)
                    tmp.set_rssi(line)
                except Exception:
                    print('Failed to parse.')
                    

if __name__ == '__main__':
    
    p1 = multiprocessing.Process(target=run_lescan, args=())
    p1.daemon = True
    p1.start()
    p2 = multiprocessing.Process(target=run_btmon, args=())
    p2.daemon = True
    p2.start()
    #sys.exit(sub())
    while True:
        time.sleep(1)
