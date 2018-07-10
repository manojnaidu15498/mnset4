z=int(input())
def fib(n):
    a, b = 0, 1
    result = [0]
    while a < n:
        result.append(b)
        a, b = b, a+b
    return result
print(fib(z))
