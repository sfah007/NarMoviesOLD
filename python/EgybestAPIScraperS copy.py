import json
import grequests
import requests
from bs4 import BeautifulSoup as bs
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from tqdm import tqdm


url = "https://api.timemovies.net/api/v2.6/app/works/cat"

headers = {
  'x-t': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTNjZmU4ZTA5ZTBiMjljNjA5NjZmMGYiLCJuYW1lIjoiMU9UUyDigKIgVGhlIFNhdmFnZXMiLCJlbWFpbCI6Iml0c3pldXN4MDQyQGdtYWlsLmNvbSIsImRsIjoiYXIiLCJhbCI6ImFyIiwiaWRzIjpmYWxzZSwiaWF0IjoxNjMyNjY0NjkwLCJleHAiOjE2MzMyNjk0OTB9.LUsZh8RYYJTNOgIierS4lkD6EUFVTc1gJsaAdp066m8',
  'ai': '602b1b13d7a19a2d6786544d',
  'Content-Type': 'application/json'
}
rqsts = []
final = []
s = requests.Session()
retries = Retry(total=10, backoff_factor=0.2, status_forcelist=[
                500, 502, 503, 504], raise_on_redirect=True, raise_on_status=True)
s.mount('http://', HTTPAdapter(max_retries=retries))
s.mount('https://', HTTPAdapter(max_retries=retries))

for pageIndex in range(30) :
    payload = json.dumps({
  "cat": {
    "_id": "eace4fbb-bdb8-468b-98d5-55394b39cca8",
    "name": "Recently Added Searies",
    "is_movie": False,
    "cat": "publish_date",
    "dir": -1,
    "is_history": False,
    "is_tag": False
  },
  "page": pageIndex,
  "size": 15
})
    rqsts.append(grequests.post(url , headers=headers , data=payload , session=s))
results = grequests.map(rqsts)
for response in results :
        final += response.json()

with open("EgybestAllSeriesAR.json" , "w" , encoding="utf-8") as f :
    json.dump(final , f ,ensure_ascii=False)