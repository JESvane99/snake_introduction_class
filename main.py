# %% [markdown]
# # Guided steps (quick start)
#
# 1) Run all cells to play one round.
# 2) Change `snake_color` and `food_color`, then rerun the setup cells.
# 3) Change `delay` (for speed) and `game_width`/`game_height`, then rerun.
# 4) Play again and notice the differences.
#
# If something breaks, that is fine. Fixing errors is part of learning.

# %% [markdown]
# ## General game setup
#
# The following cells include the general setup for the game.
#
# ### First we import the following libraries:
# - `turtle` for the actual game graphics and game loop
# - `time` for controlling the speed of the game
# - `random` for generating random positions for the food
#

# %%
import turtle
import time
import random

# %% [markdown]
# ### Then we define the following variables:
#
# #### General setup for the game to run:
# - `delay` to control the speed of the game
# - `score` to keep track of the player's score
# - `high_score` to keep track of the highest score achieved during the game
# - `game_width` and `game_height` to define the size of the actual game area where the snake can move
# - `window_width` and `window_height` to define the size of the turtle graphics window
#

# %%
delay = 0.1
score = 0
high_score = 0
game_width = 600
game_height = 600
window_width = 700
window_height = 700

# %% [markdown]
# #### Movement variables to control the direction of the snake:
# - `button_up`, `button_down`, `button_left`, and `button_right` to control the direction of the snake's movement
# - `direction` to keep track of the current direction of the snake's movement

# %%
button_up, button_down, button_left, button_right = "Up", "Down", "Left", "Right"
direction = "stop"

# %% [markdown]
# #### Design variables to control the appearance of the game:
# - `screen_title` to define the title of the game window
# - `snake_color` to define the color of the snake
# - `snake_pattern` to define the pattern of the snake's body segments
# - `food_color` to define the color of the food
# - `background_color` to define the color of the game background
# - `score_color` to define the color of the score display
# - `score_font` to define the font and size of the score display

# %%
screen_title = "Snake Game"
snake_color = "green"
snake_head_shape = "square"
snake_segment_shape = "square"
food_color = "red"
food_shape = "circle"
background_color = "black"
score_color = "white"
score_font = ("Arial", 24, "normal")

# %%
# Lists: try color options
color_options = [snake_color, food_color, "blue"]
color_options.append("yellow")
print("colors list:", color_options)
print("first color:", color_options[0])

# Tuples: fixed sizes for the game area
sizes = (game_width, game_height)
print("sizes tuple:", sizes)
print("width == height:", sizes[0] == sizes[1])

# Dicts: store settings
settings = {"speed": delay, "background": background_color}
settings["speed"] = 0.08
print("settings:")
for key, value in settings.items():
    print(f"    {key}: {value}")
print("settings keys:", list(settings.keys()))
print("has speed:", "speed" in settings)

# Sets: unique colors
unique_colors = {snake_color, food_color, "red"}
unique_colors.add("green")
print("unique colors:", unique_colors)
print("red in set:", "red" in unique_colors)

# %% [markdown]
# ## Collections quick demo (game context)
#
# Run this once. It uses game settings to show lists, tuples, dicts, sets, and a few operators.

# %% [markdown]
# ### Now we calculate some variables to use in the game setup
# - maximum and minimum values of `x` and `y` coordinates to define the boundaries of the game area based on the defined game width and height
# - `score_x` and `score_y` to define the position of the score display based on the defined game height and score font size

# %%
x_min = (
    -game_width // 2
)  # uses floor division to ensure we get an integer - could do it with regular division to teach about int and float
x_max = game_width // 2
y_min = -game_height // 2
y_max = game_height // 2
score_x = 0
score_y = game_height // 2 - score_font[1] - 10


# %% [markdown]
# ### Then comes the function definitions, which include:
# - `move()` to control the movement of the snake based on the current direction
# - `go_up()`, `go_down()`, `go_left()`, and `go_right()` to change the direction of the snake's movement when the corresponding button is pressed


# %%
def move(head, direction):
    """Move the snake based on the current set direction."""
    if direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def go_up():
    """change direction of snake head to up if it is not currently moving down."""
    global direction
    if direction != "down":
        direction = "up"


