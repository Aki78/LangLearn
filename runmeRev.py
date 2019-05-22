import sys
import random
import os
import PySimpleGUI as sg      
from gtts import gTTS
from pygame import mixer

mixer.init()
results = []
counter = 0
outerCounter = 0
correctWord = ""
count = 0

filename = sys.argv[1]  # "somethingRev.txt"

layout = [[sg.Text('Start by pressing Read', font = ("Helvetica", 15) ,size = (40,1),key='text1')],      
          [sg.Text('', font = ("Helvetica", 15),text_color = "Magenta", size = (40,1),key='text2')],      
          [sg.Input(size = (60,1)),],      
          [sg.RButton('Read',bind_return_key = True) , sg.Exit()],
          [sg.Text(' ',size = (40,1),text_color = 'Red',font=("Helvetica",25) , key='text3')]]
window = sg.Window('Fill in alaviivia').Layout(layout)      

with open('Files/' + filename) as inputfile:
    for line in inputfile:
        if (counter % 3) == 0: #
            tts = gTTS(text=line.replace("@", "").replace("_", " "), lang='fi') #
            tts.save("Sounds/text" + str(counter) + ".mp3") #
        results.append(line.strip().split(' '))
        counter += 1
    
counter = 0
myNumList = []
while True:
    event, values = window.Read()      
#    for count in range(len(results)//3):
    while True:
#        count = random.randint(0, len(results)//3)
        myNumList = list(range(len(results)//3 + 1))
        while myNumList != []:
            count = random.choice(myNumList)
            soundFile =  "Sounds/text" + str(count*3 ) +".mp3"
            os.system( "mpg321 " + soundFile )
            print(myNumList)
            print(count)
            if count in myNumList:
                myNumList.remove(count)
            EnLine = results[count * 3]
            FiLine = results[count * 3 + 1].copy()
            for x in range(len(FiLine)):
                if '@' in FiLine[x]:
                    correctWord = FiLine[x].replace("_", " ")
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
                if correctWord.replace("@","") == values[0]:
                    itIsTrue = False
#                    mixer.music.load("Sounds/Correct.mp3")
#                    mixer.music.play()
                    window.FindElement('text3').Update(' ')
                else:
                    window.FindElement('text3').Update(correctWord)
    if event is None or event == 'Exit':      
        break


window.Close()
