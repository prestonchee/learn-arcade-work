import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 1

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           scale=0.6)
        self.player_sprite.center_x = 432
        self.player_sprite.center_y = 301
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        # border wall
        # bottom wall
        for x in range(380, 1596, 32):
            border_wall = arcade.Sprite("outer-wall.png", 2)
            border_wall.center_x = x
            border_wall.center_y = 250
            self.wall_list.append(border_wall)
            # left wall
            for x in range(250, 1364, 32):
                border_wall = arcade.Sprite("outer-wall.png", 2)
                border_wall.center_x = 380
                border_wall.center_y = x
                self.wall_list.append(border_wall)
            # right wall
            for x in range(250, 1364, 32):
                border_wall = arcade.Sprite("outer-wall.png", 2)
                border_wall.center_x = 1564
                border_wall.center_y = x
                self.wall_list.append(border_wall)
            # top wall
            for x in range(380, 1596, 32):
                border_wall = arcade.Sprite("outer-wall.png", 2)
                border_wall.center_x = x
                border_wall.center_y = 1348
                self.wall_list.append(border_wall)

        # Table walls
        for i in range(440, 1536, 63):
            for j in range(314, 1236, 70):
                table_wall_list = [[i, j]]
                for coordinate in table_wall_list:
                    wall = arcade.Sprite("table.png", .1)
                    wall.center_x = coordinate[0]
                    wall.center_y = coordinate[1]
                    # bottom row - row 0
                    if 760 > i > 500 or 820 < i < 940 or 1000 < i < 1500:
                        if 330 < j < 400:
                            self.wall_list.append(wall)
                    # row 1
                    if 550 > i > 440 or 650 < i < 850 or 1000 < i < 1250 or 1300 < i < 1536:
                        if 470 < j < 540:
                            self.wall_list.append(wall)
                    # row 2
                    if 400 < i < 850 or 950 < i < 1200 or 1250 < i < 1500:
                        if 610 < j < 680:
                            self.wall_list.append(wall)
                    # row 3
                    if 500 < i < 750 or 900 < i < 1100 or 1200 < i < 1350:
                        if 750 < j < 830:
                            self.wall_list.append(wall)
                    # row 4
                    if 600 < i < 850 or 950 < i < 1300 or 1400 < i < 1536:
                        if 900 < j < 970:
                            self.wall_list.append(wall)
                    # row 5
                    if 400 < i < 1200:
                        if 1040 < j < 1110:
                            self.wall_list.append(wall)
                    # row 6
                    if 500 < i < 750 or 900 < i < 1100 or 1200 < i < 1350 or 1400 < i < 1536:
                        if 1180 < j < 1250:
                            self.wall_list.append(wall)

        # Add chairs
        chair_list = [[550, 525],
                      [950, 525],
                      [1370, 805],
                      [1212, 805],
                      [820, 805],
                      [500, 945],
                      [1370, 1085],
                      [1400, 1085],
                      [1005, 1160]]
        for coordinate in chair_list:
            chair = arcade.Sprite("chair.png", .102)
            chair.center_x = coordinate[0]
            chair.center_y = coordinate[1]
            self.wall_list.append(chair)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.FLORAL_WHITE)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
