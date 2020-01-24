import requests
p = requests.get('https://meduza.io/image/attachments/images/000/017/651/original/qAvIE71BRQOTl9q96t0kRA.svg')
out = open("img.svg", "wb")
out.write(p.content)
out.close()
