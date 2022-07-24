import json

import PySimpleGUI as sg
from time import time
from random import randint

filename = 'score.json'

with open(filename) as openfile:
    score_trcker = json.load(openfile)


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
speed = 0.5

highscore_values = score_trcker.values()
highscore_player = score_trcker
highscore_list = list(highscore_values)
highscore_list_player = list(highscore_player)
highscore = highscore_list_player[0], highscore_list[0]

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
          [
            sg.Text('Score:', font='Young 50'),
            sg.Text(Score, key='_SCORE_',font='Young 50')
           ],
          [
            sg.Text('Highest Score', key='_HIGHTSCORE_',font='Young 50')
          ],
          [
            sg.Text(highscore_list_player[0], key='_HIGHTSCORE_',font='Young 20'),
            sg.Text(': ', key='_HIGHTSCORE_',font='Young 20'),
            sg.Text(highscore_list[0], key='_HIGHTSCORE_',font='Young 20')]
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
    if time_since_start >= speed:
        start_time = time()

        # apple snake collision
        if snake_body[0] == apple_pos:
            apple_pos = polace_apple()
            apple_eaten = True
            speed -= 0.02
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
            print('Final Score: ', Score)


            player_name = input('Enter Name:')
            score_trcker[player_name] = Score
            score_trcker = sorted(score_trcker.items(), key=lambda x: x[1], reverse=True)
            sortdict = dict(score_trcker)
            with open(filename, 'w') as openfile:
                json.dump(sortdict, openfile, indent=4)
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
