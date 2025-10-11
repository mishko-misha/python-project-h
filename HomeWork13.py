import string

any_letters = input("Enter  letter + - + letter: ")
letters = string.ascii_letters

parts = any_letters.split("-")

index_first_letter = letters.index(parts[0])
index_second_letter = letters.index(parts[1])

print(letters[index_first_letter:index_second_letter + 1])

# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA
