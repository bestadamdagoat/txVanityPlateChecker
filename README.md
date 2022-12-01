<div align="center">

# ![Plate Checker Logo](insert link here)

## A bot that will check if vanity plates are available or taken, poorly coded in Python using BeautifulSoup. (MOVE THIS LINE LOWER) If this bot surprisingly worked for you, it would be cool if you donated to me. It would convince me to code better and actually be more commited to these projects. Check the sidebar for ways to donate to me.
<img alt="GitHub" src="https://img.shields.io/github/license/bestadamdagoat/txVanityPlateChecker"> ![Website](https://img.shields.io/website?label=myplates%20api&url=https%3A%2F%2Fwww.myplates.com/api/licenseplates/passenger/classic-black-silver/TEST) ![Liberapay receiving](https://img.shields.io/liberapay/receives/bestadam?label=receiving%20on%20liberapay) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beautifulsoup4) ![GitHub issues](https://img.shields.io/github/issues/bestadamdagoat/txVanityPlateChecker) ![GitHub repo size](https://img.shields.io/github/repo-size/bestadamdagoat/txVanityPlateChecker) ![GitHub repo file count](https://img.shields.io/github/directory-file-count/bestadamdagoat/txVanityPlateChecker) ![Lines of code](https://img.shields.io/tokei/lines/github/bestadamdagoat/txVanityPlateChecker)
</div>

Basically what this bot does is:
- Reads your query.txt file.
- Appends the next line to the [MyPlates API link](https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/).
- Opens the API link with urllib and reads the page using BeautifulSoup (explained later).
- Checks if the plate is taken, available, or if you're being blocked by incapsula.

## NOTES: 
- The default query.txt file will contain random plates that are available and not available. If every plate is coming up as either available/not-available, go into the main.py and set debug mode to true to get a further insight into what the bot is seeing.

- On the dev branch, debug mode is enabled by default.

- The default checklink is for the Classic Black Silver plate, which supports up to 7 characters.

- The default wait time is 3 seconds. Set it to whatever you want.

## UPCOMING FEATURES:
NOTE: If you want to see the latest planned features/progress on them, go to the Issues tab and sort by the tag [enhancement](https://github.com/bestadamdagoat/txVanityPlateChecker/labels/enhancement). 

- Make settings configured by a config file https://github.com/bestadamdagoat/txVanityPlateChecker/issues/4
- Make code cleaner https://github.com/bestadamdagoat/txVanityPlateChecker/issues/3
- Fix formatting of the console log https://github.com/bestadamdagoat/txVanityPlateChecker/issues/2

## HOW TO USE THE BOT:
NOTE: Make sure you are using Python 3.
1. Clone the repository
     - You can do this by going to Code (the green button) and either downloading this repo as a zip (make sure to unzip it) or doing it the cool way and cloning with Git.
2. Open up the file in your favorite IDE (like PyCharm or VScode)
     - If you can open up this file in CMD/Terminal, you do not need an explanation on how to get this thing fully setup.
3. Go into the terminal and type `pip install -r requirements.txt`
4. Edit the query.txt file to your liking
     - Make sure to separate all the plates by new lines. Also make sure all the queries fit the plate requirements.
5. You are now ready to run the bot!

## COMMON ISSUES + FIXES
NOTE: This will not always be up-to-date, and I will not add uncommon issues to this list. If you want an up-to-date list of fixes, click [here](https://github.com/bestadamdagoat/txVanityPlateBot/issues?q=is%3Aissue+is%3Aclosed).

- insert incapsula error
