nums = []
user_num = input().split()
user_num_positive = [float(i) for i in user_num if float(i) > -1]

nums_average = sum(user_num_positive) / len(user_num_positive)

print(f"{max(user_num_positive):.2f} {nums_average:.2f}")
