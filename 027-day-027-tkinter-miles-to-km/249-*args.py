def add(*args):
    print(args)  # (5, 4, 3, 2, 1)
    print(args[0])  # 5
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(5, 4, 3, 2, 1))  # 15
