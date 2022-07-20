class HashTable:
    def __init__(self):

        self.hash = [[] for i in range(10)]
    def gethash(self,key):
        total = 0
        for i in key:
            total += ord(i)
        return total%10

    def __getitem__(self,key):
        h = gethash(key)
        return self.hash[h]

    def __setitem__(self,key,value):
        h = gethash(key)
        self.hash[h] = value

import pandas as pd
a = pd.read_csv(r"C:\Users\vkasturi\Desktop\nyc_weather.csv")
nytemp = HashTable()
for i in a:
    tokens = i.split(',')
    key = tokens[0]
    value = tokens[1]
    nytemp[key]=value

#1.Find Max

