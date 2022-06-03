import PySimpleGUI as sg

print(sg.Window('', [[sg.Input(), sg.Button('ok'), sg.Button('cancel')]]).read())