def sort_ascending(*args):
    srclist = list(args)
    n = 1
    while (n < len(srclist)):
        for i in range(len(srclist) - n):
            if srclist[i] > srclist[i + 1]:
                srclist[i], srclist[i + 1] = srclist[i + 1], srclist[i]
        n += 1
    return srclist

newList = sort_ascending(5, 2, 5, 6, 2, 54, 8, 6, 75, 3, 21, 5, 51, 4, 262, 15)
print(f'sorted list: {newList}')

if __name__ == '__main__':
    assert sort_ascending(3, 2, 1, 49, 0) == [0, 1, 2, 3, 49], "Ошибка при сортировке списка целых чисел!"