import feedparser
rss_url=feedparser.parse('https://overclockers.ru/rss/news.rss')
feed = feedparser.parse( rss_url )
print(rss_url)