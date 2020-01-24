import requests

def currence():
    req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data=req.json()
    msg='курсы валют на сегодня\n'
    msglong = 'курсы валют на сегодня\n'
    valuteshrt=['USD','EUR','USD']
    valuteall=list(data['Valute'].keys())
    for i in valuteall:
        tmp=list(data['Valute'][i].values())
        msglong+=f'{tmp[3]} {tmp[2]} {tmp[5]}\n'
    # print(data['Valute']['USD'].values())
    # print(data['Valute']['EUR'].keys())
    for i in valuteshrt:
        tmp=list(data['Valute'][i].values())
        msg+=f'{tmp[3]} {tmp[2]} {tmp[5]}\n'




    return msg, msglong

a,b=currence()
