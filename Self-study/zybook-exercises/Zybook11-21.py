user_list = input().split()
lower_words = [word.lower() for word in user_list]

values = [lower_words.count(word) for word in lower_words]

for i in range(len(user_list)):
    print(f"{user_list[i]} {values[i]}")
