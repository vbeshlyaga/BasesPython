# Task 1
mathOperations = {
    '*': lambda x,y: x * y,
    '/': lambda x,y: x / y if y != 0 else 'Делить на 0 нельзя!!!!!!!!!!',
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y
}
def getNumbers():
    try:
        x = float(input("Введите Ваше первое число: "))
        y = float(input("Введите Ваше второе число: "))
        operation = input("Введите операцию (например, +, -, *, /): ")

        if operation in mathOperations:
            result = mathOperations[operation](x, y)
            print(result)
    except ValueError:
        print("Что-то пошло не так")

def newOperation():
    new_symbol = input("Введите символ новой операции: ")

    if new_symbol in mathOperations:
        print("Такая операция уже существует.")
        return
    
    code = input(f"Введите выражение для операции с переменными 'x' и 'y' (например, 'x ** y' для возведения в степень): ")

    try:
        compiled_code = compile(f"lambda x, y: {code}", "<string>", "eval")
        mathOperations[new_symbol] = eval(compiled_code)
        print(f"Операция '{new_symbol}' успешно добавлена!")
    except Exception as e:
        print(f"Ошибка при добавлении новой операции: {e}") 
    
def showListOfMathOperations():
    for _ in mathOperations:
        print(_)

def taskOne():
    while True:
        print("\nМеню:")
        print("1. Выполнить операцию")
        print("2. Добавить новую операцию")
        print("3. Показать доступные операции")
        print("4. Выход")

        choice = int(input("Выберите действие: "))
        match choice:
            case 1:
                getNumbers()
            case 2:
                newOperation()
            case 3:
                showListOfMathOperations()
            case 4:
                print("Выход из программы")
                break


# Task 2
def taskTwo():
    students = [
        ('Алиса', 85),
        ('Борис', 90),
        ('Виктор', 78),
        ('Галина', 92),
        ('Денис', 88)
    ]

    def sort_students(students, grow=True):
        return sorted(students, key=lambda student: student[1], reverse=not grow)

    print("Список студентов до сортировки:")
    for student in students:
        print(f"{student[0]}: {student[1]}")

    order = input("Введите '>' для сортировки по возрастанию или '<' для сортировки по убыванию: ")

    inputGrow = True if order == '>' else False

    sorted_students = sort_students(students, grow=inputGrow)

    print("\nСписок студентов после сортировки:")
    for student in sorted_students:
        print(f"{student[0]}: {student[1]}")


# Task 3
counter = 0
def getCounter():
    global counter
    counter += 1
    print(f"Функцию вызвали {counter} раз")

def resetCounter():
    global counter
    counter = 0
    print("Счетчик был сброшен на ноль.")

def taskThree():
    while True:
        print("\nМеню:")
        print("1. Вызвать функцию-счетчик")
        print("2. Сбросить счетчик")
        print("3. Выход")
        
        choice = input("Выберите действие (1/2/3): ")

        if choice == "1":
                number = int(input("Сколько раз хотите вызвать функцию: "))
                for _ in range(number):
                    getCounter()
        if choice == "2":
                resetCounter()
        if choice == "3":
                print("Выход из программы.")
                break


# Task 4
def sales(prices, discountFunction):
    return [discountFunction(price) for price in prices]

def taskFour():
    prices = list(map(float, input("Введите через пробел цену на Ваши товары и нажмите Enter: ").split()))

    print("Начальные цены товаров:", prices)

    print("\nВыберите тип скидки:")
    print("1. Скидка 10%")
    print("2. Скидка 20%")
    print("3. Скидка 50 рублей на каждую покупку")
    print("4. Скидка 15%, если товар дороже 200 рублей, иначе 5%")

    choice = input("Введите номер скидки (1/2/3/4): ")

    if choice == '1':
        discountFunction = lambda price: price * 0.9
    elif choice == '2':
        discountFunction = lambda price: price * 0.8
    elif choice == '3':
        discountFunction = lambda price: price - 50 if price > 51 else price * 1 
    elif choice == '4':
        discountFunction = lambda price: price * 0.85 if price > 200 else price * 0.95
    else:
        print("Ошибка: неверный выбор.")
        return
    
    final_prices = sales(prices, discountFunction)
    print("\nЦены товаров после применения скидки:", final_prices)


# Task 5
exchange_rates = {
    "USD": 75,
    "EUR": 90,
    "GBP": 105,
    "JPY": 0.55,
    "CNY": 10.5,
    "AUD": 50,
    "CAD": 52,
    "CHF": 82,
    "INR": 1.0,
}

