def swap(rr):
    rr[0], rr[-1] = rr[-1], rr[0]

m = int(input("Введите длину массива: "))
A = []

for i in range(m):
    elem = int(input("Введите элемент: "))
    A.append(elem)

print("Исходный массив A:", A)
swap(A)
print("Полученный массив A:", A)
