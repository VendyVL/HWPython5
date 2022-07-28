# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = ('абв где опрос по слово п680сн "Забвение" про забава').split(" ")

a = []
for i in range(len(text)):
    if text[i].find('абв') >= 0: 
        a.append(i)

print(a)
for i in a:
    text.pop(i)

print (text)