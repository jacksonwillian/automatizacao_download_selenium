import os
import sys
from blib import visao
from blib import gerencia_webdriver
from blib import anbient_scraper
from blib import servidor_donwload
from blib import gerencia_download
import logging

def toDownload(url_pagina = None, max_download_simultaneo = 1, eps_ignorados = [], nome_servidor = None, diretorio_download = None):

	# valida parametros
	if(url_pagina == None or url_pagina == ""):
		raise Exception ("url da página não foi informado")
	elif("www.anbient.com" not in  url_pagina.lower()):
		raise Exception ("url da pagina não pertecende ao 'www.anbient'")
	elif (nome_servidor != None and nome_servidor != "") and (nome_servidor.lower() not in ["zippyshare"]):
		raise Exception ("nome do servidor não é válido")
	elif(diretorio_download == None) or (diretorio_download == "") or (not os.path.exists(diretorio_download)):
		diretorio_download = os.getcwd()

	# fixa msg na tela	
	variavel = "Página do Anime = '{}'\nIgnorar Espisódios: {}\nServidor = '{}'\nDownload Simultaneo: {}\nSalvar em = '{}'".format(url_pagina, eps_ignorados, nome_servidor, max_download_simultaneo,diretorio_download)
	visao.telaAppend( variavel = variavel)
	visao.telaUpdate()
	
	# inicializa variavel driver
	driver = None

	try:

		# configura webdriver
		driver = gerencia_webdriver.abre_navegador(diretorio_download)

		# buscando links para download
		lstLinks = anbient_scraper.scraperLinksEp(driver = driver, url_pagina = url_pagina, eps_ignorados = eps_ignorados, nome_servidor = nome_servidor)
		
		# fixa msg na tela
		variavel = "\nForam encontrados {} link(s) para download.".format(len(lstLinks))
		visao.telaAppend( variavel = variavel)
		visao.telaUpdate()

		if (lstLinks != []):
			# fixa msg na tela
			variavel = "\nInformação de Download:\n"
			visao.telaAppend( variavel = variavel)
			visao.telaUpdate()

			# controla os downloads
			quant_donwload_atual = 0
			limite = False
			for i in range (len(lstLinks)):
				link = lstLinks[i]
				if (not limite) and  (quant_donwload_atual <= max_download_simultaneo):
					resultado = servidor_donwload.zippyshare(driver = driver, url = link, diretorio_download = diretorio_download)
					if resultado == True:
						quant_donwload_atual += 1
					else:
						print("\nNão foi possível fazer o download. O programa tentará o próximo link")
					if quant_donwload_atual == max_download_simultaneo:
						limite = True
				if (limite) or (i == (len(lstLinks) - 1)):
					gerencia_download.listen_donwload(driver)
					quant_donwload_atual = 0
					limite = False
	except:
		e = sys.exc_info()
		variavel = "\n# O PROGRAMA PAROU # Leia o arquivo 'error.log' para mais informações.\n"
		visao.telaAppend( variavel = variavel)
		logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
		logging.error(e)
	finally:
		gerencia_webdriver.fecha_navegador(driver)
		variavel = "\nEncerrou"
		visao.telaAppend( variavel = variavel)
		visao.telaUpdate()
