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


if_days = input('是否双日购票？ 请输入 y/n （是/否,均小写，输入后回车）')
if_people = input('是否双人购票？ 请输入 y/n （是/否，均小写，输入后回车）')
account = input('请输入账号：')
password = input('请输入密码：')

print('\n\n\n')

print('——————————————————————————————————')
print('|              提示               |')
print('——————————————————————————————————\n')

print('——————————————————————————————————')
print('请确保购票人身份信息已经添加成功')
print('——————————————————————————————————')
print('本程序只提供VIP抢票代点功能，如未抢到，概不负责_(:з」∠)_')
print('——————————————————————————————————\n')

print('——————————————————————————————————')
print('出现浏览器窗口请勿关闭，请在弹出的浏览器内进行操作')
print('——————————————————————————————————\n')

print('——————————————————————————————————')
print('浏览器若持续刷新属正常现象')
print('——————————————————————————————————\n')

print('——————————————————————————————————')
print('提示选择购票人信息时，请手动在页面上进行操作')
print('——————————————————————————————————')
print('随后在命令行窗口内，按任意键继续')
print('——————————————————————————————————\n\n\n')


chrome_path = '.\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

driver.get('https://store.allcpp.cn/#/ticket/detail?event=980')

# 登陆
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="l-user-id"]')))

driver.find_element_by_xpath('//*[@id="l-user-id"]').send_keys(account)
driver.find_element_by_xpath('//*[@id="l-user-pd"]').send_keys(password)
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
        if if_people == 'y':
            driver.find_element_by_xpath(
                '//div[@class="ticket-form-item"]/div[@class="buy-ticket-count"]/div[@class="buy-ticket-plus"]').click()
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

        if_buyable = True
    else:
        if_buyable = False


# 买第二天
if if_days == 'y':
    driver.get('https://store.allcpp.cn/#/ticket/detail?event=980')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[2]')))

    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[2]').click()

    print('——————————————————————————————————')
    print('请选择购票人信息……')
    print('——————————————————————————————————')
    input('选择完成后请按任意键继续……')

    if if_people == 'y':
        driver.find_element_by_xpath(
            '//div[@class="ticket-form-item"]/div[@class="buy-ticket-count"]/div[@class="buy-ticket-plus"]').click()
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
