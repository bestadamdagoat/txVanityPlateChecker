<div align="center">

# ANNOUNCEMENT: Check out the plate Show and Tell thread [here](https://github.com/bestadamdagoat/txVanityPlateChecker/discussions/7)!

# ![Plate Checker Logo](https://github.com/bestadamdagoat/txVanityPlateChecker/blob/main/platechecker.png?raw=true)

## A bot that will check if vanity plates are available or taken, poorly coded in Python using urllib and BeautifulSoup.
#### If this bot surprisingly worked for you, it would be cool if you donated to me. It would convince me to code better and actually be more commited to these projects. Check the sidebar for ways to donate to me.
<img alt="GitHub" src="https://img.shields.io/github/license/bestadamdagoat/txVanityPlateChecker"> ![Website](https://img.shields.io/website?label=myplates%20api&url=https%3A%2F%2Fwww.myplates.com/api/licenseplates/passenger/classic-black-silver/TEST) ![Liberapay receiving](https://img.shields.io/liberapay/receives/bestadam?label=receiving%20on%20liberapay) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beautifulsoup4) ![GitHub issues](https://img.shields.io/github/issues/bestadamdagoat/txVanityPlateChecker) ![GitHub repo size](https://img.shields.io/github/repo-size/bestadamdagoat/txVanityPlateChecker) ![GitHub repo file count](https://img.shields.io/github/directory-file-count/bestadamdagoat/txVanityPlateChecker) ![Lines of code](https://img.shields.io/tokei/lines/github/bestadamdagoat/txVanityPlateChecker)
</div>

Basically what this bot does is:
- Reads your query.txt file.
- Appends the next line to the [MyPlates API link](https://www.myplates.com/api/licenseplates/passenger/classic-black-silver/).
- Opens the API link with urllib and reads the page using BeautifulSoup (explained later).
- Checks if the plate is taken, available, or if you're being blocked by incapsula.
- Exports all the available plates to a txt.
- And does a lot more in the background.

## WHY URLLIB and BEAUTIFULSOUP?
I know what you're thinking, "This guy is insane to be accessing an api without using requests!" And you'd be correct. The only problem is that Incapsula is really smart and blocks my requests. I spent such a long time figuring out how to bypass incapsula with requests, that I even quit on this project for a while because of how much time I was spending. I decided to try a different way as all my methods were not working (custom headers, cookies, etc.). I ended up figuring out that urllib was able to access the site without getting blocked. I then decided to use BeautifulSoup to parse the api, as it was easy for me to understand. Now I have this project. I feel like this workaround should not have worked, seeing [all](https://www.reddit.com/r/webscraping/comments/bpc8ix/any_option_to_bypass_incapsula/) the [other](https://stackoverflow.com/questions/71537488/i-cant-get-the-content-of-the-web-site) people who failed using this same workaround. But you know what they say, "If it ain't broke, don't fix it!"

## NOTES: 
- The default `query.txt` file will contain random plates that are available and not available. If every plate is coming up as either available/not-available, go into the main.py and set debug mode to true to get a further insight into what the bot is seeing and open up an issue with a log from the console.

- The default checklink is for the Classic Black Silver plate, which supports up to 7 characters.

- EXE releases will always be based off of the main branch.

- There is a lightweight version that you can obtain from [here](https://github.com/bestadamdagoat/txVPC-lw).

- Developer/Maintainer Notes:
     - Main Branch requires a PR and will only be updated after a few commits to dev. All important issues with main/important updates must require a PR. 
     - Dev Branch gets updated frequently. All updates/mini issue fixes must be pushed to dev first. 

## CONFIG.INI
- NOTE: Leaving any of these unset/incorrectly set will set the variables to their defaults.
1. `debug`
    - Can be set to either `true` or `false`. Enables/disables debug mode, which outputs the checklink with the query, the page, and the query. The default setting for this is `false`.
2. `sleeptime`
    - Can be set to any time in seconds (ex. `3`, `7`, `1`). The default setting for this is `3`.
3. `minimode`
    - Can be set to either `true` or `false`. Enables/disables mini mode, which disables output of not-available plates. The default setting for this is `false`.

## UPCOMING FEATURES:
NOTE: If you want to see the latest planned features/progress on them, go to the Issues tab and sort by the tag [enhancement](https://github.com/bestadamdagoat/txVanityPlateChecker/labels/enhancement). 

- Add Preset Lists https://github.com/bestadamdagoat/txVanityPlateChecker/issues/26
- Update Checker https://github.com/bestadamdagoat/txVanityPlateChecker/issues/25
- Make the Program Into an Executable https://github.com/bestadamdagoat/txVanityPlateChecker/issues/5 

## HOW TO USE THE BOT:
NOTE: Make sure you are using Python 3.
1. Clone the repository
     - Or download the zip using [this link](https://github.com/bestadamdagoat/txVanityPlateChecker/archive/refs/heads/main.zip).
2. Open up the folder in your favorite IDE (like PyCharm or VScode)
     - If you can open up this file in CMD/Terminal, you do not need an explanation on how to get this thing fully setup.
3. Go into the terminal and type `pip install -r requirements.txt`
4. Edit the `query.txt` file to your liking
     - Make sure to separate all the plates by new lines. Also make sure all the queries fit the plate requirements.
5. Edit the `config.ini` file to your liking
6. You are now ready to run the bot! Make sure to run `main.py`. 

## COMMON ISSUES + FIXES:
NOTE: This will not always be up-to-date, and I will not add uncommon issues to this list. If you want an up-to-date list of fixes, click [here](https://github.com/bestadamdagoat/txVanityPlateBot/issues?q=is%3Aissue+is%3Aclosed).

- Currently, there are no observed errors. If you are aware of an error, please open up an issue!

