name = input("Enter your name first name + _ + second name: ")

string_punctuation = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']

keyword_kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'case',
                  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
                  'global', 'if', 'import', 'in', 'is', 'match', 'nonlocal', 'not', 'or', 'pass', 'raise',
                  'return', 'try', 'while', 'with', 'yield']
if "___" in name:
    print(False)  # __ => False
elif "__" in name:
    print(False)  # ___ => False
if "_" in name:
    parts_of_name = name.split("_")
    if (len(parts_of_name) == 2 and all(part.isalpha() for part in parts_of_name)
            and parts_of_name[0].istitle() and parts_of_name[1].islower()):
        print(False)  # Get_value => False
    elif (len(parts_of_name) == 2 and all(part.isalpha() for part in parts_of_name)
          and parts_of_name[0].islower() and parts_of_name[1].istitle()):
        print(False)  # get_Value => False
    elif len(parts_of_name) == 2 and all(part.isalpha() and part.islower() for part in parts_of_name):
        print(True)  # _ => True and get_value => True
    elif len(parts_of_name) == 4 and all(part.isalpha() and part.islower() for part in parts_of_name):
        print(True)  # some_super_puper_value => True

if name[0].isdigit():
    print(False)  # 3m => False
elif name[-1].isdigit():
    print(True)  # m3 => True

if " " in name:
    parts_of_name = name.split(" ")
    if len(parts_of_name) == 2 and all(part.isalpha() for part in parts_of_name):
        print(False)  # get value => False
elif name.isalpha() and not name[1:]:
    print(True)  # x => True

if "_" not in name:
    for i, letter in enumerate(name[1:], start=1):
        if letter.isalpha() and letter.isupper():
            print(False)  # getValue => False

for char in string_punctuation:
    if char in name:
        parts_of_name = name.split(char)
        if len(parts_of_name) == 2 and all(part.isalpha() for part in parts_of_name):
            print(False)  # get!value => False

if name in keyword_kwlist:
    print(False)  # assert => False
#else doesn't work
else:
    print(True)  # assert_exception => True
