import requests
import os
import random
import time
try:
    auth = os.environ.get("auth")
    super_properties = os.environ.get("super")
    cookies = os.environ.get("cookies")
except:
    pass



headers = {"authorization": auth,
           "x-super-properties": super_properties}


while True:
    zxc = {"content": "!work", "nonce": random.randint(1,1000000000), "tts": False}
    r = requests.post("https://discord.com/api/v8/channels/407574359209934848/messages", cookies=cookies, json=zxc, headers=headers)
    print(r.text)
    time.sleep(600)
