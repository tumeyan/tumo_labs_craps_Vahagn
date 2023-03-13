import random

one = random.randint(1,6)
two = random.randint(1,6)
craps_sum = one + two
sum_goal = 0
i = 7
print(f'The sum of dice is {one} + {two} = {craps_sum}')
if craps_sum == 11 or craps_sum == 7:
    print("You won")
elif craps_sum == 2 or craps_sum == 3 or craps_sum == 12:
    print("Casino wins")
else:
    print(f'Now your goal number is {craps_sum}')
    player_won = False # added flag variable
    while i != sum_goal:
        one1 = random.randint(1,6)
        two2 = random.randint(1,6)
        sum_goal = one1 + two2
        print(f'The sum of dice is {one1} + {two2} = {sum_goal}')
        if craps_sum == sum_goal:
            print("You won")
            player_won = True 
            break
    if not player_won: 
        print("You lose")
