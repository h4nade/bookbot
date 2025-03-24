def get_num_words(text):
    arr = text.split()
    print(arr)
    return len(arr)

def get_char_count(text):
    dictionary = {}
    arr = list(text);
    arr2 = []
    for letter in arr:
        char = letter.lower()
        if char in dictionary:
            dictionary[char] = dictionary[char] + 1
        else:
            dictionary[char] = 1
    for key in dictionary:
        arr2.append({"char": key, "count": dictionary[key]})
    arr2.sort(reverse=True, key=sort_on)
    for obj in arr2:
        print(str(obj['char'] + ': ' + str(obj['count'])))
    # return dictionary

def sort_on(dict):
    return dict["count"]