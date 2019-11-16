import protection
import datetime

print('Type the name of the file that you would like to check the md5 hash of (EG: rice.txt):')
inputfile = input()

filehash = protection.checkFileMD5(inputfile)

f = open(datetime.datetime.now().strftime('%y.%m.%d-%H..%M..%S')+ '- MD5 check on ' + inputfile + '.txt','w')
f.write(filehash)
f.close()

print(filehash)
