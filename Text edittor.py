import PySimpleGUI as sg
from pathlib import Path

smiley = [
    'happy', [';)', ':)', 'XD', ':D', '<3'],
    'sad', [':(', 'T_T'],
    'Other', [':3']
]
smiley_evenet = smiley[1] + smiley[3] + smiley[5]

menu_layout = [
    ['File', ['open', 'save', '---', 'exit']],
    ['tools',['Word Count']],
    ['Add', smiley]
]

sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untiltled', key='_DOCNAME_')],
    [sg.Multiline(no_scrollbar=True, size=(50, 40), key='_TEXTBOX_')]
]

window = sg.Window('Text Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'open':
        file_path = sg.popup_get_file('open', no_window=True)
        if file_path:
            file = Path(file_path)
            window['_TEXTBOX_'].update(file.read_text())
            window['_DOCNAME_'].update(file_path.split('/')[-1])

    if event == 'save':
        file_path = sg.popup_get_file('Save as', no_window= True, save_as=True)
        file = Path(file_path)
        file.write_text(values['_TEXTBOX_'])
        window['_DOCNAME_'].update(file_path.split('/')[-1])

    if event == 'Word Count':
        full_text = values['_TEXTBOX_']
        cleantext = full_text.replace('\n', ' ').split(' ')
        word_count = len(cleantext)
        char_count = len(' '.join(cleantext))
        sg.popup(f'words {word_count}\ncharecters: {char_count}')

    if event in smiley_evenet:
        current_values = values['_TEXTBOX_']
        new_text = current_values + ' ' + event
        window['_TEXTBOX_'].update(new_text)

window.close()
