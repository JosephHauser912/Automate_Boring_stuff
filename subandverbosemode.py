import re

namesRegex = re.compile(r'Agent \w+')

print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob'))

# namesRegex = re.compile(r'Agent (\w)\w*')
# print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))

# print(namesRegex.sub('Agent \1*****','Agent Alice gave the secret documents to Agent Bob'))

re.compile(r'''
(\d\d\d-) |  #AREA CODE
\d\d\d  #FIRST 3
-
\d\d\d\d'#LAST DIGITS''', re.VERBOSE | re.IGNORECASE | re.DOTALL) #VERBOSE ALLOWS
