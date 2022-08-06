# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import string

b = 'ABCABCABCDDDFFFFFF'
a = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

def split_letters(a):
    list1 = []
    list1.append(a[0])
    j = 0
    for i in range (1, len(a)):
        if i<=len(a)-1:
            if a[i-1]==a[i]:
                list1[j]+=a[i]
            elif a[i-1]!=a[i]!=a[i+1]:
                list1[j]+=a[i]
            elif a[i-1]!=a[i]:
                list1.append(a[i])
                j+=1           
    return list1   

def len_and_name(list1):
    list2 = []
    for i in range (0, len(list1)):
        count = 1
        if len(list1[i]) !=1:
            list2.append(len(list1[i]))
            list2.append(list1[i][0])
        
            


    return list2


c = 'ABCABCABCDDDFFFFFFABDRRR'
print(split_letters(c))
# list1 = split_letters(c)
# print(len_and_name(list1)) 


# list_t = []
# x = ""
# for i in range (0, len(list1)):
#     if len(list1[i])==1:
#         if len(list1[i+1])==1:
#             x = x + list1[i]
#     list_t.append(f'-{len(x)}{x}')
    



# print("".join(map(str,len_and_name(list1))))
# cout = 1
# for i in range(len(c)-1):
#     if i <= len(c):
#         if c[i] == c[i + 1]:
#             cout += 1
#         else:
#             a = c[i]
#             print(cout, c[i])
#             cout = 1
# print(cout, c[i])