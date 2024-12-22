def alg(N):
    ch = [int(i) for i in list(filter(lambda x: x in "02468", list(str(N))))]
    ne_ch = [int(i) for i in list(filter(lambda x: x in "13579", list(str(N))))]
    if len(ch) > len(ne_ch):
        res = sum(ch)
    else:
        res = sum(ne_ch)
    if res % 2 == 0:
        res = str(res) + str(max(ch))
    else:
        res = str(min(ne_ch)) + str(res)
    return int(res)


count = 0
for n in range(1000, 9999 + 1):
    if any(i in str(n) for i in "02468") and any(i in str(n) for i in "13579"):
        if alg(n) == 111:
            count += 1
print(count)
