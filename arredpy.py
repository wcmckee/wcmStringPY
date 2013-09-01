import requests
import string
import json
from pprint import pprint

def rectxt():
    files = open('doc', 'w')
    r2 = requests.get('http://www.reddit.com/r/redditgetsdrawn.json')
 
    j2 = json.loads(r2.text)
    
    #pprint(j2)  #here's the final respone, printed out nice an readable format
    #ed2 = str(j2)
    x = j2[u'data'][u'children']
    #pprint(x)
    for info in x:
         ContentText = info[u'data'][u'selftext']      
         ContentText = str(ContentText)
         
         ContentAuthor = info[u'data'][u'title']
         ContentAuthor = str(ContentAuthor)
         
         ContentScore = info[u'data'][u'score']
         ContentScore = str(ContentScore)
         
         ContentUrl = info[u'data'][u'url']
         
         pprint(ContentText)
         pprint(ContentAuthor)
         pprint(ContentScore)
         pprint(ContentUrl)
 
        
rectxt()
