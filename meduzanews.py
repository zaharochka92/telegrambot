# import meduza
#
# def meduzanews():
#     news=''
#     try:
#         for article in meduza.section('news', n=12, lang='ru'):
#             news+=f" - {article['title']}\n"
#         return news
#     except Exception as error:
#         return f'some error{error}'