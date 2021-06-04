# -*- coding=utf-8 -*-

#     \   |   |     |             |   | __ \
#    _ \  __| __ \  |  _ \  __ \  |   | |   |
#   ___ \ |   | | | | (   | |   | ___ | |   |
# _/    _\__|_| |_|_|\___/ _|  _|_|  _|____/


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chrome_path = './chromedriver'
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

driver.get('https://store.allcpp.cn/#/ticket/detail?event=980')

# 登陆
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="l-user-id"]')))

driver.find_element_by_xpath('//*[@id="l-user-id"]').send_keys('18516340245')
driver.find_element_by_xpath('//*[@id="l-user-pd"]').send_keys('LRJ990212')
driver.find_element_by_xpath('//*[@id="l-user-login"]').click()

# # 回到活动页面
# driver.get('https://store.allcpp.cn/#/ticket/detail?event=980')
# WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/img')))

# 买第一天
if_buyable = False
while if_buyable is False:
    driver.get('https://store.allcpp.cn/#/ticket/detail?event=980')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//div[@class="ticket-form"]/div[@style="display: flex;"]/button')))
    button_text = driver.find_element_by_xpath('//div[@class="ticket-form"]/div[@style="display: flex;"]/button').text
    if button_text == '立即购票':

        print('——————————————————————————————————')
        print('请选择购票人信息……')
        print('——————————————————————————————————')
        input('选择完成后请按任意键继续……')

        # 调整数量
        # driver.find_element_by_xpath(
        #     '//div[@class="ticket-form-item"]/div[@class="buy-ticket-count"]/div[@class="buy-ticket-plus"]').click()
        driver.find_element_by_xpath('//div[@class="ticket-form"]/div[@style="display: flex;"]/button').click()  # 立即购票

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]')))
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]').click()  # 微信支付
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/button').click()  # 立即付款

        WebDriverWait(driver,10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="modal-root"]/div/div/div')))

        print('——————————————————————————————————')
        print('请在手机端前往支付……')
        print('——————————————————————————————————')

        if_buyable = True
    else:
        if_buyable = False


# 买第二天
driver.get('https://store.allcpp.cn/#/ticket/detail?event=980')
WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[2]')))

driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[2]').click()

print('——————————————————————————————————')
print('请选择购票人信息……')
print('——————————————————————————————————')
input('选择完成后请按任意键继续……')

# driver.find_element_by_xpath(find_element_by_xpath
#     '//div[@class="ticket-form-item"]/div[@class="buy-ticket-count"]/div[@class="buy-ticket-plus"]').click()
driver.find_element_by_xpath('//div[@class="ticket-form"]/div[@style="display: flex;"]/button').click()  # 立即购票

WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]')))
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]').click()  # 微信支付
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/button').click()  # 立即付款
WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="modal-root"]/div/div/div')))

print('——————————————————————————————————')
print('请在手机端前往支付……')
print('——————————————————————————————————')


driver.quit()
