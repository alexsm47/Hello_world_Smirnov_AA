a = input("ФИО исследователя: ")
b = input("Дата: ")
c = input("название эксперимента: ")
d = input("Вывод: ")

with open("journal.txt", "w", encoding = "utf-8") as file:
    file.write(f"Электронный лабораторный журнал\n")
    file.write(f"ФИО исследователя: {a}\n")
    file.write(f"Дата: {b}\n")
    file.write(f"название эксперимента:  {c}\n")
    file.write(f"Вывод: {d}\n")