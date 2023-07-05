# У всіх завданнях використовувати обробку винятків

# 1. Користувач вводить із клавіатури номер дня тижня (1-7).
# Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.

##################################################################
# try:
#     dayNambers = int(input("Enter day numbers of the week (1-7): "))
#     match dayNambers:
#         case 1:
#             print(f"{dayNambers} day of the week is Monday.")
#         case 2:
#             print(f"{dayNambers} day of the week is Tuesday.")
#         case 3:
#             print(f"{dayNambers} day of the week is Wednesday.")
#         case 4:
#             print(f"{dayNambers} day of the week is Thursday.")
#         case 5:
#             print(f"{dayNambers} day of the week is Friday.")
#         case 6:
#             print(f"{dayNambers} day of the week is Saturday.")
#         case 7:
#             print(f"{dayNambers} day of the week is Sunday.")
#         case _:
#             print("Enter a number in the range (1-7)!")
# except ValueError as error:
#    print("Enter only integer!")

##################################################################
# 2. Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання

##################################################################

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     if num1 == num2:
#         print("Numbers 2 and 3 are equal to")
#     else:
#         if num1 < num2:
#             print(num1, num2)
#         else:
#             print(num2, num1)
# except ValueError as error:
#     print("Enter only integer!")

##################################################################

# 3. Користувач вводить два числа та матем дію: + - * або /.
# Залежно від введеної матем дії вивести результат.

##################################################################

##################################################################