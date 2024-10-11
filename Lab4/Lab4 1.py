import datetime

n = [10,11,12]
m = ['октября','ноября','декабря']
t = str(datetime.datetime.now())

for i in zip(n,m):
    if int(t[5:][:2]) in i:
        print(f'Сегодня: {t[8:][:2]} {i[1]} {t[:4]} года \nМосковское время: {t[11:][:8]}')