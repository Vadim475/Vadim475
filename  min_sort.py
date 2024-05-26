def min_sort(sequence):
    # Створюємо новий порожній список для збереження відсортованих елементів
    result = list()
    
    # Проходимо по всіх елементах вхідного списку
    for counter in range(len(sequence)):
        # Знаходимо мінімальний елемент у списку
        min_element = min(sequence)
        # Знаходимо індекс мінімального елемента
        index_of_min = sequence.index(min_element)
        # Видаляємо мінімальний елемент з оригінального списку
        sequence.pop(index_of_min)
        # Додаємо мінімальний елемент до результатного списку
        result.append(min_element)
        
        # Альтернативний спосіб видалення та додавання мінімального елемента за один рядок:
        # result.append(sequence.pop(sequence.index(min(sequence))))
        
    # Повертаємо відсортований список
    return result

if __name__ == "__main__":
    # Задаємо список, який потрібно відсортувати
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    # Викликаємо функцію сортування і друкуємо відсортований список
    print(min_sort(to_sort))
