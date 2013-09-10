import requests
import string
import json
import random
from pprint import pprint
from clint.textui import puts, colored

def rectxt():
    numb = random.randint(1,10)
    numb = str(numb)
    #categ  = input('Which number: ')
    r2 = requests.get('http://api.trademe.co.nz/v1/Search/General.json?category=' + numb + '&sort_order=BidsMost')
    artCtrl = requests.get('http://artcontrol.me/?wpapi=get_posts&dev=0')
    r3 = requests.get('http://api.trademe.co.nz/v1/Listings/Latest.json')
    j2 = json.loads(r2.text)
    artCtrl = json.loads(artCtrl)
    j3 = json.loads(r3.text)
    #pprint(j2)  #here's the final respone, printed out nice an readable format
    #ed2 = str(j2)
    x = j2[u'List']
    postCtrl = artCtrl[u'posts']
    #pprint(x)
    for blogInfo in postCtrl:
         ContentName = blogInfo['name']
         ContentName = str(ContentName)
         

         contentDate = info['date', 'name', 'excerpt']
         contentDate = str(contentDate)
         pprint(contentDate)
        
         
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
         ContentImage = info[u'PictureHref']
         ContentImage = str(ContentImage)
         #pprint(ContentTitle)
         #puts(colored.red(ContentTitle))
         #pprint(ContentPath)
         #puts(colored.white(ContentPath))
         #pprint(ContentRegion)
         #puts(colored.green(ContentRegion))
         #pprint(ContentBuyNow)
         files = open('doc', 'w')
         title = open('title', 'w')
         #imagePic = open('imagePic', 'w')
         #imagePic.write(ContentImage)
         #imagePic.close()
         title.write(ContentTitle)
         title.close()
         files.write('<p>')
         files.write(ContentTitle)
         files.write('</p><p>')
         files.write('Buy now: ') 
         files.write(ContentBuyNow)
         files.write('</p>')
         files.write('Area: ')
         files.write(ContentRegion)
         files.write(', ')
         files.write(ContentSuburb)
         files.write('</h2>')
         files.write('<img class=\"aligncenter\" alt=\"\" src =\"')
         files.write(ContentImage)
         files.write('\" width=\"60\" height=\"30\" />')
         files.close()
rectxt()
