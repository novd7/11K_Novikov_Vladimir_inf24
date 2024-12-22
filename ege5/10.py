from string import digits, ascii_lowercase


def convert_to(num, base):
    alph = digits + ascii_lowercase
    res = ""
    while num > 0:
        res = alph[num % base] + res
        num //= base
    return res


def alg(N):
    dv = convert_to(N, 20)
    for _ in range(2):
        dv = dv.replace("a", "1")
        dv = dv.replace("e", "1")
        dv = dv.replace("i", "1")
        dv += convert_to(N % 20, 20)
        dv = dv[1:] + dv[0]
    return int(dv, 20)


print(max(list(filter(lambda x: x % 2030 == 0, [alg(n) for n in range(10000, 99999 + 1)]))))
