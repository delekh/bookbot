def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

#helper function to get num of each character in a dict
def get_num(e):
    return e["num"]

def get_ordered_character_count(character_dict):
    sorted_character_dict_list = []
    for char in character_dict:
        sorted_character_dict_list += [{"char": char, "num": character_dict[char]}]
    
    sorted_character_dict_list.sort(key=get_num, reverse=True)

    return sorted_character_dict_list