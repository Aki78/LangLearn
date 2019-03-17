import sys
import os
import PySimpleGUI as sg      
from gtts import gTTS
from pygame import mixer

mixer.init()
results = []
counter = 0
outerCounter = 0
correctWord = ""

layout = [[sg.Text('Start by pressing Read', font = ("Helvetica", 15) ,size = (80,1),key='text1')],      
          [sg.Text('', font = ("Helvetica", 15),text_color = "Magenta", size = (80,1),key='text2')],      
          [sg.Input(size = (80,1)),],      
          [sg.RButton('Read',bind_return_key = True) , sg.Exit()],
          [sg.Text(' ',size = (80,1),text_color = 'Red',font=("Helvetica",25) , key='text3')]]
window = sg.Window('Fill in alaviivia').Layout(layout)      

with open('Files/conjunction.txt') as inputfile:
    for line in inputfile:
#        if (counter % 3) == 1:
#            tts = gTTS(text=line.replace("@",""), lang='fi')
#            tts.save("text" + str(counter) + ".mp3")
        results.append(line.strip().split(' '))
        counter += 1
    
counter = 0
while True:
    event, values = window.Read()      
    for count in range(len(results)//3):
        EnLine = results[count * 3]
        FiLine = results[count * 3 + 1]
        for x in range(len(FiLine)):
            if '@' in FiLine[x]:
                correctWord = FiLine[x]
                FiLine[x] = "____"
        newLineEn = " ".join(x for x in EnLine) 
        newLineFi = " ".join(x for x in FiLine)

#             os.system("mpg321 Sounds/text" + str(count) + ".mp3" )
        itIsTrue = True
        while itIsTrue:
      #-------GUI--------------------------------------
            window.FindElement('text1').Update(newLineEn)
            window.FindElement('text2').Update(newLineFi)
            event, values = window.Read()      
            print(values)
            print(correctWord)
            if correctWord.replace("@","") == values[0]:
                itIsTrue = False
                mixer.music.load("Sounds/Correct.mp3")
                mixer.music.play()
                window.FindElement('text3').Update(' ')
            else:
#                mixer.music.load("Sounds/Wrong.mp3")
#                mixer.music.play()
                window.FindElement('text3').Update(correctWord)
            soundFile =  "Sounds/text" + str(count*3 + 1) +".mp3"
            os.system( "mpg321 " + soundFile )
    if event is None or event == 'Exit':      
        break


window.Close()
