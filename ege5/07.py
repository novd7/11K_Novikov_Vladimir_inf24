from string import digits, ascii_lowercase


def convert_to(num, base):
    alph = digits + ascii_lowercase
    res = ""
    while num > 0:
        res = alph[num % base] + res
        num //= base
    return res


def alg(N):
    dv = convert_to(N, 2)
    if N % 2 == 0:
        dv = "10" + dv
    else:
        dv = "1" + dv + "01"
    return int(dv, 2)


print(max([alg(n) for n in range(1, 12 + 1)]))
