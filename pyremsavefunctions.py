print('Save functions library started')
import os

try:
	os.mkdir('saves/')
except:
	pass

#Load editable non-constant data from the file
def loadSaveFromDate(datestr):
	date = datestr.split('/')
	try:
		f = open('saves/'+date[2]+'.txt')
		f.close()
	except:
		f = open('saves/'+date[2]+'.txt','w')
		f.close()
	f = open('saves/'+date[2]+'.txt')
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
	return event[1].rstrip().replace('*#new#*','\n')

#Save the data to a file for the editable non-constant
def saveDataToDate(data,date):
	year = date.split('/')[2]
	if os.path.exists('saves/'+year+'.txt') == False:
		f = open('saves/'+year+'.txt','w')
		#f.write('')
		f.close()
	f = open('saves/'+year+'.txt','r')
	file = f.readlines()
	f.close()
	print(date)
	for a in range(len(file)):
		if date in file[a-1]:
			data = data+'*#new#*'+file[a-1].replace(date+';','')
			file.pop(a-1)
    
	os.remove('saves/'+year+'.txt')
	file.append(date+';'+data)
	f = open('saves/'+year+'.txt','w')
	for a in file:
		f.write(a)
		
	f.close()

#Save data to the editable constant file
def saveConstantData(data):
	try:
		os.remove('saves/const.txt')
	except:
		pass
	f = open('saves/const.txt','w')
	f.write(data)
	f.close()

#Loads data from the editable constant file
def loadConstantData():
	f = open('saves/const.txt')
	data = f.read()
	f.close()
	return data
