# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(participants_first_group, participants_second_group, r=','):
    list1 = []  # Новый список общих участников
    list1 = participants_first_group.split(r)  # Разбиваем строку по указанному разделителю
    list2 = participants_second_group.split(r)  # Разбиваем строку по указанному разделителю
    s1 = set(list1)
    s2 = set(list2)

    # пересечения
    set1 = s1.intersection(s2)

    # Converts resulting set to list
    list1 = list(set1)
    list1 = sorted(list1)
    return list1

# TODO Провеьте работу функции с разделителем отличным от запятой
n = find_common_participants(participants_first_group, participants_second_group, r='|')
print(n)
