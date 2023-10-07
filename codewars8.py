def is_isogram(string):
    letters = []
    for letter in string.lower():
        if letter not in letters:
            letters.append(letter)
        else:
            return False
    return True
