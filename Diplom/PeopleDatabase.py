import json
import os
from Diplom.Person import Person


class People:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    # list comprehension [expression for item in iterable if condition]
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
            birth_date = Person.get_date(person.birth_date)
            death_date = Person.get_date(person.death_date)

            birth = birth_date.strftime('%d.%m.%Y') if birth_date else None
            death = death_date.strftime('%d.%m.%Y') if death_date else None

            data.append({
                'first_name': person.first_name,
                'middle_name': person.middle_name,
                'last_name': person.last_name,
                'gender': person.get_gender(),
                'birth_date': birth,
                'death_date': death,
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

            print(f'Дані завантажено у папку data файл на ім\'я {filename}')
        except FileNotFoundError:
            print('Файл не знайдено.')
