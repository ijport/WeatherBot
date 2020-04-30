import codebug_tether
import codebug_tether.sprites
import time

codebug = codebug_tether.CodeBug()

while True:
    if codebug.get_input('A') == 1:
        cbmessage = codebug_tether.sprites.StringSprite(("Banana"))
        for i in range(0,-70,-1):
            codebug.draw_sprite(i, 0, cbmessage)
            time.sleep(0.15)
        #codebug.draw_sprite(0, 0, cbmessage)
    if codebug.get_input('B') == 1:
        cbmessage = codebug_tether.sprites.StringSprite(("Done!"))
        for i in range(0,-70,-1):
            codebug.draw_sprite(i, 0, cbmessage)
            time.sleep(0.15)
        #codebug.draw_sprite(0, 0, cbmessage)
        break
