list = []

for i in range(13):
 number = int(input(f"Введіть {i + 1}-й елемент масиву: "))
 list.append(number)
 
max=max(list)
print(max)
list.sort(reverse=True)
print(list)

