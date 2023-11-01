import requests
import json
from colorama import Fore, Style
import pyttsx3

MAX_LINE_LENGTH = 100  # Maximum characters per line for description
api_key = "YOUR_API_KEY"

query = input("What type of news are you interested in? ")
num_headlines = int(input("How many headlines would you like to display? "))
readOrnot = input("Do you want to read it out loud or not? (yes/no): ").lower()

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-09-18&sortBy=publishedAt&apiKey={api_key}"
r = requests.get(url)
news = json.loads(r.text)
articles = news['articles']

num_headlines = min(num_headlines, len(articles))
engine = pyttsx3.init()

for article in articles[:num_headlines]:
    title = article['title']
    description = article['description']
    colored_title = f"{Fore.GREEN}{title}{Style.RESET_ALL}"
    print(colored_title)
  
    description_lines = [description[i:i+MAX_LINE_LENGTH] for i in range(0, len(description), MAX_LINE_LENGTH)]
    for line in description_lines:
        colored_line = f"{Fore.BLUE}{line}{Style.RESET_ALL}"
        print(colored_line)
      
    print("----------------------------------------------------------------------------------")
  
    if readOrnot == "yes":
        engine.say(title)
        for line in description_lines:
            engine.say(line)
    else:
        pass
      
engine.runAndWait()
