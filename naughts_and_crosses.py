
import PySimpleGUI as sg

layout = [[sg.Text("Hello")], [sg.Button("ok")]]

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()

    if event == "ok" or event == sg.WIN_CLOSED:
        break

window.close()

