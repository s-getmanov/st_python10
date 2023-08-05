# Ссылка на github
#https://github.com/s-getmanov/st_python10.git

pets = {}

#Запустим безконечный цикл для ввода данных о питомцах. 
#
while True:

    command = input("Введите команду(n - добавить питомца, r - редактировать данные, p - вывести данные питомцев на экран, q - выход):")

    if not command in "nrpq":
        print("Неверная команда!")
        continue
 
    if command == "q":
        break
    elif command == "n" or  command == "r":
        pet_name = input("Введите имя питомца:")

    #Обработаем ошибочные ситуации
    if command == "n" and pet_name in pets:
        print(f"Питомец с именем {pet_name} уже добавлен ранее! Для редактирования используйте команду r")
        continue
    if command == "r" and not pet_name in pets:
        print(f"Питомец с именем {pet_name} отсутствует в списке! Для добавления используйте команду n")
        continue
    
    #Обработка команд  
    if command == "p":

        for pet_name in pets:

            # Сформируем окончание для слова год
            ending = ""
            if pets[pet_name]['Возраст питомца'] % 10 == 1 and pets[pet_name]['Возраст питомца'] != 11:
                ending = 'год'
            elif 2 <= pets[pet_name]['Возраст питомца'] % 10 <= 4 and not (12 <= pets[pet_name]['Возраст питомца'] <= 14):
                ending = 'года'
            else:
                ending = 'лет'
    
            print(f"Это {pets[pet_name]['Вид питомца']} по кличке {pet_name}. Возраст питомца: {pets[pet_name]['Возраст питомца']} {ending}. Имя владельца: {pets[pet_name]['Имя владельца']}")
        continue
    
    if command == "n":

        pets[pet_name] = {
                           "Вид питомца":"",
                           "Имя владельца:":"", 
                           "Возраст питомца":0,
                           } 
        
        current_pet = pets[pet_name]
        current_pet["Вид питомца"] = input(f"Введите вид питомца:")  
        current_pet["Имя владельца"]  = input("Имя владельца:")   
        current_pet["Возраст питомца"] = int(input("Возраст питомца:"))     

    elif  command == "r":  

        current_pet = pets[pet_name]  

        input_data = input(f"Введите вид питомца (текущее значение {current_pet['Вид питомца']}):")
        if not input_data == "":
            current_pet["Вид питомца"] = input_data

        input_data = input(f"Имя владельца (текущее значение {current_pet['Имя владельца']}):")
        if not input_data == "":
             current_pet["Имя владельца"] = input_data

        input_data = input(f"Возраст питомца (текущее значение {current_pet['Возраст питомца']}):")
        if not input_data == "":
           current_pet["Возраст питомца"] = int(input_data)

    
     



 

   




