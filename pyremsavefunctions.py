print('Save functions library started')
import os

#load editable non-constant data from the file
def loadSaveFromDate(datestr):
	date = datestr.split('/')
	f = open(date[2]+'.txt')
	yearsdata = f.readlines()
	f.close
	entry = 0
	eventtime = 0
	while eventtime != datestr:
		#print(entry)
		event = yearsdata[entry]
		event = event.split(';')
		eventtime = event[0]
		entry += 1
	return event[1].rstrip()

#save the data to a file for the editable non-constant
def saveDataToDate(data,date):
	year = date.split('/')[2]
	if os.path.exists(year+'.txt') == False:
		f = open(year+'.txt','w')
		#f.write('')
		f.close()
	f = open(year+'.txt','r')
	file = f.readlines()
	f.close()
	os.remove(year+'.txt')
	file.append(date+';'+data)
	f = open(year+'.txt','w')
	for a in file:
		f.write(a)
		f.write('\n')
	f.close()
	
