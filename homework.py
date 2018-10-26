def unique_func(*args):
    '''
        Gets any number of arguments with different types.
        Returns a list with unique elements.
    '''

    result_lst = []
    for i in args:
        if i not in result_lst:
            result_lst.append(i)
    return result_lst

print(f'{unique_func(3, 5, 6, 4, 6.4, 3, 2, 8, 9, 2, "repeat", "repeat", "repeat", "dont repeat", [2, 2, 8], [2, 2, 8])}')
