raw_input = input("Введите элементы массива через пробел: ").split()
A = [int(x) for x in raw_input if x.lstrip('-').isdigit()]

min_idx = A.index(min(A))
max_idx = A.index(max(A))

start = min(min_idx, max_idx) + 1
end = max(min_idx, max_idx)


negative_sum = sum(x for x in A[start:end] if x < 0)

print(f"\nРаспознанный массив чисел: {A}")
print(f"Сумма отрицательных элементов между ними: {negative_sum}")