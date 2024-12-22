from string import digits, ascii_lowercase


def convert_to(num, base):
    alph = digits + ascii_lowercase
    res = ""
    while num > 0:
        res = alph[num % base] + res
        num //= base
    return res


def alg(N):
    tr = convert_to(N, 3)
    if N % 2 == 0:
        tr = "2" + tr + convert_to(int(tr[-1]) * 2, 3)
    else:
        tr = convert_to(int(tr[0]) * 2, 3) + tr + "2"
    return int(tr, 3)


print(min(list(filter(lambda x: x > 100, [alg(n) for n in range(1, 1000)]))))
