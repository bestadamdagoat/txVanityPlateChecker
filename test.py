from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from colorama import Fore, init
import time

init(autoreset=True)
checkurl = 'https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/'
queryfile = open('query.txt')
debug = True

while True:
    query = queryfile.readline()
    if not query:
        quit(print("end of file"))
    if debug is True:
        print(query)
    uClient = uReq(checkurl + query)
    if debug is True:
        print(checkurl + query)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    page_soup.h1
    page = page_soup.get_text()
    if debug is True:
        print(page_soup)
        print(page_soup.get_text())
    if "incapsula" in page:
        print(Fore.RED, "incapsula block :(")
        print(page_soup)
        quit(print("quitting"))
    else:
        if "not-available" in page:
            print(Fore.RED + query + "is not available")
        else:
            print(Fore.GREEN + query + "is available")
    time.sleep(3)

# TO DO
# fix formatting of the available/not available text
# clean code
# some other things i probably forgot