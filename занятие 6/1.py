text = "Ну вообще какойто левый текст слово на е надо придумать енот еда емкость и тд"
words = text.split()
count = 0
for word in words:
    if word.startswith("е") or word.startswith("Е"):
        count += 1
print("Количество слов, начинающихся с буквы 'е'", count)
