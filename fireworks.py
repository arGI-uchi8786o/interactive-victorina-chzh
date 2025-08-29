import tkinter as tk
import random
import math
import time

class MegaFireworksShow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.window = None
        self.canvas = None
        self.particles = []
        self.burst_count = 0
        self.max_bursts = 15  # More bursts for bigger show
        
    def show(self):
        """Start the mega fireworks show"""
        self.window = tk.Toplevel(self.root)
        self.window.title("🎆 МЕГА ФЕЙЕРВЕРК ШОУ! 🎆")
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        
        # Bind keys to close
        self.window.bind('<Escape>', lambda e: self.close())
        self.window.bind('<Any-Key>', lambda e: self.close())
        self.window.bind('<Button-1>', lambda e: self.close())
        
        self.canvas = tk.Canvas(self.window, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        
        # Add title text
        self.canvas.create_text(
            self.window.winfo_screenwidth() // 2,
            50,
            text="🎆 ПОБЕДА! МЕГА ФЕЙЕРВЕРК! 🎆",
            fill="white",
            font=("Arial", 24, "bold")
        )
        
        # Start the show with multiple bursts
        self.start_show()
        
        self.window.focus_force()
        self.root.mainloop()
    
    def start_show(self):
        """Start the fireworks show with timed bursts"""
        if self.burst_count < self.max_bursts:
            self.create_mega_burst()
            self.burst_count += 1
            # Schedule next burst with random delay
            delay = random.randint(300, 800)
            self.window.after(delay, self.start_show)
        else:
            # Final grand finale
            self.window.after(1000, self.grand_finale)
    
    def create_mega_burst(self):
        """Create a massive firework burst"""
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        # More vibrant colors
        colors = [
            '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF',
            '#FF00FF', '#FFA500', '#800080', '#FFFFFF', '#FF69B4',
            '#00FF7F', '#FF4500', '#DA70D6', '#7FFF00', '#FFD700'
        ]
        
        # Create multiple burst centers
        centers = []
        for _ in range(random.randint(2, 4)):
            center_x = random.randint(100, screen_width - 100)
            center_y = random.randint(100, screen_height - 200)
            centers.append((center_x, center_y))
        
        # Create 150-200 particles per burst center
        for center_x, center_y in centers:
            for _ in range(random.randint(150, 200)):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(3, 10)  # Faster particles
                size = random.randint(3, 8)    # Bigger particles
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
                    'life': random.randint(60, 100),  # Longer life
                    'color': color,
                    'size': size
                })
        
        # Start animation
        self.update_animation()
    
    def grand_finale(self):
        """Grand finale - massive simultaneous bursts"""
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF']
        
        # Create 5 massive bursts simultaneously
        for i in range(5):
            center_x = screen_width // 6 + (screen_width // 3) * (i % 3)
            center_y = screen_height // 4 + random.randint(-50, 50)
            
            for _ in range(250):  # Huge number of particles
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(4, 12)
                size = random.randint(4, 10)
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
                    'life': random.randint(80, 120),
                    'color': color,
                    'size': size
                })
        
        self.update_animation()
    
    def update_animation(self):
        """Update all particles"""
        if not self.window or not self.canvas:
            return
            
        to_remove = []
        
        for p in self.particles:
            p['life'] -= 1
            if p['life'] <= 0:
                # Fade out effect
                current_alpha = p['life'] / 100.0
                if current_alpha > 0:
                    # Simulate fade by reducing size
                    new_size = max(1, int(p['size'] * current_alpha))
                    coords = self.canvas.coords(p['id'])
                    center_x = (coords[0] + coords[2]) / 2
                    center_y = (coords[1] + coords[3]) / 2
                    self.canvas.coords(p['id'], 
                        center_x - new_size, center_y - new_size,
                        center_x + new_size, center_y + new_size
                    )
                else:
                    self.canvas.delete(p['id'])
                    to_remove.append(p)
            else:
                self.canvas.move(p['id'], p['dx'], p['dy'])
                # Stronger gravity for more dramatic effect
                p['dy'] += 0.15
        
        # Remove dead particles
        for p in to_remove:
            if p in self.particles:
                self.particles.remove(p)
        
        # Continue animation
        if self.particles:
            self.window.after(25, self.update_animation)
        elif self.burst_count >= self.max_bursts:
            # Show closing message
            self.canvas.create_text(
                self.window.winfo_screenwidth() // 2,
                self.window.winfo_screenheight() // 2,
                text="🎉 ШОУ ЗАВЕРШЕНО! 🎉",
                fill="white",
                font=("Arial", 32, "bold")
            )
            self.window.after(3000, self.close)
    
    def close(self):
        """Close the show"""
        if self.window:
            self.window.destroy()
        if self.root:
            self.root.quit()
            self.root.destroy()

def show_mega_fireworks():
    """Start the mega fireworks show"""
    show = MegaFireworksShow()
    show.show()

if __name__ == "__main__":
    show_mega_fireworks()
