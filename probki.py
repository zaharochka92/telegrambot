import requests
from bs4 import BeautifulSoup


def probki():
    image_url='https://api-maps.yandex.ru/services/constructor/1.0/static/?um=constructor%3Acf59c400f858104ab41d1487bbdf90f79345d45530329ec69611989e6819d876&amp;width=522&amp;height=450&amp;lang=ru_RU'
    img_data = requests.get(image_url).content
    with open('probki.jpg', 'wb') as handler:
        handler.write(img_data)


    request = requests.get('https://export.yandex.ru/bar/reginfo.xml?region=213')
    soup = BeautifulSoup(request.text)
    msg=''
    page_parse =soup.prettify()
    level_prboki_start = page_parse.find('<level>')
    level_prboki_end = page_parse.find('</level>')
    probki_lvl = page_parse[level_prboki_start+8:level_prboki_end]
    probki_lvl = probki_lvl.replace(' ','')
    probki_lvl = probki_lvl.replace('\n', '')
    if ord(probki_lvl)==48 or ord(probki_lvl)>52 or probki_lvl=='10':
        balli='баллов'
    elif ord(probki_lvl)==49 :
        balli='балл'
    else : balli = 'балла'
    msg += f'- Пробки в Москве {probki_lvl} {balli}:'
    msg += '\n'
    description_probki_start = page_parse.find('<hint lang="ru">')
    description_probki_end =page_parse.find('</hint>')
    description_probki = page_parse[description_probki_start+16:description_probki_end]


    description_probki= ' '.join(description_probki.split())
    msg+= '- ' + description_probki

    return msg



