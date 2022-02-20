from selenium import webdriver
import os
import time

print(os.environ["PATH"])
driver = webdriver.Chrome()

driver.get('https://m.weibo.cn')

# wait for the webpage to open
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# WebDriverWait(driver, 30).until(lambda x: x.find_element(By.CLASS_NAME, "NavItem_text_3Z0D7"))

# open dev view (windows Ctrl + Shift + I) mac (Cmd + Opt + I)
# locate an element by the following ways
# 前三行字段更新后消失，仅作演示说明
element = driver.find_element(By.ID,'app')
#element = driver.find_element(By.CLASS_NAME,'m-text-cut')
#element = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[1]/a/aside/label/div')

#element = driver.find_element_by_class_name()
#element = driver.find_element(By.CLASS_NAME,'NavItem_text_3Z0D7')
print(element.text)

# close web browser
# driver.quit()