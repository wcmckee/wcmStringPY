import requests


def carGet():
    x = requests.get('http://api.trademe.co.nz/v1/Categories/UsedCars.json')
    print(x)
    for data in x:
        #return data
        print(data)
    deta = str(data)
    x = deta['Cars'] 
    print(x)
        
carGet()