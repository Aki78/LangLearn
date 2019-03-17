import PySimpleGUI as sg      

layout = [[sg.Text('Click read to ___ the input value',key='text')],      
          [sg.Input()],      
          [sg.RButton('Read',bind_return_key = True) , sg.Exit()]]      

window = sg.Window('Fill alaviivia').Layout(layout)      

while True:      
    event, values = window.Read()      
    window.FindElement('text').Update(values[0])
    if event is None or event == 'Exit':      
        break      
    print(event, values)   
