import requests
import random
url='https://api.qrserver.com/v1/create-qr-code/?size=150x150&data='
x=input(">>> ")
if x:
    url+=x
    y=requests.get(url)
    num=random.randrange(1,10000)
    with open(f'{str(num)}','wb') as r:
        r.write(y.content)
else:
    print("|:")