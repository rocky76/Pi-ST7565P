import st7565P
import time
import xglcd_font as font

wendy = font.XglcdFont('fonts/Wendy7x8.c', 7, 8)
glcd = st7565P.Glcd()
glcd.init()

for contrast in range(0, 64):
    glcd.clear_back_buffer()
    glcd.set_contrast(contrast)
    print("Contrast: {0} | {1}".format(contrast, hex(contrast)))
    glcd.draw_string("Contrast: {0} | {1}".format(contrast, hex(contrast)), wendy, 6, 2, spacing=0)
    glcd.fill_circle(64, 32, 16)
    glcd.flip()

    time.sleep(.1)
    

#glcd.cleanup()