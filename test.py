from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as ureq
from colorama import Fore, init
import time
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
config = config_object["CONFIG"]

init(autoreset=True)
checkurl = 'https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/'
queryfile = open('query.txt')
debug = config["debug"]
sleeptime = float(config["sleeptime"])
checknum = 0

while True:
    query = queryfile.readline()
    if not query:
        quit(print("end of file"))
    if debug == "true":
        print(query)
    uClient = ureq(checkurl + query)
    if debug == "true":
        print(checkurl + query)
    page_html = uClient.read()
    uClient.close()
    page_soup = Soup(page_html, "html.parser")
    page = page_soup.get_text()
    query = query.replace('\n', '')
    if debug == "true":
        print(page_soup)
    if "incapsula" in page:
        checknum = checknum + 1
        print(Fore.RED + "incapsula block, strike " + str(checknum))
        print(page_soup)
        if checknum == 3:
            quit(print(Fore.RED + "three strikes, quitting. (try refreshing your ip)"))
    else:
        checknum = 0
        if "not-available" in page:
            print(Fore.RED + query + " is not available")
        else:
            print(Fore.GREEN + query + " is available")
    time.sleep(sleeptime)
