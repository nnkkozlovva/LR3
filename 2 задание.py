# TODO Напишите функцию find_common_participants

def find_common_participants(group1_str, group2_str, separator=","):
    """
    Находит общих участников среди двух групп.

    Args:
        group1_str (str): Строка с участниками первой группы
        group2_str (str): Строка с участниками второй группы
        separator (str, optional): Разделитель фамилий. По умолчанию ','

    Returns:
        list: Отсортированный список общих участников
    """
    # Разбиваем строки на списки участников
    group1_list = group1_str.split(separator)
    group2_list = group2_str.split(separator)

    # Находим пересечение множеств (общие элементы)
    common_participants = list(set(group1_list) & set(group2_list))

    # Сортируем результат в алфавитном порядке
    common_participants.sort()

    return common_participants


# Тест 1: Использование стандартного разделителя (запятая)
participants1_comma = "Иванов,Петров,Сидоров"
participants2_comma = "Петров,Сидоров,Смирнов"

common_comma = find_common_participants(participants1_comma, participants2_comma)
print(f"Общие участники (запятая как разделитель): {common_comma}")

# Тест 2: Использование вертикальной черты как разделителя (из примера)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызываем функцию с явным указанием разделителя
common_pipe = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator="|"
)
print(f"Общие участники (вертикальная черта как разделитель): {common_pipe}")

# Тест 3: Другие разделители
participants1_semicolon = "Иванов;Петров;Сидоров"
participants2_semicolon = "Петров;Сидоров;Смирнов"

common_semicolon = find_common_participants(
    participants1_semicolon,
    participants2_semicolon,
    separator=";"
)
print(f"Общие участники (точка с запятой как разделитель): {common_semicolon}")

# Тест 4: Без общих участников
group1 = "Иванов,Петров"
group2 = "Сидоров,Смирнов"
common_none = find_common_participants(group1, group2)
print(f"Общие участники (нет общих): {common_none}")

# Тест 5: Пустые группы
group_empty = ""
group_full = "Иванов,Петров"
common_empty = find_common_participants(group_empty, group_full)
print(f"Общие участники (одна группа пустая): {common_empty}")

# TODO Провеьте работу функции с разделителем отличным от запятой
