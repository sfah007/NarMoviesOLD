import json
import grequests
import requests
from bs4 import BeautifulSoup as bs
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from tqdm import tqdm


url = "https://api.timemovies.net/api/v3.2/app/works/cat"

headers = {
  'x-t': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTUwOGZlYTA5ZTBiMjljNjA0ZGUzNTQiLCJuYW1lIjoiMU9UUyDigKIgVGhlIFNhdmFnZXMiLCJlbWFpbCI6Iml0c3pldXN4MDQyQGdtYWlsLmNvbSIsImRsIjoiYXIiLCJhbCI6ImFyIiwiaWRzIjpmYWxzZSwic3FsIjoiMjQwcCIsImRxbCI6IjI0MHAiLCJpc192aXAiOmZhbHNlLCJ2aXBfdG8iOm51bGwsInZpcF9wbGFuIjpudWxsLCJpc19nb29nbGVfcGxheSI6dHJ1ZSwiaXNfcmVxdWVzdCI6dHJ1ZSwiaXNfc3RyZWFtIjp0cnVlLCJpc19kb3dubG9hZCI6dHJ1ZSwiaXNfc3VzcGVuZGVkIjpmYWxzZSwiaXNfc2V0dGluZyI6dHJ1ZSwiaXNfbmV3cyI6ZmFsc2UsImlhdCI6MTYzNjc1NDc5NCwiZXhwIjoxNjM3MzU5NTk0fQ.nKGCT2pZ8C7SbWsUEjMrEvYzcNu39WVU1m6xqo7b1Ro',
  'ai': '60129f949ea4ea03d6598c06',
  'Content-Type': 'application/json'
}
rqsts = []
final = []
s = requests.Session()
retries = Retry(total=10, backoff_factor=0.2, status_forcelist=[
                500, 502, 503, 504], raise_on_redirect=True, raise_on_status=True)
s.mount('http://', HTTPAdapter(max_retries=retries))
s.mount('https://', HTTPAdapter(max_retries=retries))

for pageIndex in range(173) :
    payload = json.dumps({
  "cat": {
    "_id": "2a2c349d-d11c-4656-96fd-4c8505c42981",
    "search_prop": "publish_date",
    "is_movie": True,
    "is_tag": False,
    "mode": None,
    "cat": "publish_date",
    "dir": -1,
    "is_history": False,
    "is_more": True,
    "title": {
      "ar": "افلام مضافة حديثا",
      "en": "Recently Added Movies",
      "fr": "Films récemment ajoutés",
      "sp": "Películas agregadas recientemente"
    },
    "name": "افلام مضافة حديثا"
  },
  "page": 0,
  "size": 15
})
    rqsts.append(grequests.post(url , headers=headers , data=payload , session=s))
results = grequests.map(rqsts)
for response in results :
        final += response.json()

with open("EgybestAllMoviesENNEWX.json" , "w" , encoding="utf-8") as f :
    json.dump(final , f ,ensure_ascii=False)