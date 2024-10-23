import random
# Task 1
def taskOne():
    age = int(input("Напишите Ваш возраст: "))
    if age < 18:
        print("Доступ запрещен")
    elif 18 <= age <= 25:
        print("Добро пожаловать, молодой гость")
    elif 25 < age <= 60:
        print("Добро пожаловать в клуб")
    elif age > 60:
        print("Будьте осторожны, пожалуйста")
    elif age > 100:
        print("Да вы долгожитель!!!")
    else: 
        print("Попробуете существующий возраст ввести")

# Task 2
def taskTwo():
    arrayOfTemerature = []

    for _ in range(7):
        temperature = float(input(f"Пожалуйста, введи температуру на {_ + 1} день в градусах Цельсия: "))
        arrayOfTemerature.append(temperature)

    averageTemperature = sum(arrayOfTemerature)/len(arrayOfTemerature)

    print("Минимальная температура на этой неделе: ", min(arrayOfTemerature))
    print("Максимальная температура на этой неделе: ", max(arrayOfTemerature))

    if averageTemperature < 0:
        print("Зимняя одежда вам к лицу.")
    elif 0 <= averageTemperature < 10:
        print("Осенняя одежда вам к лицу.")
    elif 10 <= averageTemperature < 20:
        print("Весенняя одежда вам к лицу.")
    else:
        print("Одежда будем лишним.")

# Task 3
def taskThree():
    days = int(input("Сколько осталось до прибытия Деда Мороза? "))
    while days > 1:
        print(f"Осталось {days} дня до Нового года!")
        days -= 1
    if days == 1:
        print("Завтра Новый год!")

# Task 4
def taskFour():
    number = int(input("Напишите то самое число, только никому не говорите: "))
    for _ in range(1,11):
        print(f"{number} * {_} = {number * _}", end = ", " if _ < 10 else ".")

# Task 5
def taskFive():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    yourMessage = input("Напиши свой самый большой секрет: ")
    encryptedMessage = ""

    for _ in yourMessage:
        if _ in alphabet:
            indexOfLetter = alphabet.index(_)
            if indexOfLetter == len(alphabet) - 1:
                encryptedMessage += alphabet[0]
            else:
                encryptedMessage += alphabet[indexOfLetter + 1]
        else:
            encryptedMessage += _

    print("Я так и знал, что ты", encryptedMessage)

# Task 6
def taskSix():
    input("Введите ваш пароль от скрытой вкладки в галерее))): ")
    password = input()
    psIsDigit = False
    psISupper = False
    psSpecial = False
    special_characters = "!@#$%^&*()-_=+[]{};:'\"\\|,.<>?/`~"

    if len(password) < 8:
        print("Пароль должен содержать не менее 8 символов.")
        return False

    for char in password:
        if char.isdigit():
            psIsDigit = True
        elif char.isupper():
            psISupper = True
        elif char in special_characters:
            psSpecial = True
    
    if not psIsDigit:
        print("Пароль должен содержать хотя бы одну цифру по-братски.")
    if not psISupper:
        print("Пароль должен содержать хотя бы одну заглавную букву по-братски.")
    if not psSpecial:
        print("Пароль должен содержать хотя бы один специальный символ по-братски.")

    if psIsDigit and psISupper and psSpecial:
        print("Пароль прошел проверку, красачик!")
        return True
    else:
        print("Пароль не прошел проверку. Пожалуйста, улучшите его по-братски.")
        return False

# Task 7
def taskSeven(text):
    total_characters = len(text)
    
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    vowel_count = sum(1 for char in text if char in vowels)

    words = text.split()

    unique_words = set(words)

    print(f"Общее количество символов (включая пробелы): {total_characters}")
    print(f"Количество гласных букв: {vowel_count}")
    print("Слова в тексте:")
    for word in words:
        print(word)
    
    print("Уникальные слова в тексте:")
    for unique_word in unique_words:
        print(unique_word)

# user_text = input("Введите текст: ")
# taskSeven(user_text)

