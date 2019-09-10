import os 
from bs4 import BeautifulSoup


converted_filename = "html4.html"

def crearTxt(nombre, content):
	file2=open("./pages/"+nombre+".html", "a+") 
	file2.write(content)
	file2.close()

def extractText():
	file = open("%s" %(converted_filename), "r+")
	contenido = file.readlines()
	nro_pagina = 1
	content = ''
	for line in contenido:
		line = line.replace("&#160;", " ")
		#print(line)
		content += str(line)
		if('</html>' in line):
			print('parseando html')
			#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#attributes
			tag = BeautifulSoup(content)
			if(tag.name == 'p'):
				tag['style'] = ''
			content += str(tag.contents)
			print(f"----------------------------CREANDO TXT {nro_pagina}----------------------")
			crearTxt("pagina_"+str(nro_pagina), content)
			content = ''
			nro_pagina+=1
			if(nro_pagina == 14):
				exit()

	file.close()

	#texto_final = '<div class="page"><div class="chapter">'+texto_final+'</b></div></div></div>'
	#crearTxt("texto_final", texto_final)


#TODO: QUITAR tie- rra / se- gún
#TODO QUITAR NRO DE HOJAS
#	para quitar nro de hojas, si lo primero es un nro y no tiene más caracteres, es el nro de hoja
#	si lo primero es el nombre del libro, lo segundo sera el capitulo y seguido el nro del versiculo
#	
if __name__ == "__main__":
	extractText()

	#pages = open('texto_final.txt', 'r').read()
	#crearPdf(pages, 'btx_final')


