# 用于存储已经计算过的斐波那契数
fib_cache = {}


def fibonacci(n):
    """
    此函数使用递归和缓存优化来计算斐波那契数列的第 n 项。
    :param n: 要计算的斐波那契数列的位置
    :return: 斐波那契数列的第 n 项的值
    """
    
    if n in fib_cache:
        return fib_cache[n]
    
    if n == 0 or n == 1:
        result = n
    else:
        
        result = fibonacci(n - 1) + fibonacci(n - 2)
        
    fib_cache[n] = result
    return result


if __name__ == "__main__":
    try:
        
        n = int(input("请输入要计算斐波那契数列的位置（非负整数）: "))
        if n < 0:
            print("输入无效，请输入一个非负整数。")
        else:
            
            result = fibonacci(n)
            print(f"斐波那契数列的第 {n} 项是: {result}")
    except ValueError:
        print("输入无效，请输入一个有效的非负整数。")
