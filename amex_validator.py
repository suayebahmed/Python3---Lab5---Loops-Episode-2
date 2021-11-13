# American Express Card number validator
card_number = input('Enter a card number: ')

# Checking first two digit of the card
if card_number[:2] == '34' or card_number[:2] == '37':
    first_two_digit = "YES"
else:
    first_two_digit = "NO"

# only digit and 15 digit check
if len(card_number) == 15 and card_number.isdigit() == True:
    digit_length = "YES"
else:
    digit_length = "NO"

# Luhn Formula implementation
numbers_to_double = card_number[-2::-2]
sum_1 = 0
if card_number.isdigit():
    for i in numbers_to_double:
        i = int(i) * 2
        if i > 9:
            i -= 9
        sum_1 += i
else:
    luhn_satisfied = 'NO'

rest_numbers = card_number[-1::-2]
sum_2 = 0
if card_number.isdigit():
    for i in rest_numbers:
        sum_2 += int(i)
else:
    luhn_satisfied = 'NO'

sum = sum_1 + sum_2

if card_number.isdigit():
    if sum % 10 == 0:
        luhn_satisfied = 'YES'
    else:
        luhn_satisfied = 'NO'

# Showing the final output
if first_two_digit == "YES" and luhn_satisfied == "YES" and digit_length == "YES":
    print("That’s a VALID AmEx number!\n")
else:
    print("That’s an INVALID AmEx number!\n")

print(f"Begins with 34 or 37    - {first_two_digit}")
print(f"15 digits in length     - {digit_length}")
print(f"Satisfies Luhn formula  - {luhn_satisfied}\n")