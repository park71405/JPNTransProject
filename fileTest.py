import os
import sys
import urllib.request
import json

client_id = "네이버 클라이언트 아이디"
client_secret = "네이버 클라이언트 비번"

client_id2 = "네이버 클라이언트 아이디"
client_secret2 = "네이버 클라이언트 비번"

#파일 열기
f = open('c:/park2023/api/JPPapagoProject/3화.txt', 'r', encoding='UTF-8')
f2 = open('c:/park2023/api/JPPapagoProject/resultText.txt', 'a', encoding='UTF-8')

#readlines() 함수 : 모두 읽기 list 반환
str = f.readlines()

for s in str:
    if s == "\n":
        f2.write(s)
    else:
        encQuery = urllib.parse.quote(s)
        data = "query=" + encQuery
        url = "https://openapi.naver.com/v1/papago/detectLangs"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        
        if(rescode==200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            res = json.loads(result)
            
            if(res['langCode'] == "ja"): #일본어 이면 번역 시작
                encText = urllib.parse.quote(s)
                data = "source=ja&target=ko&text=" + encText
                url = "https://openapi.naver.com/v1/papago/n2mt"
                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id",client_id2)
                request.add_header("X-Naver-Client-Secret",client_secret2)
                response = urllib.request.urlopen(request, data=data.encode("utf-8"))
                rescode = response.getcode()
                
                if(rescode==200):
                    response_body = response.read()
                    resultText = response_body.decode('utf-8')
                    res2 = json.loads(resultText)

                    ja_text = res2["message"]["result"]["translatedText"]
                    f2.write(ja_text)
                else:
                    print("Error code: " + rescode)

            else: #일본어가 아니면
                f2.write(s)
        else:
            print("Error Code:" + rescode)

f.close()
f2.close()