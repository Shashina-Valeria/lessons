#задание_1
dlina = int(input("Введите длину: "))
shirina = int(input("Введите ширину: "))
s = dlina * shirina
p = (dlina + shirina) * 2
print("площадь: ", s, "периметр: ", p)

#задание_2
x = int(input("Введите число: "))
у_10 = (x % 100)//10
b_1 = x % 10
e = (x// 100) % 10
c = x // 10000
d = (x// 1000) % 10

result = ((у_10**b_1)*e) / (c - d)
print(result)