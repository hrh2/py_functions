def character_frequency(string):
    frequency_dictionary = {}
    for char in string:
        if char in frequency_dictionary:
            frequency_dictionary[char] += 1
        else:
            frequency_dictionary[char] = 1
    return frequency_dictionary

