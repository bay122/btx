# modules for 
import PyPDF2
# pdf file object
# you can find find the pdf file with complete code in below
pdfFileObj = open('biblia-textual_unlocked.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
#print(pdfReader.numPages)
# a page object
pageObj = pdfReader.getPage(10)
# extracting text from page.
# this will print the text you can also save that into String
text = pageObj.extractText().replace('\n', ' ')
text = text.replace('   ', ' ')
print(text)

'''
for i in xrange(read_pdf.getNumPages()):
    page = read_pdf.getPage(i)
    print 'Page No - ' + str(1+read_pdf.getPageNumber(page))
    page_content = page.extractText()
    print page_conten
'''

# closing the pdf file object 
pdfFileObj.close() 

#https://towardsdatascience.com/python-for-pdf-ef0fac2808b0
#https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
#
#pdf2txt.py biblia-textual_unlocked.pdf
#pdf2txt.py -o prueba.txt -p 10 biblia-textual_unlocked.pdf

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