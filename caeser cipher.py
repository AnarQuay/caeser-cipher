from pprint import pprint #debugging - prints lists in a nicer format
from typing import List #allows me to set the type of data in lists
from appJar import gui

#app gui config
app = gui("Caesar Cipher")
app.addLabel("title1", "Encrypter and Decrypter")
app.addLabelEntry("Text to be encoded/decoded")
app.addLabelEntry("offset")
app.addOptionBox("encode/decode",["encode","decode"])
app.addLabel("title2", "Encoded/Decoded text: ")
app.setSize("400x400")

#variables
item = ''
library = 'abcdefghijklmnopqrstuvwxyz'
LIBRARY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#indexing function
def getIndex(array, target):
    index = 0
    for item in array:
        if item != target:
            index += 1
        else:
            break
    return index

#word spitting function
def splitter(input, output):
    for cha in input:
        output.append(cha)
#pprint(ssplit)

#checks whether the input is a letter
def isletter(letter):
    if letter in library or letter in LIBRARY:
        return True
    else:
        return False

#checks if the letter is uppercase or lowercase
def isLower(letter):
    if letter in library:
        return True
    else:
        return False

#encrypts or decrypts input1 and outputs newList
def moving(ssplit : List[str], moveby, library : List[str], LIBRARY : List[str]):    #get place of each letter in ssplit and add number moveby to its place in library
    newList = []
    for item in ssplit: #run for each letter in the word
        if isletter(item):
            if isLower(item):
                place = getIndex(library, item)
                place += moveby
                if place >= 26:
                    place = place % -26
                if place <= -1:
                    place = place % 26
                item = library[place]
                #print("%s %d"%(item, place))
                newList.append(item) #add to the end of the list
            else:
                place = getIndex(LIBRARY, item)
                place += moveby
                if place >= 26:
                    place = place % -26
                if place <= -1:
                    place = place % 26
                item = LIBRARY[place]
                #pprint("%s %d"%(item, place))
                newList.append(item) #add to the end of the list
        else:
            newList.append(item) #when not letter add to the compiler list
    return newList  #outputs the compiled encoded or decoded text

#on button press
def onButtonPress():
    global library, LIBRARY, input1, Offset
    
    #decide whether encoding
    if ('encode') == str(app.getOptionBox("encode/decode")):
        PreEncoding = True
    else:
        PreEncoding = False

    #get the value for ssplit and moveby
    input1 = str(app.getEntry("Text to be encoded/decoded")) 
    ssplit : List[str] = []
    isEncoding = PreEncoding
    
    #converts letters to the integer offset amount
    preOffset = 0
    preOffset = str(app.getEntry("offset"))
    if isletter(preOffset):
        if isLower(preOffset):
            preOffset = getIndex(library, preOffset) + 1
        else:
            preOffset = getIndex(LIBRARY, preOffset) + 1
    else:
        preOffset = int(app.getEntry("offset"))

    Offset = preOffset #shifting from initial offset to completed offset
    if not isEncoding: Offset *= -1    #makes the integer offset negative if the app drop down is set to decode
    splitter(input1,ssplit)  #ssplit is modified

    #updates the app gui to show the encoded or decoded text
    CL = moving(ssplit, Offset, library, LIBRARY)  #encoding/decoding function 
    print(''.join(CL))
    CCL = (''.join(CL)) #compiled completed list = compiling completed list
    app. setLabel("title2","Encoding/Decoding Complete: "+str(CCL))


app.addButton("Process", onButtonPress) #adds button that runs the code within the gui
app.go()    #runs the app gui