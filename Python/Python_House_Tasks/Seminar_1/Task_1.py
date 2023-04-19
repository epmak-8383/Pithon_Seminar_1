# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и выводит название этого дня недели.
 
weeks_day = int(input("Введите число: "))
if weeks_day == 1:
    print("Сегодня понедельник")
if weeks_day == 2:
   print("Сегодня вторник")
if weeks_day == 3:
   print("Сегодня среда")
if weeks_day == 4:
    print("Сегодня четверг")
if weeks_day == 5:
    print("Сегодня пятница")
if weeks_day == 6:
    print("Сегодня суббота")
if weeks_day == 7:
    print("Сегодня воскресенье")
if weeks_day < 1 or weeks_day > 7:
    print("Сегодня бесконечость")