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
from selenium.common.exceptions import NoSuchElementException

#https://goo.gl/oFB4GJ
#entertoken = raw_input("Please Enter The Your Token : ")
#likelink = raw_input("Please Enter The Your Share Link : ")

try:
	
	link = "https://www.facebook.com/NewBet/posts/1310330502359232"
	path = r"/home/osman/Desktop/chromedriver"
	browser = webdriver.Chrome(path)
	browser.get("http://begen.co/index.php")
	a = raw_input("Token Bekleniyor")
	#token = browser.find_element_by_name("token")
	#token.send_keys(entertoken)
	log_but2 = "//input[@class='submit']"
	browser.find_element_by_xpath(log_but2).click()
	log_but3= "//input[@class='greyishBtn']"
	browser.find_element_by_xpath(log_but3).click()

	def kaydet():
		time.sleep(2)
		ab = browser.page_source.encode("utf-8")
		ls = str(ab)

		ca = raw_input("Kayitli Olmayan Captcha'yi Girin : ")
		reg = re.search('<img src=.+alt=',ls)
		kaydet1 = open("cap.txt","a+")
		yazdir = reg.group().replace('<img src="/l/captcha.php?_CAPTCHA&amp;t=',"")[:4] + ":" + ca + "\n"
		kaydet1.writelines(yazdir)
		kaydet1.close()
		print "Kayitli Olmayan Captcha Kaydedildi."
		print len(browser.window_handles)
		captcha = browser.find_element_by_name("captcha")
		captcha.send_keys(ca)
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
					if "Hata Kodu:107" in browser.page_source.encode("utf-8"):
						browser.find_element_by_xpath("//a[@href ='../']").click()
						time.sleep(4)
						fonk()
					if "Facebooktan kaynaklanan" in browser.page_source.encode("utf-8"):
						browser.find_element_by_xpath("//a[@href ='../']").click()
						time.sleep(4)
						fonk()



				else:
					time.sleep(2)

	def captchaKaydet(ab1,ls1):
		time.sleep(5)
		reg1 = re.search('<img src=.+alt=',ls1)
		af = open("cap.txt")
		re1 = af.read()
		time.sleep(6)
		regex = reg1.group().replace('<img src="/l/captcha.php?_CAPTCHA&amp;t=',"")[:4]
		if "<img" in regex:
			browser.get("http://begen.co/index.php")
			print "Kaynak Kod Okunamadi TEKRAR DENENIYOR"
			head = browser.find_element_by_xpath("//input[contains(@class, 'validate[required]')]")
			head.send_keys(link)
			log_but4= "//input[@class='greyishBtn submitForm']"
			browser.find_element_by_xpath(log_but4).click()
			time.sleep(1)
			ab1 = browser.page_source.encode("utf-8")
			ls1 = str(ab1)
			captchaKaydet(ab1,ls1)
		print "Captcha Id = %s" %regex
		if regex in re1:
			af1 = open("cap.txt")
			re2 = af1.readlines()
		
			for i in re2:

				if regex in i:
					ay = i.split(":")
					print "Kayitli Captcha Bulundu"
					print "Tarayicidaki Sekme Sayisi %s " %len(browser.window_handles)
					#if len(browser.window_handles) >= 2:
						#while(1):
							#browser.get("http://begen.co/index.php")
							#head = browser.find_element_by_xpath("//input[contains(@class, 'validate[required]')]")
							#head.send_keys(link)
							#log_but4= "//input[@class='greyishBtn submitForm']"
							#browser.find_element_by_xpath(log_but4).click()
							#time.sleep(1)
							#ab1 = browser.page_source.encode("utf-8")
							#ls1 = str(ab1)
							#captchaKaydet(ab1,ls1)

			captcha = browser.find_element_by_name("captcha")
			captcha.send_keys(ay[1])
			time.sleep(2)
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
						if "Hata Kodu:107" in browser.page_source.encode("utf-8"):
							browser.find_element_by_xpath("//a[@href ='../']").click()
							time.sleep(4)
							fonk()
						if "Facebooktan kaynaklanan" in browser.page_source.encode("utf-8"):
							browser.find_element_by_xpath("//a[@href ='../']").click()
							time.sleep(4)
							fonk()
				else:
					time.sleep(2)

		if not regex in re1:
			kaydet()			
			

		
		#captcha = browser.find_element_by_name("captcha")
		#captcha.send_keys(ay[1])
		


				
				#log_but4 = "//input[@type='submit']"
				#browser.find_element_by_xpath(log_but4).click()

	def fonk():
		while(1):

			head = browser.find_element_by_xpath("//input[contains(@class, 'validate[required]')]")
			head.send_keys(link)
			log_but4= "//input[@class='greyishBtn submitForm']"
			browser.find_element_by_xpath(log_but4).click()
			time.sleep(1)
			ab1 = browser.page_source.encode("utf-8")
			ls1 = str(ab1)
			captchaKaydet(ab1,ls1)
			#captcha = browser.find_element_by_name("captcha")
			#captcha.send_keys(ca)
			#kaydet(ca)
			#log_but4 = "//input[@type='submit']"
			#browser.find_element_by_xpath(log_but4).click()

	fonk()


except NoSuchElementException:
	print "reklam"
	while(1):

		browser.get("http://begen.co/index.php")
		head = browser.find_element_by_xpath("//input[contains(@class, 'validate[required]')]")
		head.send_keys(link)
		log_but4= "//input[@class='greyishBtn submitForm']"
		browser.find_element_by_xpath(log_but4).click()
		time.sleep(1)
		ab1 = browser.page_source.encode("utf-8")
		ls1 = str(ab1)
		captchaKaydet(ab1,ls1)

