array = 10
list = []

for i in range(array):
 number = int(input(f"Введіть {i + 1}-й елемент масиву: "))
 list.append(number)
 
max=max(list)
print(max)
list.sort(reverse=True)
print(list)

