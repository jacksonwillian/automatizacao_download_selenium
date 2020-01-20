import os

tela = ""

def telaUpdate( variavel = "" ):
	os.system('cls' if os.name == 'nt' else 'clear')
	global tela
	print( tela + "\n" + variavel)

def telaAppend( variavel = ""):
	global tela
	tela = tela + "\n" + variavel
