print('Добро пожаловать в викторину!')
one_name = int(input('В каком году родился Джим Керри?: ')) #Джим Керри 1962
two_name = int(input('В каком году родился Александр III?: ')) #Александр 1845
three_name = int(input('В каком году родился Карл Маркс?: ')) #Карл Маркс 1818
four_name = int(input('В каком году родился Пол Маккартни?: ')) #Пол Маккартни 1942
five_name = int(input('В каком году родился Анна Ахматова?: ')) #Анна Ахматова 1889

right = 0
not_true = 0
if one_name == 1962:
    right += 1
else:
    not_true += 1

if two_name == 1845:
    right += 1
else:
    not_true += 1

if three_name == 1818:
    right += 1
else:
    not_true += 1

if four_name == 1942:
    right += 1
else:
    not_true += 1

if five_name == 1889:
    right += 1
else:
    not_true += 1

print('Количество правильных ответов: ', right)
print('Количество ошибок: ', not_true)
print('Процент правильных ответов: ', right*100/5)
print('Процент не правильных ответов: ', not_true*100/5)