import pyremsavefunctions
import time
from datetime import datetime
from plyer import notification

#Returns the time interval from the settings
def getTime():
    f = open('saves/settings.txt','r')
    tim = f.read()
    f.close()
    return(tim)
	

def notify():
    try:
        data = pyremsavefunctions.loadSaveFromDate(datetime.now().strftime('%d/%m/%y'))+'\n(powered by pyRemind)'
        remindersAvailible = True
    except IndexError:
        remindersAvailible = False
    if remindersAvailible == True:
        notification.notify('Your reminders for today:',data)
    else:
        notification.notify('You have no reminders set for today.','Create some in pyRemind!')
notification.notify('pyRemind auto-notifier has started','You will recieve notifications every '+str(getTime())+' minute(s).')
while True:
    try:
        time.sleep(int(getTime())*60)
        notify()
    except ValueError:
        notification.notify('Configuration error','Please set the notification interval in pyRemind settings.')
        time.sleep(10)
