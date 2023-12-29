import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''
joseph alexander 805-123-1235

home 123-543-0987
'''

# print(phoneRegex.search(resume))
# print(phoneRegex.findall(resume))#returns a list of results
# print(type(phoneRegex.findall(resume)))

# phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# print(phoneRegex.findall(resume)) #returns tuples of strings in a list

# phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
# print(phoneRegex.findall(resume))

# lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

# xmasRegex = re.compile(r'\d+\s\w+')# \d digits + 1 or more \s space \w letter + one or more (stop at the next space)
# print(xmasRegex.findall(lyrics))

# vowelRegex =  re.compile(r'[aeiouAEIOU]{2}')# []any of the contained, {2} in a row
# print(vowelRegex.findall('Robocop eats baby food'))

# vowelRegex =  re.compile(r'[^aeiouAEIOU]')# ^ is opposites
# print(vowelRegex.findall('Robocop eats baby food.'))

# beginsWithHello = re.compile(r'^Hello') #^needs to begin with
# print(beginsWithHello.search('Hello There.'))
# print(beginsWithHello.search('Why Hello There.'))

# endsWithWorld = re.compile(r'World!$') # $ ends with
# print(endsWithWorld.search('Hello World!'))
# print(endsWithWorld.search('Hello World!asdfwa'))


# allDigits = re.compile(r'^\d+$')# ^ and $ mean it can only have digits \d+
# print(allDigits.search('3216543216'))
# print(allDigits.search('6543215s35241'))

# atRegex = re.compile(r'.at')  #. means any new character
# print(atRegex.findall('The cat in the hat sat on the flat mat'))


# atRegex = re.compile(r'.{1,2}at')
# print(atRegex.findall('The cat in the hat sat on the flat mat'))

# # 'First Name: Al Last Name: Sweigart'  
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # .* is greedy
# print(nameRegex.findall( 'First Name: Al Last Name: Sweigart'))

# serve = '<To serve humans> for dinner.>'

# nongreedy = re.compile(r'<(.*?)>')  #shortest possible

# print(nongreedy.findall(serve))

# greedy = re.compile(r'<(.*)>')
# print(greedy.findall(serve))  #longest

# prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law.'

# dotStar = re.compile(r'.*')
# print(dotStar.search(prime))

# dotStar = re.compile(r'.*', re.DOTALL)
# print(dotStar.search(prime))

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.search('Al, why does your programming book talk about RoboCop so much?'))

print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))

vowelRegex= re.compile(r'[aeious]', re.I)  #both lower and uppcase
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))
