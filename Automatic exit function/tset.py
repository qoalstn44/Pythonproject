import re
word="hello"
reg = re.compile(r'[a-zA-Z]')

if reg.match(word):
    print("It is an alphabet")
else:
    print("It is not an alphabet")
    
word="hello"
reg = re.compile(r'[a-z]')
if reg.match(word):
    print("It is an alphabet")
else:
    print("It is not an alphabet")