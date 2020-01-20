def get_parte_texto(texto, sentido, limitador):
	frase = ""
	if (sentido == "torigth" and limitador in texto):
		for i in range (0, len(texto)):
			if (texto[i] != limitador):
				frase =  frase + texto[i]
			else:
				return frase
	elif(sentido == "toleft" and limitador in texto):
		for i in range (len(texto)-1, -1, -1):
			if (texto[i] != limitador):
				frase =  texto[i] + frase
			else:
				return frase
	return frase