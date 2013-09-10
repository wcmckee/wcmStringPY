'''
Created on 6/12/2012
 
@author: Will
'''
import pylast
import pprint
 
API_KEY = '917060f2353e4ad89224f2295e146ddf'
API_SECRET = '9407d29e78647abbc1bc440d94aa1f70'
passwordz = input('Password: ')
username = "galf666"
password_hash = pylast.md5(passwordz)
 
network = pylast.LastFMNetwork(API_KEY, api_secret =
API_SECRET, username=username, password_hash=password_hash)
 
arti = input("Enter the artist name: ")
 
artist = network.get_artist(arti)
 
cart = artist.get_bio_content()
pprint.pprint(cart)
test = artist.get_similar(20)
pprint.pprint(test)
 
 
doc = open('hellothere', 'w')
doc.write('---~~~--- ')
doc.write(arti)
doc.write('---~~~--- ')
doc.write('\n')
doc.write(cart)
doc.write('\n')
doc.write(arti)
doc.write('---~~~--- ')
doc.write('\n')
doc.close
