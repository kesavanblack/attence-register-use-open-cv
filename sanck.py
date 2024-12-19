import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 400
SEG_SIZE = 20
SPEED = 100

# Directions
UP = (0, -SEG_SIZE)
DOWN = (0, SEG_SIZE)
LEFT = (-SEG_SIZE, 0)
RIGHT = (SEG_SIZE, 0)

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        
        # Canvas for drawing the game
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()

        # Initial snake and food settings
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Snake's initial position
        self.food = None
        self.direction = RIGHT
        self.game_over = False

        self.score = 0
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack()

        self.create_food()
        self.update_snake()
        self.listen_for_keypress()

        self.run_game()

    def run_game(self):
        if not self.game_over:
            self.move_snake()
            self.check_collision()
            self.check_food_collision()
            self.update_snake()
            self.root.after(SPEED, self.run_game)
        else:
            self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over", fill="white", font=("Arial", 24))

    def move_snake(self):
        # Get the current head of the snake
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        
        # Move the snake
        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        # Check if the snake hits the wall
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.game_over = True

        # Check if the snake hits itself
        if (head_x, head_y) in self.snake[1:]:
            self.game_over = True

    def check_food_collision(self):
        # Check if the snake eats the food
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food
        if head_x == food_x and head_y == food_y:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.snake.append(self.snake[-1])  # Add a new segment to the snake
            self.create_food()  # Create new food

    def create_food(self):
        self.food = (random.randrange(0, WIDTH, SEG_SIZE), random.randrange(0, HEIGHT, SEG_SIZE))
        while self.food in self.snake:  # Ensure the food doesn't spawn on the snake
            self.food = (random.randrange(0, WIDTH, SEG_SIZE), random.randrange(0, HEIGHT, SEG_SIZE))

    def update_snake(self):
        # Clear the canvas and redraw the snake and food
        self.canvas.delete("all")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + SEG_SIZE, self.food[1] + SEG_SIZE, fill="red")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="green")

    def listen_for_keypress(self):
        self.root.bind("<Up>", lambda event: self.change_direction(UP))
        self.root.bind("<Down>", lambda event: self.change_direction(DOWN))
        self.root.bind("<Left>", lambda event: self.change_direction(LEFT))
        self.root.bind("<Right>", lambda event: self.change_direction(RIGHT))

    def change_direction(self, new_direction):
        # Prevent the snake from turning back on itself
        if (new_direction == UP and self.direction != DOWN) or \
           (new_direction == DOWN and self.direction != UP) or \
           (new_direction == LEFT and self.direction != RIGHT) or \
           (new_direction == RIGHT and self.direction != LEFT):
            self.direction = new_direction


# Create the main window
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
