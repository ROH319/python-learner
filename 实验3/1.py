def cal_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



try:
    number = int(input("请输入一个整数来计算它的阶乘: "))
    if number < 0:
        print("负数没有阶乘，请输入一个非负整数。")
    else:
        factorial = cal_factorial(number)
        print(f"{number} 的阶乘是: {factorial}")
except ValueError:
    print("输入无效，请输入一个有效的整数。")
