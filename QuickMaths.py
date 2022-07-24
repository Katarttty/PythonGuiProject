import random
import PySimpleGUI as sg

correct = 0
incorrect = 0

sg.theme('GrayGrayGray')
layout = [
    [
        sg.Text('', key='_EQUATION_'),
        sg.Input('', key='_GUESS_'),
        sg.Button('Enter', key='_BUTTON2_')
    ],
    [
        sg.Text('', key='_ANSWER_'),
        sg.Button('Start', key='_BUTTON_'),
        sg.Text(
            f'Correct {correct}: Incorrect {incorrect}',
            key='_SCORE_'
                )

    ]
]

window = sg.Window('Simple Maths', layout)


while True:
    event, values = window.read()
    result = 0
    incorrectt = 0
    if event == sg.WIN_CLOSED:
        break
    if event == '_BUTTON_':

        first_num = random.randint(1, 100)
        second_num = random.randint(1, 100)
        window['_BUTTON_'].update('Next')
        if first_num >= second_num:
            evaluation_symb = random.randint(1, 4)
            if evaluation_symb == 1:
                equation = f'{first_num} + {second_num}'
                result = first_num + second_num
                window['_EQUATION_'].update(equation)
            elif evaluation_symb == 2:
                equation = f'{first_num} - {second_num}'
                result = first_num - second_num
                window['_EQUATION_'].update(equation)
            elif evaluation_symb == 3:
                equation = f'{first_num} * {second_num}'
                result = first_num * second_num
                window['_EQUATION_'].update(equation)
            elif evaluation_symb == 4:
                equation = f'{first_num} / {second_num}'
                result = round(float(first_num / second_num), 2)
                window['_EQUATION_'].update(equation)

        elif first_num <= second_num:
            evaluation_symb = random.randint(1, 4)
            if evaluation_symb == 1:
                equation = f'{second_num} + {first_num}'
                result = second_num + first_num
                window['_EQUATION_'].update(equation)
            elif evaluation_symb == 2:
                equation = f'{second_num} - {first_num}'
                result = second_num - first_num
                window['_EQUATION_'].update(equation)
            elif evaluation_symb == 3:
                equation = f'{second_num} * {first_num}'
                result = second_num * first_num
                window['_EQUATION_'].update(equation)
            elif evaluation_symb == 4:
                equation = f'{second_num} / {first_num}'
                result = round(float(second_num / first_num), 2)
                window['_EQUATION_'].update(equation)

    if event == '_BUTTON2_':
        input_Value = values['_GUESS_']
        input_Value = float(input_Value)
        if input_Value == result:
            correctt = f'Correct {result}'
            correct += 1
            window['_ANSWER_'].update(correctt)
            window['_SCORE_'].update(f'Correct {correct}'
                                     f': Incorrect {incorrect}')
        elif input_Value != result:
            incorrectt = f'incorrect {result}'
            print(result)
            incorrect += 1
            window['_ANSWER_'].update(incorrectt)
            window['_SCORE_'].update(f'Correct {correct}'
                                     f': Incorrect {incorrect}')
        else:
            window['_ANSWER_'].update(incorrectt)

window.close()
