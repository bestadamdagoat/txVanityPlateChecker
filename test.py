from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from colorama import Fore, init
import time
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
config = config_object["CONFIG"]

init(autoreset=True)
checkurl = 'https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/'
queryfile = open('query.txt')
# debug mode, set it to either true or false
debug = config["debug"]
sleeptime = float(config["sleeptime"])

while True:
    query = queryfile.readline()
    if not query:
        quit(print("end of file"))
    if debug == "true":
        print(query)
    uClient = uReq(checkurl + query)
    if debug == "true":
        print(checkurl + query)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    page = page_soup.get_text()
    if debug == "true":
        print(page_soup)
    if "incapsula" in page:
        print(Fore.RED, "incapsula block :(")
        print(page_soup)
        quit(print("quitting"))
    else:
        if "not-available" in page:
            print(Fore.RED + query + "is not available")
        else:
            print(Fore.GREEN + query + "is available")
    # wait time to check if a plate is available, set it to whatever you want (in seconds)
    time.sleep(sleeptime)
# explain why using BS in the readme
# change test.py to main.py
