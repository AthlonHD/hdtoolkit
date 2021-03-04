import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_path = './chromedriver'
chrome_options.add_argument('--ignore-certificate-errors')  # 无视证书引发的错误
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)  # 配置chrome设置
from tqdm import tqdm
#获取歌单ID
i = 0
link,name = [],[]

#获取说唱分类下歌单的前三页，每页含有歌单35个
for i in range(0,71,35):
    print("\n获取第{}个页信息！".format( (i//35) +1))
    url = 'https://music.163.com/#/discover/playlist/?cat=%E6%80%80%E6%97%A7limit=35&offset='+str(i)
    # url = 'https://www.baidu.com'
    driver.get(url)
    driver.switch_to.frame("contentFrame")
    time.sleep(2)
    try:
        data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
        for j in tqdm(range(len(data))):
            nb = data[j].find_element_by_class_name("nb").text
            msk = data[j].find_element_by_css_selector("a.msk")
            name.append(msk.get_attribute('title'))
            link.append(msk.get_attribute('href'))
            #print (link)
    except:
        print('此歌单不可用，获取下一页信息')

#url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
infos = {'name': name, 'link': link}
playlist = pd.DataFrame(infos, columns=['name', 'link'])
playlist.to_csv("playlist.csv",encoding="utf_8_sig")