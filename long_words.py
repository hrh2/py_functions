def words_with_more_chars(lists):
    new_list = []
    for string in lists:
        if len(string) > 5:
            new_list.append(string)
        else:
            pass
    return new_list
