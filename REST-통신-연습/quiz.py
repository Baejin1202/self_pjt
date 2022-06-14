import requests
from pprint import pprint

url = "http://13.125.222.176/quiz/jordan"
data = requests.post(url, json={
    "nickname" : "구미3반배혜진",
    "yourAnswer" : "Kubernetes",
})
print()
pprint(data.json())

