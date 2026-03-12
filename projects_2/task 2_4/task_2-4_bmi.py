weight = float(input("Введите вес (кг): "))
hight = float(input("Введите рост (м): "))
bmi = weight / (hight*2)

print(f"Введите вес: {weight}(кг)\n Введите рост: {hight}(м)\n\n Отчет о состоянии здоровья\n Рост: {hight}\n Вес: {weight}\n Индекс массы тела: {bmi}")