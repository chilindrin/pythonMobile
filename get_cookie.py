import requests

url = 'https://www.mytischtennis.de/public/home?fromlogin=1&logout=true'
myobj = {'userNameB': 'myusername',
    'userPassWordB': '***'}

x = requests.post(url, json=myobj)
andres = x.headers
mysetCookie = andres['set-cookie']
print(mysetCookie)