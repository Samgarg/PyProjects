__author__ = 'Davidws'

from bs4 import BeautifulSoup
import requests as req
import lxml

url = 'http://jindal.utdallas.edu/the-utd-top-100-business-school-research-rankings/'
realurl = 'http://jindal.utdallas.edu/the-utd-top-100-business-school-research-rankings/application/functions.php'
opts = {'option': 'loadSearchResults', 'id': '2', 'frmDate': '2012', 'toDate': '2015', 'journal_ids': '28,27,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,8,7,5,4,3,2,1,',
'universities': '1663,', 'applyAnd': '0'}
html = req.post(realurl, opts)
doc = BeautifulSoup(html)
print(doc.prettify())