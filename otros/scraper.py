#https://lingwars.github.io/blog/scrape-xpath.html
#https://www.bibleserver.com/text/BTX/Génesis1
#scraper_btx_test.mhtml
#
# pip install pdfkit
# sudo apt-get install wkhtmltopdf
'''
div: chapter
Titulos: h3.caption
Versiculos:
<div id="b41ref1001001" class="v1001001 verse">
	<span class="verseNumber">
		<a id="b41ref1001001_vno" href="javascript:void('Verse details');" no="1,1">1</a>&nbsp;
	</span>
	En un principio creó ’Elohim los cielos y la tierra.
</div>


Probaremos algunas cadenas XPath típicas para ver qué nos devuelven:

//a/@href: devuelve el atributo href de los nodos cuya etiqueta sea a y que se encuentren en cualquier punto del árbol jerárquico (//).
//title/text(): devuelve el texto (el contenido que hay entre las etiquetas) de los nodos cuya etiqueta sea title y que se encuentren en cualquier punto del árbol.
//div[@id='content']//p/text(): devuelve el texto de todos los nodos tipo p que estén por debajo del nodo div cuyo atributo id es content, en cualquier lugar en que se encuentre este nodo.
//div[@id='content']//p//text(): prácticamente igual que la anterior, pero con una sutil diferencia. Esta cadena XPath devuelve el texto de todos los nodos hijo de todos los nodos tipo p (también el texto del propio nodo p).
'''

import requests
import sys

def download(url):
    """Returns the HTML source code from the given URL
        :param url: URL to get the source from.
    """
    r = requests.get(url)
    if r.status_code != 200:
        sys.stderr.write("! Error {} retrieving url {}".format(r.status_code, url))
        return None

    return r.text


if __name__ == '__main__':
    sys.stdout.write("=============================\n")
    sys.stdout.write("== Lingwars - Scrape XPath ==\n")
    sys.stdout.write("=============================\n")

    url = "http://localhost/scraper_btx_test.mhtml"
    #url = "https://www.bibleserver.com/text/BTX/Génesis1"

    page = download(url)
    if page:
        sys.stdout.write("\n\n1) Download text from {}\n".format(url))
        sys.stdout.write(page.text[:200])

        # Parse the text to XML structures
        sys.stdout.write("\n\n2) Let's try some XPath expresions:")
        tree = html.fromstring(page.content)

        # Execute xpath over retrieved html content
        xpath_string = '//a/@href'
        results = tree.xpath(xpath_string)
        sys.stdout.write('\n\t'.join(results))

    else:
        sys.stdout.write("Nothing was retrieved.")