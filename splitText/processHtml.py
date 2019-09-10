from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
file_content = open('', 'r').read()
parser.feed(file_content)


import bs4

# load the file
with open("pages/pagina_13.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt)

# create new link
new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
# insert it into the document
soup.head.append(new_link)

# save the file again
with open("pages/pagina_13.html", "w") as outf:
    outf.write(str(soup))