def convert_currency(amount, currency):

    if currency in exchange_rates:
        return amount / exchange_rates[currency]
    else:
        print(f"Ошибка: Валюта '{currency}' не найдена.")
        return None

def update_exchange_rate(currency, rate):
    exchange_rates[currency] = rate
    print(f"Курс валюты '{currency}' обновлен на {rate}.")

def add_currency(currency, rate):
    exchange_rates[currency] = rate
    print(f"Валюта '{currency}' добавлена с курсом {rate}.")

def remove_currency(currency):
    if currency in exchange_rates:
        del exchange_rates[currency]
        print(f"Валюта '{currency}' удалена.")
    else:
        print(f"Ошибка: Валюта '{currency}' не найдена.")

def taskFive():
    while True:
        print("\nМеню:")
        print("1. Конвертировать рубли в валюту")
        print("2. Обновить курс валюты")
        print("3. Добавить новую валюту")
        print("4. Удалить валюту")
        print("5. Посмотреть текущие курсы валют")
        print("6. Выход")
        
        choice = input("Выберите действие (1/2/3/4/5/6): ")
        
        if choice == '1':
            amount = float(input("Введите сумму в рублях: "))
            currency = input("Введите валюту для конвертации: ").upper()
            converted_amount = convert_currency(amount, currency)
            print(f"{amount} рублей = {converted_amount:.2f} {currency}")

        elif choice == '2':
            currency = input("Введите валюту для обновления курса: ").upper()
            rate = float(input("Введите новый курс: "))
            update_exchange_rate(currency, rate)

        elif choice == '3':
            currency = input("Введите новую валюту: ").upper()
            rate = float(input("Введите курс новой валюты: "))
            add_currency(currency, rate)

        elif choice == '4':
            currency = input("Введите валюту для удаления: ").upper()
            remove_currency(currency)

        elif choice == '5':
            print("Текущие курсы валют:")
            for currency, rate in exchange_rates.items():
                print(f"{currency}: {rate} рублей")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Ошибка: Неверный выбор. Пожалуйста, выберите снова.")


# Task 6
def find_duplicates(users):
    unique_users = set()
    duplicates = set()

    for user in users:
        if user in unique_users:
            duplicates.add(user)
        else:
            unique_users.add(user)
    
    if duplicates:
        print("Найдены дубликаты:", ", ".join(duplicates))
    else:
        print("Дубликатов не найдено.")
    return list(unique_users)

def remove_duplicates(users):
    return list(set(users))

def taskSix():
    while True:
        user_list = input("Введите имена пользователей через запятую: ").split(",")
        user_list = [user.strip() for user in user_list]
        unique_users = find_duplicates(user_list)
        
        print("Список без дубликатов:", unique_users)

        repeat = input("Хотите ввести новый список? (да/нет): ").lower()
        if repeat != "да":
            break


# Task 7
menu = (
    ("Паста", 500),
    ("Салат", 300),
    ("Суп", 400),
    ("Бургер", 600),
    ("Пицца", 700),
)

menu_list = list(menu)

def show_menu(menu):
    print("\nТекущее меню:")
    for dish, price in menu:
        print(f"{dish}: {price} руб.")
    print("\n")

def filter_by_budget(budget, menu):
    affordable_dishes = list(filter(lambda x: x[1] <= budget, menu))
    
    if affordable_dishes:
        print(f"Вы можете позволить себе следующие блюда:")
        for dish, price in affordable_dishes:
            print(f"{dish}: {price} руб.")
    else:
        print(f"К сожалению, на ваш бюджет нет доступных блюд.")

def add_dish(menu_list):
    dish_name = input("Введите название нового блюда: ")
    dish_price = int(input("Введите стоимость блюда: "))
    menu_list.append((dish_name, dish_price))
    print(f"Блюдо '{dish_name}' добавлено с ценой {dish_price} руб.")

def update_dish_price(menu_list):
    dish_name = input("Введите название блюда, цену которого нужно обновить: ")
    for i, (name, price) in enumerate(menu_list):
        if name == dish_name:
            new_price = int(input(f"Введите новую стоимость для блюда '{dish_name}': "))
            menu_list[i] = (dish_name, new_price)
            print(f"Цена блюда '{dish_name}' обновлена до {new_price} руб.")
            break
    else:
        print(f"Блюдо с названием '{dish_name}' не найдено в меню.")

def taskSeven():
    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Показать меню")
        print("2. Показать блюда, которые вы можете позволить себе на ваш бюджет")
        print("3. Добавить новое блюдо")
        print("4. Обновить стоимость блюда")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            show_menu(menu_list)
        elif choice == "2":
            budget = int(input("Введите ваш бюджет: "))
            filter_by_budget(budget, menu_list)
        elif choice == "3":
            add_dish(menu_list)
        elif choice == "4":
            update_dish_price(menu_list)
        elif choice == "5" or choice.lower() == "выход":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 5.")



