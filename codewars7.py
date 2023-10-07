def solution(text, ending):
    number = len(ending)
    if text[-number:] == ending:
        print(text[-number:])
        return True
    else:
        return False


print(solution('abc', 'bc'))
