def get_num_words(words):
    return len(words.split())

def character_count(words):
    words = words.lower()
    characters_in_words =  list(words)
    character_count = dict.fromkeys(characters_in_words)
    for k, v in character_count.items():
        character_count[k] = characters_in_words.count(k)
    return character_count

def sort_characters(character_counts):
    list_dict_chars = []
    for char, num in character_counts.items():
        list_dict_chars.append({"char": char, "num": num})
    def sort_on(items):
        return items["num"]    
    list_dict_chars.sort(reverse=True, key=sort_on)
    return list_dict_chars
