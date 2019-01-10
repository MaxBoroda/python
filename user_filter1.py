#!/usr/bin/env python3

import json
import re

def is_number(char):
    return char.isnumeric()

def is_valid_phone(phone):
    #Здесь в фигурных скобках указана длина от 5-ти до 20-ти символов.
    pattern = re.compile('^\+[0-9-]{5,20}')
    if not pattern.fullmatch(phone):
        return False

    clean = "".join(filter(is_number, phone))
    #Длину строки можно сразу в регулярке задавать.
    #Но если там ожидается мусор(скобки и тире), то лучше чистить и потом проверять как здесь.
    if len(clean) == 11:
        return True
    return False

def is_valid_email(email):
    #Раньше эта регулярка парсила только email'ы с доменами первого уровня.
    #А бывают еще адреса с субдоменами. Лучше парсить больше 1 точки после собачки.
    pattern = re.compile('[a-z0-9._-]+@[a-z0-9._-]+')
    if pattern.fullmatch(email.lower()):
        return True
    return False

# Load DATA
people_file = './user.json'

with open(people_file) as file:
    people_data = json.load(file)

# Fix age field
for person_data in people_data:
    try:
        age = int(person_data['age'])
    except:
        age = -1
    person_data['age'] = age

    #Ошибка была из-за "Null" значений вместо почты или телефона.
    #Такое бывает в списках, по этому лучше их тоже обрабатывать.
    if person_data['email'] is None:
        person_data['email'] = 'No Email'
    if person_data['phone'] is None:
        person_data['phone'] = 'No Phone'

# Filtering
valid_people_data = list(filter(lambda x: is_valid_email(x['email']), people_data))
valid_people_data = list(filter(lambda x: is_valid_phone(x['phone']), valid_people_data))
valid_people_data = list(filter(lambda x: x['age'] >= 30, valid_people_data))

print(json.dumps(valid_people_data, indent=4, sort_keys=True))

#---------Write to file-------------
filtered_json_file = open(people_file + '.filtered.json', 'w')
# 'r' : открыть для чтений
# 'w' : открыть для записи. Создает если нет. Перезаписывает весь файл.
# 'x' : для создания и записи в новый файл
# 'a' : для добавления вконец файла
# 'r+' : для чтения и записи в тот же файл

#write принимает String.
filtered_json_file.write(json.dumps(valid_people_data, indent=4, sort_keys=True))
filtered_json_file.close()