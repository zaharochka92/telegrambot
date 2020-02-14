import feedparser
rss_url='https://overclockers.ru/rss/news.rss'
def overclockersnews():
    rss_url = 'https://overclockers.ru/rss/news.rss'
    feed = feedparser.parse( rss_url )
    msg=''

    for article in feed['entries']:
        msg += '- '
        msg+=article['title']
        msg+='\n'
        msg+=article['description']
        msg+='\n'
    return msg

def habrhabr(key):
    # choose key 0-3 for day-year
    rss_url_bestday='https://habr.com/ru/rss/best/daily/?fl=ru'
    rss_url_bestweek='https://habr.com/ru/rss/best/weekly/?fl=ru'
    rss_url_bestmonth='https://habr.com/ru/rss/best/monthly/?fl=ru'
    rss_url_bestyear='https://habr.com/ru/rss/best/yearly/?fl=ru'

    periods=[rss_url_bestday, rss_url_bestweek, rss_url_bestmonth, rss_url_bestyear]

    feed = feedparser.parse(periods[key])
    msg=''
    for article in feed['entries']:
        msg += '- '
        msg+=article['title']
        msg+='\n'
        msg += article['link']
        msg += '\n'
    return msg

