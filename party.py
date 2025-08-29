
import tkinter as tk
from tkinter import messagebox
import random
import math
import time
from PIL import Image, ImageTk
import io
import pygame
import base64
import winsound

class ChaosParty:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ВЕЧЕРИНКА ХАОСА!")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
       
        # Блокируем закрытие (но ненадолго!)
        self.root.protocol("WM_DELETE_WINDOW", self.nope)
        self.root.bind("<Alt-F4>", self.nope)
        self.root.bind("<Escape>", self.nope)
       
        # Холст для всего безумия
        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
       
        # Создаем крокодильчиков из base64
        self.crocodiles = []
        self.create_crocodiles()
       
        # Запускаем все виды безумия
        self.start_chaos()
        
        # Добавляем звуковые эффекты вечеринки
        self.play_party_sounds()
       
    def play_party_sounds(self):
        """Play party music indefinitely."""
        try:
            # Initialize pygame mixer
            pygame.mixer.init()
            # Play random beep sounds in a loop
            self.play_random_sounds()
        except:
            pass
        
        # Выход по клавише q
        self.root.bind("<q>", self.exit_party)

    def play_random_sounds(self):
        """Play random beep sounds"""
        try:
            frequency = random.randint(200, 1000)
            duration = random.randint(50, 300)
            winsound.Beep(frequency, duration)
        except:
            pass
        
        # Add mouse click sound effects
        self.canvas.bind("<Button-1>", self.play_click_sound)
        
        # Continue playing random sounds
        self.root.after(random.randint(100, 500), self.play_random_sounds)

    def play_click_sound(self, event=None):
        """Play sound on mouse click"""
        try:
            frequency = random.randint(300, 800)
            duration = random.randint(20, 100)
            winsound.Beep(frequency, duration)
            
            # Create visual effect on click
            self.create_click_effect(event.x, event.y)
        except:
            pass

    def create_click_effect(self, x, y):
        """Create visual effect on mouse click"""
        colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'white']
        for i in range(8):
            angle = i * 45
            rad = math.radians(angle)
            dx = math.cos(rad) * 10
            dy = math.sin(rad) * 10
            color = random.choice(colors)
            particle = self.canvas.create_oval(x-3, y-3, x+3, y+3, fill=color, outline='')
            self.animate_click_particle(particle, dx, dy)

    def animate_click_particle(self, particle, dx, dy):
        """Animate click particle effect"""
        self.canvas.move(particle, dx, dy)
        
        # Fade out effect
        current_color = self.canvas.itemcget(particle, "fill")
        if random.random() < 0.2:  # Random disappearance
            self.canvas.delete(particle)
            return
        
        # Slow down
        dx *= 0.9
        dy *= 0.9
        
        if abs(dx) > 0.5 or abs(dy) > 0.5:
            self.root.after(30, lambda: self.animate_click_particle(particle, dx, dy))
        else:
            self.canvas.delete(particle)

    def exit_party(self, event=None):
        """Exit the party when q is pressed."""
        self.party_over()

    def nope(self, event=None):
        return "break"

    def create_crocodiles(self):
        """Создаем спрайты крокодильчиков из base64"""
        croc_data = [
            "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAABCElEQVRYhe2WQQ6DMAwF/0E5cOQ+ZCRGjhw5j8TIsWckRoyMRGJkJEaOjERi5MiRkUiMHDlyHokxcuTIeSTGyJEj55EYI0eOnEdijBw5ch6JMXLkyHkkxsiRI+eRGCNHjpxHYowcOXIeiTFy5Mh5JMbIkSPnkRgjR46cR2KMHDlyHokxcuTIeSTGyJEj55EYI0eOnEdijBw5ch6JMXLkyHkkxsiRI+eRGCNHjpxHYowcOXIeiTFy5Mh5JMbIkSPnkRgjR46cR2KMHDlyHokxcuTIeSTGyJEj55EYI0eOnEdijBw5ch6JMXLkyHkkxsiRI+eRGCNHjpxHYowcOXIeiTFy5Mh5JMbIkSPnkRgjR46cR2L8A9WbZQZchykLAAAAAElFTkSuQmCC",
            "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAA0ElEQVRIie2VMQ7CMAxF/6EcOHKfMRIjR46cR2Lk2DFGYsTISCQSI0eOjERi5MiR80iMkSNHziMxRo4cOY/EGDly5DwSY+T8/Hm9XvV8PuvxeNT9ftftdqvr9arL5aLz+azT6aTj8ajD4aD9fq/dbqftdqvtdivP8+Q4jizLkmmaMgxDmqZJVVUpiiJZlqUoimRZlgzDkK7r0jRNqqpKURTJsiwFQSBd16VpmlRVlaIokmVZCoJAuq5L0zSpqipFUSTLshQEgXRdl6ZpUlVViqJIlmUpCALpui5N06SqqhRFkSzLUhAE0nVdmqZJVVUpiiJZlqUgCKTrujRNk6qqUhRFsixLQRBI13VpmiZVVaUoimRZloIgkK7r0jRNqqpKURTJsiwFQSBd16VpmlRVlaIokmVZCoJAuq5L0zSpqipFUSTLshQEgXRdl6ZpUlVViqJIlmUpCALpui5N06SqqhRFkSzLUhAE0nVdmqZJVVUpiiJZlqUgCKTrujRNk6qqUhRFsixLQRBI13VpmiZVVaUoimRZloLgDdM7ZQZchykLAAAAAElFTkSuQmCC"
        ]
       
        for data in croc_data:
            try:
                image_data = base64.b64decode(data)
                image = Image.open(io.BytesIO(image_data))
                photo = ImageTk.PhotoImage(image)
                self.crocodiles.append(photo)
            except:
                pass
       
        # Если крокодильчики не загрузились, создаем простые фигуры
        if not self.crocodiles:
            for _ in range(5):
                self.crocodiles.append(None)

    def start_chaos(self):
        """Запускаем все анимации хаоса"""
        self.create_floating_text()
        self.create_bouncing_shapes()
        self.create_rainbow_background()
        self.create_fireworks()
        self.create_floating_crocodiles()
        self.create_rotating_shapes()
        self.create_pulsating_circles()
        self.create_mouse_trail()
        self.create_spinning_text()
        self.create_screen_shake()

    def create_floating_text(self):
        texts = ["ХАОС!", "🎉", "ВЕЧЕРИНКА!", "🐊", "БЕЗУМИЕ!", "✨", "КОДИКИ!", "🚀"]
        for i in range(20):
            x = random.randint(0, self.root.winfo_screenwidth())
            y = random.randint(0, self.root.winfo_screenheight())
            text = random.choice(texts)
            color = random.choice(['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'white'])
            item = self.canvas.create_text(x, y, text=text, font=("Arial", random.randint(20, 48)),
                                         fill=color, tags="floating_text")
            self.animate_text(item)

    def animate_text(self, item):
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
       
        def move():
            nonlocal dx, dy
            self.canvas.move(item, dx, dy)
            coords = self.canvas.coords(item)
            if coords[0] > self.root.winfo_screenwidth() or coords[0] < 0:
                dx = -dx
            if coords[1] > self.root.winfo_screenheight() or coords[1] < 0:
                dy = -dy
            self.root.after(50, move)
       
        move()

    def create_bouncing_shapes(self):
        shapes = []
        for _ in range(15):
            x = random.randint(50, self.root.winfo_screenwidth()-50)
            y = random.randint(50, self.root.winfo_screenheight()-50)
            size = random.randint(20, 60)
            color = random.choice(['red', 'blue', 'green', 'yellow', 'cyan', 'magenta'])
           
            if random.choice([True, False]):
                item = self.canvas.create_oval(x, y, x+size, y+size, fill=color, outline='')
            else:
                item = self.canvas.create_rectangle(x, y, x+size, y+size, fill=color, outline='')
           
            shapes.append({'item': item, 'dx': random.choice([-4, -3, -2, 2, 3, 4]),
                          'dy': random.choice([-4, -3, -2, 2, 3, 4])})
       
        self.animate_shapes(shapes)

    def animate_shapes(self, shapes):
        for shape in shapes:
            self.canvas.move(shape['item'], shape['dx'], shape['dy'])
            coords = self.canvas.coords(shape['item'])
           
            if coords[0] <= 0 or coords[2] >= self.root.winfo_screenwidth():
                shape['dx'] = -shape['dx']
            if coords[1] <= 0 or coords[3] >= self.root.winfo_screenheight():
                shape['dy'] = -shape['dy']
       
        self.root.after(30, lambda: self.animate_shapes(shapes))

    def create_rainbow_background(self):
        colors = ['#ff0000', '#ff7f00', '#ffff00', '#00ff00', '#0000ff', '#4b0082', '#8b00ff']
        current_color = 0
       
        def change_bg():
            nonlocal current_color
            self.root.configure(bg=colors[current_color])
            self.canvas.configure(bg=colors[current_color])
            current_color = (current_color + 1) % len(colors)
            self.root.after(200, change_bg)
       
        change_bg()

    def create_fireworks(self):
        def create_firework():
            x = random.randint(100, self.root.winfo_screenwidth()-100)
            y = random.randint(100, self.root.winfo_screenheight()-100)
            color = random.choice(['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'white'])
           
            for angle in range(0, 360, 15):
                rad = math.radians(angle)
                dx = math.cos(rad) * 5
                dy = math.sin(rad) * 5
                particle = self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=color, outline='')
                self.animate_particle(particle, dx, dy)
           
            self.root.after(random.randint(500, 2000), create_firework)
       
        create_firework()

    def animate_particle(self, particle, dx, dy):
        self.canvas.move(particle, dx, dy)
        if random.random() < 0.3:  # Случайное исчезновение
            self.canvas.delete(particle)
            return
       
        # Замедление
        dx *= 0.95
        dy *= 0.95
       
        if abs(dx) > 0.1 or abs(dy) > 0.1:
            self.root.after(30, lambda: self.animate_particle(particle, dx, dy))
        else:
            self.canvas.delete(particle)

    def create_floating_crocodiles(self):
        for i in range(min(10, len(self.crocodiles))):
            x = random.randint(50, self.root.winfo_screenwidth()-50)
            y = random.randint(50, self.root.winfo_screenheight()-50)
           
            if self.crocodiles[i] is not None:
                item = self.canvas.create_image(x, y, image=self.crocodiles[i])
            else:
                # Простая замена если крокодильчики не загрузились
                item = self.canvas.create_text(x, y, text="🐊", font=("Arial", 36))
           
            self.animate_crocodile(item)

    def animate_crocodile(self, item):
        dx = random.choice([-3, -2, -1, 1, 2, 3])
        dy = random.choice([-3, -2, -1, 1, 2, 3])
       
        def move():
            nonlocal dx, dy
            self.canvas.move(item, dx, dy)
            coords = self.canvas.coords(item)
            if coords[0] > self.root.winfo_screenwidth() or coords[0] < 0:
                dx = -dx
            if coords[1] > self.root.winfo_screenheight() or coords[1] < 0:
                dy = -dy
            self.root.after(40, move)
       
        move()

    def create_rotating_shapes(self):
        stars = []
        for _ in range(8):
            x = random.randint(100, self.root.winfo_screenwidth()-100)
            y = random.randint(100, self.root.winfo_screenheight()-100)
            size = random.randint(20, 40)
            color = random.choice(['red', 'blue', 'green', 'yellow', 'cyan', 'magenta'])
            star = self.canvas.create_polygon(self.create_star_points(x, y, size), fill=color, outline='')
            stars.append({'item': star, 'center_x': x, 'center_y': y, 'angle': 0, 'size': size})
       
        self.rotate_shapes(stars)

    def create_star_points(self, x, y, size):
        points = []
        for i in range(5):
            angle = math.pi/2 + i * 2*math.pi/5
            points.extend([x + size * math.cos(angle), y - size * math.sin(angle)])
            angle += math.pi/5
            points.extend([x + size/2 * math.cos(angle), y - size/2 * math.sin(angle)])
        return points

    def rotate_shapes(self, stars):
        for star in stars:
            self.canvas.delete(star['item'])
            star['angle'] += 0.1
            new_points = []
            for i in range(0, len(self.create_star_points(0, 0, star['size'])), 2):
                px = self.create_star_points(0, 0, star['size'])[i]
                py = self.create_star_points(0, 0, star['size'])[i+1]
                rx = px * math.cos(star['angle']) - py * math.sin(star['angle'])
                ry = px * math.sin(star['angle']) + py * math.cos(star['angle'])
                new_points.extend([star['center_x'] + rx, star['center_y'] + ry])
           
            star['item'] = self.canvas.create_polygon(new_points, fill=random.choice(['red', 'blue', 'green', 'yellow']), outline='')
       
        self.root.after(50, lambda: self.rotate_shapes(stars))

    def create_pulsating_circles(self):
        circles = []
        for _ in range(5):
            x = random.randint(100, self.root.winfo_screenwidth()-100)
            y = random.randint(100, self.root.winfo_screenheight()-100)
            size = random.randint(10, 30)
            color = random.choice(['red', 'blue', 'green', 'yellow', 'cyan', 'magenta'])
            circle = self.canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline='')
            circles.append({'item': circle, 'x': x, 'y': y, 'size': size, 'growing': True})
       
        self.pulsate_circles(circles)

    def pulsate_circles(self, circles):
        for circle in circles:
            if circle['growing']:
                circle['size'] += 1
                if circle['size'] > 50:
                    circle['growing'] = False
            else:
                circle['size'] -= 1
                if circle['size'] < 10:
                    circle['growing'] = True
           
            self.canvas.delete(circle['item'])
            circle['item'] = self.canvas.create_oval(
                circle['x']-circle['size'], circle['y']-circle['size'],
                circle['x']+circle['size'], circle['y']+circle['size'],
                fill=random.choice(['red', 'blue', 'green', 'yellow']), outline=''
            )
       
        self.root.after(100, lambda: self.pulsate_circles(circles))

    def create_mouse_trail(self):
        """Создаем след от мыши"""
        self.mouse_trail = []
        self.canvas.bind("<Motion>", self.add_mouse_trail_point)
        self.animate_mouse_trail()

    def add_mouse_trail_point(self, event):
        """Добавляем точку в след мыши"""
        if len(self.mouse_trail) > 20:  # Ограничиваем длину следа
            self.mouse_trail.pop(0)
        self.mouse_trail.append((event.x, event.y))

    def animate_mouse_trail(self):
        """Анимируем след от мыши"""
        if hasattr(self, 'mouse_trail') and self.mouse_trail:
            for i in range(len(self.mouse_trail) - 1):
                x1, y1 = self.mouse_trail[i]
                x2, y2 = self.mouse_trail[i + 1]
                color = random.choice(['red', 'blue', 'green', 'yellow', 'cyan', 'magenta'])
                self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
        
        self.root.after(50, self.animate_mouse_trail)

    def create_spinning_text(self):
        """Создаем вращающийся текст"""
        texts = ["💫", "🌀", "⚡", "🌟", "✨", "🌪️"]
        for i in range(5):
            x = random.randint(100, self.root.winfo_screenwidth()-100)
            y = random.randint(100, self.root.winfo_screenheight()-100)
            text = random.choice(texts)
            color = random.choice(['red', 'blue', 'green', 'yellow', 'cyan', 'magenta'])
            item = self.canvas.create_text(x, y, text=text, font=("Arial", 48), fill=color)
            self.animate_spinning_text(item, 0)

    def animate_spinning_text(self, item, angle):
        """Анимируем вращение текста"""
        coords = self.canvas.coords(item)
        if coords:
            x, y = coords
            self.canvas.delete(item)
            new_item = self.canvas.create_text(x, y, text=self.canvas.itemcget(item, "text"), 
                                             font=("Arial", 48), fill=self.canvas.itemcget(item, "fill"),
                                             angle=angle)
            self.root.after(100, lambda: self.animate_spinning_text(new_item, (angle + 10) % 360))

    def create_screen_shake(self):
        """Создаем эффект тряски экрана"""
        self.original_position = self.root.winfo_x(), self.root.winfo_y()
        self.shake_screen()

    def shake_screen(self):
        """Трясем экран"""
        if hasattr(self, 'original_position'):
            dx = random.randint(-10, 10)
            dy = random.randint(-10, 10)
            self.root.geometry(f"+{self.original_position[0] + dx}+{self.original_position[1] + dy}")
            self.root.after(100, self.reset_screen_position)

    def reset_screen_position(self):
        """Возвращаем экран в исходное положение"""
        if hasattr(self, 'original_position'):
            self.root.geometry(f"+{self.original_position[0]}+{self.original_position[1]}")
            self.root.after(random.randint(500, 2000), self.shake_screen)

    def party_over(self):
        """Завершаем вечеринку"""
        self.canvas.delete("all")
        self.root.configure(bg='black')
        self.canvas.configure(bg='black')
       
        # Прощальное сообщение
        self.canvas.create_text(
            self.root.winfo_screenwidth()//2,
            self.root.winfo_screenheight()//2 - 50,
            text="🎉 ВЕЧЕРИНКА ЗАВЕРШЕНА! 🎉",
            font=("Arial", 36, "bold"),
            fill="white"
        )
       
        self.canvas.create_text(
            self.root.winfo_screenwidth()//2,
            self.root.winfo_screenheight()//2 + 50,
            text="Нажмите любую клавишу для выхода",
            font=("Arial", 20),
            fill="yellow"
        )
       
        # Разрешаем выход
        self.root.unbind("<Escape>")
        self.root.bind("<Key>", lambda e: self.root.destroy())

    def run(self):
        try:
            self.root.mainloop()
        except:
            try:
                self.root.destroy()
            except:
                pass

if __name__ == "__main__":
    party = ChaosParty()
    party.run()



