import sys
import mechanize
from BeautifulSoup import BeautifulSoup
from pprint import pprint

br = mechanize.Browser()
resp = br.open("https://egov.uscis.gov/cris/processTimesDisplayInit.do")
br.select_form("processTimesForm")
control = br.form.find_control("officeId")
br[control.name] = ['338']
resp = br.submit()
#fd = open("temp.html", 'w')
#fd.write(response.read())
#fd.close()

#fd = open("temp.html", 'r')
#lines = fd.readlines()
#text = "\n".join(lines)
text = resp.read()

if not text:
    print "fetch fail"
    sys.exit(0)
soup = BeautifulSoup(text)
post = soup.find(id="posted")
print post.text
fields = soup.findAll('td')
texts = []
for field in fields:
    text = field.text
    text.replace('<td>', '')
    text.replace('</td>', '')
    text.replace('', '')
    if text == "&nbsp;":
        continue
    texts.append(text)

results = texts[-6:]
ret = {}
ret[results[0]] = results[1]
ret[results[2]] = results[3]
ret[results[4]] = results[5]

pprint(ret)
