n = int(input())
k = int(input())

# Количество яблок на каждого школьника
slash = n // k

# Количество оставшихся яблок в корзинке
percentage = n % k

print(slash)
print(percentage)