import os
from os import system
import sys

ffmpeg = 'Lib\\ffmpeg-20200415-51db0a4-win64-static\\bin\\ffmpeg.exe'
you_get = 'venv\\Scripts\\you-get.exe'

# test for exceptions in arguments format
args = sys.argv
if len(args) == 1:
    print('Must provide filepath to input text document')
    exit()
if len(args) > 2:
    print('Received more arguments than epected. Expects: [String]')
    exit()
if not os.path.exists(args[1]):
    print('Could not find path to input file: ' + args[1])
    exit()


with open(args[1]) as f:    # reads input file
    inputs = []
    for line in f:
        inputs.append(line.strip('\n'))


for i in range(len(inputs)):    # downloads all inputs into vids/inputs/
    system(you_get + ' -o vids\\inputs -O input'+str(i) + ' ' + inputs[i])
downloaded = 0
for i in range(len(os.listdir('vids\\inputs'))):   # checks number of sucessfully downloaded files
    downloaded += 1
if downloaded < len(inputs):
    print('Failed to download ' + str(len(inputs) - downloaded) + " inputs.")


inters = ''
for i in range(downloaded):    # converts all inputs into .mpg file format, places in vids/inters/
    system(ffmpeg + " -y -i vids\\inputs\\input"+str(i)+".mp4 -qscale:v 1 vids\\inters\\inter"+str(i)+".mpg")
    inters += 'vids\\inters\\inter'+str(i)+'.mpg|'
inters = inters[:-1]


# combines inter files into one, and converts into .mp4 file format
system(ffmpeg + " -y -i concat:\""+inters+"\" -c copy vids\\inters\\inter.mpg")
system(ffmpeg + " -y -i vids\\inters\\inter.mpg -qscale:v 2 vids\\out.mp4")


# cleans all input and inter files
for i in range(downloaded):
    os.remove('vids\\inputs\\input'+str(i)+'.mp4')
    os.remove('vids\\inters\\inter'+str(i)+'.mpg')
    os.remove('vids\\inters\\inter.mpg')

print('Operation completed. Output file found under vids\\out.mp4')