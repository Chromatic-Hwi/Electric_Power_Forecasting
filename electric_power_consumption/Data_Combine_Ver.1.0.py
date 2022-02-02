#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import csv

try:
    os.mkdir('./Combined_Data')
    for y in range(2013, 2017):
        os.mkdir('./Combined_Data/'+str(y))
    print('저장 폴더 생성 완료.')
    
except FileExistsError:
    print('해당 폴더가 이미 존재합니다.\n폴더를 확인해주세요.')
    
print('------------------------------< Start Working!! >------------------------------\n')

month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for y in range(2013, 2017):
    
    for m in range(1,13):
        csv_electric = pd.read_csv("./Electric_Data/Electirc_Data_CSV_FInal/"+str(y)+"/"+str(y)+'_'+str(m)+'_'+"House1_Ch1_Electric_Data_Final.csv", encoding='cp949')
        csv_weather = pd.read_csv("./Weather_Data/Weather_Data_24H_CSV/"+str(y)+"/"+str(y)+'_'+str(m)+'_'+"London_Temperature_24H.csv", encoding='utf-8')
        csv_electric["Temp"]=csv_weather['Temp']
        s = 0
        for d in range(month[m]):
            d=d+1 
            
            for n in range(s, s+24):
                combine_list=[]
                combine_list.append(csv_electric['DateTime'][n])
                combine_list.append(csv_electric['Day'][n])
                combine_list.append(csv_electric['Holiday'][n])
                combine_list.append(csv_electric['Seq'][n])
                combine_list.append(csv_electric['Watt'][n])
                combine_list.append(csv_electric['Temp'][n])
                with open("./Combined_Data/"+str(y)+"/"+str(y)+'_'+str(m)+'_'+"House1_Ch1_Combined_Data.csv", 'a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(combine_list)
            s=s+24
            
        csv_origin = pd.read_csv("./Combined_Data/"+str(y)+"/"+str(y)+'_'+str(m)+'_'+"House1_Ch1_Combined_Data.csv", names = ['DateTime', 'Day', 'Holiday', 'Seq', 'Watt', 'Temp'], header = None, encoding='cp949')
        csv_origin.to_csv("./Combined_Data/"+str(y)+"/"+str(y)+'_'+str(m)+'_'+"House1_Ch1_Combined_Data.csv", encoding='cp949')
        
print('\n------------------------------< Job Done!! >------------------------------\n')

