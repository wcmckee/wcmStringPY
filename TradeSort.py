import pprint

data = open('doc', 'r')
result = open('result', 'w')

for info in data:
       pprint.pprint(info)
       result.seek(0, 2)
       result.write(info)
       result.close()
