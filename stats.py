def get_word_count(book_str):
    li=book_str.split()
    return len(li)


def get_char_count(book_str:str) -> dict:
    book_ch=book_str.lower()
    book_ch=set(book_ch)
    dict_count = {}
    for ch in book_ch:
        dict_count[ch]=0
    for ch in book_str.lower():
        if ch in dict_count.keys():
            dict_count[ch]+=1
    return dict_count


def get_dict_list(char_dict: dict) -> list:
    li_char_count=[]
    for key in sorted(char_dict, key=char_dict.get, reverse=True):
        if key.isalpha():
            li_char_count.append({"char":key,"num":char_dict[key]})
    return li_char_count
