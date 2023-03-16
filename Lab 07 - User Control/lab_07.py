"""
Moving Objects
Preston Chee
3/02/2023
CS 1400
"""

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


# Functions to draw simple items
def draw_sky():
    arcade.draw_lrtb_rectangle_filled(0, 800, 600, 450, arcade.csscolor.SKY_BLUE)


# Draw a circle pond
def draw_pond():
    arcade.draw_circle_filled(450, 250, 150, arcade.csscolor.DARK_CYAN)


# draw the fisherman
def draw_fisherman():
    # head
    arcade.draw_circle_filled(275, 300, 13, arcade.color.BLACK)
    # body
    arcade.draw_line(275, 250, 275, 300, arcade.color.BLACK, 4)
    # left leg
    arcade.draw_line(275, 250, 250, 225, arcade.color.BLACK, 4)
    # right leg
    arcade.draw_line(275, 250, 300, 225, arcade.color.BLACK, 4)
    # right arm
    arcade.draw_line(275, 265, 300, 280, arcade.color.BLACK, 4)

    # fishing pole
    arcade.draw_line(285, 250, 317, 310, arcade.color.BLACK_OLIVE, 3)
    # fishing line
    arcade.draw_line(317, 310, 400, 200, arcade.color.BLACK, 1)

    # Draw fish that faces to the left

    # Draw tree


def draw_tree():
    arcade.draw_rectangle_filled(120, 280, 20, 80, arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(((120, 360), (100, 320), (90, 280), (150, 280), (140, 320)), arcade.csscolor.DARK_GREEN)


# Class creates sun object
class Sun:
    def __init__(self, position_x, position_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        # Draw the sun with the instance variables we have.
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
        arcade.draw_triangle_filled(self.position_x + 10, self.position_y + 10,
                                    self.position_x, self.position_y + 40,
                                    self.position_x - 10, self.position_y + 10, self.color)
        arcade.draw_triangle_filled(self.position_x + 10, self.position_y + 10,
                                    self.position_x - 40, self.position_y,
                                    self.position_x - 10, self.position_y - 10, self.color)
        arcade.draw_triangle_filled(self.position_x - 10, self.position_y - 10,
                                    self.position_x, self.position_y - 40,
                                    self.position_x + 10, self.position_y - 10, self.color)
        arcade.draw_triangle_filled(self.position_x - 10, self.position_y - 10,
                                    self.position_x + 40, self.position_y,
                                    self.position_x + 10, self.position_y + 10, self.color)


# Creates fish class object
class Fish:
    # Instance variables
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        # Load sound effect
        self.error_sound = arcade.load_sound("error.ogg")

    # Draw fish based off of instance variables
    def draw(self):
        arcade.draw_triangle_filled(self.position_x, self.position_y,
                                    self.position_x, self.position_y + 10,
                                    self.position_x - 5, self.position_y + 5, self.color)
        arcade.draw_ellipse_filled(self.position_x - 10, self.position_y + 5,
                                   self.radius, 8, self.color)

    # Based on key pressed change the location of the fish.

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Make sure fish does not move off-screen
        if self.position_x < self.radius:
            self.position_x = self.radius
            # Make a noise when the fish hits the border of the screen
            arcade.play_sound(self.error_sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.error_sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.error_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.error_sound)


# Creates the second main class to run the game.
class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color(arcade.color.DIRT)

        self.set_mouse_visible(False)

        # Create instance variable of sun and fish in retrospect of their Class
        self.sun = Sun(50, 50, 20, arcade.color.YELLOW)

        self.fish = Fish(450, 210, 0, 0, 13, arcade.color.PINK)

    # On screen items are drawn
    def on_draw(self):
        arcade.start_render()
        draw_sky()
        draw_pond()
        draw_fisherman()
        draw_tree()
        self.fish.draw()
        self.sun.draw()

    # Mouse input
    def on_mouse_motion(self, x, y, dx, dy):
        self.sun.position_x = x
        self.sun.position_y = y

    def update(self, delta_time):
        self.fish.update()

    # Keyboard input
    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.fish.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.fish.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.fish.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.fish.change_y = -MOVEMENT_SPEED

    # sets the fish changes to 0
    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.fish.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.fish.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
