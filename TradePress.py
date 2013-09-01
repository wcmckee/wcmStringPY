from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import pprint

PriceInfo = open('doc', 'r')
for Result in PriceInfo:
        pprint.pprint(Result)

wp = Client('http://wcmckee.com/xmlrpc.php', 'wcmckee', 'blahblah123')
Posts = wp.call(GetPosts())
for data in Posts:
      pprint.pprint(data)

#post = WordPressPost()
#post.title = 
