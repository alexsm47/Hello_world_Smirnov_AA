seq = ["ATATAGATGTCTGA", "ATCGTGTGCAGCTGCTAGCG"]
for letter in seq:
    print(f"Последовательность целиком: \n {letter} \n Последовательность построчно:")
    for nucl in letter:
            print(nucl)
    print()
print("Цикл выполнен")
