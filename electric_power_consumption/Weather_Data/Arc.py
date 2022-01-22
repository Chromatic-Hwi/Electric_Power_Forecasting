#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    def set_chrome_driver():
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver

def Monthly_Temp(YYYY, MM):
    YYYY = y
    MM = m

    # 각 달마다 일수가 다르고 하루 단위로 동작되는 코드는 중복되는 내용이 많기 때문에 간소화를 위해 월 Dict 이용
    month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    d=0
    while(d<month[m]):
        d=d+1
        print('====================< %d일 >=========================' %d)
        print()
        driver.get('https://www.wunderground.com/history/daily/gb/london/EGLC/date/'+str(y)+'-'+str(m)+'-'+str(d))
        driver.implicitly_wait(10)
        time.sleep(3)
                
        h = 1 # 여기서는 하루를 30분 단위로 쪼갠 온도 개수, 데이터의 개수를 h로 설정해서 반복시켰는데, 48이 안되는 경우도 있음.
        h2 = 1
        
        clk = driver.find_element(By.XPATH,'//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody/tr['+str(h2)+']/td[1]/span')
        clk_str = clk.text
        clk_str.split()
        
        
        # 11:50 PM 데이터부터 존재하는 경우
        if(h==clk_11_48[clk_str]):
            while (h2 < 49):
                try:    
                    clk = driver.find_element(By.XPATH,'//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody/tr['+str(h2)+']/td[1]/span')
                    clk_str = clk.text
                    clk_str.split()
                    
                    if(h==clk_11_48[clk_str]):
                        date_list = [int(y), int(m), int(d)] # 연,월,일 정보로 구성된 날짜 리스트 생성
                        date_list.append(clk_str) # 날짜 리스트에 해당 시각 원소 추가
                        date_list.append(int(h)) # 해당 시각이 그날 48개로 분할된 시간 중 몇번째인지 원소 추가
                        temp = driver.find_element(By.XPATH,'//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody/tr['+str(h2)+']/td[2]')
                        temp_str = temp.text # 스크래핑한 xpath의 온도를 str로 변경
                        temp_list = date_list 
                        temp_list.append(temp_str) # 날짜+시각 리스트에 온도 원소 추가
                        time.sleep(0.02)
                        print(temp_list) # 확인용 print
                        # 시간 루프 종료 지점
                            
                        # csv 추가 및 저장
                        with open("./"+str(y)+'_'+str(m)+'_'+"London_Temperature.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(temp_list)
                        print('h >>', str(h), 'h2 >>', str(h2))
                        print()
                        h2 = h2+1
                    
                    else:
                        date_list = [int(y), int(m), int(d)]
                        print('결손 데이터 칸의 정상 시각 >>',re_clk_11_48[h])
                        print('사이트에서 스크래핑한 시각 >>', clk_str)
                        date_list.append(re_clk_11_48[h])
                        date_list.append(int(h))
                        na_list = date_list
                        na_list.append('Null')
                        print(na_list)
                            
                        with open("./"+str(y)+'_'+str(m)+'_'+"London_Temperature.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(na_list)
                        print('h >>', str(h), 'h2 >>', str(h2))        
                        print() 
                    h = h+1
                    
                except NoSuchElementException:
                    if(h<49):
                        # 맨 마지막에 데이터가 없어 조기 종료 되버리는 경우
                        date_list = [int(y), int(m), int(d)]
                        print('결손 데이터 칸의 정상 시각 >>',re_clk_11_48[h])
                        print('사이트에서 스크래핑한 시각 >>', clk_str)
                        date_list.append(re_clk_11_48[h])
                        date_list.append(int(h))
                        na_list = date_list
                        na_list.append('Null')
                        print(na_list)
                            
                        with open("./"+str(y)+'_'+str(m)+'_'+"London_Temperature.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(na_list)
                            print('h >>', str(h), 'h2 >>', str(h2))        
                            print() 
                        h = h+1
                        
                    else:
                        break
                
                
        # 10:50 PM 데이터부터 존재하는 경우
        if(h==clk_10_48[clk_str]):
            while (h2 < 49):
                try:
                    clk = driver.find_element(By.XPATH,'//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody/tr['+str(h2)+']/td[1]/span')
                    clk_str = clk.text
                    clk_str.split()

                    if(h==clk_10_48[clk_str]):
                        date_list = [int(y), int(m), int(d)] # 연,월,일 정보로 구성된 날짜 리스트 생성
                        date_list.append(clk_str) # 날짜 리스트에 해당 시각 원소 추가
                        date_list.append(int(h)) # 해당 시각이 그날 48개로 분할된 시간 중 몇번째인지 원소 추가
                        temp = driver.find_element(By.XPATH,'//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody/tr['+str(h2)+']/td[2]')
                        temp_str = temp.text # 스크래핑한 xpath의 온도를 str로 변경
                        temp_list = date_list 
                        temp_list.append(temp_str) # 날짜+시각 리스트에 온도 원소 추가
                        time.sleep(0.02)
                        print(temp_list) # 확인용 print
                        # 시간 루프 종료 지점
                            
                        # csv 추가 및 저장
                        with open("./"+str(y)+'_'+str(m)+'_'+"London_Temperature.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(temp_list)
                        print('h >>', str(h), 'h2 >>', str(h2))
                        print()
                        h2 = h2+1
                    
                    else:
                        date_list = [int(y), int(m), int(d)]
                        print('결손 데이터 칸의 정상 시각 >>',re_clk_10_48[h])
                        print('사이트에서 스크래핑한 시각 >>', clk_str)
                        date_list.append(re_clk_10_48[h])
                        date_list.append(int(h))
                        na_list = date_list
                        na_list.append('Null')
                        print(na_list)
                            
                        with open("./"+str(y)+'_'+str(m)+'_'+"London_Temperature.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(na_list)
                        print('h >>', str(h), 'h2 >>', str(h2))        
                        print()
                    h = h+1
                    
                except NoSuchElementException:
                    if(h<49):
                        # 맨 마지막에 데이터가 없어 조기 종료 되버리는 경우
                        date_list = [int(y), int(m), int(d)]
                        print('결손 데이터 칸의 정상 시각 >>',re_clk_10_48[h])
                        print('사이트에서 스크래핑한 시각 >>', clk_str)
                        date_list.append(re_clk_10_48[h])
                        date_list.append(int(h))
                        na_list = date_list
                        na_list.append('Null')
                        print(na_list)
                            
                        with open("./"+str(y)+'_'+str(m)+'_'+"London_Temperature.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(na_list)
                            print('h >>', str(h), 'h2 >>', str(h2))        
                            print() 
                        h = h+1
                        
                    else:
                        break
                    
                    
        print('< Day End >')
        print('\n'*4)

