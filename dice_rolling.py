# DICE ROLLING analyzes rolling OF two dice

# taking inputs for side of the dice
first_dice = int(input('Enter number of sides on first die: '))
second_dice = int(input('Enter number of sides on second die: '))

print(f"There are {first_dice * second_dice} possible outcomes from rolling 1d{first_dice} and 1d{second_dice}:")

# nested loop
for i in range(1, first_dice + 1):
    for j in range(1, second_dice + 1):
        print(f"{i, j}")
