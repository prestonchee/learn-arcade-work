import random
import arcade
import math

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_FISH = 0.5
SPRITE_SCALING_SHOT = 1
FISH_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Shot(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class Fish(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the fish
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.fish_list = None
        self.shot_list = None
        self.good_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.fish_list = arcade.SpriteList()
        self.shot_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()


        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("duck.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(FISH_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            fish = Fish("fish.png", SPRITE_SCALING_FISH)

            # Position the coin
            fish.center_x = random.randrange(SCREEN_WIDTH)
            fish.center_y = random.randrange(SCREEN_HEIGHT)
            fish.change_x = random.randrange(-3, 4)
            fish.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.fish_list.append(fish)

        for j in range(50):
            # Create the coin instance
            # Coin image from kenney.nl
            shot = Shot("shot.png", SPRITE_SCALING_SHOT / 3)

            # Position the center of the circle the coin will orbit
            shot.circle_center_x = random.randrange(SCREEN_WIDTH)
            shot.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            shot.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            shot.circle_angle = random.random() * 2 * math.pi

            self.shot_list.append(shot)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.fish_list.draw()
        self.player_list.draw()
        self.shot_list.draw()

        # Put the text on the screen.


        if len(self.fish_list) > 0:
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        else:
            output = "Game Over"
            arcade.draw_text(output, (SCREEN_WIDTH / 2) - 50, SCREEN_HEIGHT / 2, arcade.color.RED, 20)
            output = f"Score: {self.score}"
            arcade.draw_text(output, (SCREEN_WIDTH / 2) - 25, (SCREEN_HEIGHT / 2) - 50, arcade.color.WHITE, 15)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        if len(self.fish_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)

        if len(self.fish_list) > 0:
            self.fish_list.update()
            self.shot_list.update()

        # Generate a list of all sprites that collided with the player.
            self.good_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.fish_list)
            bad_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.shot_list)

        # Loop through each colliding sprite, remove it, and add to the score.
            for fish in self.good_list:
                fish.remove_from_sprite_lists()
                self.score += 1
            for shot in bad_list:
                self.score -= 1
                shot.circle_center_x = random.randrange(SCREEN_HEIGHT)
                shot.circle_center_y = random.randrange(SCREEN_WIDTH)







def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()



main()