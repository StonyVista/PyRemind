print('Started protection library')
import hashlib

#Checks MD5 Files to see if they can be opened and hashed
def checkFileMD5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
