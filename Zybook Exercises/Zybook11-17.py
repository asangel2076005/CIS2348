user_list = input().split(" ")
user_negative_list = [int(i) for i in user_list if int(i) <= -1]
user_negative_list.sort(reverse=True)

for neg_num in user_negative_list:
    print(f"{neg_num}", end=" ")
