class Person:

    def __init__(self, first_name, middle_name=None, last_name=None, birth_date=None, death_date=None, gender=None):
        self.first_name = first_name.capitalize()
        self.middle_name = middle_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender.lower() if gender in ('м', 'ж') else 'невідомо'

    @staticmethod
    def _get_date(text):
        for char in [' ', '.', '/','-']:
            text = text.replace(char, ' ')
        parts = text.split()

        if len(parts) != 3:
            raise ValueError("Невірний формат дати,повинно бути 3 числа).")
        day = parts[0].zfill(2)
        month = parts[1].zfill(2)
        year = parts[2].zfill(2)

        return f'{day}.{month}.{year}'

    def get_age(self):
        pass

    def get_gender(self):
        return 'чоловік' if self.gender == 'м' else 'жінка' if self.gender == 'ж' else 'невідомо'

    def __str__(self):
        info = f'Name: {self.first_name}, Middle name: {self.middle_name}, Last Name: {self.last_name}'
        return info