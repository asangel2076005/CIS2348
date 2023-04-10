# Angelo Angel (2076005)

num_calls = 0


def partition(ids, i, k):
    pivot = user_ids[(i + k) // 2]
    leap = i - 1
    heap = k + 1
    while True:
        leap = leap + 1
        while ids[leap] < pivot:
            leap = leap + 1
        heap = heap - 1
        while ids[heap] > pivot:
            heap = heap - 1
        if leap >= heap:
            return heap
        ids[leap], ids[heap] = ids[heap], ids[leap]


def quicksort(ids, i, k):
    global num_calls
    num_calls = num_calls + 1
    if i >= k:
        return
    else:
        pep = partition(ids, i, k)
        quicksort(ids, i, pep)
        quicksort(ids, pep + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()

    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)
    print(num_calls)
    for user_id in user_ids:
        print(user_id)
