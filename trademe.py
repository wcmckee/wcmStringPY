import requests
import string
import json
import random
from pprint import pprint
from clint.textui import puts, colored

def rectxt():
    numb = random.randint(0,30)
    numb = str(numb)
    #categ  = input('Which number: ')
    r2 = requests.get('http://api.trademe.co.nz/v1/Search/General.json?category=' + numb + '&sort_order=BidsMost')
    r3 = requests.get('http://api.trademe.co.nz/v1/Listings/Latest.json')
    j2 = json.loads(r2.text)
    j3 = json.loads(r3.text)
    #pprint(j2)  #here's the final respone, printed out nice an readable format
    #ed2 = str(j2)
    x = j2[u'List']
    #pprint(x)
    for info in x:
         ContentPath = info[u'CategoryPath']      
         ContentPath = str(ContentPath)
        
         ContentRegion = info[u'Region']
         ContentRegion = str(ContentRegion)
         
         ContentTitle = info[u'Title']
         ContentTitle = str(ContentTitle)
         
         ContentBuyNow = info[u'PriceDisplay']
         ContentBuyNow = str(ContentBuyNow)
         
         ContentSuburb = info[u'Suburb']
         ContentSuburb = str(ContentSuburb)
         
         #pprint(ContentTitle)
         puts(colored.red(ContentTitle))
         #pprint(ContentPath)
         puts(colored.white(ContentPath))
         #pprint(ContentRegion)
         puts(colored.green(ContentRegion))
         pprint(ContentBuyNow)
         files = open('doc', 'w')
         files.write('[')
         files.write(ContentTitle)
         files.write(', ') 
         files.write(ContentBuyNow)
         files.write(', ')
         files.write(ContentRegion)
         files.write(', ')
         files.write(ContentSuburb)
         files.write(']')
         files.close()
rectxt()
