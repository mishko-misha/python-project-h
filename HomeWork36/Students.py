from HomeWork36.Human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'name: {self.first_name} {self.last_name}, age: {self.age} years old, gender: {self.gender},  record book: {self.record_book}'

    def __eq__(self, student):
        if isinstance(student, Student):
            return str(self) == str(student)
        return False

    def __hash__(self):
        return hash(str(self))
