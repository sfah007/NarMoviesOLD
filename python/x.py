import json

cats = [
  {
    "_id": "5d0990a7c89e354c3f924a31",
    "name_ar": "مغامرة"
  },
  {
    "_id": "5d0990a7c89e354c3f924a32",
    "name_ar": "اكشن"
  },
  {
    "_id": "5d0990a7c89e354c3f924a33",
    "name_ar": "كوميدي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a34",
    "name_ar": "كرتون"
  },
  {
    "_id": "5d0990a7c89e354c3f924a35",
    "name_ar": "عائلي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a36",
    "name_ar": "خيال"
  },
  {
    "_id": "5d0990a7c89e354c3f924a37",
    "name_ar": "دراما"
  },
  {
    "_id": "5d0990a7c89e354c3f924a38",
    "name_ar": "خيال علمي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a39",
    "name_ar": "رومانسي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a3a",
    "name_ar": "غموض"
  },
  {
    "_id": "5d0990a7c89e354c3f924a3b",
    "name_ar": "قصير"
  },
  {
    "_id": "5d0990a7c89e354c3f924a3c",
    "name_ar": "اثارة"
  },
  {
    "_id": "5d0990a7c89e354c3f924a3d",
    "name_ar": "جريمة"
  },
  {
    "_id": "5d0990a7c89e354c3f924a3e",
    "name_ar": "واقعي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a3f",
    "name_ar": "وثائقي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a40",
    "name_ar": "تاريخي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a41",
    "name_ar": "رعب"
  },
  {
    "_id": "5d0990a7c89e354c3f924a42",
    "name_ar": "غربي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a43",
    "name_ar": "موسيقي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a44",
    "name_ar": "عروض العاب"
  },
  {
    "_id": "5d0990a7c89e354c3f924a45",
    "name_ar": "حرب"
  },
  {
    "_id": "5d0990a7c89e354c3f924a46",
    "name_ar": "سيرة ذاتيه"
  },
  {
    "_id": "5d0990a7c89e354c3f924a47",
    "name_ar": "موسيقى"
  },
  {
    "_id": "5d0990a7c89e354c3f924a48",
    "name_ar": "رياضي"
  },
  {
    "_id": "5d0990a7c89e354c3f924a49",
    "name_ar": "إخباري"
  },
  {
    "_id": "5d0990a7c89e354c3f924a4a",
    "name_ar": "توك شو"
  },
  {
    "_id": "5d0990a7c89e354c3f924a4b",
    "name_ar": "بالغين فقط"
  },
  {
    "_id": "6021f6dcfabdebf2be76cf24",
    "name_ar": "تلفزيوني"
  },
  {
    "_id": "60240050ca8ec17d4939e7f6",
    "name_ar": "سياسي"
  },
  {
    "_id": "60244187bfce0388b093e294",
    "name_ar": "أطفال"
  }
]
results = []
for cat in cats :
    x = cat["name_ar"]
    results.append(f"/movies-list?genre={x}")
print(results)