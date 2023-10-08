# itératif


def fibo_i(n):
    fibo = [0, 1]
    for i in range(2, number + 1):
        current_term = fibo[i-2] + fibo[i-1]
        fibo.append(current_term)
    return fibo[number]


number = int(input("Enter an integer to calculate the fibonacci: "))

# récursif


def fibo_r(number):
    fib = [0, 1]
    if number == 0:
        return fib[0]
    elif number == 1:
        return fib[1]
    else:
        return fibo_r[number-2] + fibo_r[number-1]


print(calculate_string(";$%§fsdfsd235??df/sdfgf5gh.000kk0000"))
print(calculate_string("fsdfsd235???34.4554s4234df-sdfgf2g3h4j442"))
print(calculate_string("fsdfsd234.4554s4234df+sf234442"))
