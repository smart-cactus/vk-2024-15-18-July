a = []
n = input("Введите товар или 'стоп' для завершения: ")

while n.lower() != "стоп":
    a.append(n)
    n = input("Введите товар или 'стоп' для завершения: ")

print("\nВаш список покупок:")
for item in a:
    print(item)
