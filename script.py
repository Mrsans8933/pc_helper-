import keyboard
print("нажми / чтобы запустить кликер, esc чтобы остановить")
keyboard.wait("/")
while True:
    keyboard.send("w")

    if keyboard.is_pressed("esc"):
        print("остановка")
        break