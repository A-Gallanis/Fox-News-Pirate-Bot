# Fox-News-Pirate-Bot
This is the repository of the Twitter bot that translates Fox News tweets and reposts them in pirate speak. 

Hello Mr. Won,

In theory, this script should be working. However, we are in dependency hell in terms of our libraries and API access. We have comments explaining all of our methods, however, I would like to bullet point all of the dependency issues we have and the solution we will have at the end.
• Dependency #1: Twint - Twint Requires Python 3.6 to run and install. It also has a lot more requirements on the ReadMe file. https://github.com/twintproject/twint. I accidentally deleted python the other day, so this is harder to reproduce.
• Dependency #2: OpenAI - It seems like OpenAI requires Python 3.7 to run.
•Dependency #3: Tweepy - Tweepy, the official Twitter API, requires the latest version of Python to run.
•Dependency #4: Posting Tweets - Selenium Webdriver is deprecated for posting tweets. To Tweet with Python, we need an elevated access developer account. We applied for elevated access earlier this week and are in the process of getting it.

Our dependency solutions:
• Waiting for Elevated Access: There's really nothing we can do except for wait for an elevated access Twitter account to post tweets. The free cap was increased to 500,000 tweets/month after Elon Musk responded to criticism, so this would probably eliminate the need for Twint entirely aswell.
•Virtual Machine: Even if we get an elevated access Twitter account to scrape and post tweets completely through the OpenAI API, we need a still need a way to run this bot in the background and somehow incorporate the Python 3.7 openAI library. To do this, we'll need to set up a virtual instance (probably on Google Cloud), with a sacrificial credit card to get our Python dependencies all isolated in this environment and to allow multiple scripts to split up the work of Extracting the Fox News Tweets (3rd party Twint or Twitter API), Transforming them (OpenAI python 3.7 library), and Loading them onto Twitter (by posting them with elevated access Twitter API).

I hope this explains our situation. We have our methods working, but our dependencies are not, and we are planning to set up a virtual instance when we get back from school and wait for our elevated access Twitter Developer account.
