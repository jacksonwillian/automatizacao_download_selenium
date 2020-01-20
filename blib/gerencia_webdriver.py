from selenium import webdriver
from fake_useragent import UserAgent
import os

def get_chromedriver():
	if(os.name == 'nt'):
		if not os.path.exists('./chromedriver.exe'):
			raise Exception ("É necessário o arquivo 'chromedriver.exe' no diretório atual")
		return './chromedriver.exe'
	else:
		if not os.path.exists('./chromedriver'):
			raise Exception ("É necessário o arquivo 'chromedriver' no diretório atual")
		return './chromedriver'

def abre_navegador( diretorio_download ):
	options = webdriver.ChromeOptions()	
	ua = UserAgent()
	userAgent = ua.random
	options.add_argument(f'user-agent={userAgent}')	
	options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
	options.add_experimental_option('useAutomationExtension', False)
	options.add_experimental_option("prefs", {
									 "download.default_directory": r"{}".format(diretorio_download),
									 "download.prompt_for_download": False,
									 "download.directory_upgrade": True,
									 "safebrowsing.enabled": True
									})
	diretorio = get_chromedriver()
	driver = webdriver.Chrome(options=options, executable_path=diretorio)
	return driver

def fecha_navegador(driver):
	try:
		driver.close()	
	except:
		pass
