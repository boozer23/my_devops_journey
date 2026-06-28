numbers = input("Введите числа через пробел: ").split()

even = 0
odd = 0

for n in numbers:
    if int(n) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Чётных: {even}, нечётных: {odd}")
