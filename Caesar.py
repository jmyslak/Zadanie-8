def encryption(text:str, k:int ) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_dict = {}

    for i,letter in enumerate(alphabet):
        alphabet_dict[letter] = i

    text2 = ""
    for letter in text:
        if letter in alphabet_dict:
            index_0 = alphabet_dict[letter]
            new_index = (index_0 +k)%len(alphabet)
            for key, value in alphabet_dict.items():
                if value == new_index:
                    text2 += key
        else: text2 += " "
    return text2

# sprawdzenie
# print(encryption("ALA MA KOTA",3))

def decryption(text:str, k:int ) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_dict = {}

    for i,letter in enumerate(alphabet):
        alphabet_dict[letter] = i

    text2 = ""
    for letter in text:
        if letter in alphabet_dict:
            index_0 = alphabet_dict[letter]
            new_index = (index_0 -k)%len(alphabet)
            for key, value in alphabet_dict.items():
                if value == new_index:
                    text2 += key
        else: text2 += " "
    return text2







