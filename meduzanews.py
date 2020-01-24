import meduza

def meduzanews():
    news=''
    for article in meduza.section('news', n=12, lang='ru'):
        news+=f" - {article['title']}\n"
    return news
