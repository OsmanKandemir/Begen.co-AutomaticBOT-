#! usr/bin/env python
#! -*- coding : utf - 8 -*-



import re
import mechanize
import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#https://goo.gl/oFB4GJ
#entertoken = raw_input("Please Enter The Your Token : ")
#likelink = raw_input("Please Enter The Your Share Link : ")


path = r"/home/osman/Desktop/chromedriver"
browser = webdriver.Chrome(path)
browser.get("http://begen.co/index.php")
a = raw_input("deneme")
#token = browser.find_element_by_name("token")
#token.send_keys(entertoken)
log_but2 = "//input[@class='submit']"
browser.find_element_by_xpath(log_but2).click()
log_but3= "//input[@class='greyishBtn']"
browser.find_element_by_xpath(log_but3).click()

def kaydet(ca):
	ab = browser.page_source.encode("utf-8")
	ls = str(ab)
	reg = re.search('<img src=.+alt=',ls)
	kaydet1 = open("cap.txt","a+")
	yazdir = reg.group().replace('<img src="/l/captcha.php?_CAPTCHA&amp;t=',"")[:4] + ":" + ca + "\n"
	kaydet1.writelines(yazdir)
	kaydet1.close()


def fonk():
	while(1):

		head = browser.find_element_by_xpath("//input[contains(@class, 'validate[required]')]")
		head.send_keys("https://www.facebook.com/NewBeTurkey/posts/611801562340285")
		log_but4= "//input[@class='greyishBtn submitForm']"
		browser.find_element_by_xpath(log_but4).click()
		ca = raw_input("gir bakam : ")
		captcha = browser.find_element_by_name("captcha")
		captcha.send_keys(ca)
		kaydet(ca)
		log_but4 = "//input[@type='submit']"
		browser.find_element_by_xpath(log_but4).click()
		time.sleep(1)
		while(1):
			if 'src="index/success.png"' in browser.page_source.encode("utf-8"):
				browser.find_element_by_xpath("//a[@href ='../']").click()
				time.sleep(4)
				fonk()
			elif not 'src="index/success.png"' in browser.page_source.encode("utf-8"):
				while(1):
					time.sleep(2)
					if 'src="index/success.png"' in browser.page_source.encode("utf-8"):
						browser.find_element_by_xpath("//a[@href ='../']").click()
						time.sleep(4)
						fonk()
					if  'Her 50 saniyede' in browser.page_source.encode("utf-8"):
						browser.find_element_by_xpath("//a[@href ='../']").click()
						time.sleep(4)
						fonk()
					if "Hata Kodu:104" in browser.page_source.encode("utf-8"):
						browser.find_element_by_xpath("//a[@href ='../']").click()
						time.sleep(4)
						fonk()



			else:
				time.sleep(2)

fonk()




