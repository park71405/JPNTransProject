import os
import sys
import urllib.request
import json

client_id = "네이버 클라이언트 아이디"
client_secret = "네이버 클라이언트 비번"

encText = urllib.parse.quote("반갑습니다")
data = "source=ja&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))

    resultText = response_body.decode('utf-8')

    res = json.loads(resultText)
    jaText = res["message"]["result"]["translatedText"]

    f = open("c:/park2023/api/JPPapagoProject/resultText.txt", "a", encoding='UTF-8')

    f.write(jaText)
else:
    print("Error Code:" + rescode)