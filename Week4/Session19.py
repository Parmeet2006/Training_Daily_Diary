import requests
import json

API_KEY = 'f1a7e3de4dbcecf93fc9e450b764dda50bc09b56'
url = "https://google.serper.dev/search"

payload = {
  "q": input('Enter Search Query: ')
}
headers = {
  'X-API-KEY': API_KEY,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)
# print(response.text)
search_result = json.loads(response.text)
results = search_result['organic']
for result in results:
    print(result['title'])
    print(result['snippet'])
    print('~'*20)

