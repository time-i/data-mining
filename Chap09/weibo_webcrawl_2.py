from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import pandas as pd

WAIT_SECONDS_LONG = 30
WAIT_SECONDS_MID = 10
WAIT_SECONDS_SHORT = 5

def open_url(url):
    driver.get(url)
    time.sleep(WAIT_SECONDS_SHORT)
    # driver.maximize_window()  # 窗口最大化

# 将滚动条移动到页面的底部（重复3次）
def tobottom(times):
    js = "var q=document.documentElement.scrollTop=100000"
    for i in range(times):
        driver.execute_script(js)
        time.sleep(WAIT_SECONDS_SHORT)


# 将滚动条移动到页面的顶部
def totop():
    js = "var q=document.documentElement.scrollTop=0"
    driver.execute_script(js)
    time.sleep(3)


# 解析
def parse_item():
    page_source0 = driver.page_source
    html0 = etree.HTML(page_source0)
    items = html0.xpath('//div[@action-data="cur_visible=0"]')
    for i in range(1, len(items) + 1, 1):
        result = {}
        date = driver.find_element_by_xpath(
            '//div[@action-data="cur_visible=0"][{}]/div/div[@class="WB_detail"]/div[2]/a'.format(i)).get_attribute(
            'title')
        text = ''.join(tuple(driver.find_element_by_xpath(
            '//div[@action-data="cur_visible=0"][{}]/div/div[@class="WB_detail"]/div[4]'.format(i)).text.strip()))

        try:
            image = ''.join(driver.find_element_by_xpath(
                '//div[@action-data="cur_visible=0"][{}]/div/div[@class="WB_detail"]/div[6]//img[1]'.format(
                    i)).get_attribute('src').strip())
        except:
            image = ''

        try:
            forward = driver.find_element_by_xpath(
                '//div[@action-data="cur_visible=0"][{}]/div[2]//li[2]//em[2]'.format(i)).text
        except:
            forward = ''

        try:
            comment = driver.find_element_by_xpath(
                '//div[@action-data="cur_visible=0"][{}]/div[2]//li[3]//em[2]'.format(i)).text
        except:
            comment = ''

        try:
            like = driver.find_element_by_xpath(
                '//div[@action-data="cur_visible=0"][{}]/div[2]//li[4]//em[2]'.format(i)).text

        except:
            like = ''

        # 定位评论
        try:
            # 定位到需要爬取评论内容的微博，使得评论按钮可见可点击
            comment_button = driver.find_element_by_xpath(
                '//div[@action-data="cur_visible=0"][{}]/div/div[@class="WB_detail"]/div[6]//img'.format(i))
            driver.execute_script("arguments[0].scrollIntoView();", comment_button)
            time.sleep(WAIT_SECONDS_SHORT)

            # 模拟点击评论，将评论内容展开
            driver.find_element_by_xpath(
                '//div[@action-data="cur_visible=0"][{}]/div[2]//li[3]//em[2]'.format(i)).click()
            time.sleep(WAIT_SECONDS_SHORT)

            # 获取网页源代码，解析得到评论人ID
            page_source = driver.page_source
            html = etree.HTML(page_source)
            comment_id = html.xpath(
                '//div[@action-data="cur_visible=0"][{}]//div[@node-type="replywrap"][1]/div[@class="WB_text"][1]/a[1]/@usercard'.format(
                    i))

            # 解析得到评论内容，和ID拼接起来
            user_comment = ''
            for j in range(len(comment_id)):
                comments = ''.join(html.xpath(
                    '//div[@action-data="cur_visible=0"][{}]//div[{}]/div[@node-type="replywrap"][1]/div[@class="WB_text"][1]/text()'.format(
                        i, j + 1))).strip()
                user_comment += comment_id[j] + comments + '\n'
        except:
            user_comment = ''

        # 使用生成器返回数据
        result['date'] = date
        result['text'] = text
        result['image'] = image
        result['forward'] = forward
        result['comment'] = comment
        result['user_comment'] = user_comment
        yield result


# 翻页
def next_page():
    next_page = driver.find_element_by_xpath('//a[@class="page next S_txt1 S_line1"]')
    next_page.click()


if __name__ == '__main__':
    url = 'https://weibo.com/wuhandaxue'  # 网页入口

    driver = webdriver.Chrome()

    # 设置需要爬取的页数
    PAGES = 1
    results = []
    open_url(url)
    time.sleep(WAIT_SECONDS_SHORT)

    for i in range(PAGES):
        time.sleep(WAIT_SECONDS_SHORT)
        tobottom(3)
        time.sleep(WAIT_SECONDS_SHORT)
        totop()
        result = parse_item()
        print(result)
        for item in result:
            results.append(item)
            print(item)
        # next_page()
        time.sleep(WAIT_SECONDS_SHORT)

