def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_characters(text):
    characters = {}
    text = text.lower()
    for i in text:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_characters(chars):
    list_of_char = []
    temp_dict = {"name": None, "num": None}
    for i in chars:
        if i.isalpha():
            list_of_char.append({"name": i, "num": chars[i]})

    list_of_char.sort(reverse = True, key = sort_on)

    return list_of_char
