# 1 час = 3600 с
# 1 м = 60с
time = int(input('Введите время в секундах: '))
hh = time // 3600
mm = time % 3600 // 60
ss = time % 3600 % 60
if hh < 10:
    hh = f'0{hh}'
else:
    hh = hh
if mm < 10:
    mm = f'0{mm}'
else:
    mm = mm
if ss < 10:
    ss = f'0{ss}'
else:
    ss = ss
print(f'{time} секунд = {hh}:{mm}:{ss}')