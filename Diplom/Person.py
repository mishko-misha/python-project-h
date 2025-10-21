from datetime import datetime


class Person:

    def __init__(self, first_name, middle_name='', last_name='', birth_date=None, death_date=None, gender=None):
        self.first_name = first_name.capitalize()
        self.middle_name = middle_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender.lower()

    @staticmethod
    def get_date(text):
        if not text:
            return None
        for format_date in ('%d.%m.%Y', '%d %m %Y', '%d/%m/%Y', '%d-%m-%Y'):
            try:
                return datetime.strptime(text.strip(), format_date).date()
            except ValueError:
                continue
        raise ValueError(f"Неправильний формат дати: {text}")

    def get_age(self):
        birth = self.get_date(self.birth_date)
        death = self.get_date(self.death_date)

        if not birth:
            return None

        end_date = death or datetime.today().date()
        age = end_date.year - birth.year
        if (end_date.month, end_date.day) < (birth.month, birth.day):
            age -= 1
        return age

    def get_gender(self):
        return 'чоловік' if self.gender in ('ч', 'чоловік') else 'жінка' if self.gender in ('ж','жінка') else 'невідомо'

    def __str__(self):
        info = [f'Ім\'я: {self.first_name}']

        if self.middle_name:
            info.append(f'По-батькові: {self.middle_name}')
        if self.last_name:
            info.append(f'Прізвище: {self.last_name}')
        if self.get_age():
            info.append(f'Вік: {self.get_age()} років')

        if self.gender in ('ч', 'м', 'чоловік'):
            info.append(f'Стать: {self.get_gender()}')

        birth = self.get_date(self.birth_date)
        death = self.get_date(self.death_date)

        if birth:
            gender_check = 'Народився:' if self.gender in ('ч', 'чоловік') else 'Народилася:' if self.gender in ('ж','жінка') else 'Народився/лася: '
            info.append(f'{gender_check}{birth.strftime("%d.%m.%Y")}')
        if death:
            gender_check = 'Помер:' if self.gender in ('ч', 'м', 'чоловік') else 'Померла' if self.gender in ('ж','жінка') else 'Помер/ла: '
            info.append(f' {gender_check} {death.strftime("%d.%m.%Y")}')
        return ' '.join(filter(None, info))
