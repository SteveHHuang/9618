def factorial(n,):
    # 基线条件
    if n == 0:
        return 1
    # 递归调用
    return n * factorial(n - 1)



print(factorial(15))