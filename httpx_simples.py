
import httpx as web
import json as js
import datetime as dt
import pandas as pd
#https://pt.libretranslate.com/


#lista = ['badges', 'being', 'clear', 'damn', 'hang up', 'leave', 'obey', 'seek', 'suddenly', 'tights', 'whole']

df_txt = pd.read_excel('comics_civil_war.ods')

lista = df_txt['word'].values.tolist()

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

f = []
t1 = dt.datetime.now()
for i in lista:
    try:
        r = web.get(url + i)
        j = js.loads(r.text)

        f += [j]
    except:
        pass

print(f)
t2 = dt.datetime.now()
print(f)
print(t2-t1)
