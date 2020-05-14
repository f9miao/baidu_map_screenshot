import time
import datetime
from selenium.webdriver import Chrome

# 批处理数据(经纬度)
array = [
    ['113.23', '23.16'],
    ['113.23', '23.20'],
]

chrome = Chrome(executable_path='chromedriver.exe')  # 注意chrome驱动版本要匹配
chrome.get('file:///E:/PycharmProjects/baidu_map_screenshot/page.html')  # 静态网页加载用绝对路径

longitude = chrome.find_element_by_css_selector('#longitude')  # 精度
latitude = chrome.find_element_by_css_selector('#latitude')  # 纬度
map = chrome.find_element_by_css_selector('#allmap')  # 地图按钮
query = chrome.find_element_by_css_selector('#r-result > input:nth-child(3)')  # 查询按钮

for item in array:

    longitude.clear()
    latitude.clear()

    longitude.send_keys(item[0])
    latitude.send_keys(item[1])

    query.click()  # 点击查询按钮
    time.sleep(3)

    map.screenshot(filename=time.strftime("%Y%m%d%H%M%S{}", time.localtime()).format('.png'))
