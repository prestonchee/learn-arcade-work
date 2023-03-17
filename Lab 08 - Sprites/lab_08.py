"""
First Drawing - Fishing Pond
Preston Chee
3/16/2023
CS 1400
"""
import random
import arcade
import math

# Constant Variables
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_FISH = 0.5
SPRITE_SCALING_SHOT = 1
FISH_COUNT = 50
SHOT_COUNT = 50

# Set Screen size
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# Bad Sprite
class Shot(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        # Constructor
        super().__init__(filename, sprite_scaling)

        # Set angle
        self.circle_angle = 0

        # Orbit radius
        self.circle_radius = 0

        # Orbit Speed
        self.circle_speed = 0.008

        # Orbits center point
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        # x and y change
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y

        # Set angle to speed
        self.circle_angle += self.circle_speed

# Good Sprite
class Fish(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)
        # Initiate change variables
        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the fish
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If object hits the edge of screen move in different direction
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

# Main game class
class MyGame(arcade.Window):

    def __init__(self):

        # Parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        # Sprite List Variables
        self.player_list = None
        self.fish_list = None
        self.shot_list = None
        self.good_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        # Hide mouse cursor
        self.set_mouse_visible(False)

        # Main background color set
        arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

        # Create sound variable
        # Sound from Kennel.nl
        self.gun_shot = arcade.load_sound("pistol.wav")

    # Main game setup
    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.fish_list = arcade.SpriteList()
        self.shot_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()

        # Set up the player
        # Image from Kennel.nl
        self.player_sprite = arcade.Sprite("duck.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the number of fishes to start off with
        for i in range(FISH_COUNT):

            # Create the fish instance
            # Image from Kennel.nl
            fish = Fish("fish.png", SPRITE_SCALING_FISH)

            # Set fish location
            fish.center_x = random.randrange(SCREEN_WIDTH)
            fish.center_y = random.randrange(SCREEN_HEIGHT)
            fish.change_x = random.randrange(-3, 4)
            fish.change_y = random.randrange(-3, 4)

            # Add the fish to list
            self.fish_list.append(fish)

        for j in range(SHOT_COUNT):
            # Create the fish instance
            # Image from Kennel.nl
            shot = Shot("shot.png", SPRITE_SCALING_SHOT / 3)

            # Set center of the circle the shot will orbit
            shot.circle_center_x = random.randrange(SCREEN_WIDTH)
            shot.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Set radius to range from 50 to 250
            shot.circle_radius = random.randrange(50, 250)

            # Start angle from 0 to 2pi
            shot.circle_angle = random.random() * 2 * math.pi

            self.shot_list.append(shot)

    # Draw subclass that creates the images
    def on_draw(self):

        arcade.start_render()
        self.fish_list.draw()
        self.player_list.draw()
        self.shot_list.draw()

        # Place text on screen for score and when the game end with final score
        if len(self.fish_list) > 0:
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        else:
            output = "Game Over"
            arcade.draw_text(output, (SCREEN_WIDTH / 2) - 50, SCREEN_HEIGHT / 2, arcade.color.RED, 20)
            output = f"Score: {self.score}"
            arcade.draw_text(output, (SCREEN_WIDTH / 2) - 25, (SCREEN_HEIGHT / 2) - 50, arcade.color.WHITE, 15)

    # Allow mouse movement
    def on_mouse_motion(self, x, y, dx, dy):

        # Allow the person to move the good sprite until all good sprites are gone
        if len(self.fish_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):

        # Keep updating until all good sprites are gone
        if len(self.fish_list) > 0:
            self.fish_list.update()
            self.shot_list.update()

        # create list of both good and bad sprites that collide with the player sprite
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
                arcade.play_sound(self.gun_shot)

# Main method
def main():
    # execute game
    window = MyGame()
    window.setup()
    arcade.run()


# Execute main method
main()
