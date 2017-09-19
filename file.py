import requests
import sys
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits
fileupload = sys.argv[-1]
enc = sys.argv[1]

if (enc == "e"):
    print "Generate random name"
    fname = ''.join(choice(digits + ascii_uppercase + ascii_lowercase) for i in range(64))
    fname = fname+fileupload[fileupload.find('.'):]
else:
    print "Uploading using file name"
    fname = fileupload

url = 'your url'
files = {'file': (fname, open(fileupload, 'rb'))}

r = requests.post(url, files=files, auth=('a', 'b'))
print (r.text)
