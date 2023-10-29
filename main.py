import requests

api_key = "19379b53d074490f846dc7afb97f4ae8"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-29&" \
      "sortBy=publishedAt&apiKey=19379b53d074490f846dc7afb97f4ae8"

request = requests.get(url)
content = request.json()

# print(type(content))

for article in content['articles']:
    print(article['title'])
    print(article['description'])
    print("\n")
