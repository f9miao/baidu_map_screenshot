import os
import time
from selenium.webdriver import Chrome


# 批处理数据(经纬度)
array = [
    ['113.23', '23.16'],
    ['113.23', '23.20'],
]

chrome = Chrome(executable_path='chromedriver.exe')  # 注意chrome驱动版本要匹配
chrome.get('file:///%s/page.html' % os.getcwd())  # 静态网页加载用绝对路径

longitude = chrome.find_element_by_css_selector('#longitude')  # 精度
latitude = chrome.find_element_by_css_selector('#latitude')  # 纬度
map = chrome.find_element_by_css_selector('#allmap')  # 地图按钮
query = chrome.find_element_by_css_selector('#r-result > input:nth-child(3)')  # 查询按钮

for item in array:
    # 清空输入
    longitude.clear()
    latitude.clear()
    # 输入经纬度
    longitude.send_keys(item[0])
    latitude.send_keys(item[1])
    # 点击查询按钮
    query.click()
    # 等待三秒后进行截图
    time.sleep(3)
    # 截图
    map.screenshot(filename=time.strftime("result/%Y%m%d%H%M%S{}", time.localtime()).format('.png'))

chrome.close()
print('exit!!!')
