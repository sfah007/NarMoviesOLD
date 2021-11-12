import json

f1 = open("Databases\EgybestAllSeriesAR.json" , "r" , encoding="utf-8")
f2 = open("Databases\EgybestAllSeriesEN.json" , "r" , encoding="utf-8")

data1 = json.load(f1)
data2 = json.load(f2)

for index in range(len(data1)) :
    data1[index].update({"title" : data2[index]["title"]} )

f3 = open("Databases\EgybestAllSeries.json" , "w" , encoding="utf-8")
json.dump(data1 , f3 , ensure_ascii=False)