from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('character.png')



def handle_events():
    global running, move_x, direction, move_y, Move_nothing

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            Move_nothing = False
            if event.key == SDLK_RIGHT:
                move_x += 1
                direction = 0
            elif event.key == SDLK_LEFT:
                move_x -= 1
                direction = 2
            if event.key == SDLK_UP:
                move_y += 1
                direction = 3
            elif event.key == SDLK_DOWN:
                move_y -= 1
                direction = 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            Move_nothing = True
            if event.key == SDLK_RIGHT:
                move_x -= 1
                direction = 0
            elif event.key == SDLK_LEFT:
                move_x += 1
                direction = 2
            elif event.key == SDLK_UP:
                move_y -= 1
                direction = 3
            elif event.key == SDLK_DOWN:
                move_y += 1
                direction = 1
        else:
            Move_nothing = True


running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
direction = 0;
move_x = 0
move_y = 0
Move_nothing = False
move_shape = 100
# fill here
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame*64,direction*64,64,64,x,y,100,move_shape)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 9
    if Move_nothing:
        # Move_nothing 활성화 시 move_shape 조절
        move_shape = (move_shape -1)%20+80
    else:
        move_shape = 100




    if(x>TUK_WIDTH):
        x = TUK_WIDTH
    elif(x<0):
        x = 0
    else:
        x += move_x * 5

    if (y > TUK_HEIGHT):
        y = TUK_HEIGHT
    elif (y < 0):
        y = 0
    else:
        y += move_y * 5

    delay(0.05)

close_canvas()

