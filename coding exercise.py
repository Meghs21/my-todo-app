import PySimpleGUI as sg
label1=sg.Text("Enter feet:")
label2=sg.Text("Enter inches:")
input1 = sg.Input("")
input2 = sg.Input("")
button1=sg.Button("convert")

window=sg.Window("Convertor",layout=[[label1,input1],[label2,input2],[button1]])

window.read()
window.close()

