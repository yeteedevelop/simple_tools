import re
import sys

if sys.argv = 0:
	print("Please run this with xargs and find command, [ find . -print0 | xargs -0 python urls.py ]")

f = open(sys.argv[1], 'r')

data = f.read()

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)

for url in urls:
	print(url+'\n') 
