import string
new_word = "carolinefaure"
my_dict = {}
for letter in new_word:
    if letter in my_dict.keys():
        my_dict[letter] += 1
    else:
        my_dict[letter] = 1
print(my_dict)


def row_sum_odd_numbers(n):
    if n == 1:
        return 1


alphabet = string.ascii_lowercase
print(alphabet)
