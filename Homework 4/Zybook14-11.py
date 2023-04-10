# Angelo Angel (2076005)

def selection_sort_descend_trace(n):
    for row in range(len(n) - 1):
        t = row
        for item in range(row + 1, len(n)):
            if n[t] < n[item]:
                t = item
        n[row], n[t] = n[t], n[row]
        for value in n:
            print(value, end=" ")
        print()
    return n


if __name__ == "__main__":
    user_input = [int(i) for i in input("").split()]
    selection_sort_descend_trace(user_input)
