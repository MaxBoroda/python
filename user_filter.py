#!/usr/bin/env python

import json
import re


def is_number(char):
    return char.isnumeric()


def is_valid_phone(phone):
    pattern = re.compile('\+[0-9-]+')
    if not pattern.fullmatch(phone):
        return False

    clean = "".join(filter(is_number, phone))
    if len(clean) == 11:
        return True
    return False


def is_valid_email(email):
    pattern = re.compile('[a-z0-9._-]+@[a-z0-9.]+\.[a-z0-9]+')
    if pattern.fullmatch(email.lower()):
        return True
    return False


def run_filter(data):
    vpd = list(filter(lambda x: is_valid_email(x['email']), data))
    vpd = list(filter(lambda x: is_valid_phone(x['phone']), vpd))
    vpd = list(filter(lambda x: x['age'] >= 30, vpd))
    return vpd


def main():
    # Load DATA
    people_file = 'user.json'

    with open(people_file) as file:
        people_data = json.load(file)

    # Fix age field
    for person_data in people_data:
        try:
            age = int(person_data['age'])
        except:
            age = -1
        person_data['age'] = age

    valid_people_data = run_filter(people_data)

    print(json.dumps(valid_people_data, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
