def summation(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + identity(k), k + 1
        return total
def identity(x):
        return x
def sum_naturals(n):
        return summation(n)

print(sum_naturals(10))