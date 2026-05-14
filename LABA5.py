import itertools


seq1 = [1, 2]
seq2 = ['a', 'b']
seq3 = [True, False]


combinations = itertools.product(seq1, seq2, seq3)

# Применяем map
mapped = map(lambda combo: f"{combo[0]}-{combo[1]}-{combo[2]}", combinations)

total = len(seq1) * len(seq2) * len(seq3)
print(f"Общее число комбинаций: {total}")

print("Результат применения map (строка):")
for item in list(mapped)[:5]:
    print(item)
