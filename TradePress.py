from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import pprint
wp = Client('http://wcmckee.com/xmlrpc.php', 'trademe', 'qwerty123')

PriceInfo = open('doc', 'r')
TitleInfo = open('title', 'r')
RedditInfo = open('redditdrawn', 'r')
LordeInfo = open('LastData')

for Result in PriceInfo:
     pprint.pprint(Result)

for Titles in TitleInfo:
     pprint.pprint(Titles)
     
for Reddit in RedditInfo:
    pprint.pprint(Reddit)

#for data in Posts:
 #    pprint.pprint(data)

for Lorde in LordeInfo:
    pprint.pprint(Lorde)     
     
Posts = wp.call(GetPosts())
post = WordPressPost()
post.title = (Lorde)
post.content = (Reddit)
post.terms_names = {
     'post_tag': ['trademe', 'dataprocess', 'python', 
                  'reddit', 'lastfm']}
{'category': ['trademe']}
post.post_status = 'publish'
wp.call(NewPost(post)) 
