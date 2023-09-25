from pico2d import *


open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')



def handle_events():
    global running, move_x, direction,move_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
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

running = True
x = 800 // 2
y = 90
frame = 0
direction = 0;
move_x = 0
move_y = 0

# fill here
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*64,direction*64,64,64,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 9
    x += move_x * 5
    y += move_y * 5
    delay(0.05)

close_canvas()

