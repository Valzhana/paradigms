# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] < item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    return nums


list_of_nums = [9, 1, 15, 28, 6]
result = sort_list_imperative(list_of_nums)
print(result)


# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(nums):
    return sorted(nums, reverse=True)


list_of_nums = [1, 1, 7, 28, 6]
result = sort_list_declarative(list_of_nums)
print(result)
