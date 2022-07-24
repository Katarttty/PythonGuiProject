import PySimpleGUI as sg
from time import time

def create_window():

    sg.theme('black')
    layout = [
        [sg.Push(), sg.Image('cross.png', pad=0, enable_events=True, key='_CLOSE_')],
        [sg.VPush()],
        [sg.Text('', font='Young 50', key='_TIME_')],
        [
            sg.Button('Start', button_color=('#FFFFFF', '#FF1256'), border_width=0, key='_START_'),
            sg.Button('Lap', button_color=('#FFFFFF', '#FF1256'), border_width=0, key='_LAP_', visible=False)],
        [sg.Column([[]], key='_LAPS_')],
        [sg.VPush()]
    ]
    return sg.Window(
        'Stopwatch',
        layout,
        size=(300, 300),
        no_titlebar=True,
        element_justification='center'
    )

window = create_window()
start_time = 0
active = False
laps_ammout = 1

while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, '_CLOSE_'):
        break
    if event == '_START_':
        if active:
            active = False
            window['_START_'].update('Reset')
            window['_LAP_'].update(visible=False)
        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                laps_ammout = 1
            else:
                start_time = time()
                active = True
                window['_START_'].update('Stop')
                window['_LAP_'].update(visible=True)
    if active:
        elapsed_time = round(time() - start_time, 1)
        window['_TIME_'].update(elapsed_time)

    if event == '_LAP_':
        window.extend_layout(window['_LAPS_'], [[sg.Text(laps_ammout), sg.VSeparator(), sg.Text(elapsed_time)]])
        laps_ammout  += 1

window.close()