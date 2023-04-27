# Write a function that takes two lists as input and
# returns a new list that contains only the elements that are common to both lists
def common_elements(list1, list2):
    new_list = []
    x = 0
    while x < len(list1):
        if list1[x] in list2 and not list1[x] in new_list:
            new_list.append(list1[x])
        x += 1
    return new_list

