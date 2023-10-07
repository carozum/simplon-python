def get_middle(s):
    if len(s) % 2 == 1:
        index = int((len(s) - 1)/2)
        return s[index]
    else:
        index = len(s)//2
        return s[index-1:index+1]
        # 2 characters


print(get_middle("test"))
get_middle("of")
get_middle('carol')
get_middle("middle")
