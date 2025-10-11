number = input("Enter five-digit number: ")
d1, mod1 = divmod(int(number), 10000)
d2, mod2 = divmod(mod1, 1000)
d3, mod3 = divmod(mod2, 100)
d4, mod4 = divmod(mod3, 10)
d5, mod5 = divmod(mod4, 1)

revers_number = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1
print(revers_number)
