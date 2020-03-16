
"""
Реалізуйте підпрограму сортування масиву.
"""

N = 1000000  # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """

    if len(array) > 1:     
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        sort(left)
        sort(right)

        i, j, k = 0, 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


from random import randint

arr = []
for i in range(0, 100000):
    randnum = randint(0, 10000)
    arr.append(randnum)

sort(arr)
print(arr[0:100])
    
    

