import os
import requests
import json
import wave
from gtts import gTTS
from IPython.display import Audio
from IPython.display import display

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
key = 'ca52f3c544c0fc39a1a1461ee66258d8'
headers = {
    "Content-Type": "application/xml",
    "Authorization": "KakaoAK " + key,
}

# 텍스트를 입력합니다.
text = "안녕하세요. 제 이름은 카카오 음성합성 API 입니다. 만나서 반가워요. ㅋㅋㅋ"

# 입력한 텍스트를 변환하여 api를 호출합니다.
data = f"<speak>{text}</speak>".encode('utf-8').decode('latin1')
res = requests.post(url, headers=headers, data=data)

# 호출하여 불러온 결과값을 저장합니다.
with open('hello_kakao.wav', 'wb') as f:
    f.write(res.content)

wn = Audio('prosody.wav', autoplay=True)
display(wn)
