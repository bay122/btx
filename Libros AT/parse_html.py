#https://pypi.org/project/pdfkit/
#http://www.pythondiario.com/2018/01/web-scraping-extrayendo-informacion-de.html
#http://lopezpino.com/2017/05/27/python-pdfkit-wkhtmltopdf-and-non-ascii-characters/
#https://www.geeksforgeeks.org/python-format-function/
#https://stackoverflow.com/questions/4581620/get-parts-of-html-code-as-a-new-string-in-python
#https://es.switch-case.com/30601322
#https://stackoverflow.com/questions/49836676/error-after-upgrading-pip-cannot-import-name-main
#https://duguls.wordpress.com/2012/01/01/gtk-warning-imposible-encontrar-el-motor-de-temas-en-la-ruta-al-_modulo-pixmap/
#https://www.bibleserver.com/text/BTX/Génesis2
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
##https://medium.com/@speedforcerun/python-crawler-http-error-403-forbidden-1623ae9ba0f
#python3 -m pip install pdfkit
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pdfkit



def getChapter(chapter):
	title = 'Génesis'
	"""Returns the HTML source code from the given URL
    	:param url: URL to get the source from.
	"""
	
	#url = "http://localhost/btx_{}.html".format(chapter)
	url = "https://www.bibleserver.com/text/BTX/Genesis{}".format(chapter)

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	req = Request(url=url, headers=headers) 

	html = urlopen(req).read().decode('utf-8')
	#print(html)
	soup = BeautifulSoup(html, "lxml")
	t = soup.find('div', attrs={"class":"chapter"})

	'''if(chapter == 1):
		new_tag = soup.new_tag("h1")
		new_tag.string = title
		t.insert(0,new_tag)
		new_tag = soup.new_tag("h2")
		new_tag.string = str(chapter)+"."
		t.insert(1,new_tag)
	else:
		new_tag = soup.new_tag("h2")
		new_tag.string = str(chapter)+"."
		t.insert(0,new_tag)
	'''
	
	chapter_tag = soup.new_tag("h2", style="display: inline;")
	chapter_tag.string = str(chapter)+"."
	t.find().insert(0,chapter_tag)
	
	if(chapter == 1):
		title_tag = soup.new_tag("h1")
		title_tag.string = title
		t.insert(0,title_tag)

	new_tag = soup.new_tag("br")
	t.append(new_tag)
	#print(t.prettify())
	return t.prettify()


def setPage(content):
	page = '<div class="page">\n{}</div>\n\n'.format(content)
	return page


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


def crearTxt(nombre, content):
	file=open(nombre+".txt", "a+") 
	file.write(content)


pages = ''

crear_pdf = True
if(crear_pdf):
	pages = open('1-genesis.txt', 'r').read()
	crearPdf(pages, 'btx')
else:
	for i in range(50):#2
		chapter = getChapter(i+1)
		pages += setPage(chapter)
		crearTxt("1-Gen_"+str(i+1), pages)

	crearTxt("1-genesis", pages)