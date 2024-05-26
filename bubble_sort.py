def bubble_sort(sequence):
    # Проходимо по кожному елементу в послідовності
    for counter in range(len(sequence)):
        # Проходимо по елементах, які ще не відсортовані
        for index in range(len(sequence) - counter - 1):
            # Якщо поточний елемент більший за наступний
            if sequence[index] > sequence[index+1]:
                # Міняємо їх місцями
                sequence[index], sequence[index+1] = sequence[index+1], sequence[index]
        # Друкуємо послідовність після кожного проходу
        print(sequence)
    # Повертаємо відсортовану послідовність
    return sequence

if __name__ == "__main__":
    # Задаємо список, який потрібно відсортувати
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    # Викликаємо функцію сортування і друкуємо відсортований список
    print(bubble_sort(to_sort))
