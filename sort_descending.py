# Сортировки чисел в списке в порядке убывания.

# Процедура в императивном стиле.
def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# Процедура в декларативном стиле.
def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

numbers = [5, 2, 8, 1, 3]
print(sort_list_imperative(numbers))
print(sort_list_declarative(numbers))
