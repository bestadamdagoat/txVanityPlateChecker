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
This bot is very bad and will eventually fail due to either unknown reasons or AntiCaptcha being too slow, make sure to check up on it at least once an hour.

When initially starting the bot, make sure to close out the tab that asks for you to accept cookies. If you don't the bot will fail.

You will **NOT** win every time when using this bot, be patient.

The Pringle links will go to your email/catchall.

You are free to modify the code in any way you want, but if you do PLEASE make a fork.

## UPCOMING FEATURES:
NOTE: I probably won't implement these unless this promotion gets extended or revived (after the end of it). If you want to see the latest planned features/progress on them, go to the Issues tab and sort by the tag [enhancement](https://github.com/bestadamdagoat/pringles-bot/labels/enhancement). 

- Auto Accept Cookies https://github.com/bestadamdagoat/pringles-bot/issues/1
- Re-enter using the same generated account https://github.com/bestadamdagoat/pringles-bot/issues/2
- Make the script into an Executable and configure it using a config file https://github.com/bestadamdagoat/pringles-bot/issues/3
- Use different captcha system https://github.com/bestadamdagoat/pringles-bot/issues/4
- Track the Wins/Losses https://github.com/bestadamdagoat/pringles-bot/issues/5
- Send info to a Discord Webhook https://github.com/bestadamdagoat/pringles-bot/issues/6
- DeprecationWarning Fix https://github.com/bestadamdagoat/pringles-bot/issues/8

## HOW TO USE THE BOT:
NOTE: Make sure you have any version of Chrome 104 installed (unless you manually upgraded chromedriver.exe). You can do this by going to chrome://version.
1. Clone the repository
     - You can do this by going to Code (the green button) and either downloading this repo as a zip (make sure to unzip it) or doing it the cool way and cloning with Git
2. Open up the file in your favorite IDE (like PyCharm or VScode)
     - If you can open up this file in CMD/Terminal, you do not need an explanation on how to get this thing fully setup.
3. Go into the terminal and type `pip install -r requirements.txt`.
4. Unzip `anticaptcha-blank.zip` and put your [AntiCaptcha API Key](http://getcaptchasolution.com/wfgri4goqd) in the `config_ac_api_key.js` file located at `\anticaptcha-blank.zip\js`.
     - Make sure to put the API key into the `var antiCapthaPredefinedApiKey = '';` line.
5. Rezip the `anticaptcha-blank.zip` file and replace the old one.
     - You can rezip files using 7zip or Winrar.
6. Edit the `catchall = "YOURCATCHALLHERE"` line in `pbot.py` so that `YOURCATCHALLHERE` is replaced with your catchall.
     - Your catchall is your domain (ex. github.com) not a full email (like adam@github.com).
7. You are now ready to run the bot!
     - Make sure to agree to cookies when running the bot.

## COMMON ISSUES + FIXES
NOTE: This will not always be up to date, and I will not add uncommon issues to this list. If you want an up-to-date list of fixes, click [here](https://github.com/bestadamdagoat/pringles-bot/issues?q=is%3Aissue+is%3Aclosed).

- from unknown error: cannot read manifest https://github.com/bestadamdagoat/pringles-bot/issues/10
