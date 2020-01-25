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
    return msg