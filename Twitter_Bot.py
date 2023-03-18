import twint #Requires Python 3.6
import tweepy #Requires Latest Python Version
import openai #Requires Latest Python Version
import time # Used to adhere to OpenAI API Rate Limit


# This is all API key information. I think it can be stored in a class but we don't remember how to
API_KEY = "aRTwTMMhiG1A5ezYYBpX9PPDS"
API_SECRET = "oFBs0vThVsA8aYkTKTgdEkO0lUiAAFMK5Yy7AVlBg9q49BpmkL"
ACCESS_TOKEN = "1616521652128600066-ILwJPM4LdFURSUmB4Io0SCe7XXrFBx"
ACCESS_SECRET = "Kkuy0iImSLp6DZjVUCu5LA4JjtDSkDzGua8OkBPbZvVj0"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the API object
api = tweepy.API(auth)

#Stores Scraped Fox News Tweets into a local CSV File
c = twint.Config()
c.Username = "FoxNews"
c.Search = "arrest"
c.Custom["tweet"] = ["tweet"]
c.Output = "Fox_Tweets_Scraped.csv"
c.Store_csv = True
twint.run.Search(c)

#Reads & opens scraped tweets from local CSV file to be translated by OpenAI PirateSpeak
tweets_fox = open("Fox_Tweets_Scraped.csv","r")
tweets = tweets_fox.read()

#Translates scraped tweets to PirateSpeak from CSV file into PirateSpeak using DaVinci OpenAI Model
openai.api_key = "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"
for i in tweets:
  input = i
  response = openai.Completion.create( # OpenAI Parameters to translate scraped tweets from CSV files:
    model="text-davinci-003",
    prompt="Turn this phrase into pirate speak:\n\n" + input,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
  time.sleep(5) #Adheres to 20 requests/minute limit in DaVinci OpenAI API

  # Creates a translated tweet object to post with Tweepy API
  translated_tweet = response["choices"][0]["text"] 
  api.update_status(translated_tweet)
  # ^ Still depends on Elevated Twitter account Status 