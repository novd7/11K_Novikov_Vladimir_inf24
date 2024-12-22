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
    dv += str(sum([int(j) for j in list(dv)]) % 2)
    dv += str(sum([int(j) for j in list(dv)]) % 2)
    return int(dv, 2)


print(min(list(filter(lambda x: x > 75, [alg(n) for n in range(1, 1000)]))))
