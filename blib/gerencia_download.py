from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from blib import visao
from blib import util
import time

def listen_donwload(driver):
	while True:
		variavel = ""
		download_andamento = 0
		lst_progresso = get_download_progresso(driver)
		for progress in lst_progresso:
			barra_progresso, url, descricao = progress
			situacao = ""
			if (int(barra_progresso) < 100) and (descricao != ""):
				download_andamento += 1
				situacao = "Tamanho: {} - Progresso: {}%  Transferencia: {}\n".format(util.get_parte_texto(descricao.split("de")[1].strip(),"torigth",","), barra_progresso, util.get_parte_texto(descricao,"torigth","-"))
			elif(int(barra_progresso) == 100):
				situacao = "Concluido\n"
			else:
				situacao = "interrompido\n"
			variavel += "\n\nArquivo: '{}' - {}".format(util.get_parte_texto(url,"toleft","/"), situacao)
		visao.telaUpdate("\nDonwload Atual: \n" + variavel + "\n\nDonwload em andamento: {}".format(download_andamento))
		if download_andamento == 0:
			visao.telaAppend("\n\n"+ variavel.strip())
			visao.telaUpdate()
			break
		time.sleep(1)
	time.sleep(10)
	limpa_historico(driver)

def limpa_historico(driver):
	driver.get('chrome://downloads/')
	root1  = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.TAG_NAME, 'downloads-manager')))
	shadow_root1 = in_shadow_elemento(driver, root1)	
	root2 = shadow_root1.find_element_by_css_selector('downloads-toolbar')
	shadow_root2 = in_shadow_elemento(driver, root2)
	root3 = shadow_root2.find_element_by_css_selector('cr-action-menu')
	root4 = root3.find_elements_by_tag_name('button')
	if(len(root4) == 2):
		driver.execute_script("arguments[0].click();", root4[0])
	time.sleep(3)
	return None
	
def get_download_progresso(driver):
	# https://stackoverflow.com/questions/36141681/does-anybody-know-how-to-identify-shadow-dom-web-elements-using-selenium-webdriv
	try:
		if driver.current_url != 'chrome://downloads/':
			driver.get('chrome://downloads/')
		root1  = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.TAG_NAME, 'downloads-manager')))
		shadow_root1 = in_shadow_elemento(driver, root1)
		root2 = shadow_root1.find_element_by_id('mainContainer')
		root3 = root2.find_element_by_id('downloadsList')
		root4 = root3.find_elements_by_tag_name('downloads-item')
		lst_progresso =[]
		for elemento in root4:
			shadow_root2 = in_shadow_elemento(driver, elemento)
			url = shadow_root2.find_element_by_id("url")
			description = shadow_root2.find_element_by_id("description")
			barra_progresso = shadow_root2.find_element_by_id("progress")
			safe = shadow_root2.find_element_by_id("safe")
			buttonTexto = driver.execute_script("return arguments[0].getElementsByTagName('cr-button')[0].textContent;", safe)
			barra = barra_progresso.get_attribute("value")
			if(buttonTexto.strip() == "Retomar"):
				# se o download está interrompido clica no botão retomar
				driver.execute_script("arguments[0].getElementsByTagName('cr-button')[0].click();", safe)
			## donwload concluido texto Mostrar na pasta
			# if("Mostrar na pasta" in safe.text):
			# 	barra = "100"
			lst_progresso.append((barra, url.get_attribute("href"), description.text))
		return lst_progresso
	except (KeyboardInterrupt, SystemExit):
		raise KeyboardInterrupt ("Pressionou Ctrl + C")
	except:
		return []

def in_shadow_elemento(driver, elemento):
	shadow_root = driver.execute_script('return arguments[0].shadowRoot', elemento)
	return shadow_root
