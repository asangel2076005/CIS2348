user_list = input().split()

if len(user_list) <= 9:
    sample_list = [int(i) for i in user_list]
    if len(sample_list) == 1:
        for i in sample_list:
            print(f"Middle item: {i}")
    else:
        first_half = int(len(sample_list)/2)
        last_half = int(len(sample_list)/2)
        middle_item = sample_list[first_half:-last_half]
        for i in middle_item:
            print(f"Middle item: {i}")

else:
    print("Too many inputs")
