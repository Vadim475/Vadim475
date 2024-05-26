def insertion_sort(sequence):
    # Проходимо по елементах списку починаючи з другого (index = 1)
    for index in range(1, len(sequence)):
        # Зберігаємо позицію попереднього елемента
        position = index - 1
        # Зберігаємо поточне значення
        value = sequence[index]
        # Поки позиція більша або дорівнює 0 і значення на цій позиції більше поточного значення
        while position >= 0 and sequence[position] > value:
            # Зміщуємо елемент вправо
            sequence[position + 1] = sequence[position]
            # Переходимо до попередньої позиції
            position -= 1
        # Вставляємо поточне значення на правильне місце
        sequence[position + 1] = value
        # Друкуємо поточний стан списку після кожного проходу
        print(sequence)
    # Повертаємо відсортований список
    return sequence

if __name__ == "__main__":
    # Задаємо список, який потрібно відсортувати
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    # Викликаємо функцію сортування і друкуємо відсортований список
    print(insertion_sort(to_sort))
