# coding=utf-8

import requests
from lxml import etree
import time
import socket
import csv
from selenium import webdriver
from configparser import ConfigParser
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import json


def login():
	# 打开参数
	option = ChromeOptions()
	option.add_experimental_option('excludeSwitches', ['enable-automation'])
	wb=webdriver.Chrome(options=option)
	# wb.maximize_window()
	wb.set_window_size(1200, 700)
	wb.get("https://weibo.com")
	wb.implicitly_wait(2)

	qqqqq = input("登录成功后任意输入：")
	#登录成功
	print('登录成功')
	return wb


def get_data(wb, year, start_month, end_month, day1, day2, pages):
	month = start_month
	while (month < end_month+1):
		# 发布时间的列表time2 ,博文的列表 textAll
		time2 = []
		textAll = []
		flag = 0

	# 爬取当前时间段全部页的内容
		for yeshu in range(1, pages):
			page = yeshu
			try:
				url = "https://s.weibo.com/weibo?q={}&region=custom:44:1000&typeall=1&suball=1&timescope=custom:{}-{}-{}:{}-{}-{}&Refer=g&page={}".format(
					index, year, month, day1, year, month, day2, page)
				wb.get(url)
				wb.implicitly_wait(2)

			# 错误检测
				try:
					errorTxt = ""
					merror = wb.find_element(By.XPATH,'//div[@class="card card-no-result s-pt20b40"]/p')
					errorTxt = merror.text
					# print(errorTxt)
					if (errorTxt[0] == '抱' and errorTxt[1] == '歉'):
						flag += 1
					if (flag > 4):
						break
					continue
				except:
					pass
				# 爬取时间
				time1 = wb.find_elements(By.XPATH,'//div[@class="card-feed"]/div[@class="content"]/p[@class="from"]/a[last()-1]')
				for i in time1:
					time2.append(i.text)

				# 先点击所有的展开原文
				temp = wb.find_elements(By.XPATH,
					'//div[@class="card-feed"]/div[@class="content"]/p[@node-type="feed_list_content"]/a[@action-type="fl_unfold"]')
				for i in temp:
					if (i.text[0] == "展" and i.text[1] == "开"):
						i.click()

				texttp = wb.find_elements(By.XPATH,
					'//div[@class="card-feed"]/div[@class="content"]/p[@node-type="feed_list_content_full"]')
				for i in texttp:
					temp1 = ""
					temp = i.text
					for j in temp:
						temp1 = temp1 + j
					textAll.append(temp1)
				# 如果没有展开全文按钮，就去没有展开全文按钮的段落爬
				texttp = wb.find_elements(By.XPATH,
					'//div[@class="card-feed"]/div[@class="content"]/p[@node-type="feed_list_content"]')
				for i in texttp:
					temp1 = ""
					temp = i.text
					for j in temp:
						temp1 = temp1 + j
					# print("leng=",len(temp1),temp1)
					if (len(temp1) > 0):
						textAll.append(temp1)

				time.sleep(1.1)
			except:
				continue
			# 爬取完

		# 导出json文件
		for text, _time in zip(textAll, time2):
			try:
				with open(outputExcel + '.json', 'a', encoding='utf-8') as f:
					if text != '':
						f.write(json.dumps({'time': _time, 'text': text}, ensure_ascii=False)+'\n')
			except:
				continue
		time.sleep(2)

		month+=1
		day2=30
		if(month==2):
			day2=28
		elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
			day2=31
		else:
			day2=30


if __name__ == '__main__':
	index="武汉大学"	# 关键词
	year=2021	# 年份
	start_month=11	# 起始月份
	end_month=11	# 终止月份
	day1=1		# 起始日期
	day2=30		# 终止日期
	pages=5	# 爬取页数

	# 保存爬取的数据文件文件名
	outputExcel = 'whu_weibo'

	wb = login()
	get_data(wb, year, start_month, end_month, day1, day2, pages)

