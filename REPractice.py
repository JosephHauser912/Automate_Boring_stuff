# def isPhoneNumber(text):  #415-555-
#     if len(text) != 12:
#         return False # not phone number sized
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False #no area code
#     if text[3] != '-':
#         return False # missing dash
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False  # no first 3 digits
#     if text[7] != '-':
#         return False  # missing second dash
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False # missing last four digits
#     return True


# message = 'Call me 414-555-1111 tomorrow, or at 415-555-9999 at my office line'

# foundNumber = False
# for i in range(len(message)):
#     chunk message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
#         foundNumber = True
# if not foundNumber:
#     print("Could not find any phone numbers.")

# print(isPhoneNumber('415-555-1234'))
# print(isPhoneNumber('hello'))


#====================================================================

import re

# message = 'Call me 414-555-1111 tomorrow, or at 415-555-9999 at my office line'

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# # mo = phoneNumRegex.search(message)
# #  print(mo.group())
# print(phoneNumRegex.findall(message))


# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Call me 414-555-1111 tomorrow')
# print(mo.group())

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('Call me 414-555-1111 tomorrow')
# print(mo.group(1))
# print(mo.group(2))

# phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('324-555-1111')
# mo1 = phoneNumRegex.search('(324)-555-1111')
# print(mo1.group())
# print(mo1.group())

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())

# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The adventures of Batwoman')
# mo = batRegex.search('The adventures of Batman')
# print(mo.group())


# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneRegex.search('My phoen number is 415-555-1245')
# mo = phoneRegex.search('My phoen number is (415)-555-1245')


# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo = phoneRegex.search('My phoen number is 415-555-1245')
# print(mo.group())
# mo = phoneRegex.search('My phoen number is 555-1245')
# print(mo.group())

# batRegex = re.compile(r'Bat(wo)*man')
# # mo = batRegex.search('The adventures of Batwoman')
# mo = batRegex.search('The adventures of Batman')
# print(mo.group())
# mo = batRegex.search('The adventures of Batwowowowoman')
# print(mo.group())


# regex = re.compile(r'\+\*\?')
# print(regex.search('I learned about +*? regex syntax'))
# regex = re.compile(r'(\+\*\?)+')
# print(regex.search('I learned about +*?+*?+*?+*?+*? regex syntax'))

# haRegex = re.compile(r'(ha){3}') #{3} 3 times
# print(haRegex.search('hahaha'))

# phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')#? makes the comma optional
# print(phoneRegex.search('my numbers are 415-555-1234,123-456-7890,212-212-3210'))

# haRegex = re.compile(r'(ha){3,5}') #now it's a range
# print(haRegex.search('hahaha'))
# print(haRegex.search('hahahahaha'))
# print(haRegex.search('hahahahahahaha'))

digitRegex = re.compile(r'(\d){3,5}') # greedy match, longest possible string
print(digitRegex.search('1234567890'))

digitRegex = re.compile(r'(\d){3,5}?') # with ? non-greedy match, shortest possible string
print(digitRegex.search('1234567890'))