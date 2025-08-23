def word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

def letter_count(book_text):
    lc = {}
    book_text_lower = book_text.lower()
    for i in book_text_lower:
        if i in lc:
            lc[i] = lc[i] + 1
        else:
            lc[i] = 1
    return lc

def sort_on(item):
    return item["num"]

def sort_letter_count(letter_total):
    items = []
    for letter, number in letter_total.items():
        items.append({"char": letter, "num": number})
    items.sort(reverse=True, key=sort_on)
    return items
