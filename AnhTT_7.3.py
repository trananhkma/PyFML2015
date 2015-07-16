def fibonacci(n, a=1, b=1):
    if n <= 1:
        return a
    else:
        return fibonacci(n-1, a=b, b=b+a)


if __name__ == '__main__':
    print fibonacci(10)   # 55
