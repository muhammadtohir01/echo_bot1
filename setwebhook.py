import requests
import os

url = "https://muhammad01.pythonanywhere.com/ali"

TOKEN = os.environ["TOKEN"]

payload = {
    "url" : url
}

r = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook", params=payload)

print(r.json())