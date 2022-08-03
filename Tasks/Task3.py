# Создайте программу для игры в ""Крестики-нолики"".




import tracemalloc 


def print_field (list):
    a = 0
    print('_____________')
    for i in range (0,3):
        print('|', end=' ')
        for j in range (0,3):
            print(list[a], end=' | ')
            a+=1
        print('\n_____________')


def hod(name, list):
    a = int(input(f'Куда ставим {name}?  '))
    if list[a-1] != 'X' and list[a-1] != 'O':
        if name == 'крестик':
            list[a-1] = 'X'
        else: list[a-1] = 'O'
    else: 
        print('Неверный ход')
        hod(name, list)
    return list


def check(list, name):
    if list[0]==list[1]==list[2]: 
        print(f'побеждает {name}') 
        return True
    elif list[3]==list[4]==list[5]:
        print(f'побеждает {name}') 
        return True
    elif list[6]==list[7]==list[8]:
        print(f'побеждает {name}') 
        return True
    elif list[0]==list[3]==list[8]:
        print(f'побеждает {name}') 
        return True
    elif list[1]==list[4]==list[7]:
        print(f'побеждает {name}') 
        return True
    elif list[2]==list[5]==list[8]:
        print(f'побеждает {name}') 
        return True
    elif list[0]==list[4]==list[8]:
        print(f'побеждает {name}') 
        return True
    elif list[2]==list[4]==list[6]:
        print(f'побеждает {name}') 
        return True
    else: return False


name = ['крестик', 'нолик', 'крестик', 'нолик', 'крестик', 'нолик', 'крестик', 'нолик', 'крестик']
desk = [1,2,3,4,5,6,7,8,9]

print_field(desk)


for i in range (0, len(name)):
    if check (desk, name[i]) == False:
        desk = hod(name[i], desk)
        print_field(desk)

# Некоторая ерунда с тем, кто побеждает (и с количеством строк в коде) Но игра хотя бы научилась заканчиваться.