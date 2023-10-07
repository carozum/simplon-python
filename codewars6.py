def square_digits(num):
    list_digit = list(str(num))
    list_digit_squared = [str(int(element)**2) for element in list_digit]
    return int("".join(list_digit_squared))


print(square_digits(987))
