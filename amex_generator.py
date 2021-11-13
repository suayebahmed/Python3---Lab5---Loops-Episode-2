# American Express Card Number Generator
import random

n = int(input("How many AmEx numbers would you like today? "))
while n < 1:
    n = int(input("Must enter at least 1!  Try again: "))

print()
print("Here you go, have fun:")
for i in range(n):
    # randomly generate 34 or 37
    first_two_digit = random.choice([34, 37])

    # generate next 12 number between 0-9
    list_of_0_9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    random_list_of_12_num = []
    for i in range(12):
        s = random.choice(list_of_0_9)
        random_list_of_12_num.append(s)

    # list to string
    random_str_of_12_num = ""
    for x in random_list_of_12_num:
        random_str_of_12_num += str(x)

    # Luhn formula 

    half_done_card = str(first_two_digit) + random_str_of_12_num + "x"  # Card number before Luhn Algorithm implemented

    numbers_to_double = half_done_card[-2::-2]
    sum_1 = 0
    for i in numbers_to_double:
        i = int(i) * 2
        if i > 9:
            i -= 9
        sum_1 += i

    rest_of_the_num = half_done_card[-3::-2]
    sum_2 = 0
    for i in rest_of_the_num:
        sum_2 += int(i)

    final_sum = sum_1 + sum_2

    # finding the hidden number, x.
    for i in range(10):
        s = final_sum + i
        if s % 10 == 0:
            hidden_num = i
            break

    # finally showing the card number
    final_card_number = str(first_two_digit) + random_str_of_12_num + str(hidden_num)
    print(final_card_number)
print()
