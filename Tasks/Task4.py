# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import string

b = 'ABCABCABCDDDFFFFFF'
a = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

# def rleCompress(a):
#     result = ''
#     i = 0
#     while i < len(a):
#         count = 1
#         while i+1 < len(a) and a[i] == a[i+1]:
#             count+=1
#             i+=1
#         result += str(count) + a[i]
#         i+=1
#     return result

def split_letters(a):
    list1 = []
    list1.append(a[0])
    j = 0
    for i in range (1, len(a)):
        if i<=len(a)-1:
            if a[i-1]==a[i]:
                list1[j]+=a[i]
            # elif a[i-1]!=a[i]!=a[i+1]:
                # list1[j]+=a[i]
            elif a[i-1]!=a[i]:
                list1.append(a[i])
                j+=1           
    return list1 

def rleCompress(a):
    list = split_letters(a)
    rle_str = ''
    for i in range (0,len(list)):
        if len(list[i]) == 1:
            rle_str += list[i]
        else:
            rle_str += str(len(list[i])) + list[i][0]
    return rle_str

def rleDecompr(a):
    res = ''
    for i in range (0,len(a)):
        if string.indigit(a[i]):# Тут какая-то ошибка...
            if string.indigit(a[i+1]):
                x = int(a[i]+a[i+1])#а если число будет трёхзначным?
                for j in range (0, x):
                    res += a[i+2]
            else:
                x = int(a[i])
                for j in range (0, x):
                    res += a[i+1]
        else: res += a[i]
    return res

# def len_and_name(list1):
#     list2 = []
#     for i in range (0, len(list1)):
#         count = 1
#         if len(list1[i]) !=1:
#             list2.append(len(list1[i]))
#             list2.append(list1[i][0])
#     return list2


c = 'ABCABCABCDDDFFFFFFABDRRR'
print(rleCompress(c))
print(rleDecompr(rleCompress(c)))
