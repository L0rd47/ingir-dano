#====================================================================================================
#https://testnet.binance.vision/ <- все данные были получены с помощью нижезакоменченных строк кода
# api_key= "b4zVrEPCftNFXR8Pt46L3nwOBo48oM3yJOlWQXTXEbe7FGLlXT0Qq06TEBcYBlR7"
# secret_key="13iqdxGG4IMvkmr40gvRkZA0b361X7DqUXNsQ33dSoKO0iFfYWroItciH7OiWbYm"
# from binance.client import Client
# client = Client(api_key,secret_key, testnet=True)
#
# all_tickers = client.get_all_tickers()
# print(all_tickers)
# jSon = open("my_jSon", 'r+')
# jSon.writelines(f'{all_tickers}')
# print(jSon.read())
# jSon.close()
#=====================================================================================================
import json
from bs4 import BeautifulSoup
temp_file = dict()
with open("my_jSon") as js:
     valid_js = js.read().replace("\'", "\"")
     temp_file = json.loads(valid_js)

soup = BeautifulSoup(features="html.parser")
table = soup.new_tag("table")
tr = soup.new_tag("tr")
for key, val in temp_file[0].items():
     th = soup.new_tag("th")
     th.string = key
     tr.append(th)
table.append(tr)


for tick in temp_file:
     tr = soup.new_tag("tr")
     for key, val in tick.items():
          td = soup.new_tag("td")
          td.string = val
          tr.append(td)
     table.append(tr)

soup.append(table)
with open('r_text_69.html', 'w') as result:
     result.write(soup.prettify())
     result.write("\n")