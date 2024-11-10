import random

n = int(input("Masukan Nilai N:"))

for i in range(1, n):
    a = random.uniform(0, 0.5)
    print(f"data ke {i}: {a}")
    
