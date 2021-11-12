import json
import grequests
import requests
from bs4 import BeautifulSoup as bs
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from tqdm import tqdm


url = "https://api.timemovies.net/api/v2.6/app/works/episodes?wk="

headers = {
  'x-t': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MTNjZmU4ZTA5ZTBiMjljNjA5NjZmMGYiLCJuYW1lIjoiMU9UUyDigKIgVGhlIFNhdmFnZXMiLCJlbWFpbCI6Iml0c3pldXN4MDQyQGdtYWlsLmNvbSIsImRsIjoiYXIiLCJhbCI6ImFyIiwiaWRzIjpmYWxzZSwiaWF0IjoxNjMyNjY0NjkwLCJleHAiOjE2MzMyNjk0OTB9.LUsZh8RYYJTNOgIierS4lkD6EUFVTc1gJsaAdp066m8',
  'ai': '602b1b13d7a19a2d6786544d',
  'Content-Type': 'application/json'
}

series = json.load(open("Databases\EgybestAllSeries.json" , "r" , encoding="utf-8"))

rqsts = []
final = []
s = requests.Session()
retries = Retry(total=10, backoff_factor=0.2, status_forcelist=[
                500, 502, 503, 504], raise_on_redirect=True, raise_on_status=True)
s.mount('http://', HTTPAdapter(max_retries=retries))
s.mount('https://', HTTPAdapter(max_retries=retries))

for serie in series :
  link = url + str(serie["_id"])
  rqsts.append(grequests.get(link , headers=headers , session=s))
results = grequests.map(rqsts)
for i in range(len(series)) :
  series[i].update({"episodes" : results[i].json()})

with open("Etest.json" , "w" , encoding="utf-8") as f :
    json.dump(series , f ,ensure_ascii=False)