import random


# Генеруємо 10 випадкових чисел у діапазоні (30, 90)
random_numbers = [random.randint(30, 90) for _ in range(13)]

# Додаємо останню цифру студента до кожного числа
result_numbers = [num for num in random_numbers]

# Виводимо результат
print(result_numbers)
