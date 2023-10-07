for d1 in range(10):
    for u1 in range(10):
        for d2 in range(10):
            for u2 in range(10):
                if (d1*10 + u1) < (d2*10 + u2):
                    str = f"{d1}{u1} {d2}{u2}"
                    print(str)
