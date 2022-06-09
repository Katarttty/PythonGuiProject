import PySimpleGUI as sg
from time import time
from random import  randint

def convert_pos_to_Pixel(cell):
    tl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
    br = tl[0] + CELL_SIZE, tl[1] + CELL_SIZE
    return tl, br

def polace_apple():
    apple_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    while apple_pos in snake_body:
        apple_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    return apple_pos


# game constants
FILED_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FILED_SIZE / CELL_NUM
Score = 0

# sanke
snake_body = [(4,4),(3,4),(2,4)]
DIRECTIONS = {'left': (-1,0),'right': (1,0), 'up':(0,1), 'down':(0,-1)}
direction = DIRECTIONS['up']

#apple
apple_pos = polace_apple()
apple_eaten = False


sg.theme('Green')
field = sg.Graph(
    canvas_size=(FILED_SIZE, FILED_SIZE),
    graph_bottom_left=(0, 0),
    graph_top_right=(FILED_SIZE, FILED_SIZE),
    background_color='black'
)
layout = [[field],
          [sg.Text('Score:', font='Young 50'),
           sg.Text(Score, key='_SCORE_',font='Young 50')]
          ]

window = sg.Window('Snake', layout, return_keyboard_events=True)

start_time = time()
while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Left:37':
        direction = DIRECTIONS['left']
    if event == 'Up:38':
        direction = DIRECTIONS['up']
    if event == 'Right:39':
        direction = DIRECTIONS['right']
    if event == 'Down:40':
        direction = DIRECTIONS['down']

    time_since_start = time() - start_time
    if time_since_start >= 0.5:
        start_time = time()

        # apple snake collision
        if snake_body[0] == apple_pos:
            apple_pos = polace_apple()
            apple_eaten = True
            Score += 1
            window['_SCORE_'].update(Score)

        # snake update
        new_head = (snake_body[0][0] + direction[0], snake_body[0][1] + direction[1])
        snake_body.insert(0, new_head)
        if not apple_eaten:
            snake_body.pop()
        apple_eaten = False



        #  check death
        if not 0 <= snake_body[0][0] <= CELL_NUM - 1 or \
           not 0 <= snake_body[0][1] <= CELL_NUM - 1 or \
            snake_body[0] in snake_body[1:]:
            break


        field.DrawRectangle((0,0), (FILED_SIZE,FILED_SIZE), 'black')

        tl, br = convert_pos_to_Pixel(apple_pos)
        field.DrawRectangle(tl, br, 'red')



        # draw snake
        for index, part in enumerate(snake_body):
            tl, br = convert_pos_to_Pixel(part)
            color = 'yellow' if index == 0 else 'green'
            field.DrawRectangle(tl,br, color)



window.close()
