def dop(name,text):
    file = open(f'{name}' + '.txt', 'a+', encoding='utf=8')
    return file.write(f'{text}\n')