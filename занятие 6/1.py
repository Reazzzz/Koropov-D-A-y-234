def countslov(text):
    words = text.split()
    count = 0
    for word in words:
        if word.startswith("е") or word.startswith("Е"):
            count += 1
    return count

text = "Ну вообще какойто левый текст слово на е надо придумать енот еда емкость и тд"
res= countslov(text)
print("Количество слов, начинающихся с буквы 'е':", res)
