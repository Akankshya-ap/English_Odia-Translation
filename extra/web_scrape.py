import requests

url = "http://www.odialanguage.com/dictionary/?search_string=alike&mode=match_word&submit=Search"
page = requests.get(url)
page.status_code #If response starts with 2--, then page access successful

from bs4 import BeautifulSoup                               #If you inspect the webpage, then you will understand
soup = BeautifulSoup(page.content, "html.parser")           #all the variables declared here and eng-odia words
#print soup.prettify()                                      #extracted
html = list(soup.children)[2]
#print html
body = list(html.children)[3]
form = list(body.children)[3]
div = list(form.children)[1]
table = list(div.children)[5]
tbody = list(table.children)[1]
#print list(tbody.children)[0] == u'\n'
words =  [e for e in list(tbody.children) if e != u'\n']
words = words[1 : ]
#words

for word in words:
    lines = list(word.children)
    #print lines
    eng_line = lines[1]
    level = lines[3]
    level = list(level.children)[0][1 : ]
    odia_line = lines[4]
    #print eng_line, odia_line
    eng_line = list((list(eng_line.children)[0]).children)[0]
    eng_line = eng_line.lower()
    odia_line = str(odia_line)
    odia_line = odia_line.replace('<td>', '')                #formatting odia_line
    odia_line = odia_line.replace('</td>', '')
    odia_line = odia_line.replace('<br/>', '\n')
    odia_line = odia_line[: odia_line.find('\"')]
    odia_line = odia_line.replace("\xc2\xa0", "_")           #english word: one or more existing odia words 
    odia_line = odia_line.replace(" ", "_")                  #translated seperated by space: level of english word
    odia_line = odia_line.replace("\n", " ")
    odia_line = odia_line.replace("\r", "")
    print eng_line, odia_line                                #We will store in a format of
    #print level                                             #alike: ଏକ_ସମାନ: Adv
    #print odia_word

