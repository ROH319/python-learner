def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    

print("请选择转换类型：")
print("1. 摄氏度到华氏度")
print("2. 华氏度到摄氏度")
print("3. 摄氏度到开尔文")
print("4. 开尔文到摄氏度")
print("5. 华氏度到开尔文")
print("6. 开尔文到华氏度")
choice = int(input("请输入你的选择（1-6）："))

num = float(input("请输入一个数字："))
if not is_number(num):
    print("输入错误！")

if choice == 1:
    fahrenheit = (num * 9/5) + 32
    print("{:.2f} 摄氏度 = {:.2f} 华氏度".format(num, fahrenheit))


elif choice == 2:
    celsius = (num - 32) * 5/9
    print("{:.2f} 华氏度 = {:.2f} 摄氏度".format(num, celsius))

elif choice == 3:
    kelvin = num + 273.15
    print("{:.2f} 摄氏度 = {:.2f} 开尔文".format(num, kelvin))

elif choice == 4:
    celsius = num - 273.15
    print("{:.2f} 开尔文 = {:.2f} 摄氏度".format(num, celsius))

elif choice == 5:
    kelvin = (num - 32) *5/9 + 273.15
    print("{:.2f} 华氏度 = {:.2f} 开尔文".format(num, kelvin))

elif choice == 6:
    fahrenheit = (num - 273.15) * 9/5 + 32
    print("{:.2f} 开尔文 = {:.2f} 华氏度".format(num, fahrenheit))
