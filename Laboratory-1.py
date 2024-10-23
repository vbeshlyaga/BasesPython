# Laboratory 1

# Task 1

name = input("Введите Ваше имя и нажмите Enter: ")
lastname = input("Введите Вашу фамилию и нажмите Enter: ")
profession = input("Введите Вашу профессию и нажмите Enter: ")

print("=" * 28, sep = '')
print('Имя:', name, end = '; \n')
print('Фамилия:', lastname, end = '; \n' )
print('Профессия:', profession, end = '. \n')
print("=" * 28, sep = '')


# Task 2

n = int(input("Введите количетво минут и нажмите Enter "))
if(n > 1440):
    print("Прошло больше сутки")
elif(n < 60):
    print("Количество минут: ", n)
else:
    hours = n//60
    minutes = n % 60
    print("Количество часов:", hours,"Количество минут:", minutes)


# Task 3

n = int(input("Введите трехзначное число и нажмите Enter: "))
while(n > 999 or n < 100):
    n = int(input("Введи ТРЕХЗНАЧНОЕ число и нажмите Enter: "))

sum_of_digits = n//100+ n % 10 + (n//10)%10
print("Сумма цифр равна:", sum_of_digits)


# Task 4

seconds = int(input("Введите количетво секунд и нажмите Enter "))

hours = (seconds // 3600) % 24
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(hours, minutes, seconds, sep = ':')


# Task 5

number = int(input("Введите целое цисло, не превышающее 1000 и нажмите Enter "))

print("Следующее за ним четное число:", number - number % 2 + 2)


# Task 6

startPoint = int(input("Введите координаты первой точки и нажмите Enter: "))
endPoint = int(input("Введите координаты второй точки и нажмите Enter: "))

distance = abs(startPoint - endPoint)
print("Расстояние между ними:", distance)


# Task 7

numbers = list(map(int, input("Введите четыре числа через пробел и нажмите Enter: ").split()))
average = 0
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print("Среднее арифметическое четырех введенных целых чисел", sum / len(numbers))


# Task 8

person = int(input("Введите количетсво пассажиров и нажмите Enter: "))
if person % 4 == 0:
    print("Придется вызвать", person // 4, "такси.")
else:
    print("Придется вызвать", person//4  + 1, "такси.")


# Task 9

separator = input("Введите разделитель и нажмите Enter: ")
result = ""

for i in range(1,6):
    result += str(i)
    if i < 5:
        result += separator

print(result)





