import requests
from send_email import send_email
from langdetect import detect

api_key = "19379b53d074490f846dc7afb97f4ae8"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-29language=en" \
      "sortBy=publishedAt&apiKey=19379b53d074490f846dc7afb97f4ae8"

request = requests.get(url)
content = request.json()

# print(type(content))

raw_message = ""

for article in content['articles']:
    if article['title'] is not None:
        title_val = article['title'] + "\n"
        raw_message += title_val

        des_val = article['description'] + "\n"
        raw_message += des_val

inter_message = f"""\
Subject : Daily news digest

{raw_message}
"""

final_message = inter_message.encode("utf-8")
send_email(final_message)
# print(final_message)
