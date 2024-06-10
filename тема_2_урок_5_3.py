sum = 100
ivan = int(input("Введите сумму Ивана:"))
mike = int(input("Введите сумму Майка:"))
both = mike + ivan
if both < sum:
    print("Результат - 2")
if both > sum:
    if mike or ivan < sum:
        print("Результат - 1")
        else:
        print("Результат - 0")

        #задача не доделана, потому не получается вывести только один результат и выдает какую-то ошибку