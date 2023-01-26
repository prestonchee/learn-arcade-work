"""
Third Drawing - Fishing Pond with moving fish
Preston Chee
1/26/2023
CS 1400
"""

# import arcade library
import arcade

# open up a window from the arcade library
# name the window Lab_3
# set the window size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# draw the Sky
def draw_sky():
    arcade.draw_lrtb_rectangle_filled(0, 600, 600, 450, arcade.csscolor.SKY_BLUE)

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

#Draw fish that faces to the left
def draw_fish(x,y):
    arcade.draw_point(x, y, arcade.color.RED, 8)
    #Tail
    arcade.draw_triangle_filled(x, y, x, y + 10, x - 5, y + 5, arcade.color.ORANGE)
    # body
    arcade.draw_ellipse_filled(x - 10, y + 5, 13, 8, arcade.csscolor.ORANGE)

#Draw fish that faces to the right
def draw_fish_rev(x, y):
    # create fish #3
    arcade.draw_triangle_filled(x, y, x, y + 10, x + 5, y + 5, arcade.color.YELLOW)
    # body
    arcade.draw_ellipse_filled(x + 10, y + 5, 13, 8, arcade.color.YELLOW)

#Draw tree
def draw_tree():
    arcade.draw_rectangle_filled(120, 280, 20, 80, arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(((120, 360), (100, 320), (90, 280), (150, 280), (140, 320)), arcade.csscolor.DARK_GREEN)

# method that puts everything together
def on_draw(delta_time):
    # ready to draw
    arcade.start_render()

    draw_sky()
    draw_pond()
    draw_fisherman()
    draw_tree()
    draw_fish(on_draw.fish1_x, 200)

#increaase or decrease the fish position
#when fish hits desired x value reset the fish
    on_draw.fish1_x -= 1
    if (on_draw.fish1_x == 330):
        on_draw.fish1_x = 450

    draw_fish(on_draw.fish2_x , 150)
    on_draw.fish2_x -= 1
    if (on_draw.fish2_x == 350):
        on_draw.fish2_x = 540

    draw_fish_rev(on_draw.fish3_x , 260)
    on_draw.fish3_x += 1
    if (on_draw.fish3_x == 580):
        on_draw.fish3_x = 345

#fish x values set
on_draw.fish1_x = 450
on_draw.fish2_x = 540
on_draw.fish3_x = 345

#main method
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing With Functions")
    # ready to draw
    arcade.start_render()
    arcade.set_background_color(arcade.color.DIRT)

    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()