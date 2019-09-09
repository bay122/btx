
#https://www.geeksforgeeks.org/python-convert-html-pdf/
#(i) Already Saved HTML page
import pdfkit 
pdfkit.from_file('scraper_btx_test.mhtml', 'out.pdf') 

#(ii) Convert by website URL
import pdfkit 
pdfkit.from_url('https://www.google.co.in/','shaurya.pdf')

#(iii) Store text in PDF
import pdfkit 
pdfkit.from_string('Shaurya GFG','GfG.pdf') 