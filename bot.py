import requests
import os
import random
import time
try:
    auth = os.environ.get("auth")
    super_properties = os.environ.get("super")
    cookies = {'__cfduid': 'd7620fa4faf230ef59c909ad4253cd29f1605346829', '_fbp': 'fb.1.1605365010427.787883345', '_ga': 'GA1.2.1155749774.1605365009', '_gid': 'GA1.2.2080419407.1607794052', 'locale': 'ru'}
except:
    pass



headers = {"authorization": auth,
           "x-super-properties": super_properties}


while True:
    zxc = {"content": "!work", "nonce": random.randint(1,1000000000), "tts": False}
    r = requests.post("https://discord.com/api/v8/channels/407574359209934848/messages", cookies=cookies, json=zxc, headers=headers)
    print(r.text)
    time.sleep(600)
