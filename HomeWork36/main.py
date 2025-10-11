from HomeWork36.Students import Student
from HomeWork36.Group import Group
from HomeWork36.GroupLimitError import GroupLimitError

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
assert gr.find_student('Jobs') == st1
gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

try:
    for i in range(1, 11):
        gr.add_student(Student('Male', 18 + i, f'Name{i}', f'Lastname{i}', f'AN{i}'))
    gr.add_student(st1)
except GroupLimitError as e:
    print("Error:", e)

