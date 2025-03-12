def word_count(text):
    total_count = 0
    words = text.split()
    for word in words:
        total_count +=1

    return total_count

def character_count(bc):
    character_dict = {}
    for char in bc.lower():
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1

    return character_dict

def sort_dictionary(dict):
    def sort_on(dict):
        return dict["num"]
    dicts_list = []
    for key, value in dict.items():
        if key.isalpha():
            new_dict = {
                "char": key,
                "num": value
            }
            dicts_list.append(new_dict)
    dicts_list.sort(reverse=True, key=sort_on)

    return dicts_list