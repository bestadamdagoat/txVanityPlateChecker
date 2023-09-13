from urllib.request import urlopen as ureq
from colorama import Fore, init
import time
from configparser import ConfigParser
import logging
import os.path


def writeconfig(variable, setting):
    config_object.set("CONFIG", variable, setting)
    with open('config.ini', 'w') as configfile:
        config_object.write(configfile)


def errorprocess(errormsg):
    print(Fore.RED + errormsg)
    time.sleep(2)
    print(f"{Fore.RED}Quitting, restart the script.")
    quit(time.sleep(2))


def debugprint(printmsg):
    if debug == "true":
        print(printmsg)


if os.path.isfile("available-plates.txt"):
    print("You have an available-plates log already in this directory. Continuing will erase that file.")
    print("Are you sure you want to continue? (Y/N)")
    while True:
        continuewithprogram = input()
        if continuewithprogram.lower() not in ('y', 'n'):
            continue
        if continuewithprogram.lower() == "y":
            break
        else:
            quit()

logging.basicConfig(filename="available-plates.txt", format='%(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

init(autoreset=True)

config_object = ConfigParser()
config_object.read("config.ini")
try:
    config = config_object["CONFIG"]
except KeyError:
    writeconfig = open("config.ini", "w")
    writeconfig.write("[CONFIG]\ndebug = false\nsleeptime = 3\nminimode = false")
    errorprocess("Config file missing. Don't worry though, I made one for you with the default options.")

debug = config["debug"]
minimode = config["minimode"]
try:
    sleeptime = float(config["sleeptime"])
except ValueError:
    print(
        f"{Fore.RED}Please specify sleeptime in seconds (ex. 3) next time. Defaulting to 3."
    )
    writeconfig("sleeptime", "3")
    sleeptime = float(config["sleeptime"])
    time.sleep(3)
if debug.lower() not in ("false", "true"):
    print(
        f"{Fore.RED}Please specify if debug is true or false next time. Defaulting to false."
    )
    writeconfig("debug", "false")
    debug = config["debug"]
    time.sleep(3)
if minimode.lower() not in ("false", "true"):
    print(
        f"{Fore.RED}Please specify if minimode is true or false next time. Defaulting to false."
    )
    writeconfig("minimode", "false")
    minimode = config["minimode"]
    time.sleep(3)

try:
    queryfile = open('query.txt')
except FileNotFoundError:
    errorprocess("No query specified. Make sure you created a query.txt file.")

checkurl = 'https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/'
checknum = 0

if minimode == "true":
    print("Started")
while True:
    query = queryfile.readline()
    if not query:
        quit(print("End of query"))
    query = query.replace('\n', '')
    debugprint(query)
    debugprint(checkurl + query)
    page = ureq(checkurl + query).read()
    debugprint(page)
    if b"incapsula" in page:
        checknum = checknum + 1
        print(f"{Fore.RED}Incapsula block, strike {str(checknum)}")
        print(page)
        if checknum == 3:
            quit(print(f"{Fore.RED}Three strikes, quitting. (try refreshing your ip)"))
    else:
        checknum = 0
        if b'"available' in page:
            if minimode == "false":
                print(Fore.GREEN + query + " is available")
            else:
                print(query)
            logger.info(query)
        elif minimode == "false":
            print(Fore.RED + query + " is not available")
    time.sleep(sleeptime)