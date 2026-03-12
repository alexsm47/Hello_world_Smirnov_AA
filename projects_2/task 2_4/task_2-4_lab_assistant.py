a = int(input("Введите нужный объем раствора (мл): "))

b = a *0.009
c = round(b, 2)

with open("recipe2.txt", "w", encoding = "utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write(f"Общий объем: {a} мл\n")
    file.write(f"Масса соли = {c} г \n")
    file.write(f"Объем воды: {a}")