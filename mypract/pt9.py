"""numbers = []
n = int(input("введи количество чисел списка: "))
for i in range(n):
    num = int(input(f"Введи число {i+1}: "))
    numbers.append(num)
print("исход. список: ", numbers)
numbers = [num for num in numbers if num % 2 != 0]
result = sum(numbers)
average = result / len(numbers)
maximum = max(numbers)
minimum = min(numbers)
negative = sum(1 for num in numbers if num < 0)
print("Список чисел: ", numbers)
print("Сумма чисел: ", result)
print("Среднее арифметическое: ", average)
print("Максмум: ", maximum)
print("минимум: ", minimum)
print("Отриц. числа: ", negative)
numbers = [num for num in numbers if num % 2 != 0]
print("без четных чисел: ", numbers)
for i in range(len(numbers)):"""


