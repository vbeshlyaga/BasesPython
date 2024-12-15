import math
import json


# Task 1
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __gt__(self, other):
        return self.length() > other.length()

    def __len__(self):
        return int(self.length())

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


def taskOne():
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print('v1 + v2:', v1 + v2)
    print('v1 - v2:', v1 - v2)
    print('v1 * 3:', v1 * 3)
    print('v1 > v2:', v1 > v2)
    print('Длина v1:', len(v1))


# Task 2
class Figure:
    def area(self):
        raise NotImplementedError('Этот метод должен быть переопределен в подклассах.')


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def taskTwo():
    shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
    for shape in shapes:
        print(f'{shape.__class__.__name__} area: {shape.area()}')


# Task 3
class User:
    def __init__(self, user_id, name, email, age):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        return f'{self.user_id}, {self.name}, {self.email}, {self.age}'

    def to_dict(self):
        return {'id': self.user_id, 'name': self.name, 'email': self.email, 'age': self.age}


class FileManager:
    FILE_NAME = 'files/users.txt'

    @staticmethod
    def load_users():
        try:
            with open(FileManager.FILE_NAME, 'r') as file:
                return [User(**user) for user in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def save_users(users):
        with open(FileManager.FILE_NAME, 'w') as file:
            json.dump([user.to_dict() for user in users], file)


def taskThree():
    users = FileManager.load_users()

    while True:
        print('\n1. Добавление нового пользователя\n2. Удаление пользователя по id\n3. Редактирование информации\n4. Просмотр списка всех пользователей\n5. Exit')
        choice = input('Choose an option: ')

        if choice == '1':
            name = input('Введите имя: ')
            email = input('Введите email: ')
            age = int(input('Введите возраст: '))
            user_id = len(users) + 1
            users.append(User(user_id, name, email, age))
            FileManager.save_users(users)
            print('Пользователь добавлен.')

        elif choice == '2':
            user_id = int(input('Введите ID пользователя для удаления: '))
            users = [user for user in users if user.user_id != user_id]
            FileManager.save_users(users)
            print('Пользователь удален.')

        elif choice == '3':
            user_id = int(input('Введите ID пользователя для изменения: '))
            for user in users:
                if user.user_id == user_id:
                    user.name = input('Введите новое имя: ')
                    user.email = input('Введите новый email: ')
                    user.age = int(input('Введите новый возраст '))
                    break
            FileManager.save_users(users)
            print('Данные пользователя обновлены.')

        elif choice == '4':
            for user in users:
                print(user)

        elif choice == '5':
            break


# Task 4
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f'{self.name} ({self.category}) - ${self.price}'


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def total(self):
        return sum(product.price for product in self.products)


def taskFour():
    cart = Cart()
    p1 = Product('Laptop', 1000, 'Electronics')
    p2 = Product('Book', 20, 'Education')
    p3 = Product('Phone', 500, 'Electronics')

    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)
    print('Общая стоимость корзины: ', cart.total())
    cart.remove_product(p2)
    print('Итоговая стоимость', cart.total())


# Запуск задач
taskOne()
taskTwo()
taskThree()
taskFour()