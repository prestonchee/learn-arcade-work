"""
food collecting game
Preston Chee
3/20/2023
CS 1400
"""
import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NOM NOM GAME"
NUMBER_OF_FOOD = 20
SERVER_NUM = 10
PIE_SPEED = 5

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# camera pan speed
CAMERA_SPEED = 0.1

# Character speed
PLAYER_MOVEMENT_SPEED = 5

class Server(arcade.Sprite):

    def reset_pos(self):
        self.center_x = random.randrange(380,
                                         1564)
        self.center_y = random.randrange(250, 1348)

    def update(self):

        self.center_x += 1

        if self.right > 1570:
            self.reset_pos()


#  game class
class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.food_list = None
        self.server_list = None
        self.pie_list = None

        # Set up the player
        self.player_sprite = None
        self.life = 3
        self.score = 0

        # Physics engine
        self.physics_engine = None

        # Key press tracker
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.space_pressed = False

        # Create cameras.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Initialized noise variable
        # sound produced by me
        self.bite = arcade.load_sound("bite.wav")

    # setup walls and sprites
    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.food_list = arcade.SpriteList()
        self.server_list = arcade.SpriteList()
        self.pie_list = arcade.SpriteList()

        # Set up the player
        # player image found from Kenny.nl
        self.player_sprite = arcade.Sprite("adventurer.png",
                                           scale=0.6)
        self.player_sprite.center_x = 432
        self.player_sprite.center_y = 301
        self.player_list.append(self.player_sprite)

        # border walls
        # bottom wall, outer wall.png taken from Kenney.nl
        for x in range(380, 1596, 32):
            border_wall = arcade.Sprite("outer-wall.png", 2)
            border_wall.center_x = x
            border_wall.center_y = 250
            self.wall_list.append(border_wall)
            # left wall
            for y in range(250, 1364, 32):
                border_wall = arcade.Sprite("outer-wall.png", 2)
                border_wall.center_x = 380
                border_wall.center_y = y
                self.wall_list.append(border_wall)
            # right wall
            for z in range(250, 1364, 32):
                border_wall = arcade.Sprite("outer-wall.png", 2)
                border_wall.center_x = 1564
                border_wall.center_y = z
                self.wall_list.append(border_wall)
            # top wall
            for n in range(380, 1596, 32):
                border_wall = arcade.Sprite("outer-wall.png", 2)
                border_wall.center_x = n
                border_wall.center_y = 1348
                self.wall_list.append(border_wall)

        # Table walls
        # run through each range for the x and y coordinates
        for i in range(440, 1536, 63):
            for j in range(314, 1236, 70):
                table_wall_list = [[i, j]]
                # table.png taken from freepik.com
                for coordinate in table_wall_list:
                    wall = arcade.Sprite("table.png", .1)
                    wall.center_x = coordinate[0]
                    wall.center_y = coordinate[1]
                    # create conditions to place tables in a range going row by row
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
        # Second obstacles placed by a list
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
            # chair.png taken from freepik.com
            chair = arcade.Sprite("chair.png", .102)
            chair.center_x = coordinate[0]
            chair.center_y = coordinate[1]
            self.wall_list.append(chair)

        for i in range(random.randrange(20, 40)):
            # sushi.png taken from pngtree.com
            food = arcade.Sprite("sushi.png", .06)

            food_placed_success = False

            # place the food as long as it does not overlap with the walls or obstacles
            while not food_placed_success:

                food.center_x = random.randrange(400, 1536)
                food.center_y = random.randrange(314, 1364)

                wall_hit_list = arcade.check_for_collision_with_list(food, self.wall_list)

                food_hit_list = arcade.check_for_collision_with_list(food, self.food_list)

                if len(wall_hit_list) == 0 and len(food_hit_list) == 0:

                    food_placed_success = True

            self.food_list.append(food)

        for z in range(SERVER_NUM):

            server = Server("server.png", scale=0.022)

            server.center_x = random.randrange(380, 1564)
            server.center_y = random.randrange(250, 1348, 64)

            self.server_list.append(server)

        # keeps the player from going through walls
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.FLORAL_WHITE)

    # things to draw on screen
    def on_draw(self):

        # make sure that it starts clean
        self.clear()

        # main camera that draws sprites
        self.camera_sprites.use()

        # Draw sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.food_list.draw()
        self.server_list.draw()
        self.pie_list.draw()

        # displays our gui on screen
        self.camera_gui.use()

        # Draw score in bottom corner until all food is gone
        if len(self.food_list) > 0:
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)
        # once food is gone display game over and the final score
        else:
            output = "Game Over"
            arcade.draw_text(output, (SCREEN_WIDTH / 2) - 50, SCREEN_HEIGHT / 2, arcade.color.RED, 20)
            output = f"Score: {self.score}"
            arcade.draw_text(output, (SCREEN_WIDTH / 2) - 25, (SCREEN_HEIGHT / 2) - 50, arcade.color.BLACK, 15)

    def on_key_press(self, key, modifiers):

        # once the food list is empty allow for no more input
        if len(self.food_list) > 0 or self.life > 0:
            if key == arcade.key.UP:
                self.up_pressed = True
            elif key == arcade.key.DOWN:
                self.down_pressed = True
            elif key == arcade.key.LEFT:
                self.left_pressed = True
            elif key == arcade.key.RIGHT:
                self.right_pressed = True
            elif key == arcade.key.SPACE:
                self.space_pressed = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.SPACE:
            self.space_pressed = False
            pie = arcade.Sprite("pie.png", .03)

            pie.center_x = self.player_sprite.center_x
            pie.bottom = self.player_sprite.center_y
            pie.change_x = PIE_SPEED

            self.pie_list.append(pie)

    def on_update(self, delta_time):

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        self.server_list.update()
        self.pie_list.update()

        # how fast to adjust player position change based of off movement speed
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Check to see if player has collided with a food item
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.food_list)
        bad_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.server_list)

        # if the player has collided remove the food and increase score, also make a noise.
        for food in hit_list:
            food.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.bite)

        for server in bad_list:
            server.reset_pos()
            self.life -= 1

        for pie in self.pie_list:
            shot_list = arcade.check_for_collision_with_list(pie, self.server_list)

            for server in shot_list:
                server.reset_pos()

            if len(shot_list) > 0:
                pie.remove_from_sprite_lists()

            if pie.bottom > SCREEN_WIDTH:
                pie.remove_from_sprite_lists
        # update all sprites
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):

        # scroll camera to the player
        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        # adjust the window to same size as the camera moves with player

        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


main()
