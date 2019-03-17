import sys
import os
from gtts import gTTS
from pygame import mixer

mixer.init()
results = []
counter = 0
outerCounter = 0
with open('Files/conjunction.txt') as inputfile:
    for line in inputfile:
#        if (counter % 3) == 1:
#            tts = gTTS(text=line.replace("@",""), lang='fi')
#            tts.save("text" + str(counter) + ".mp3")
        results.append(line.strip().split(' '))
        counter+=1

counter = 0
while True:
    for count in range(len(results)):
        sys.stdout.write("\033[0;0m")
        line = results[count]
        if (count % 3) == 0:
            for words in line:
                sys.stdout.write(words)
                sys.stdout.write(" ")
            sys.stdout.write("\n")
        outerCounter = 0
        isThisTrue = True
        if (count % 3) == 1:
            while isThisTrue:
                counter = 0
                for words in line:
                    if('@' in words):
                        sys.stdout.write('___')
                        sys.stdout.write(" ")
                        outerCounter = counter
                    else:
                        sys.stdout.write(words)
                        sys.stdout.write(" ")
                    counter += 1
                text = input("\n: ")
                if(text == line[outerCounter].replace("@", "")):
                    isThisTrue = False
                    mixer.music.load("Sounds/Correct.mp3")
                    mixer.music.play()
                    sys.stdout.write("\033[1;36m")
                    print(text == line[outerCounter].replace("@", ""))
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                else:
                    mixer.music.load("Sounds/Wrong.mp3")
                    mixer.music.play()
                    sys.stdout.write("\033[1;31m")
                    print(text == line[outerCounter])
                    print(line[outerCounter])
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            os.system("mpg321 Sounds/text" + str(count) + ".mp3" )
