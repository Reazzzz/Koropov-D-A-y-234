def summa_proiz(list):
    summa = sum(list)
    proiz = 1
    for element in list:
        proiz *= element
    return summa, proiz

spisok = [1, 2, 3, 4, 5]
summa, proiz = summa_proiz(spisok)
print("Сумма элементов списка:", summa)
print("Произведение элементов списка:", proiz)


def replace(rar):
    vsya_sum = sum(rar)
    ne_zero = len([elem for elem in rar if elem != 0])
    if ne_zero == 0:
        return arr
    avg = vsya_sum / ne_zero
    for i in range(len(rar)):
        if rar[i] == 0:
            rar[i] = avg
    return rar
rar=[1,2,0,4,5,0]
new_rar= replace(rar)
print(new_rar)
