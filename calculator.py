import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font= 'Franklin 18', button_element_size=(6,3))
    button_size = (6,3)
    layout = [
        [sg.Text(' ',
                 font='Franklin 26',
                 justification= 'right',
                 expand_x=True,
                 pad=(10, 5),
                 right_click_menu= theme_menu,
                 key='_TEXT_')
         ],
        [sg.Button('Enter', expand_x=True), sg.Button('C',expand_x=True)],
        [sg.Button(7, size=button_size), sg.Button(8, size=button_size), sg.Button(9, size=button_size), sg.Button('/', size=button_size)],
        [sg.Button(4, size=button_size), sg.Button(5, size=button_size), sg.Button(6, size=button_size), sg.Button('-', size=button_size)],
        [sg.Button(1, size=button_size), sg.Button(2, size=button_size), sg.Button(3, size=button_size), sg.Button('+', size=button_size)],
        [sg.Button(0, expand_x=True), sg.Button('.', size=button_size), sg.Button('*', size=button_size,)]
    ]
    return sg.Window('calculator', layout)


theme_menu = ['menu', ['LightBrown8', 'TealMono', 'Reds', 'random']]
window = create_window('dark')

current_num = []
full_operatrion = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0','1', '2','3', '4','5', '6','7', '8','9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['_TEXT_'].update(num_string)

    if event in ['+', '/', '-', '*']:
        full_operatrion.append(''.join(current_num))
        current_num = []
        full_operatrion.append(event)
        window['_TEXT_'].update('')

    if event == 'Enter':
        full_operatrion.append(''.join(current_num))
        result = eval(' '.join(full_operatrion))
        window['_TEXT_'].update(result)
        full_operatrion = []

    if event == 'C':
        current_num = []
        full_operatrion = []
        window['_TEXT_'].update(' ')

window.close()
