import time #y=запуск f=остановка g=кнопка которую жмут
import keyboard
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("выберите пункт:")
print("1.кликер")
print("2.зажатие клавиш")
print("3.выход")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<")
x = int(input())
if x == 1:
    y = input("выберите клавишу запуска:")
    f = input("выбеите клавишу остановки:")
    g = input("выберете клавишу клика:")
    keyboard.wait(y)
    while True:
        time.sleep(0.2)
        keyboard.send(g)
        if keyboard.is_pressed(f):
            break
    print("остановка")

elif x == 2:
    y = input("выберите клавишу запуска:")
    f = input("выбеите клавишу остановки:")
    g = input("выберете клавишу зажатия:")
    keyboard.wait(y)
    keyboard.press(g)
    if keyboard.is_pressed(f):
        keyboard.release(g)
    print("остановка")
elif x == 3:
    exit()
