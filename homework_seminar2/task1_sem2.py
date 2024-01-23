# На вход подается число n.
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# Пример вывода:

# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result = i * j
            print(f"{i} * {j} = {result}")
        print('')


n = int(input("Введите число N: "))
multiplication_table(n)


# Здесь присутствует и процедурная и структурная парадигмы.
# Структурная парадигма, поскольку она предполагает использование цикла for.
# Процедурная парадигма - код оформлен в виде процедуры multiplication_table().