def go_down():
    """change direction of snake head to down if it is not currently moving up."""
    global direction
    if direction != "up":
        direction = "down"


def go_left():
    """change direction of snake head to left if it is not currently moving right."""
    global direction
    if direction != "right":
        direction = "left"


def go_right():
    """change direction of snake head to right if it is not currently moving left."""
    global direction
    if direction != "left":
        direction = "right"


# %% [markdown]
# # Explore freely
#
# You now have a working game. Try changing values, colors, shapes, or keys. If you get an error, read it and try again.

# %% [markdown]
# ### Turtle graphics setup and game loop:
#
# >This section is a bit more complex so it can be explored if one is interested
# but the main focus of this notebook is on the introduction to python structures
# and not on the actual game implementation.
#
# It includes the setup of the turtle objects for the game window itself, the snake's head, the food, and the score display. It also includes the main game loop where the game logic is executed, such as checking for collisions, updating the score, and moving the snake.
# The variables and functions defined in the previous sections are used throughout this part to control the game flow and update the game state based on user input and game events.

# %%
# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor(background_color)
wn.setup(width=window_width, height=window_height)
wn.tracer(0)  # Turns off the screen updates

# %%
# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape(snake_head_shape)
head.color(snake_color)
head.penup()
head.goto(0, 0)
direction = "stop"  # add direction attribute to head turtle object - this can be done because of pythons dynamic typing
snake = [head]

# %%
# Bug hunt: the snake must be mutable to grow
snake = (head,)

# %% [markdown]
# ## Bug hunt: list vs tuple
#
# This cell changes the snake container. Run the notebook, then play until the snake eats food. If it crashes, find and fix the mistake here.

# %%
# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape(food_shape)
food.color(food_color)
food.penup()
food.goto(0, 100)

# %%
# Pen for score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape(
    "square"
)  # One could also define a variable for the pen shape and use it here to make it more customizable
pen.color(score_color)
pen.penup()
pen.hideturtle()
pen.goto(score_x, score_y)
pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=score_font)

# %%
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, button_up)
wn.onkeypress(go_down, button_down)
wn.onkeypress(go_left, button_left)
wn.onkeypress(go_right, button_right)

# %%
# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    border_collision = (
        head.xcor() > x_max
        or head.xcor() < x_min
        or head.ycor() > y_max
        or head.ycor() < y_min
    )
    snake_collision = any(
        segment.distance(head) < 20 for segment in snake[1:]
    )  # check if head collides with any segment in the snake body (excluding the head itself)
    if border_collision or snake_collision:
        direction = "stop"
        for segment in snake:
            segment.shape("turtle")
            wn.update()  # update the screen to show the change in segment shapes before clearing them
            time.sleep(
                0.5
            )  # add a small delay to make it more clear that the segments are being hidden
        [
            segment.reset() for segment in snake[1:]
        ]  # clear the segments instead of moving them off screen

        # Clear the segments list
        head.goto(0, 0)
        head.shape(snake_head_shape)  # reset the head shape
        snake = [head]

        # Reset the score
        score = 0

        pen.clear()
        pen.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=score_font,
        )

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape(snake_segment_shape)
        new_segment.color(snake_color)
        new_segment.penup()
        new_segment.goto(food.xcor(), food.ycor())
        snake.append(new_segment)

        # Move the food to a random spot
        x = random.randint(
            x_min, x_max
        )  # use defined variables for min and max x and y to make it more customizable
        y = random.randint(y_min, y_max)
        food.goto(x, y)

        # Shorten the delay
        # if increase_delay:
        #   delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
            pen.clear()
            pen.write(
                f"Score: {score}  High Score: {high_score}",
                align="center",
                font=score_font,
            )

    # Move the end segments first in reverse order
    for i in range(len(snake) - 1, 0, -1):
        if i > 0:
            x = snake[i - 1].xcor()
            y = snake[i - 1].ycor()
        snake[i].goto(x, y)

    move(head, direction)

    time.sleep(0.2)


# %%
