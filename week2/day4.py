def greet(name):
    print("Привет,", name)

greet("Владимир")
greet("Иван")
greet("Мария")

def calculate_age(birth_year):
    age = 2026 - birth_year
    return age

my_age = calculate_age(1994)
print("Мне", my_age, "лет")

print(calculate_age(1994))

def check_salary(salary):
    if salary < 50000:
        return "пора менять работу"
    elif salary < 150000:
        return "неплохо"
    else:
        return "девопс работает"

print(check_salary(30000))
print(check_salary(60000))
print(check_salary(200000))

echo "День 2. Git изучен." >> journal.txt
cat journal.txt

a = 10
b = 20

if a > b:
    return "a больше b"

else:
    return "a меньше или равно b"