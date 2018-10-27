def unique_func(iterable, seen = set()):
    seen.clear()
    for item in iterable:
        if item not in seen:
            seen.add(item)
    return seen

given_arr = [3, 5, 6, 4, 6.4, 3, 2, 8, 9, 2, "repeat", "repeat", "repeat", "dont repeat"]
res = unique_func(given_arr)
print(f'{res}')
