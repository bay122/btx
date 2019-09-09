import os

input="biblia-textual-at.pdf"
output="out.txt"
os.system(("ps2ascii %s %s") %( input , output))