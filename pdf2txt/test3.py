file=open('biblia-textual-at.pdf','r')
#infile=file.readlines()
infile=file.readline()
print(infile.decode('latin-1').encode("utf-8"))