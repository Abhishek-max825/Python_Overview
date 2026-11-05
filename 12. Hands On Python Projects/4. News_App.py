import requests

query = input("In which event are you interested in ?? ")

api = "api_key"

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api}"

r = requests.get(url)

data = r.json()
articles = data["articles"]

for index,result in enumerate(articles):
    print(index + 1,".",result["title"],result["url"],result["content"])
    print("\n***********************************************************\n")
    