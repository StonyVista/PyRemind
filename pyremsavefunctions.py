print('Save functions library started')
import os

#load editable non-constant data from the file
def loadSaveFromDate(date):
	date = date.split('/')
	f = open(date[2]+'.txt')
	yearsdata = f.readlines()
	f.close
	entry == 0
	while eventtime != date.rstrip():
		event = yearsdata[entry]
		event = event.split(';')
		eventtime = event[0]
		entry += 1
	return event

#save the data to a file for the editable non-constant
def saveDataToDate(data,date()):
	year = date.split('/')[2]
	f = open(year+'.txt','r')
	file = f.readlines()
	f.close()
	os.remove(year+'.txt')
	file.append(data+';'+data)
	f = open(year+'.txt',w)
	f.write(file)
	f.close()
