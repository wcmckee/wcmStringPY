import requests
import string
import json
from pprint import pprint

def rectxt():
    files = open('doc', 'w')
    r2 = requests.get('http://api.trademe.co.nz/v1/Search/General.json?category=202&sort_order=BidsMost')
 
    j2 = json.loads(r2.text)
    
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
         
         pprint(ContentTitle)
         pprint(ContentPath)
         pprint(ContentRegion)
         pprint(ContentBuyNow)
 
        
rectxt()
