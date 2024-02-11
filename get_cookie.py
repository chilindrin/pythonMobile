import requests

getCookieUrl = 'https://www.mytischtennis.de/public/home?fromlogin=1&logout=true'
myCredentials = {'userNameB': 'algo',
    'userPassWordB': 'algo'}

cookiesResponse = requests.post(getCookieUrl, json=myCredentials)
responseHeaders = cookiesResponse.headers
mysetCookie = responseHeaders['set-cookie']
print(mysetCookie)