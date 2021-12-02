"""
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
"""
import arcade
import math
SH = 260
SW = SH*1.9
stripe = int(SH/13)
arcade.open_window(SW, SH, "The Stars and Stripes", True)
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

#Red Stripes
for i in range(int(stripe/2), SH+1, int(2*stripe)):
    arcade.draw_rectangle_filled(SW/2, i, SW, stripe, (191, 10, 48))


#Blue Field
arcade.draw_rectangle_filled((0.76 * SH)/2, (9.5/13*SH), 0.76 * SH, (7/13 * SH), (0, 40, 104))


#Stars
for i in range(50):
    if i <= 5:
        SY = SH - SH * 0.054
        SX = SH * 0.063 + i * (2 * SH * .063)
    elif 5 < i <= 10:
        SY = SH - 2 * SH * 0.054
        SX = 2 * SH * 0.063 + (i - 6) * (2 * SH * .063)
    elif 10 < i <= 16:
        SY = SH - 3 * SH * .054
        SX = SH * .063 + (i-11) * (2 * SH * .063)
    elif 16 < i <= 21:
        SY = SH - 4 * SH * 0.054
        SX = 2 * SH * 0.063 + (i - 17) * (2 * SH * .063)
    elif 21 < i <= 27:
        SY = SH - 5 * SH * 0.054
        SX = SH * 0.063 + (i - 22) * (2 * SH * .063)
    elif 27 < i <= 32:
        SY = SH - 6 * SH * 0.054
        SX = 2 * SH * 0.063 + (i - 28) * (2 * SH * .063)
    elif 32 < i <= 38:
        SY = SH - 7 * SH * 0.054
        SX = SH * 0.063 + (i - 33) * (2 * SH * .063)
    elif 38 < i <= 43:
        SY = SH - 8 * SH * 0.054
        SX = 2 * SH * 0.063 + (i - 39) * (2 * SH * .063)
    else:
        SY = SH - 9 * SH * 0.054
        SX = SH * 0.063 + (i - 44) * (2 * SH * .063)
    arcade.draw_polygon_filled([
        [(SH * 0.0616) / 6 * math.cos(math.radians(54)) + SX, (SH*0.0616)/6 * math.sin(math.radians(54))+SY],
        [SH * 0.0616 / 2 * math.cos(math.radians(90)) + SX, SH*0.0616/2 * math.sin(math.radians(90)) + SY],
        [(SH * 0.0616) / 6 * math.cos(math.radians(126)) + SX, (SH * 0.0616) / 6 * math.sin(math.radians(126)) + SY],
        [SH * 0.0616 / 2 * math.cos(math.radians(162)) + SX, SH*0.0616/2 * math.sin(math.radians(162)) + SY],
        [(SH * 0.0616) / 6 * math.cos(math.radians(198)) + SX, (SH * 0.0616) / 6 * math.sin(math.radians(198)) + SY],
        [SH * 0.0616 / 2 * math.cos(math.radians(234)) + SX, SH * 0.0616 / 2 * math.sin(math.radians(234)) + SY],
        [(SH * 0.0616) / 6 * math.cos(math.radians(270)) + SX, (SH * 0.0616) / 6 * math.sin(math.radians(270)) + SY],
        [SH * 0.0616 / 2 * math.cos(math.radians(306)) + SX, SH * 0.0616 / 2 * math.sin(math.radians(306)) + SY],
        [(SH * 0.0616) / 6 * math.cos(math.radians(342)) + SX, (SH * 0.0616) / 6 * math.sin(math.radians(342)) + SY],
        [SH * 0.0616 / 2 * math.cos(math.radians(18)) + SX, SH * 0.0616 / 2 * math.sin(math.radians(18)) + SY]
        ], arcade.color.WHITE)


arcade.finish_render(),
arcade.run()
