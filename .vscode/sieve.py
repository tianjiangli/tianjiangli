


"""下面是埃拉托斯特尼筛法中“筛”这个部分的完整代码："""
sieve=[True]*101
for i in range(2,100):
    if sieve[i]:
        print(i)
        for j in range(i*i,100,i):
            sieve[j]=False

from selenium import webdriver
import time,sys

# dirver=webdriver.Firefox(executable_path=r'D:\Program Files\Mozilla Firefox\firefox.exe')
dirver=webdriver.Edge()
dirver.get(r'https://www.baidu.com/')
time.sleep(10)
dirver.quit()
