# TODO Напишите функцию find_common_participants
# TODO Проверьте работу функции с разделителем отличным от запятой

def find_common_participants(group1, group2, separator=','):
  participants1 = set(group1.split(separator))
  participants2 = set(group2.split(separator))
  common_participants = participants1.intersection(participants2)

  return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(common_participants)

participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

common_participants_comma = find_common_participants(participants_first_group_comma, participants_second_group_comma)
print(common_participants_comma)