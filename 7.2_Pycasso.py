'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
SW = 500
SH = 400
#Start of the picture
arcade.open_window(SW, SH, "Zachary Blum's Flappy Bird", True)
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

for i in range(0, SW+1, 20):
    arcade.draw_line(i, 0, i, 400, arcade.color.BLACK)
    arcade.draw_line(0, i, 500, i, arcade.color.BLACK)

#Wings, Body, and Mouth
arcade.draw_circle_filled(SW/2, SH/2, 150, arcade.color.YELLOW, 0)
arcade.draw_ellipse_filled(SW/2+100, SH/2-30, 200, 75, arcade.color.CYBER_YELLOW, 180, 0)
arcade.draw_ellipse_filled(SW/4, SH/2, 150, 75, arcade.color.ORANGE, 180, 0)



#Eye
arcade.draw_circle_filled(SW/2, SH/2+40, 50, arcade.color.WHITE, 0)
arcade.draw_ellipse_filled(SW/2, SH/2+40, 30, 50, arcade.color.BLACK, 180, 0)

arcade.draw_line(SW/2+30, SH/2-30, SW/2+200, SH/2-30, arcade.color.BLACK, 1)
arcade.finish_render()
arcade.run()
