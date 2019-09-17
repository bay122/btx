from bs4 import BeautifulSoup
import pdfkit
import re

html_capitulos = '''
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
<title></title>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
 <br/>
<style type="text/css">
<!--
	p {margin: 0; padding: 0; display: inline;}
	.cap{font-size:36px;font-family:Times;color:#231f20;}
	.cabecera{font-size:14px;font-family:Times;color:#231f20;}
	.ver{font-size:13px;font-family:Times;color:#231f20;}
	.desc{font-size:9px;font-family:Times;color:#231f20;}
	.hidden {display: none}
-->
</style>
</head>
<body bgcolor="#fff" vlink="blue" link="blue">
</body>
</html>
'''


def crearPdf(html_content, nombre='btx'):
	#https://www.programcreek.com/python/example/100584/pdfkit.from_string
	options = {
            'page-size': 'A5',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'dpi': 150,
            'quiet': '',
            # 'print-media-type': '',
        }
	pdfkit.from_string(html_content,nombre+'.pdf', options=options)

def crearTxt(nombre, content):
	file2=open("./"+nombre+".html", "a+") 
	file2.write(content)
	file2.close()

def processPages(nro_pagina = 11):
	paginas_generales = [1,2,3,4,5,6,7,8,9,10]
		
	# load the file
	with open("pages/pagina_"+str(nro_pagina)+".html") as inf:
	    html_doc = inf.read()
	    soup = BeautifulSoup(html_doc, 'html.parser')

	#print(soup.prettify())
	#soup.find_all('p')
	if(nro_pagina not in paginas_generales):
		print("Buscando clases CSS de los versiculos...")
		clases_capitulos = []
		clases_cabecera = []
		clases_versiculos = []
		clases_descripcion = []
		styles = soup.head.style.string.split('\n')
		string_style = ''
		for style in styles:
			print("buscando clase css en: "+style)
			found = re.search('font-size:(.+?)px;', style)
			if(found != None):
				print("Estilo detectado!")
				if(found.group(1) == '36'):
					print("Agregando a clases_capitulos")
					clases_css = re.search('ft(.+?){', style).group(1)
					print("ft"+clases_css)
					print("\n")
					clases_capitulos.append("ft"+clases_css)
				elif(found.group(1) == '14'):
					print("Agregando a clases_cabecera")
					clases_css = re.search('ft(.+?){', style).group(1)
					print("ft"+clases_css)
					print("\n")
					clases_cabecera.append("ft"+clases_css)
				elif(found.group(1) == '13'):
					print("Agregando a clases_versiculos")
					clases_css = re.search('ft(.+?){', style).group(1)
					print("ft"+clases_css)
					print("\n")
					clases_versiculos.append("ft"+clases_css)
				elif(found.group(1) == '9'):
					print("Agregando a clases_descripcion")
					clases_css = re.search('ft(.+?){', style).group(1)
					print("ft"+clases_css)
					print("\n")
					clases_descripcion.append("ft"+clases_css)
				else:
					print("clase desconocida detectada\n")
					print(style)
			else:
				print("No registra estilos\n")

		##limpio estilo de div page
		#https://linuxhint.com/python-beautifulsoup-tutorial-for-beginners/
		soup.find_all("div")[0].attrs['style'] = "position:relative;width:874px;height:1240px;"
		
		'''[Tipos de clase css]
		Capitulo: 36px;
		Versiculos 13px;
		cabecera de pagina: 14px;
		nro de pagina: 14px;
		descripcion: 9px;
		'''

		#print("clases_capitulos: "+str(clases_capitulos))
		#print("clases_cabecera: "+str(clases_cabecera))
		#print("clases_versiculos: "+str(clases_versiculos))
		#print("clases_descripcion: "+str(clases_descripcion))

		#if(len(clases_versiculos)>0):
		#	print("Se detectaron las clases CSS de los versiculos!!")
		#	print("Aplicando corrección de estilo...")
		#	style_p = 'p.'+', p.'.join(clases_versiculos)
		#	styletag = soup.new_tag('style')
		#	styletag["type"] = "text/css"
		#	styletag.string = f"<!-- {style_p} "+" { display: inline } -->"
		#	soup.head.append(styletag)
		
		#SE REEMPLAZA POR PLANTILLA
		#styletag = soup.new_tag('style')
		#styletag["type"] = "text/css"
		#print("\nAplicando corrección de estilo a los parrafos...")
		#styletag.string = "<!-- p { display: inline } .hidden {display: none} -->"
		#soup.head.append(styletag)

		#SE REEMPLAZA POR PLANTILLA
		#print("Eliminando imagenes de fondo...")
		#imagenes = soup.find_all('img')
		#for img in imagenes:
		#	img.extract()

		#SE REEMPLAZA POR PLANTILLA
		#print("Aplicando corrección de color de fondo...")
		#soup.body["bgcolor"] = "#fff"

		print("Limpiando estilo de versiculos\n")
		textos = soup.find_all('p')

		#bo_agregar_salto_linea = True

		###Verificar si el último elemento es un titulo (Tamaño 13 con etiquetas <b> alrededor)
		#Si es un titulo, hacer un pop y agregar a la cabecera

		for tag in textos:
			#tag.attrs
			#tag['id']
			#print(tag.string)
			#tag.string.replace_with("No longer bold")
			#print(tag.get('style'))
			if(tag.name == 'p'):
				tag['style'] = ''
			#https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
			#check if list1 contains any elements in list2
			bo_es_capitulo =  any(elem in tag["class"]  for elem in clases_capitulos)
			bo_es_cabecera =  any(elem in tag["class"]  for elem in clases_cabecera)
			bo_es_versiculo =  any(elem in tag["class"]  for elem in clases_versiculos)
			bo_es_descripcion =  any(elem in tag["class"]  for elem in clases_descripcion)
			if(bo_es_capitulo):
				tag['class'] = ['cap']
				#print("Capitulo detectado!")
				#print("Agregando salto de linea...\n")
				#br_tag = soup.new_tag("br")
				#br_tag2 = soup.new_tag("br")
				#tag.insert_after(br_tag)
				#tag.insert_after(br_tag2)
			elif(bo_es_cabecera):
				'''
					Si es primera cabecera, agregar estilo (o clase) para mostrar en esquina superior izquierda
					Si segunda primera cabecera, agregar estilo (o clase) para mostrar en esquina superior derecha
				'''
				print("Cabecera detectado!")
				print("ocultando linea...\n")
				#https://codereview.stackexchange.com/a/41426
				#tag['class'] = tag.get('class', []) + ['hidden']
				tag['class'] = ['cabecera', 'hidden']

				##print("Agregando salto de linea...\n")
				##br_tag = soup.new_tag("br")
				##br_tag2 = soup.new_tag("br")
				##tag.insert_after(br_tag)
				##tag.insert_after(br_tag2)
			elif(bo_es_versiculo):
				tag['class'] = ['ver']
				arr_next_element = tag.find_next_siblings('p')#tag.next_element.next_element
				next_element = arr_next_element[0] if (len(arr_next_element)>0) else None
				if(next_element):
					bo_next_element_es_descripcion =  any(elem in next_element["class"]  for elem in clases_descripcion)
					bo_next_element_es_capitulo =  any(elem in next_element["class"]  for elem in clases_capitulos)
					if(bo_next_element_es_descripcion):
						print("El siguiente elemento es una descripción!")
						print("Agregando salto de linea...\n")
						br_tag = soup.new_tag("br")
						br_tag2 = soup.new_tag("br")
						tag.insert_after(br_tag)
						tag.insert_after(br_tag2)
					elif(bo_next_element_es_capitulo):
						print("El siguiente elemento es un capitulo!")
						print("Agregando salto de linea...\n")
						br_tag = soup.new_tag("br")
						br_tag2 = soup.new_tag("br")
						tag.insert_after(br_tag)
						tag.insert_after(br_tag2)
			elif(bo_es_descripcion):
				tag['class'] = ['desc']
			'''if((not bo_es_versiculo) and bo_agregar_salto_linea):
				print("Añadiendo salto de linea...")
				# create a new tag
				br_tag = soup.new_tag("br")
				br_tag2 = soup.new_tag("br")
				#br_tag.append("some text here")
				# insert the new tag after the current tag
				tag.insert_after(br_tag)
				tag.insert_after(br_tag2)
				bo_agregar_salto_linea = False
			elif(bo_es_versiculo and (not bo_agregar_salto_linea)):
				bo_agregar_salto_linea = True
			#elif():
			'''


		#print(tag.prettify())
		print("\nHTML generado con exito!")
		#print(soup.prettify())
		#print("creando pdf...")
		#crearPdf(soup.pret1tify())
	else:
		print("PAGINA DE CONTENIDO GENERAL")
		print("corrigiendo ancho de archivo")
		soup.find_all("div")[0].attrs['style'] = "position:relative;width:874px;height:1240px;page-break-after: always;"
		print("Eliminando imagenes de fondo...")
		imagenes = soup.find_all('img')
		for img in imagenes:
			img.extract()
		print("Aplicando corrección de color de fondo...")
		soup.body["bgcolor"] = "#fff"
	#Tomar solo el div con clase page12-div y le quito el height
	crearTxt("test", soup.prettify())
	print("finalizado!")


if __name__ == "__main__":
	paginas_totales = 0
	nro_pagina = 1
	while(nro_pagina <= 979):
		processPages(nro_pagina)
		nro_pagina+=1
		paginas_totales+=1
		if(paginas_totales==40):
			print("creando pdf...")
			with open("test.html") as inf:
				html_doc = inf.read()
				crearPdf(html_doc)
			exit()

#https://kite.com/python/examples/1742/beautifulsoup-find-the-next-element-after-a-tag