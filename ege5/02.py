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
    if sum([int(j) for j in list(dv)]) % 2 == 0:
        dv = "10" + dv[2:] + "0"
    else:
        dv = "11" + dv[2:] + "1"
    return int(dv, 2)


for n in range(1, 1000):
    if alg(n) > 50:
        print(n)
        break
