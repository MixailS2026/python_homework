def month_to_season(month):
    if 1 <= month <= 3:
        return "Зима"
    if 4 <= month <= 6:
        return "Весна"
    if 7 <= month <= 9:
        return "Лето"
    if 10 <= month <= 12:
        return "Осень"
    return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))
