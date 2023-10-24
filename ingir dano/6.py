import requests
import json

data = json.loads(requests.get(f"https://restcountries.com/v3.1/name/canada").text)[0]

HTML_TEMPLATE = f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8" />
<title></title>
<link rel="stylesheet" href="style.css" />
</head>
<body>
<h1>country {data['name']['common']}</h1>
<p>timezones: {data['timezones'][3]}</p>
<p>subregion: {data['subregion']}</p>
<p>flag: {data['flag']}</p>
<p>capital: {data['capital'][0]}</p>
<p>startOfWeek: {data['startOfWeek']}</p>
<p>translations	: {data['translations']['jpn']['official']}</p>
</body>
</html>
"""


# Запись вывода в HTML файл
with open("canada.html", "w", encoding='utf-8', newline="") as file:
    file.write(HTML_TEMPLATE)
