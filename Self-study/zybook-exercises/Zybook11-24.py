user1_sentence = input().split()
user2_sentence = input().split()

for i in range(len(user1_sentence)):
    if user1_sentence[i] != user2_sentence[i]:
        print(f"{user1_sentence[i]} {user2_sentence[i]}")
