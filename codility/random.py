def it_sum(k):
    acc = 0
    while (k > 0):
        acc += k
        k = k - 1
    return acc

print(it_sum(2))
