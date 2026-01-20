# TODO Напишите функцию для поиска индекса товара
def find_item_index(items, target):
    """
    Находит индекс первого вхождения товара в списке.

    Args:
        items (list): Список товаров
        target (any): Товар, который нужно найти

    Returns:
        int or None: Индекс первого вхождения товара или None, если товар не найден
    """
    for i, item in enumerate(items):
        if item == target:
            return i
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции поиска
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
