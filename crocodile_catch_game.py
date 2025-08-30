import tkinter as tk
import random
import winsound
import math
import os

class CrocodileCatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Поймай Крокодила")
        self.width = 800
        self.height = 600
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#87CEEB")
        self.canvas.pack()
        
        # Load previous score
        self.score_file = "crocodile_score.txt"
        self.caught_count = self.load_score()
        
        # Different crocodile types
        self.crocodile_types = [
            {"color": "#228B22", "speed": 8, "size": 60, "score": 1, "name": "Молодой крокодил"},
            {"color": "#8B4513", "speed": 6, "size": 80, "score": 2, "name": "Взрослый крокодил"},
            {"color": "#2F4F4F", "speed": 10, "size": 50, "score": 3, "name": "Быстрый крокодил"}
        ]
        
        self.crocodiles = []
        self.max_crocodiles = 6
        
        # Score display
        self.count_text = self.canvas.create_text(20, 20, anchor="nw", 
                                                text=f"Поймано: {self.caught_count}", 
                                                font=("Arial", 20, "bold"), 
                                                fill="#8B0000")
        
        # Game instructions
        self.canvas.create_text(self.width//2, self.height-40, 
                               text="Кликай на крокодилов, чтобы поймать их!", 
                               font=("Arial", 14), fill="#000080")
        self.canvas.create_text(self.width//2, self.height-20, 
                               text="Нажми Q для выхода (сохраняется счёт)", 
                               font=("Arial", 12), fill="#000080")
        
        # Bind keys and window close event
        self.root.bind('q', self.quit_game)
        self.root.bind('Q', self.quit_game)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.spawn_crocodile()
        self.move_crocodiles()
        self.canvas.bind("<Button-1>", self.catch_crocodile)

    def load_score(self):
        """Load score from file"""
        try:
            if os.path.exists(self.score_file):
                with open(self.score_file, 'r') as f:
                    return int(f.read().strip())
        except:
            pass
        return 0

    def save_score(self):
        """Save score to file"""
        try:
            with open(self.score_file, 'w') as f:
                f.write(str(self.caught_count))
        except:
            pass

    def create_real_crocodile(self, x, y, croc_type):
        """Create a realistic crocodile"""
        size = croc_type["size"]
        color = croc_type["color"]
        dark_color = self.darken_color(color)
        croc_id = []
        
        # Main body (streamlined crocodile shape)
        body_length = size * 2.2
        body_points = [
            x, y + size*0.5,
            x + body_length*0.2, y + size*0.2,
            x + body_length*0.5, y,
            x + body_length*0.8, y + size*0.2,
            x + body_length, y + size*0.5,
            x + body_length*0.8, y + size*0.8,
            x + body_length*0.5, y + size,
            x + body_length*0.2, y + size*0.8,
            x, y + size*0.5
        ]
        croc_id.append(self.canvas.create_polygon(body_points, fill=color, outline=dark_color, width=2, smooth=1))
        
        # Head with snout
        head_size = size * 0.9
        head_points = [
            x + body_length, y + size*0.4,
            x + body_length + head_size*0.6, y + size*0.3,
            x + body_length + head_size, y + size*0.5,
            x + body_length + head_size*0.6, y + size*0.7,
            x + body_length, y + size*0.6
        ]
        croc_id.append(self.canvas.create_polygon(head_points, fill=color, outline=dark_color, width=2, smooth=1))
        
        # Eyes
        eye_size = size * 0.12
        croc_id.append(self.canvas.create_oval(
            x + body_length + head_size*0.4, y + size*0.35,
            x + body_length + head_size*0.4 + eye_size, y + size*0.35 + eye_size,
            fill="yellow", outline="black"
        ))
        croc_id.append(self.canvas.create_oval(
            x + body_length + head_size*0.4 + eye_size*0.3, y + size*0.37,
            x + body_length + head_size*0.4 + eye_size*0.6, y + size*0.37 + eye_size*0.3,
            fill="black"
        ))
        
        # Nostrils
        nostril_size = size * 0.06
        for i in range(2):
            nostril_x = x + body_length + head_size*0.7 + i*head_size*0.1
            croc_id.append(self.canvas.create_oval(
                nostril_x, y + size*0.45,
                nostril_x + nostril_size, y + size*0.45 + nostril_size,
                fill="black"
            ))
        
        # Teeth
        tooth_size = size * 0.08
        for i in range(3):
            tooth_x = x + body_length + head_size*0.2 + i*head_size*0.25
            croc_id.append(self.canvas.create_polygon(
                tooth_x, y + size*0.55,
                tooth_x + tooth_size*0.5, y + size*0.6,
                tooth_x + tooth_size, y + size*0.55,
                fill="white", outline="black"
            ))
        
        # Legs (four legs)
        leg_size = size * 0.35
        leg_positions = [
            (x + body_length*0.2, y + size*0.6),
            (x + body_length*0.4, y + size*0.6),
            (x + body_length*0.6, y + size*0.6),
            (x + body_length*0.8, y + size*0.6)
        ]
        
        for leg_x, leg_y in leg_positions:
            croc_id.append(self.canvas.create_oval(
                leg_x, leg_y,
                leg_x + leg_size, leg_y + leg_size,
                fill=color, outline=dark_color
            ))
        
        # Tail
        tail_length = size * 1.5
        tail_points = [
            x, y + size*0.5,
            x - tail_length*0.3, y + size*0.3,
            x - tail_length*0.6, y + size*0.4,
            x - tail_length, y + size*0.5,
            x - tail_length*0.6, y + size*0.6,
            x - tail_length*0.3, y + size*0.7,
            x, y + size*0.5
        ]
        croc_id.append(self.canvas.create_polygon(tail_points, fill=color, outline=dark_color, width=2, smooth=1))
        
        # Back scales
        scale_size = size * 0.15
        for i in range(4):
            scale_x = x + body_length*0.25 + i*body_length*0.2
            croc_id.append(self.canvas.create_polygon(
                scale_x, y,
                scale_x + scale_size, y - scale_size*0.5,
                scale_x + scale_size*2, y,
                fill=dark_color, outline=dark_color
            ))
        
        return croc_id

    def darken_color(self, color):
        """Darken a hex color"""
        if color.startswith('#'):
            r = max(0, int(color[1:3], 16) - 40)
            g = max(0, int(color[3:5], 16) - 40)
            b = max(0, int(color[5:7], 16) - 40)
            return f"#{r:02x}{g:02x}{b:02x}"
        return color

    def spawn_crocodile(self):
        if len(self.crocodiles) < self.max_crocodiles:
            croc_type = random.choice(self.crocodile_types)
            x = random.randint(100, self.width - 200)
            y = random.randint(100, self.height - 150)
            croc_parts = self.create_real_crocodile(x, y, croc_type)
            direction = random.uniform(0, 2 * math.pi)
            self.crocodiles.append({
                "parts": croc_parts,
                "type": croc_type,
                "direction": direction,
                "x": x,
                "y": y
            })
        self.root.after(1000, self.spawn_crocodile)

    def move_crocodiles(self):
        for croc in self.crocodiles[:]:
            speed = croc["type"]["speed"]
            dx = math.cos(croc["direction"]) * speed
            dy = math.sin(croc["direction"]) * speed
            
            new_x = croc["x"] + dx
            new_y = croc["y"] + dy
            
            # Bounce off walls
            if new_x < 50 or new_x > self.width - 200:
                croc["direction"] = math.pi - croc["direction"] + random.uniform(-0.3, 0.3)
            
            if new_y < 50 or new_y > self.height - 150:
                croc["direction"] = -croc["direction"] + random.uniform(-0.3, 0.3)
            
            # Update position
            dx_move = new_x - croc["x"]
            dy_move = new_y - croc["y"]
            for part_id in croc["parts"]:
                self.canvas.move(part_id, dx_move, dy_move)
            
            croc["x"] += dx_move
            croc["y"] += dy_move
        
        self.root.after(50, self.move_crocodiles)

    def catch_crocodile(self, event):
        clicked = self.canvas.find_overlapping(event.x-10, event.y-10, event.x+10, event.y+10)
        for i, croc in enumerate(self.crocodiles[:]):
            for part_id in croc["parts"]:
                if part_id in clicked:
                    # Remove crocodile
                    for part_id in croc["parts"]:
                        self.canvas.delete(part_id)
                    self.crocodiles.pop(i)
                    self.caught_count += croc["type"]["score"]
                    self.canvas.itemconfig(self.count_text, text=f"Поймано: {self.caught_count}")
                    
                    # Play sound
                    winsound.Beep(500, 100)
                    winsound.Beep(700, 80)
                    return

    def quit_game(self, event=None):
        """Save score and quit"""
        self.save_score()
        self.root.quit()

    def on_closing(self):
        """Handle window close event"""
        self.save_score()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = CrocodileCatchGame(root)
    root.mainloop()
