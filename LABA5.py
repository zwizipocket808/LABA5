import itertools


seq1 = [1, 2]
seq2 = ['a', 'b']
seq3 = [True, False]

def combo_generator (s1, s2, s3):
    for a in s1:
        for b in s2:
            for c in s3:
                yield ( a, b, c)
                
combinations = combo_generator(seq1, seq2, seq3)
mapped = map(lambda combo: f"{combo [0]}-{combo[1]}-{combo[2]}", combinations)

total = len(seq1) * len(seq2) * len(seq3)
print(f"Общее число кеомбинаций: {total}")

print ("Результат применения map (первые 5 строк):")

from itertools import islice 
for item in islice ( mapped, 5):
    print(item)
g = combo_generator(seq1, seq2,seq1)
print ( next(g))
