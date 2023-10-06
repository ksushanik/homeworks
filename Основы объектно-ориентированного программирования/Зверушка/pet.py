import tkinter as tk


class Pet:
    def __init__(self):
        self.hunger = 3  # Изначально зверушка голодна
        self.happiness = 10  # Изначально зверушка счастлива

    def feed(self):
        if self.hunger < 10:
            self.hunger += 1
            self.update_display()
        else:
            self.display_message("Зверушка уже сыта.")

    def play(self):
        if self.hunger > 0:
            if self.happiness < 10:
                self.happiness += 1
                self.hunger -= 1  # Уменьшение значения шкалы сытости
                self.update_display()
            else:
                self.display_message("Зверушка уже счастлива и не хочет играть.")
        else:
            self.display_message("Зверушка слишком голодна, чтобы играть.")

    def update(self):
        if self.happiness == 0 or self.hunger == 0:
            message_label.config(text="Одна из шкал достигла минимума. Игра окончена.")
            feed_button.config(state=tk.DISABLED)
            play_button.config(state=tk.DISABLED)
            return False  # Игра заканчивается, если одна из шкал достигла минимума

        if self.hunger > 0:
            self.hunger -= 1
        self.happiness -= 1
        self.update_display()
        return True

    def update_display(self):
        hunger_bar.config(text=f"Сытость: {'*' * self.hunger}")
        happiness_bar.config(text=f"Радость: {'*' * self.happiness}")

    def display_message(self, message):
        message_label.config(text=message)


# Создание экземпляра зверушки
pet = Pet()

# Создание окна
window = tk.Tk()
window.title("Зверушка")

# Установка фиксированного размера окна
width = 400
height = 150
window.geometry(f"{width}x{height}")

# Получение размеров экрана
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Расчет координат для центрирования окна
x = (screen_width - width) // 2
y = (screen_height - height) // 2

# Установка позиции окна
window.geometry(f"{width}x{height}+{x}+{y}")

# Создание меток для шкал сытости и радости
hunger_bar = tk.Label(window, text="Сытость: ")
hunger_bar.pack()

happiness_bar = tk.Label(window, text="Радость: **********")
happiness_bar.pack()

# Создание метки для вывода сообщений
message_label = tk.Label(window, text="")
message_label.pack()

# Создание кнопки для кормления зверушки
feed_button = tk.Button(window, text="Покормить", command=pet.feed)
feed_button.pack()

# Создание кнопки для игры с зверушкой
play_button = tk.Button(window, text="Поиграть", command=pet.play)
play_button.pack()


# Функция для обновления состояния зверушки с течением времени
def update_pet():
    if not pet.update():
        message_label.config(text="Одна из шкал достигла максимума или минимума. Игра окончена.")
        feed_button.config(state=tk.DISABLED)
        play_button.config(state=tk.DISABLED)
    else:
        window.after(2000, update_pet)  # Обновление каждые 2 секунды


# Запуск обновления состояния зверушки
update_pet()

# Запуск главного цикла окна
window.mainloop()
