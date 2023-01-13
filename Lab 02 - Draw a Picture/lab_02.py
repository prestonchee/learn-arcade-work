"""
First Drawing - Fishing Pond
Preston Chee
1/13/2023
CS 1400
"""

#import arcade library
import arcade

#open up a window from the arcade library
#name the window Lab_2
#set the window size
arcade.open_window(600, 600, "Lab_2")

#set main background color
arcade.set_background_color(arcade.color.DIRT)

# ready to draw
arcade.start_render()

#draw the Sky
arcade.draw_lrtb_rectangle_filled(0, 600, 600, 450, arcade.csscolor.SKY_BLUE)

#Draw a circle pond
arcade.draw_circle_filled(450, 250, 150, arcade.csscolor.DARK_CYAN)

#draw the fisherman
#head
arcade.draw_circle_filled(275, 300, 13, arcade.color.BLACK)
#body
arcade.draw_line(275, 250, 275, 300, arcade.color.BLACK, 4)
#left leg
arcade.draw_line(275, 250, 250, 225, arcade.color.BLACK, 4)
#right leg
arcade.draw_line(275, 250, 300, 225, arcade.color.BLACK, 4)
#right arm
arcade.draw_line(275, 265, 300, 280, arcade.color.BLACK, 4)

#fishing pole
arcade.draw_line(285, 250, 317, 310, arcade.color.BLACK_OLIVE, 3)
#fishing line
arcade.draw_line(317, 310, 400, 200, arcade.color.BLACK, 1)

#create Fish #1
#tail
arcade.draw_triangle_filled(450, 210, 450, 220, 445, 215, arcade.color.ORANGE)
#body
arcade.draw_ellipse_filled(440, 215, 13, 8, arcade.csscolor.ORANGE)


#finish drawing
arcade.finish_render()

#run until user closes
arcade.run()