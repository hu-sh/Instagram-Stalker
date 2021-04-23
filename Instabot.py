from selenium import webdriver
import os.path
import os
import time

class Instabot:
	def __init__(self, username, pw):
		self.driver = webdriver.Chrome()
		self.driver.get("https://instagram.com")

		# COOKIE
		try:
			self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]").click()
		except Exception:
			print (Exception)
		time.sleep(2)

		# USERNAME E PASSWORD
		self.driver.find_element_by_xpath('//input[@name=\"username\"]').send_keys(username)
		self.driver.find_element_by_xpath('//input[@name=\"password\"]').send_keys(pw)
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		time.sleep(4)
		
		# NOTIFCHE E RICORDA DATI
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
			.click()
		#time.sleep(2)
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
			.click()
		time.sleep(1)

	def esisto(self):
		return True

	def get_following(self, user):
		
		self.cerca(user)

		#DEH MA GUARDALI UN POINO I SEGUITI
		self.driver.find_element_by_xpath("//a[contains(@href, 'following')]")\
			.click()
		time.sleep(1)

		# TUPLA DEI SEGUITI
		names = self._get_names()
		
		# TORNA ALLA HOME (FACOLTATIVO)
		# self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a")\
		#	.click()
		
		return names
	
	def get_followers(self, user):

		self.cerca(user)

		#DEH MA GUARDALI UN POINO I FOLLOWERS
		self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]")\
			.click()
		time.sleep(1)

		# TUPLA DEI FOLLOWERS
		names = self._get_names()
		
		# TORNA ALLA HOME (FACOLTATIVO)
		# self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a")\
		#	.click()
		
		return names

	def _get_names (self):
		
		#sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
		#self.driver.execute_script('windows.scrollIntoView()', sugs)
		#time.sleep(1)
	
		# ELEMENTO HTML SCORRIBILE
		scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
		
		last_ht, ht = 0, 1
		while last_ht != ht:
			last_ht = ht
			time.sleep(1.5)
			ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scroll_box)

		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']
		print (names)

		# CHIUDE ELEMENTO SCORRIBILE
		self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
			.click()
		
		return names

	def cerca(self, user):
		#DEH CERCA UN PO
		self.driver.find_element_by_xpath('//input[@placeholder=\"Search\"]').send_keys(user)
		#self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')\
		#	.send_keys(user)
		#/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]
		time.sleep(2)

		# DEH CLICCA UN POINO SUL PRIMO RISULTATO
		self.driver.find_element_by_xpath("//a[@class='yCE8d  '][position()=1]")\
			.click()
		time.sleep(5)
		return 
