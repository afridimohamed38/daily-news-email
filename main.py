import requests
from send_email import send_email

api_key = "19379b53d074490f846dc7afb97f4ae8"
topic = "technology"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-09-29" \
      "sortBy=publishedAt&apiKey=19379b53d074490f846dc7afb97f4ae8&language=en"

request = requests.get(url)
content = request.json()

# print(type(content))

raw_message = ""

for article in content['articles'][0:20]:
    if article['title'] is not None:
        title_val = article['title'] + "\n"
        raw_message += title_val

        des_url_val = article['description'] + "\n" + article['url'] + 2 * "\n"
        raw_message += des_url_val

inter_message = f"""\
Subject : Daily news digest

{raw_message}
"""

final_message = inter_message.encode("utf-8")
send_email(final_message)
# print(final_message)
