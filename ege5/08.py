def alg(N):
    ch = list(filter(lambda x: x in "02468", list(str(N))))
    ne_ch = list(filter(lambda x: x in "13579", list(str(N))))
    ch = "".join(list(sorted(ch, reverse=True)))
    ne_ch = "".join(list(sorted(ne_ch)))
    return int(ch if ch else 0) + int(ne_ch if ne_ch else 0)


max_res = -100 ** 100
for n in range(1000, 9999 + 1):
    if any(i in str(n) for i in "02468") and any(i in str(n) for i in "13579"):
        R = alg(n)
        lst_R = list(str(R))
        if lst_R == list(sorted(lst_R, reverse=True)) and len(lst_R) == len(set(lst_R)):
            max_res = max(max_res, R)
print(max_res)
