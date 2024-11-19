a = int(input("Введите расстояние между рядами: "))
b = int(input("Введите расстояние между дырочками в ряду: "))
L = int(input("Введите длину свободного конца шнурка: "))
N = int(input("Введите количество дырочек в каждом ряду: "))

# Расчет длины шнурка
free_end_length = 2 * L   # Длина свободного конца шнурка
first_row_length  = (2 * N - 1) * a  # Длина веревки для заполнения первого ряда
second_row_length = 2 * (N - 1) * b  # Длина веревки для заполнения второго ряда

total_length = free_end_length + first_row_length + second_row_length

print(f"Общая длина шнурка: {total_length}")