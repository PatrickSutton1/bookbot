def word_count(text):
    wc = len(text.split())
    return(wc)
    # print(f"{wc} words found in the document")

def char_count(text):
    lower = text.lower()
    unique_chars = set(lower)
    a_count = {}
    count = 0
    for char in unique_chars:
        if char in lower:
            count += 1
            a_count[char] = lower.count(char)
    return a_count

def sort_on(items):
    return items["num"]

def sort_char_count(char_count):
    to_sort = []
    char_dict = {}
    for char in char_count:
        char_dict["char"] = char
        char_dict["num"] = char_count[char]
        to_sort.append(char_dict.copy())
    return to_sort
