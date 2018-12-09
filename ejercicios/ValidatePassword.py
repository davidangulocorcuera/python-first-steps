import re

password = raw_input("enter password: ")

reMayus = r'[A-Z]+'
reMinus = r'[a-z]+'
reNum = r'[0-9]+'
reExt = r'[\W]+'

if len(password) == 12 and re.match(reMayus, password) and re.match(reMinus, password) and re.match(reNum, password) and re.match(reExt, password):
    print "valid"
else:
    print "not valid"




