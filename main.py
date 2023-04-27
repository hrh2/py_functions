def reversing(word):
    x = len(word)-1
    reversed_word = ""
    while x >= 0:
        reversed_word += word[x]
        x -= 1
    return reversed_word


print(reversing("words"))
