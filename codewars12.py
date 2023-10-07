def descending_order(num):
    list_number = list(str(num))
    list_number.sort(reverse=True)
    new_str = "".join(list_number)
    return new_str


print(descending_order(428425439))
