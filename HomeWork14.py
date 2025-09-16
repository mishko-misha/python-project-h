number = int(input("Enter number from 0 to 7948799: "))

d1, mod1 = divmod(number, 24 * 60 * 60)  # days
d2, mod2 = divmod(mod1, 60 * 60)  # hours
d3, mod3 = divmod(mod2, 60)  # minutes and mod3 is seconds

day_word = "днів" if 11 <= d1 % 100 <= 14 else "день" if d1 % 10 == 1 else "дні" if 2 <= d1 % 10 <= 4 else "днів"

days = str(d1)
hours = str(d2).zfill(2)
minutes = str(d3).zfill(2)
seconds = str(mod3).zfill(2)

print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")

# # 0 -> 0 днів, 00:00:00
# # 224930 -> 2 дні, 14:28:50
# # 466289 -> 5 днів, 09:31:29
# # 950400 -> 11 днів, 00:00:00
# # 1209600 -> 14 днів, 00:00:00
# # 1900800 - > 22 дні, 00:00:00
# # 8639999 -> 99 днів, 23:59:59
# # 22493 -> 0 днів, 06:14:53
# # 7948799 -> 91 день, 23:59:59
