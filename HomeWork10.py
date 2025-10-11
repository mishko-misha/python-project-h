import keyword
import string

name = input("Enter your name first name + _ + second name: ")

string_punctuation = string.punctuation.replace("_", "")
keyword_kwlist = keyword.kwlist

if not name:
    print(False)  # False
elif name[0].isdigit():
    print(False)  # 3m => False
elif name.count("_") == len(name) and len(name) > 1:
    print(False)  # __ => False ___ => False
elif name.count("_") == len(name):
    print(True)  # True
elif name.isalpha() and name.islower() and name.lower() not in [kw.lower() for kw in keyword_kwlist]:
    print(True)  # x => True
elif "_" in name:
    parts_of_name = name.split("_")
    if len(parts_of_name) >= 2:
        first_name = parts_of_name[0]
        last_name = parts_of_name[-1]
        if all(char.isalpha() and char.islower() for part in parts_of_name for char in part):
            print(True)  # _ => True and get_value and some_super_puper_value and assert___exception => True
        elif last_name[-1].isdigit() and any(c.isalpha() for c in last_name):
            print(True)  # m3 => True
        elif first_name[0].isupper() and all(part.isalpha() for part in parts_of_name):
            print(False)  # Get_value => False
        elif last_name[0].isupper() and all(part.isalpha() for part in parts_of_name):
            print(False)  # get_Value => False
        else:
            print(False)
elif " " in name:
    print(False)  # get value => False
elif name.lower() in [kw.lower() for kw in keyword_kwlist]:
    print(False)  # assert => False
elif name.isalpha():
    for i in range(1, len(name)):
        if name[i].isupper():
            print(False)
            break  # getValue => False
    else:
        print(True)
elif any(char in name for char in string_punctuation):
    print(False)  # get!value => False
else:
    print(True)  # assert_exception => True
