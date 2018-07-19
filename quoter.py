import re
import sys
try:
    f = open('z/Users/estherkremer/Desktop/harrypotter.txt', 'r')
    text = f.read()
    f.close()
    #print(text[:1000])
    harry_quotes = re.findall('".*".*Harry.*', text)
    #
    for quote in harry_quotes:
        print(quote)
    #
    ron_quotes = re.findall('".*".*Ron.*', text)
    #
    for quote in ron_quotes:
        print(quote)
    #
    Hermione_quotes = re.findall('".*".*Hermione.*', text)
    #
    for quote in Hermione_quotes:
        print(quote)
except:
        print('error!')
        print(sys.exc_info()[0])