# Task 8
def taskEight():
    numbers = list(map(int, input("Введи 5 чисел через пробел: ").split()))

    print("Исходный список:", numbers)
    random.shuffle(numbers)
    print("Перемешанный список:", numbers)
    print("Наибольшее число в перемешанном списке:", max(numbers))
    print("Наименьшее число в перемешанном списке:", min(numbers))

# Task 9
def taskNine():
    tasks = []
    for i in range(5):
        task = input(f"Введите задачу {i + 1}: ")
        tasks.append(task)

    while True:
        print("\nСписок задач:")
        # for index, task in enumerate(tasks, start=1):
        #     print(f"{index}. {task}")

        for index in range(len(tasks)):
            print(f"{index + 1} {tasks[index]}")
    
        choice = int(input("Введите номер задачи для удаления: "))


        task_index = choice - 1 
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            if(len(tasks) >= 1):
                print(f"Задача '{removed_task}' удалена.")
            else:
                print(f"Задачи закончились.")
                break
        else:
                print("Некорректный номер задачи. Попробуйте еще раз.")

        print("\nОставшиеся задачи:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Task 10
def taskTen():
    while True:
        try:
            distance = float(input("Введите расстояние, пройденное на автомобиле (в километрах): "))
            fuel_used = float(input("Введите количество потраченного топлива (в литрах): "))
            break 
        except ValueError:
            print("Пожалуйста, введите корректные числовые значения.")

    fuel_consumption = (fuel_used / distance) * 100
    print(f"Средний расход топлива: {fuel_consumption:.2f} литров на 100 км")

    if fuel_consumption > 10:
        print("Расход топлива превышает 10 литров на 100 км. Пожалуйста, сократите расход.")

    vehicle_type = input("Какой у вас тип автомобиля (малолитражка, средний, внедорожник)? ").lower()

    if vehicle_type == "малолитражка":
        print("Нормы расхода топлива для малолитражки: до 5 литров на 100 км.")
    elif vehicle_type == "средний":
        print("Нормы расхода топлива для среднего автомобиля: до 8 литров на 100 км.")
    elif vehicle_type == "внедорожник":
        print("Нормы расхода топлива для внедорожника: до 12 литров на 100 км.")
    else:
        print("Неизвестный тип автомобиля. Пожалуйста, введите малолитражка, средний или внедорожник.")

# Task 11
def taskEleven():
    income = float(input("Введите ваш ежемесячный доход: "))

    expense_categories = ['Продукты', 'Транспорт', 'Развлечения', 'Жилищные расходы', 'Коммунальные услуги']
    expenses = {}

    print("Введите ваши ежемесячные расходы по категориям:")
    for category in expense_categories:
        while True:
            expense = float(input(f"{category}: "))
            expenses[category] = expense
            break

    total_expenses = sum(expenses.values())
    balance = income - total_expenses

    print(f"\nОбщий доход: {income} руб.")
    print(f"Общие расходы: {total_expenses} руб.")
    print(f"Остаток: {balance} руб.")

    if balance < 0:
        suggestions = [
            "Уменьшите траты на развлечения.",
            "Сократите расходы на транспорт.",
            "Пересмотрите расходы на продукты.",
            "Попробуйте экономить на коммунальных услугах.",
            "Сократите ненужные расходы."
        ]
        suggestion = random.choice(suggestions)
        print(f"Совет: {suggestion}")

    annual_savings = balance * 12
    if annual_savings < 0:
        print("К сожалению, вы не сможете накопить деньги за год.")
    else:
        print(f"Если остаток останется таким же, вы сможете накопить {annual_savings} руб. за год.")

# Task 12
def taskTwelve():
    steps_per_day = []

    for i in range(7):
        while True:            
            steps = int(input(f"Введите количество шагов за день {i + 1}: "))
            steps_per_day.append(steps)
            break

    total_steps = sum(steps_per_day)
    average_steps = total_steps / len(steps_per_day)

    print(f"\nОбщее количество шагов за неделю: {total_steps}")
    print(f"Среднее количество шагов в день: {average_steps:.2f}")

    if any(steps > 10000 for steps in steps_per_day):
        print("Поздравляем! Вы прошли более 10,000 шагов в один из дней.")

    calories_burned = total_steps * 0.05
    print(f"Общее количество сожженных калорий: {calories_burned:.2f} калорий.")