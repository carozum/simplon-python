def find_short(s):
    words = s.split(" ")
    print(words)
    short = len(words[0])
    for word in words:
        if len(word) < short:
            short = len(word)
    return short  # l: shortest word length


print(find_short("hello la vie est belle exceptionnellement !!"))
