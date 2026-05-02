import requests
import os
import platform
import colorama
from colorama import Fore, Back, Style

# --- Setup and Imports ---
print("[*] Checking Required Packages: - \n")
print("[*] Checking Requirements Module")

if platform.system().startswith("Linux"):
    packages = ["requests", "pyfiglet", "termcolor", "pystyle", "colorama", "pyuseragents"]
    for pkg in packages:
        try:
            __import__(pkg)
        except ImportError:
            os.system(f"python3 -m pip install {pkg} -q -q -q")

elif platform.system().startswith("Windows"):
    packages = ["requests", "termcolor", "pystyle", "colorama", "pyuseragents"]
    for pkg in packages:
        try:
            __import__(pkg)
        except ImportError:
            os.system(f"python -m pip install {pkg} -q -q -q")

from pystyle import Center, Colorate, Colors
import pyuseragents

colorama.deinit()
banner = Center.XCenter("""
   ___   _ ____ _____ ____       _____ _ _   _ ____  _____ ______
  / / | | / ___|___ /|  _ \     |  ___/ | \ | |  _ \| ____|  _ \ \`
 | || | | \___ \ |_ \| |_) |____| |_  | |  \| | | | |  _| | |_) | |
< < | |_| |___) |__) |  _ <_____|  _| | | |\  | |_| | |___|  _ < > >
 | | \___/|____/____/|_| \_\    |_|   |_|_| \_|____/|_____|_| \_\ |
  \_\                                                          /_/          
                            \n\n
""")

user_agent = pyuseragents.random()
blu = "\033[96m"
red = "\033[91m"
grn = "\033[32m"
ylw = "\033[93m"

# --- OSINT Functions ---

def facebook(target):
    url = f"https://www.facebook.com/{target}"
    res = requests.get(url, headers={"user-agent": user_agent})
    if "The link you followed may be broken" in res.text or res.status_code == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Facebook Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Facebook Found: {url}")

def tiktok(target):
    url = f"https://www.tiktok.com/@{target}"
    res = requests.get(url, headers={"user-agent": user_agent})
    inp = res.status_code
    if inp == 404 or "/404" in res.url:
        print(f" {ylw}[ {red}✖{ylw} ] {red}TikTok Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Tiktok Found: {res.url}")

def youtube(target):
    url = f"https://www.youtube.com/@{target}"
    res = requests.get(url, headers={"user-agent": user_agent})
    if "Not Found" in res.text or res.status_code == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}YouTube Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}YouTube Found: {url}")

def scratch(target):
    url = f"https://scratch.mit.edu/users/{target}"
    res = requests.get(url)
    if "Not Found" in res.text or res.status_code == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Scratch Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Scratch Found: {url}")

def blogspot(target):
    url = f"https://{target}.blogspot.com"
    res = requests.get(url)
    if res.status_code == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Blogspot Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Blogspot Found: {url}")

def twitter(target):
    payload = {"input": target}
    header = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
              "user-agent": user_agent,
              "x-requested-with": "XMLHttpRequest"}
    res = requests.post(f"https://tweeterid.com/ajax.php", data=payload, headers=header)
    if "error" in res.text:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Twitter Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Twitter Found: {target}")

def reddit(target):
    url = f"https://en.reddit.com/user/{target}"
    header = {"user-agent": user_agent}
    res = requests.get(f"{url}/about.json", headers=header)
    if res.status_code == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Reddit Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Reddit Found: {url}")

def github(target):
    url = f"https://www.github.com/{target}"
    res = requests.get(url)
    if res.status_code == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Github Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Github Found: {url}")

def pintrest(target):
    url = f"https://www.pinterest.com/{target}"
    res = requests.get(url, headers={"user-agent": user_agent})
    if res.status_code == 404 or "/404" in res.url or "/login" in res.url:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Pinterest Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Pinterest Found: {url}")

def med(target):
    url = f"https://medium.com/@{target}"
    res = requests.get(url, headers={"user-agent": user_agent})
    if res.status_code == 404 or "/404" in res.url:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Medium Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Medium Found: {url}")

def daily(target):
    url = f"https://www.dailymotion.com/{target}"
    res = requests.get(url, headers={"user-agent": user_agent})
    if res.status_code == 404 or "/404" in res.url or "not-found" in res.url:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Daily Motion Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Daily Motion Found: {url}")

def paste(target):
    url = f"https://pastebin.com/u/{target}"
    res = requests.get(url, headers={"user-agent": user_agent})
    if res.status_code == 404 or "/404" in res.url:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Pastebin Not Found")
    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Pastebin Found: {url}")

# ... (Include other simple 404 checks for bit, vimeo, about, cash, keybase, etc.) ...

def catc():
    try:
        print("\033c")
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
        target = input(Fore.GREEN+'[*] Enter Username:- ')
        
        # Calling all functions
        tiktok(target)
        facebook(target)
        youtube(target)
        github(target)
        med(target)
        daily(target)
        pintrest(target)
        reddit(target)
        paste(target)
        # (Call the rest of your functions here)

        input("\nPress Enter to exit...")
    except KeyboardInterrupt:
        print(f"\n{red}Exit requested.")

if __name__ == "__main__":
    catc()
