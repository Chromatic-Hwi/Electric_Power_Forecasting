#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from datetime import datetime
import os
import csv
import time

ch1 = pd.read_csv('./channel_1.dat', names=['Unix', 'Watt'],header=None, delimiter=" ")
print('Done!')

ch1.info()

ch1_date = pd.DataFrame(ch1,columns = ['Unix', 'Date', 'Watt'])

ch1_date['Date'] = pd.to_datetime(ch1['Unix'], unit='s')
ch1_date.info()
ch1_date.head(10)

try:
    os.mkdir('./Electirc_Data_CSV')
except FileExistsError:
    print('해당 폴더가 이미 존재합니다.\n폴더를 확인해주세요.')
    

month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


# 1. 
i = 431368
print('Running!', '\n'*4)


# 2. 
while(i < 20284836):
    list1 = ch1_date.loc[i].values.tolist()
    date = list1[1]
    y1 = date.year
    M1 = date.month
    d1 = date.day
    H1 = date.hour 
    n = 0 

        
    # 3. 
    while(H1 < 24):
        H0 = 0 
        
        # 3'. 
        while(H0 < 24):
            watt_list=[]
            h = date.hour
            
            # 3.1. 
            if(H1 == H0):
                
                # 3.1'. 
                while(h < h+1):
                    n=n+1
                    list2 = ch1_date.loc[i].values.tolist()
                    date = list2[1]
                    watt = list2[2]
                    y = date.year
                    M = date.month
                    d = date.day
                    h = date.hour
                    m = date.minute
                    s = date.second

                    j=h-H1

                    # 3.1'.1. 
                    if(j==0):
                        watt_list.append(watt)

                        total_date = '{0}년 {1}월 {2}일 - {3}시 {4}분 {5}초'.format(y, M, d, h, m, s)
                        i = i+1

                    # 3.1'.2.
                    elif (j==1):
                        max_watt = max(watt_list)

                        hourly_date2 = '{0}년 {1}월 {2}일 - {3}시'.format(y, M, d, H1)
                        hourly_date5 = '{0} {1} {2}'.format(y, M, d) 
                        hourly_list = []
                        hourly_list.append(hourly_date2)
                        hourly_list.append(max_watt)

                        with open("./Electirc_Data_CSV/"+str(y)+'_'+str(M)+'_'+"House1_Ch1_Electric_Data.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(hourly_list)       

                        H1 = H1+1 
                        H0 = H0+1
                        break

                    # 3.1'.3. 
                    elif(d1+1==d and h ==0 and H1 ==23):
                        d=d-1
                        h=h+24

                        max_watt = max(watt_list)
                        
                        hourly_date3 = '{0}년 {1}월 {2}일 - {3}시'.format(y, M, d, H1)
                        hourly_list = []
                        hourly_list.append(hourly_date3)
                        hourly_list.append(max_watt)

                        with open("./Electirc_Data_CSV/"+str(y)+'_'+str(M)+'_'+"House1_Ch1_Electric_Data.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(hourly_list)       

                        H1 = H1+1 
                        H0 = H0+1                   
                        break

                    # 3.1'.4.
                    elif (n>600):
                        list(hourly_date5)
                        listed = hourly_date5.split()
                        y4 = listed[0]
                        M4 = listed[1]
                        d4 = listed[2]

                        max_watt = max(watt_list)

                        hourly_date = '{0}년 {1}월 {2}일 - {3}시'.format(y4, M4, d4, H1)
                        hourly_list = []
                        hourly_list.append(hourly_date)
                        hourly_list.append(max_watt)

                        with open("./Electirc_Data_CSV/"+str(y4)+'_'+str(M4)+'_'+"House1_Ch1_Electric_Data.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(hourly_list)       
                        
                        # 3.1'.4.1. 
                        if(d1==d):
                            jc=j
                            
                            while(jc>1):
                                h=h+1
                                hourly_date = '{0}년 {1}월 {2}일 - {3}시'.format(y4, M4, d4, h-j)
                                hourly_list = []
                                hourly_list.append(hourly_date)
                                hourly_list.append('Null')

                                with open("./Electirc_Data_CSV/"+str(y4)+'_'+str(M4)+'_'+"House1_Ch1_Electric_Data.csv", 'a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow(hourly_list)  

                                jc=jc-1
                                H1 = H1+1
                                H0 = H0+1
                                
                            H1 = H1+1
                            H0 = H0+1
                                
                        # 3.1'.4.2.
                        if(d1!=d):
            
                            while(H1<23):
                                hourly_date = '{0}년 {1}월 {2}일 - {3}시'.format(y4, M4, d4, H1+1)
                                hourly_list = []
                                hourly_list.append(hourly_date)
                                hourly_list.append('Null')

                                with open("./Electirc_Data_CSV/"+str(y4)+'_'+str(M4)+'_'+"House1_Ch1_Electric_Data.csv", 'a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow(hourly_list)  

                                H1 = H1+1
                                H0 = H0+1
                                
                            H1 = H1+1
                            H0 = H0+1
                            
                            # 3.1'.4.2.1. 
                            if(int(d4)+1 != d):
                                D = int(d4)+1 
                                
                                # 3.1'.4.2.1.1. 
                                if(int(M) == int(M4)):
                                    while(D<d):
                                        for x in range (0,24):
                                            hourly_date = '{0}년 {1}월 {2}일 - {3}시'.format(y4, M4, D, x)
                                            hourly_list = []
                                            hourly_list.append(hourly_date)
                                            hourly_list.append('Null')

                                            with open("./Electirc_Data_CSV/"+str(y4)+'_'+str(M4)+'_'+"House1_Ch1_Electric_Data.csv", 'a', newline='') as file:
                                                writer = csv.writer(file)
                                                writer.writerow(hourly_list)  
                    
                                        D=D+1
                                
                                # 3.1'.4.2.1.2.
                                if(int(M) != int(M4)):
                                    while(D<=month[int(M4)]):
                                        for x in range (0,24):
                                            hourly_date = '{0}년 {1}월 {2}일 - {3}시'.format(y4, M4, D, x)
                                            hourly_list = []
                                            hourly_list.append(hourly_date)
                                            hourly_list.append('Null')

                                            with open("./Electirc_Data_CSV/"+str(y4)+'_'+str(M4)+'_'+"House1_Ch1_Electric_Data.csv", 'a', newline='') as file:
                                                writer = csv.writer(file)
                                                writer.writerow(hourly_list)  
                                                
                                        D=D+1
                                    
                                    D2 = 1
                                    while(D2 < d):
                                        for x in range (0,24):
                                            hourly_date = '{0}년 {1}월 {2}일 - {3}시'.format(y4, M, D2, x)
                                            hourly_list = []
                                            hourly_list.append(hourly_date)
                                            hourly_list.append('Null')
                                            
                                            with open("./Electirc_Data_CSV/"+str(y4)+'_'+str(M)+'_'+"House1_Ch1_Electric_Data.csv", 'a', newline='') as file:
                                                writer = csv.writer(file)
                                                writer.writerow(hourly_list)  
                                                
                                        D2 = D2+1

                        break

                        
            # 3.2. 
            if(H1 != H0):
                list3 = ch1_date.loc[i].values.tolist()
                date = list3[1]
                watt = list3[2]
                y = date.year
                M = date.month
                d = date.day
                h = date.hour
                m = date.minute
                s = date.second

                j=h-H1           

                hourly_date3121 = '{0}년 {1}월 {2}일 - {3}시'.format(y, M, d, H0)
                hourly_list3121 = []
                hourly_list3121.append(hourly_date3121)
                hourly_list3121.append('Null')

                with open("./Electirc_Data_CSV/"+str(y)+'_'+str(M)+'_'+"House1_Ch1_Electric_Data.csv", 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(hourly_list3121)       
                
                h = h+1
                H0 = H0+1
                
                if (H0 ==23):
                    break
                     
        break

        
print('Job Done!!')
time.sleep(5)

