#coding: utf-8

from selenium import webdriver
import time
import os

profile_dir=r"C:\Users\heyon\AppData\Local\Google\Chrome\User Data" 
# 对应你的chrome's user data path
chrome_options=webdriver.ChromeOptions()  
chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))
browser=webdriver.Chrome(chrome_options=chrome_options)  
browser.maximize_window() 
browser.get("http://www.uestcedu.com/ifree/console/")

m=8# 窗口数
n=[116812,116840,116868,116896,116924,116952,116979,117008]# 117035章节
for i in range(m):
	handles = browser.window_handles
	browser.switch_to.window(handles[i])# 切换handles[]
	browser.find_element_by_id('login_button').click()# login
	browser.implicitly_wait(1)
	browser.find_element_by_xpath('.//*[@id="left_menu_ul"]/li[3]/a').click()# onlinecourse
	browser.switch_to_frame("f_M00370003")
	browser.find_element_by_xpath('.//*[@id="tr_tblDataList_8"]/td[8]/a[1]').click()# 大学英语
	browser.close()
	browser.implicitly_wait(1)
	handles = browser.window_handles
	browser.switch_to.window(handles[i])
	browser.switch_to_frame('w_main')
	browser.implicitly_wait(3)
	browser.find_element_by_id('spanLearnContent_%d'%n[i]).click()
	browser.implicitly_wait(1)
	js1 = " window.open('http://www.uestcedu.com/ifree/console/')" #打开新的标签页
	browser.execute_script(js1)
handles = browser.window_handles
browser.switch_to.window(handles[m])
browser.close()

k=0
while k<2000:
	k+=1
	for j in range(m):
		handles = browser.window_handles
		browser.switch_to.window(handles[j])
		browser.implicitly_wait(3)
		browser.switch_to_default_content()
		browser.switch_to_frame('w_main')
		browser.switch_to_frame('w_lms_content')
		src1='您'
		src2='in'
		browser.implicitly_wait(1)
		try:
			status=browser.find_element_by_xpath(".//*[@id='tdRemark']/img")
			s=status.get_attribute('src')
			src2=s[52]
		except :
			src1=browser.find_element_by_xpath(".//*[@id='tdRemark']/span").text
		browser.implicitly_wait(1)
		browser.switch_to_default_content()
		browser.switch_to_frame('w_main')
		browser.switch_to_frame('w_code')
		if 'c' in (src1+src2):
			browser.find_element_by_id('btnNext').click()# 下一个
		elif '毕' in (src1+src2) :
			browser.find_element_by_id('btnNext').click()# 下一个
		browser.implicitly_wait(3)
		browser.switch_to_default_content()
		browser.switch_to_frame('w_main')
		browser.switch_to_frame('w_lms_content')
		browser.switch_to_frame('w_sco')
		browser.switch_to_frame('w_content')
		browser.switch_to_frame('w_sco')
		element = browser.find_elements_by_xpath('.//body/div/header/div[2]//span')# 获取章节标签数
		length = len(element)
		j=0
		for i in element:
			j+=1
			browser.find_element_by_xpath('.//body/div/header/div[2]/span[%d]'%j).click()
	time.sleep(10)
	print(k)