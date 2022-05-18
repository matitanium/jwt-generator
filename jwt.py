import hmac
import hashlib
import base64
import os
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
from platform import platform
#banner design
def baner():
    plat = platform()
    if "Windows" in plat:
        os.system("cls")
    else:
        os.system("clear")
    print(Fore.LIGHTRED_EX+ """
    coded by  : matin nouriyan
    ███╗   ███╗ █████╗ ████████╗██╗████████╗ █████╗ ███╗   ██╗██╗██╗   ██╗███╗   ███╗
    ████╗ ████║██╔══██╗╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║██║██║   ██║████╗ ████║
    ██╔████╔██║███████║   ██║   ██║   ██║   ███████║██╔██╗ ██║██║██║   ██║██╔████╔██║
    ██║╚██╔╝██║██╔══██║   ██║   ██║   ██║   ██╔══██║██║╚██╗██║██║██║   ██║██║╚██╔╝██║
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║   ██║   ██║  ██║██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝                                                              
                                                                                    """)


baner()

#Paste the file with the key 
path = input(Fore.GREEN+"Enter the public domain key path like => /home/matitanium/public.pem : ")
file=open(path)

key = file.read()

#Enter your header and payload here
header = input(Fore.WHITE+'Enter Your Header Like => {"alg":"HS256"} : ')
payload = input(Fore.RED+'Enter yourYour Payload Like => {"name":"admin"} : ')

#Creating encoded header
encodedHBytes = base64.urlsafe_b64encode(header.encode("utf-8"))
encodedHeader = str(encodedHBytes, "utf-8").rstrip("=")

#Creating encoded payload
encodedPBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodedPayload = str(encodedPBytes, "utf-8").rstrip("=")

#Concatenating header and payload
token = (encodedHeader + "." + encodedPayload)

#Creating signature
sig = base64.urlsafe_b64encode(hmac.new(bytes(key, "UTF-8"),token.encode('utf-8'),hashlib.sha256).digest()).decode('UTF-8').rstrip("=")
print("copy edited JWT token :) \n\n")
print(token + "." + sig)
