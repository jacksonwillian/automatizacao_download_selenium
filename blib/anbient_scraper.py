from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def scraperLinksEp(driver = None, url_pagina = None, eps_ignorados = None, nome_servidor = None):
	driver.get(url_pagina)
	elementoServidor = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'tabs-servidores')))
	textLinkEp = ""
	lstLinkSelectServidor = elementoServidor.find_elements_by_tag_name("li")
	for linkServidor in lstLinkSelectServidor:
		elementeA = linkServidor.find_element_by_tag_name("a")
		if nome_servidor in elementeA.get_attribute('href'):
			linkServidor.click()
			url = elementeA.get_attribute('href')
			id = url.split("#")[1].strip()
			linkTagA = driver.find_element_by_xpath('//*[@id="'+id+'"]/div/a[1]')
			driver.execute_script("arguments[0].click();", linkTagA) # usa o javascript para clicar no 1º parametros
			linkEpHospedado = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'server-lista')))
			textLinkEp = linkEpHospedado.text
			break
	lstLink =[]
	lst = textLinkEp.strip().split("\n")
	for i in range (len(lst)):
		if i+1 not in eps_ignorados:
			if("zippyshare.com" in lst[i]):
				lstLink.append(lst[i].strip())
	return lstLink
