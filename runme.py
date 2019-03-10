import sys
import random

results = []
counter = 0
with open('Files/testSentences.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(' '))

while True:
    for count in range(len(results)):
        sys.stdout.write("\033[0;0m")
        line = results[count]
        if (count % 3) == 0:
            for words in line:
                sys.stdout.write(words)
                sys.stdout.write(" ")
            sys.stdout.write("\n")
        if (count % 3) == 1:
            randint = random.randint(0, len(line)-1)
            counter = 0
            for words in line:
                if(counter == randint):
                    sys.stdout.write('___')
                    sys.stdout.write(" ")
                else:
                    sys.stdout.write(words)
                    sys.stdout.write(" ")
                counter += 1
            text = input(": ")
            if(text==line[randint]):
                sys.stdout.write("\033[1;36m")
                print(text==line[randint])
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            else:
                sys.stdout.write("\033[1;31m")
                print(text==line[randint])
                print(line[randint])
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
