'''
# you use 'as' so you don't need to type out the import name each time.
import PySimpleGUI as sg

# the layout is a nested list and each nested list is a new row.
# you can add more in a elements in a row by adding it to the nested list.
layout = [
    [sg.Text('Text', enable_events=True, key= '-TEXT-'), sg.Spin(['item1', 'item 2'])],
    [sg.Button('Button', key = '-BUTTON1-')],
    # the key allows you to name two elemtes with the same name but a diffrent
    # keyword to  call in other lines. most keys ar in upper case preceded by a
    # _ and followed by a _
    [sg.Input(key= '-INPUT-')],
    [sg.Text('Test'), sg.Button('test button', key = '-BUTTON2-')]
]

window = sg.Window('converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-BUTTON1-':
        window['-TEXT-'].Update()
    if event == '-BUTTON2-':
        print('test pressed')
    if event == '-TEXT-':
        print('text pressed')

window.close()
'''


import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='_INPUT_'),
        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='_UNITS_'),
        sg.Button('Convert', key='_BUTTON1_')
    ],
    [sg.Text('Output', key='_OUTPUT_')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '_BUTTON1_':
        input_values = values['_INPUT_']
        if input_values.isnumeric():
            match values['_UNITS_']:
                case 'km to mile':
                    output = round(float(input_values) * 0.6214, 2)
                    output_string = f'{input_values} km are {output} miles'
                case 'kg to pound':
                    output = round(float(input_values) * 2.20462, 2)
                    output_string = f'{input_values} kg are {output} pound'
                case 'sec to min':
                    output = round(float(input_values) / 60, 2)
                    output_string = f'{input_values} sec are {output} min'
            window['_OUTPUT_'].update(output_string)
        else:
            window['_OUTPUT_'].Update('please enter a number')

window.close()