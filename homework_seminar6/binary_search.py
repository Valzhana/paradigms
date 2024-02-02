# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.


from typing import List


def binary_search(arr: List[int], number: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    arr = [1, 2, 7, 6, 11, 33, 45]

    print(f"Source array: {arr}")
    number = int(input("Enter the element: "))
    result = binary_search(arr, number)

    if result == -1:
        print("There is no such element in the array")
    else:
        print(f"The element: {number}, index: {result}")


if __name__ == "__main__":
    main()
