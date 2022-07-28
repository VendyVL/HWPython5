# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'абв где опрос по слово п680сн "Забвение" про забава лабва'.split(" ")

a = [i for i in range(len(text)) if text[i].find('абв') >= 0]

a.reverse() # Чтобы удаляло с конца и не вышло за

for i in range (len(a)):
    del text[a[i]]

print (text)

