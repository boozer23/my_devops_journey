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