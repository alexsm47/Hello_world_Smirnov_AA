concentrite_of_substance = input("Введите название питательной среды: ")
concentere_of_agaragar = input("Ведите концентрацию агар-агара в %: ")
temperature_for_sterilization = input("Температура стерилизации: ")

with open("recipe.txt", "w", encoding = "utf-8") as file:
    file.write(f"Введите название питательной среды: {concentrite_of_substance}\n")
    file.write(f"Ведите концентрацию агар-агара в %: {concentere_of_agaragar}\n")
    file.write(f"Температура стерилизации {temperature_for_sterilization}")
print("Файл 'recipe.txt' успешно сохранен!")