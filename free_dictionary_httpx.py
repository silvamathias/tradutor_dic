from asyncio import gather, run, create_task
from httpx import AsyncClient
import pandas as pd
import json as js
import datetime as dt
import os

async def get_word(wrd):
    async with AsyncClient(base_url='https://api.dictionaryapi.dev/api/v2/entries/en/') as client:
        response = await client.get(wrd)
        try:
            j = js.loads(response.text)
            return j
        except:
            pass

async def main():
    result = await gather(*[get_word(word) for word in lista])

    return result

lista_chv  = ['chapter','word','audio_link_1','audio_link_2','audio_link_3','audio_link_4','part_of_speech','description','exemple']
df_txt = pd.read_excel('comics_civil_war.ods')

lista = df_txt['word'].values.tolist()

t1 = dt.datetime.now()
js_list = run(main())
new_js = []

for js_txt in js_list:
    try:
        lista_padrao = [df_txt[df_txt['word'] == js_txt[0]['word']].iat[0,0],js_txt[0]['word']]

        for n in range(4):
            try:
                lista_padrao += [js_txt[0]['phonetics'][n]['audio']]
            except:
                lista_padrao += [''] 
            
        for mean in js_txt[0]['meanings']:
            for definition in mean['definitions']:
                try:
                    definicao = [mean['partOfSpeech'],definition['definition'],definition['example']]
                except:
                    definicao = [mean['partOfSpeech'],definition['definition'],'']
            
                lista_vlr = lista_padrao + definicao
                dc = dict(zip(lista_chv,lista_vlr))

                new_js += [dc]
    except:
        pass

df = pd.json_normalize(new_js)

lista_chv  = ['chapter','word','part_of_speech','description','exemple','audio_link_1','audio_link_2','audio_link_3','audio_link_4']

df = df[lista_chv]

df.to_excel('dic_marvel_civil_comics.xlsx',index = False)
t2 = dt.datetime.now()
print(t2-t1)