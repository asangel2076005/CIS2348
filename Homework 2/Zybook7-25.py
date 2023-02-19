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

if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val <= 0:
        print("no change")
    else: # input_val is greater than 0
        if num_dollars > 1:
            print(f"{num_dollars} dollars")
        elif num_dollars == 1:
            print("1 dollar")

        if num_quarters > 1:
            print(f"{num_quarters} quarters")
        elif num_quarters == 1:
            print("1 quarter")

        if num_dimes > 1:
            print(f"{num_dimes} dimes")
        elif num_dimes == 1:
            print("1 dime")

        if num_nickels > 1:
            print(f"{num_nickels} nickels")
        elif num_nickels == 1:
            print("1 nickel")

        if num_pennies > 1:
            print(f"{num_pennies} pennies")
        elif num_pennies == 1:
            print("1 penny")

