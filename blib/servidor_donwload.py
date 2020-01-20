from blib import visao
from blib import util
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

def zippyshare(driver = None, url = None, diretorio_download = None):
	try:
		encontrou = False
		driver.get(url)
		button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'dlbutton')))
		url_ep = button.get_attribute("href")
		nome_file = util.get_parte_texto(url_ep,"toleft","/")
		# baixa o arquivo se ele não existe no diretorio de download
		if not ( os.path.exists(diretorio_download + "/"+ nome_file) ):
			driver.get(url_ep)
			tempo = 60
			while (tempo > 0) and (not encontrou ):
				encontrou = os.path.exists(diretorio_download + "/"+ nome_file + ".crdownload")
				time.sleep(1)
				tempo -= 1
		else:
			variavel = ""
			variavel = "\nArquivo: '{}' - Concluido".format(nome_file)
			visao.telaAppend(variavel)
			print(variavel)
			encontrou = True
		return encontrou
	except (KeyboardInterrupt, SystemExit):
		raise KeyboardInterrupt ("Pressionou Ctrl + C")
	except:
		return False

