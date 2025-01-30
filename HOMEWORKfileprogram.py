exit = 0
filename = "standart.txt"
text = "dara"

while exit != 1:
    print('Доброго времени суток')
    print('1. Записать текст в файл 2. Прочитать 3. стереть текст 4. выход 5. подробнее')
    user_choose = int(input())
    if user_choose == 1:
        with open(filename, 'a') as file:
            file.write(text)
            print('Файл записан')
    elif user_choose == 2:
        try:
            with open(filename, "r") as file:
                for filename in file:
                    print(filename, end="")
            print()
        except FileNotFoundError:
            print('Для начала, создайте файл перед тем как прочитать его')
    elif user_choose == 3:
        with open(filename, 'w') as file:
            new_text = text.replace(text, '')
            file.write(new_text)
    elif user_choose == 4:
        exit += 1
    elif user_choose == 5:
        print('Я создал очень много подобных программ, работающих по такому принципу как вы этом задании')
        print('Настолько много, что я уже устал делать замороченную менюшку')
