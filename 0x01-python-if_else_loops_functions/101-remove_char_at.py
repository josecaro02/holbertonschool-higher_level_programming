def remove_char_at(str, n):
    phrase = ""
    num = 0
    for i in str:
        if (num != n):
            phrase += i
        num += 1
    return phrase
