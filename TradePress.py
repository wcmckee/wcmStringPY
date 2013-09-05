from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import pprint

PriceInfo = open('doc', 'r')
TitleInfo = open('title', 'r')
for Result in PriceInfo:
     pprint.pprint(Result)

for Titles in TitleInfo:
     pprint.pprint(Titles)
wp = Client('http://wcmckee.com/xmlrpc.php', 'trademe', 'qwerty123')
Posts = wp.call(GetPosts())
for data in Posts:
     pprint.pprint(data)

post = WordPressPost()
post.title = (Titles)
post.content = (Result)
post.terms_names = {
     'post_tag': ['trademe', 'dataprocess', 'python'],
     'category': ['trademe']
}

wp.call(NewPost(post)) 
