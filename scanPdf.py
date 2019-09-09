import os 

directory_with_files_of_interest = "."
file_to_convert_to_txt = "biblia-textual_unlocked.pdf"
converted_filename = "test_file.txt"
import pdfkit
page = "11"
#scroll over so you don't miss cut off text here
#os.system("python3 pdf2txt.py -o %s %s/%s -p %s" %(converted_filename, directory_with_files_of_interest, file_to_convert_to_txt,page))


def crearTxt(nombre, content):
	file=open(nombre+".txt", "a+") 
	file.write(content)

def crearPdf(pages, nombre='btx'):
	#TODO: Revisar bien el css para paginas nuevas
	#https://htmlpdfapi.com/blog/using_css_page_breaks_when_converting_html_to_pdf
	html_content = """
	<!DOCTYPE html>
	<html>
	<head>
	    <meta charset="utf-8">
	    <!--style>
	    	/*.chapter {
		        break-inside: avoid;
		        page-break-inside: avoid;
		    }*/
		    .chapter{
		    	margin-bottom: 10mm;
			  	padding-bottom: 10mm;
		    }
	    	div.page {
			  width: 180mm;
			  height: 277mm;
			  overflow: hidden;
			  margin-bottom: 10mm;
			  padding-bottom: 10mm;
			  /*page-break-after: always;*/
			}
	    </style-->

	    <style>
	    	/*.verse {
		        break-inside: avoid;
		        page-break-inside: avoid;
		    }*/
	    	div.page {
			  overflow: hidden;
			  break-inside: avoid;
		      /*page-break-inside: avoid;*/
			}
	    </style>
	</head>
	<body>"""

	html_content += pages
	html_content += """	
	<body>
	</html>
	"""
	pdfkit.from_string(html_content,nombre+'.pdf') 

def extractText():
	texto_final='<div class="page">'
	#take a look at the contents
	#file = open("%s" %(converted_filename), "rt")
	file = open("%s" %(converted_filename), "r+")
	contenido = file.readlines()
	versiculo_anterior = 0
	comentario_anterior = False
	for line in contenido:
		#print(line)
		if len(line) > 1:
			if comentario_anterior:
				print("Es continuación de comentario:")
				print(line)
				texto_final +="<i>"+line+"</i>"
			else:
				primer_char = line[0]
				if primer_char.isdigit():
					segundo_char = line[1]
					if segundo_char == '.':
						print("Es comentario:")
						print(line)
						texto_final +="<br/><br/><br/><br/><b><i>"+line+"</i>"
						comentario_anterior = True
					else:
						print("es inicio de versiculo:")
						print(line)
						if line[1].isdigit():
							if line[2].isdigit():
								versiculo_anterior = int(primer_char+line[1]+line[2])
								print("nuevo versiculo: "+str(versiculo_anterior)+"<br/>")
							else:
								versiculo_anterior = int(primer_char+line[1])
								print("nuevo versiculo: "+str(versiculo_anterior)+"<br/>")
						else:
							versiculo_anterior = int(primer_char)
							print("nuevo versiculo: "+str(versiculo_anterior)+"<br/>")
						texto_final +="<br/><br/>"+line.replace(str(versiculo_anterior),'<b>'+str(versiculo_anterior)+'</b>')
						#line.rstrip('\n')Eloh
				elif int(versiculo_anterior) > 0 and (primer_char.isalpha() or primer_char == '’'):
					print("es continuación de versiculo:")
					print(line)
					texto_final +=line
					#line.rstrip('\n')
				else:
					print("no cumple ninguna condicion:")
					print(line)
					texto_final +="<h2>"+line+"</h2>"

	file.close()

	texto_final = '<div class="page"><div class="chapter">'+texto_final+'</b></div></div></div>'
	crearTxt("texto_final", texto_final)


#TODO: QUITAR tie- rra / se- gún
#TODO QUITAR NRO DE HOJAS
#	para quitar nro de hojas, si lo primero es un nro y no tiene más caracteres, es el nro de hoja
#	si lo primero es el nombre del libro, lo segundo sera el capitulo y seguido el nro del versiculo
#	
if __name__ == "__main__":
	#page = 11
	#os.system("pdf2txt.py -o %s -p %s biblia-textual_unlocked.pdf" %(converted_filename,page))
	#extractText()
	page = 12
	os.system("pdf2txt.py -o %s -p %s biblia-textual_unlocked.pdf" %(converted_filename,page))
	extractText()

	pages = open('texto_final.txt', 'r').read()
	crearPdf(pages, 'btx_final')




'''[summary]
def modificar_dato(ruta, filas, columna, nuevo_dato):
	contenido = list()
	with open(ruta, 'r+') as archivo:
		contenido = archivo.readlines()
		for fila in filas:
			columnas = contenido[fila-1].split(';')
			columnas[columna] = nuevo_dato
			contenido[fila-1] = ';'.join(columnas)+ '\n'
	with open(ruta, 'w') as archivo:
		archivo.writelines(contenido)


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO

def pdf_to_text(path):
	manager = PDFResourceManager()
	retstr = BytesIO()
	layout = LAParams(all_texts=True)
	device = TextConverter(manager, retstr, laparams=layout)
	filepath = open(path, 'rb')
	interpreter = PDFPageInterpreter(manager, device)

	for page in PDFPage.get_pages(filepath, pagenos=11, maxpages=1, check_extractable=True):
		interpreter.process_page(page)

	text = retstr.getvalue()

	filepath.close()
	device.close()
	retstr.close()
	return text


if __name__ == "__main__":
	text = pdf_to_text("biblia-textual_unlocked.pdf")
	print(text)

##################
[description]
''' 
'''[summary]
extraer texto
guardar en variable
si el primer caracter es un numero y el primer caracter es un 1, añadir nro de capitulo (¿Como? quiza con contador de capitulos)
luego seguir observando el primer caracter, si es numerico, ver si el siguiente es un punto, si es un punto entonces son los comentarios (si es un numero, continúo)
si son los comentarios, los corto, luego a todo el texto le quito los saltos de linea
luego pongo otra ves los comentarios

si el primer caracter no es numerico, quito el salto de linea final. si tiene guión, lo borro.

s.rstrip('\n')

[description]
'''
## For digit
## '1'.isdigit()
##'1'.isalpha()
#
#for char in line:
#	print(char)