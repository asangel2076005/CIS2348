def jiffies_to_second(jiffy):
    return jiffy / 100


if __name__ == '__main__':
    user_jiffy = float(input())
    print(f"{jiffies_to_second(user_jiffy):.3f}")
