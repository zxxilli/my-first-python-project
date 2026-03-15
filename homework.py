
a1 = 34
a2 = 29
a3 =90
average =(a1 + a2 + a3) / 3
print(a1,"和",a2,"和",a3,'的平均值为',average)



radius = 50
kilometers = radius*2*3.14
print(kilometers)

print("第一行内容", end=" ")
print("第二行内容")

print(f"{654123:>5}")

print(f"{1:>5}")
print(f"{12:>5}")
print(f"{123:>5}")
print(f"{1234:>5}")
print(f"{12345:>5}")

print(f'{"*":^5}')
print(f'{"***":^5}')
print(f'{"*****":^5}')


print("a", "b", "c", sep="|")
print(1, 2, 3, sep="-")

s = "1 + 2 * 3 - 4"
result =eval(s)
print(result)

expr = input("请输入数学表达式：")  # 比如输入：(5+3)*2
try:
    res = eval(expr)
    print("计算结果：", res)  # 输出：16
except:
    print("输入的表达式不合法！")





