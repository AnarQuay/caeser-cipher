from pprint import pprint
from typing import List
from appJar import gui

app = gui("Caeser Cipher")
app.addLabel("title1", "Encrypter and Decrypter")
app.addLabelEntry("Text to be encoded/decoded")
app.addLabelEntry("offset")
app.addOptionBox("encode/decode",["encode","decode"])
app.addLabel("title2", "Encoded/Decoded text: ")
app.setSize("400x400")
item = ''
library = 'abcdefghijklmnopqrstuvwxyz'
LIBRARY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def spliter(input, output):
    for cha in input:
        output.append(cha)
#pprint(ssplit)

def isletter(letter):
    if letter in library or letter in LIBRARY:
        return True
    else:
        return False

def isLower(letter):
    if letter in library:
        return True
    else:
        return False

#encrypts or decrypts input1
def moving(ssplit : List[str], moveby, library : List[str], LIBRARY : List[str]):    #get place of each letter in ssplit and add number moveby to its place in library
    newList = []
    for item in ssplit:
        if isletter(item):
            if isLower(item):
                place = library.index(item)
                place += moveby
                if place >= 26:
                    place = place % -26
                if place <= -1:
                    place = place % 26
                item = library[place]
                #print("%s %d"%(item, place))
                newList.append(item)
            else:
                place = LIBRARY.index(item)
                place += moveby
                if place >= 26:
                    place = place % -26
                if place <= -1:
                    place = place % 26
                item = LIBRARY[place]
                pprint("%s %d"%(item, place))
                newList.append(item)
        else:
            newList.append(item)
    return newList

#on button press
def onButtonPress():
    global library, LIBRARY, input1, moveby
    
    #decide whether encoding
    if ('encode') == str(app.getOptionBox("encode/decode")):
        PreEncoding = True
    else:
        PreEncoding = False

    #get the value for ssplit and moveby
    input1 = str(app.getEntry("Text to be encoded/decoded")) 
    ssplit : List[str] = []
    isEncoding = PreEncoding
    
    preMoveby = 0
    preMoveby = str(app.getEntry("offset"))
    if isletter(preMoveby):
        if isLower(preMoveby):
            preMoveby = library.index(preMoveby) + 1
        else:
            preMoveby = LIBRARY.index(preMoveby) + 1
    else:
        preMoveby = int(app.getEntry("offset"))

    moveby = preMoveby 
    if not isEncoding: moveby *= -1
    spliter(input1,ssplit)  #ssplit is modified

    newList = moving(ssplit, moveby, library, LIBRARY)#encoding/decoding function 
    print(''.join(newList))
    newnewList = (''.join(newList))
    app. setLabel("title2","Encoding/Decoding Complete: "+str(newnewList))


app.addButton("Process", onButtonPress)
app.go()