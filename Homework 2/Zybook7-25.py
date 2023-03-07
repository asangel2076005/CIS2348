# Angelo Angel (2076005)

# dollar = 100
# quarters = 25
# dimes = 10
# nickels = 5
# pennies = 1

def exact_change(user_change):
    num_dollars = user_change // 100
    user_change = user_change % 100
    num_quarters = user_change // 25
    user_change = user_change % 25
    num_dimes = user_change // 10
    user_change = user_change % 10
    num_nickels = user_change // 5
    user_change = user_change % 5
    num_pennies = user_change

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies
