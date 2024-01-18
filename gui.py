import functions
import PySimpleGUI as sg

label=sg.Text("TYPE IN A TO-DO:")
input_box=sg.InputText(tooltip="Enter todo")
add_button=sg.Button("ADD")
window=sg.Window("My To-Do App", layout=[[label],[input_box,add_button]])
window.read()
window.close()
