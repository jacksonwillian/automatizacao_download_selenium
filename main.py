from blib import gerenciador

def main():

	# url da pagina com a lista de servidores
	urlPagina = "https://www.anbient.com/anime/steinsgate-soumei-eichi-no-cognitive-computing"

	# lista de episodio a ignorar
	lstEpIgnore = [2]

	# quantidade de downloads simultâneo
	quantSimultaneo = 2

	# nome do servidor 
	nomeServidor = "zippyshare"

	# caminho da pasta do dowload
	diretorioDownload = "E:\\Downloads"

	gerenciador.toDownload(url_pagina = urlPagina, max_download_simultaneo = quantSimultaneo, eps_ignorados = lstEpIgnore, nome_servidor = nomeServidor, diretorio_download = diretorioDownload)

	return 0

main()
