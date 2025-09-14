name = input("Enter your name first name + _ + second name: ")

string_punctuation = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']

keyword_kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'case',
                  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
                  'global', 'if', 'import', 'in', 'is', 'match', 'nonlocal', 'not', 'or', 'pass', 'raise',
                  'return', 'try', 'while', 'with', 'yield']

if name.count("_") == len(name) and len(name) > 1:
    print(False)  # __ => False ___ => False
elif len(name) == 1 and name.isalpha():
    print(True)  # x => True
elif name[0].isdigit():
    print(False)  # 3m => False
elif "_" in name:
    parts_of_name = name.split("_")
    first_name = parts_of_name[0]
    last_name = parts_of_name[1]
    if all(part.isalpha() and part.islower() for part in parts_of_name):
        print(True)  # _ => True and get_value => True and some_super_puper_value => True
    elif first_name[0].istitle() and last_name.islower() and all(part.isalpha() for part in parts_of_name):
        print(False)  # Get_value => False
    elif first_name.islower() and last_name.istitle() and all(part.isalpha() for part in parts_of_name):
        print(False)  # get_Value => False
    elif first_name.isalpha() and last_name[-1].isdigit():
        print(True)  # m3 => True
elif " " in name:
    print(False)  # get value => False
elif name.isalpha():
    for i in range(1, len(name)):
        if name[i].isupper():
            print(False)  # getValue => False
elif any(char in name for char in string_punctuation):
    print(False)  # get!value => False
if name in keyword_kwlist:
    print(False)  # assert => False
else:
    print(True)  # assert_exception => True