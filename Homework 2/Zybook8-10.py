# Angelo Angel (2076005)

def palindrome(text):
    text = text.lower()
    text = ''.join(letter for letter in text if letter.isalnum())

    if text == text[::-1]:
        return print(f"{text} is a palindrome")
    else:
        return print(f"{text} is not a palindrome")

if __name__ == "__main__":

    user_text = input()
    palindrome(user_text)
