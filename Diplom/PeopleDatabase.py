import json
import os
from Diplom.Person import Person


class People:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    # list comprehension [expression for item in iterable if condition]
    # person before FOR. It  will have result in finally
    def find_person(self, request):
        request = request.lower()
        return [
            person for person in self.people
            if request in person.first_name.lower()
               or request in person.middle_name.lower()
               or request in person.last_name.lower()
        ]

    def save_person(self, filename):
        data = []

        for person in self.people:
            data.append({
                'first_name': person.first_name,
                'middle_name': person.middle_name,
                'last_name': person.last_name,
                'age': person.get_age(),
                'gender': person.get_gender(),
                'birth_date': person.birth_date,
                'death_date': person.death_date,
            })

        os.makedirs('data', exist_ok=True)
        filepath = os.path.join('data', filename)

        # indent adds gaps
        with open(filepath, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_person(self, filename):
        filepath = os.path.join('load', filename)
        try:
            with open(filepath, 'r', encoding='utf8') as file:
                data = json.load(file)
                self.people = [Person(**records) for records in data]

            self.save_person(filename)

            print(f'Дані завантажено з файлу {filename}')
        except FileNotFoundError:
            print('Файл не знайдено.')
