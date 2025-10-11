class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'name: {self.first_name} {self.last_name}, age:{self.age} years old, gender: {self.gender}'

    def __eq__(self, human):
        if isinstance(human, Human):
            return str(self) == str(human)
        return False

    def __hash__(self):
        return hash(str(self))