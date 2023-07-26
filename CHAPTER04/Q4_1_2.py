def fib2(n):
    # nより小さなフィボナッチ数列をリストで返す
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


fib_sequence = fib2(1000)
print(fib_sequence)
