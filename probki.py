import requests
from bs4 import BeautifulSoup


def probki():
    image_url='https://api-maps.yandex.ru/services/constructor/1.0/static/?um=constructor%3Acf59c400f858104ab41d1487bbdf90f79345d45530329ec69611989e6819d876&amp;width=522&amp;height=450&amp;lang=ru_RU'
    img_data = requests.get(image_url).content
    with open('probki.jpg', 'wb') as handler:
        handler.write(img_data)


    r = requests.get('https://export.yandex.ru/bar/reginfo.xml?region=213')
    soup = BeautifulSoup(r.text,features="lxml")
    a=soup.prettify()
    b=a.find('<hint lang="ru">')
    c=a.find('</hint>')
    return a[b+16:c]
