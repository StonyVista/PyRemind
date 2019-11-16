print('Imported Legacy GUI functions. This will allow integration of the old tk gui with the new qt one.')
import tkinter
import protection
import pyremsavefunctions
from datetime import datetime
filenotify = True

def modifyCheck(fname, sethash):
    existinghash = protection.checkFileMD5(fname)
    if sethash != existinghash:
        print('The file:',fname,'has been modified. The program will try to run but this file may cause errors.')

try:
    modifyCheck('pyremverdata.txt','a1309af1d19ead87d91fe825ba2a9d7d')

    f = open('pyremverdata.txt')
    prgdata = f.readlines()
    f.close()
except:
    prgdata = ['Info file not found','Unknown Version']

username = "''"
font = 'font.ttf'

prgname = prgdata[0].rstrip()
prgver = prgdata[1].rstrip()
prgnameplusver = prgname+' Ver:'+prgver
    


def displaymsg(screentext):
        def send():
            root.destroy()
        root = tkinter.Tk()
        root.title(prgname)

        w = tkinter.Label(root, text = screentext, font = font)
        w.pack()

        buttonSend=tkinter.Button(root, height=1, width=10, text =  "Close", command=lambda: send(), font = font)
        buttonSend.pack()

        root.mainloop()
def settingsUI():
    window = tkinter.Tk()
    def send():
        f = open('saves/settings.txt','w') #TEMPORARY settings save system. Not for final version
        f.write(textBox.get("1.0","end-1c"))
        f.close()
        window.destroy()
    window.title(prgnameplusver)

    w = tkinter.Label(window, text = "Settings\nHow often do you want between notifications (In minutes)?", font = font)
    w.pack()

    textBox=tkinter.Text(window, height=1, width=5, font = font)
    textBox.pack()

    buttonSend=tkinter.Button(window, height=1, width=15, text =  "SAVE", font = font, command=lambda: send())
    buttonSend.pack()
    window.mainloop()

def currentdate():
    try:
        events = pyremsavefunctions.loadSaveFromDate(datetime.now().strftime('%d/%m/%y'))
        try:
            constevents = pyremsavefunctions.loadConstantData()
        except:
            constevents = 'None'
        displaymsg('Daily events:\n'+events+'\nMulit-day events:\n'+constevents)
    except:
        displaymsg("No events can be found for today")
def futuredate():
    window = tkinter.Tk()
    def send():
        inputValue=textBox.get("1.0","end-1c")
        window.destroy()
        try:
            events = pyremsavefunctions.loadSaveFromDate(inputValue)
            try:
                constevents = pyremsavefunctions.loadConstantData()
            except:
                constevents = 'None'
            displaymsg('Daily events:\n'+events+'\nMulit-day events:\n'+constevents)
        except:
            displaymsg("No events can be found for the selected date")
    window.title(prgnameplusver)

    w = tkinter.Label(window, text = "Type the date in the format dd/mm/yy", font = font)
    w.pack()

    textBox=tkinter.Text(window, height=1, width=10, font = font)
    textBox.pack()

    buttonSend=tkinter.Button(window, height=1, width=15, text =  "Find events", font = font, command=lambda: send())
    buttonSend.pack()
    window.mainloop()

def alterconst():
    window = tkinter.Tk()
    def send():
        pyremsavefunctions.saveConstantData(textBox.get("1.0","end-1c"))
        window.destroy()
    window.title(prgnameplusver)

    w = tkinter.Label(window, text = "Edit your multi-day reminder", font = font)
    w.pack()

    textBox=tkinter.Text(window, height=5, width=40, font = font)
    textBox.pack()

    buttonSend=tkinter.Button(window, height=1, width=15, text =  "Change", font = font, command=lambda: send())
    buttonSend.pack()
    window.mainloop()

def addevent():
    window = tkinter.Tk()
    def send():
        inputValue=textBox.get("1.0","end-1c")
        inputValue2=textBox2.get("1.0","end-1c")
        pyremsavefunctions.saveDataToDate(inputValue2,inputValue)
        window.destroy()
    
    window.title(prgnameplusver)

    w = tkinter.Label(window, font = font, text = "Type the date of the event in the format dd/mm/yy")
    w.pack()

    textBox=tkinter.Text(window, height=1, width=30, font = font)
    textBox.pack()

    w2 = tkinter.Label(window, text = "Type the event", font = font)
    w2.pack()

    textBox2=tkinter.Text(window, height=4, width=30, font = font)
    textBox2.pack()

    buttonSend=tkinter.Button(window, height=1, width=30, text =  "Add event", command=lambda: send(), font = font)
    buttonSend.pack()
    window.mainloop()