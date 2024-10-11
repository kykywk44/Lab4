import package.calculations
import package.text

i = input('С каким модулем хотите работать? \n1)Текстовый модуль \n2)Вычислительный модуль \n')
if i == '1':
    name = input('Введите название файла:\n')
    text = input('Введите текст для файла:\n')
    package.text.dop(name,text)
if i == '2':
    n1 = input('Введите первое число: ')
    n2 = input('Введите второе число: ')
    d = input('Что необходимо сделать?(+,-,*) ')
    if '+' in d:
        package.calculations.s(n1,n2)
    if '-' in d:
        package.calculations.v(n1,n2)
    if '*' in d:
        package.calculations.u(n1,n2)