# Task 8
def uniqueWord(message):
    words = message.split()
    return len(set(words))

def taskEight():
    while True:
        message = input('Введите Ваше сообщение без специальных символов: ')
        result = uniqueWord(message)
        print(result)


# Task 9
def display_products(products):
    if not products:
        print("Список продуктов пуст.")
        return
    print("\nСписок продуктов и их цены:")
    for product, price in products.items():
        print(f"{product}: {price} руб.")

def search_product(products, product_name):
    price = products.get(product_name)
    if price is not None:
        print(f"Цена '{product_name}': {price} руб.")
    else:
        print(f"Продукт '{product_name}' не найден.")

def edit_product_price(products, product_name, new_price):
    if product_name in products:
        products[product_name] = new_price
        print(f"Цена продукта '{product_name}' обновлена до {new_price} руб.")
    else:
        print(f"Продукт '{product_name}' не найден.")

def delete_product(products, product_name):
    if product_name in products:
        del products[product_name]
        print(f"Продукт '{product_name}' удалён.")
    else:
        print(f"Продукт '{product_name}' не найден.")

def add_product(products, product_name, price):
    products[product_name] = price
    print(f"Продукт '{product_name}' добавлен с ценой {price} руб.")

def taskNine():
    products = {}

    while True:
        print("\nВыберите действие:")
        print("1. Добавить продукт")
        print("2. Искать продукт")
        print("3. Редактировать цену продукта")
        print("4. Удалить продукт")
        print("5. Вывести весь список продуктов")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Введите название продукта: ")
            price = float(input("Введите цену продукта: "))
            add_product(products, name, price)

        elif choice == "2":
            name = input("Введите название продукта для поиска: ")
            search_product(products, name)

        elif choice == "3":
            name = input("Введите название продукта для редактирования: ")
            new_price = float(input("Введите новую цену продукта: "))
            edit_product_price(products, name, new_price)

        elif choice == "4":
            name = input("Введите название продукта для удаления: ")
            delete_product(products, name)

        elif choice == "5":
            display_products(products)

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 6.")


# Task 11
def read_sales_data(filename):
    sales = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            product, quantity, price = line.strip().split('-')
            quantity, price = int(quantity), float(price)
            
            sales[product] = sales.get(product, 0) + quantity * price
    return sales

def write_new_sale(filename, product, quantity, price):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{product}-{quantity}-{price}\n")

def taskEleven():
    filename = './files/lab_3_task_11.txt'
    
    sales = read_sales_data(filename)
    
    if sales:
        max_product = max(sales, key=sales.get)
        min_product = min(sales, key=sales.get)
        print("Общая сумма продаж по продуктам:")
        for product, total in sales.items():
            print(f"{product}: {total:.2f}")
        print(f"\nПродукт с наибольшей суммой продаж: {max_product} ({sales[max_product]:.2f})")
        print(f"Продукт с наименьшей суммой продаж: {min_product} ({sales[min_product]:.2f})")
    else:
        print("Данные о продажах отсутствуют.")
    
    add_more = input("\nХотите добавить новую запись о продаже? (да/нет): ").strip().lower()
    if add_more == 'да':
        product = input("Введите название продукта: ")
        quantity = int(input("Введите количество: "))
        price = float(input("Введите цену: "))
        write_new_sale(filename, product, quantity, price)
        print("Новая запись добавлена. Пересчитываем суммы продаж.")

taskEleven()

# Task 12
def taskTwelve():
    search_word = input("Введите слово для поиска: ").lower()

    occurrences = 0
    matching_lines = []


    with open('./files/lab_3_task_12.txt', 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if search_word in line.lower():
                occurrences += line.lower().count(search_word)
                matching_lines.append(f"Строка {line_number}: {line.strip()}")


    print(f"Количество вхождений слова '{search_word}': {occurrences}")
    if occurrences > 0:
        print("Строки, содержащие это слово:")
        for match in matching_lines:
            print(match)
    else:
        print("Слово не найдено в файле.")


# Task 13
def taskThirteen():
    with open('./files/lab_3_task_13.txt', 'r', encoding='utf-8') as original_file:
        lines = [line.strip() for line in original_file]

    with open('./files/lab_3_task13_reversed.txt', 'w', encoding='utf-8') as reversed_file:
        for line in reversed(lines):
            reversed_file.write(line + '\n')

    print("Файл успешно создан с перевернутыми строками.")

