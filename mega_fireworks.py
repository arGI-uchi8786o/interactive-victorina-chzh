import tkinter as tk
import random
import math
import time
import os
import threading
from playsound import playsound

class MegaFireworksSpectacle:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.window = None
        self.canvas = None
        self.particles = []
        self.current_round = 0
        self.max_rounds = 3
        self.burst_count = 0
        self.music_playing = False
        
    def start_spectacle(self):
        """Start the 3-round fireworks spectacle"""
        self.window = tk.Toplevel(self.root)
        self.window.title("🎆 МЕГА ФЕЙЕРВЕРК ШОУ - 3 РАУНДА! 🎆")
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        
        # Bind keys to close
        self.window.bind('<Escape>', lambda e: self.close_show())
        self.window.bind('<Any-Key>', lambda e: self.close_show())
        
        self.canvas = tk.Canvas(self.window, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        
        # Start background music
        self.play_background_music()
        
        # Start the first round
        self.start_next_round()
        
        self.window.focus_force()
        self.root.mainloop()
    
    def play_background_music(self):
        """Play background music in separate thread"""
        def music_thread():
            try:
                if os.path.exists("fireworks.mp3"):
                    self.music_playing = True
                    playsound("fireworks.mp3")
                else:
                    print("Файл fireworks.mp3 не найден! Музыка не будет играть.")
            except:
                print("Ошибка воспроизведения музыки")
        
        thread = threading.Thread(target=music_thread)
        thread.daemon = True
        thread.start()
    
    def start_next_round(self):
        """Start the next round of fireworks"""
        self.current_round += 1
        self.burst_count = 0
        
        if self.current_round > self.max_rounds:
            self.grand_finale()
            return
            
        # Show round title
        round_titles = [
            "РАУНД 1: КЛАССИЧЕСКИЕ ВЗРЫВЫ",
            "РАУНД 2: СПИРАЛЬНЫЕ УЗОРЫ", 
            "РАУНД 3: ЦВЕТОЧНЫЕ БУРИ"
        ]
        
        self.canvas.delete("all")
        self.canvas.create_text(
            self.window.winfo_screenwidth() // 2,
            self.window.winfo_screenheight() // 2,
            text=round_titles[self.current_round - 1],
            fill="white",
            font=("Arial", 28, "bold"),
            justify="center"
        )
        
        self.window.after(2000, self.start_round_show)
    
    def start_round_show(self):
        """Start the actual fireworks for current round"""
        if self.current_round == 1:
            self.round_classic_bursts()
        elif self.current_round == 2:
            self.round_spiral_patterns()
        elif self.current_round == 3:
            self.round_flower_storms()
    
    def round_classic_bursts(self):
        """Round 1: Massive classic colorful bursts"""
        if self.burst_count < 12:
            self.create_classic_burst()
            self.burst_count += 1
            delay = random.randint(400, 700)
            self.window.after(delay, self.round_classic_bursts)
        else:
            self.window.after(1500, self.start_next_round)
    
    def round_spiral_patterns(self):
        """Round 2: Beautiful spiral patterns"""
        if self.burst_count < 8:
            self.create_spiral_burst()
            self.burst_count += 1
            delay = random.randint(600, 900)
            self.window.after(delay, self.round_spiral_patterns)
        else:
            self.window.after(1500, self.start_next_round)
    
    def round_flower_storms(self):
        """Round 3: Flower-like storm patterns"""
        if self.burst_count < 10:
            self.create_flower_burst()
            self.burst_count += 1
            delay = random.randint(300, 600)
            self.window.after(delay, self.round_flower_storms)
        else:
            self.window.after(1500, self.start_next_round)
    
    def create_classic_burst(self):
        """Create massive classic firework burst"""
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF',
                 '#FF00FF', '#FFA500', '#800080', '#FFFFFF', '#FF69B4']
        
        # Create 3-5 burst centers
        centers = []
        for _ in range(random.randint(3, 5)):
            center_x = random.randint(150, screen_width - 150)
            center_y = random.randint(150, screen_height - 250)
            centers.append((center_x, center_y))
        
        # Create 200-300 particles per center
        for center_x, center_y in centers:
            for _ in range(random.randint(200, 300)):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(4, 12)
                size = random.randint(4, 9)
                color = random.choice(colors)
                
                particle = self.canvas.create_oval(
                    center_x - size, center_y - size,
                    center_x + size, center_y + size,
                    fill=color, outline=color
                )
                
                self.particles.append({
                    'id': particle,
                    'dx': speed * math.cos(angle),
                    'dy': speed * math.sin(angle),
                    'life': random.randint(70, 120),
                    'color': color,
                    'size': size
                })
        
        self.update_animation()
    
    def create_spiral_burst(self):
        """Create beautiful spiral pattern burst"""
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        center_x = random.randint(200, screen_width - 200)
        center_y = random.randint(200, screen_height - 300)
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F9A826', '#6C5CE7']
        
        # Create spiral pattern
        spiral_arms = 6
        particles_per_arm = 50
        
        for arm in range(spiral_arms):
            base_angle = (arm * 2 * math.pi) / spiral_arms
            
            for i in range(particles_per_arm):
                distance = i * 3
                angle = base_angle + (i * 0.1)
                speed = 4 + (i * 0.1)
                size = max(2, 6 - (i * 0.08))
                color = colors[arm % len(colors)]
                
                particle = self.canvas.create_oval(
                    center_x - size, center_y - size,
                    center_x + size, center_y + size,
                    fill=color, outline=color
                )
                
                self.particles.append({
                    'id': particle,
                    'dx': speed * math.cos(angle),
                    'dy': speed * math.sin(angle),
                    'life': random.randint(80, 140),
                    'color': color,
                    'size': size
                })
        
        self.update_animation()
    
    def create_flower_burst(self):
        """Create flower-like storm pattern"""
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        center_x = random.randint(250, screen_width - 250)
        center_y = random.randint(250, screen_height - 350)
        
        colors = ['#E91E63', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3', '#00BCD4']
        
        # Create flower pattern with petals
        petals = 8
        particles_per_petal = 40
        
        for petal in range(petals):
            petal_angle = (petal * 2 * math.pi) / petals
            
            for i in range(particles_per_petal):
                # Flower shape equation
                t = i / particles_per_petal
                distance = 100 * math.sin(4 * t)
                angle = petal_angle + math.sin(8 * t) * 0.2
                
                speed = 3 + (t * 4)
                size = max(2, 5 - (t * 3))
                color = colors[petal % len(colors)]
                
                particle = self.canvas.create_oval(
                    center_x - size, center_y - size,
                    center_x + size, center_y + size,
                    fill=color, outline=color
                )
                
                self.particles.append({
                    'id': particle,
                    'dx': speed * math.cos(angle),
                    'dy': speed * math.sin(angle),
                    'life': random.randint(90, 160),
                    'color': color,
                    'size': size
                })
        
        self.update_animation()
    
    def grand_finale(self):
        """Grand finale with all patterns combined"""
        self.canvas.delete("all")
        self.canvas.create_text(
            self.window.winfo_screenwidth() // 2,
            100,
            text="🎆 ГРАНД ФИНАЛ! 🎆",
            fill="gold",
            font=("Arial", 36, "bold")
        )
        
        # Create massive combined burst
        self.create_classic_burst()
        self.window.after(500, self.create_spiral_burst)
        self.window.after(1000, self.create_flower_burst)
        self.window.after(2000, self.create_classic_burst)
        self.window.after(2500, self.create_spiral_burst)
        self.window.after(3000, self.create_flower_burst)
        
        # Show completion message
        self.window.after(8000, self.show_completion)
    
    def show_completion(self):
        """Show completion message"""
        self.canvas.create_text(
            self.window.winfo_screenwidth() // 2,
            self.window.winfo_screenheight() // 2,
            text="🎉 ШОУ ЗАВЕРШЕНО! \n3 ЭПИЧНЫХ РАУНДА! 🎉",
            fill="white",
            font=("Arial", 32, "bold"),
            justify="center"
        )
        self.window.after(4000, self.close_show)
    
    def update_animation(self):
        """Update particle animation"""
        if not self.window or not self.canvas:
            return
            
        to_remove = []
        
        for p in self.particles:
            p['life'] -= 1
            if p['life'] <= 0:
                self.canvas.delete(p['id'])
                to_remove.append(p)
            else:
                self.canvas.move(p['id'], p['dx'], p['dy'])
                p['dy'] += 0.12  # Gravity
        
        for p in to_remove:
            if p in self.particles:
                self.particles.remove(p)
        
        if self.particles:
            self.window.after(20, self.update_animation)
    
    def close_show(self):
        """Close the entire show"""
        self.music_playing = False
        if self.window:
            self.window.destroy()
        if self.root:
            self.root.quit()
            self.root.destroy()

def start_mega_fireworks():
    """Start the mega fireworks spectacle"""
    spectacle = MegaFireworksSpectacle()
    spectacle.start_spectacle()

if __name__ == "__main__":
    start_mega_fireworks()
