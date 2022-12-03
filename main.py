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
minimode = config["minimode"]
sleeptime = float(config["sleeptime"])
checknum = 0

while True:
    query = queryfile.readline()
    if not query:
        quit(print("end of file"))
    query = query.replace('\n', '')
    if debug == "true":
        print(query)
    if debug == "true":
        print(checkurl + query)
    page = Soup(ureq(checkurl + query).read(),
                "html.parser").get_text()
    if debug == "true":
        print(page)
    if "incapsula" in page:
        checknum = checknum + 1
        print(Fore.RED + "incapsula block, strike " + str(checknum))
        print(page)
        if checknum == 3:
            quit(print(Fore.RED + "three strikes, quitting. (try refreshing your ip)"))
    else:
        checknum = 0
        if '"available' in page:
            if minimode == "false":
                print(Fore.GREEN + query + " is available")
            else:
                print(query)
        else:
            if minimode == "false":
                print(Fore.RED + query + " is not available")
    time.sleep(sleeptime)
