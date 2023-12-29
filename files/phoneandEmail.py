#! python3
import re
import pyperclip
# todo: create a regex for phone numbers, 
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?     #area code (optional)
(\s|-)                      #first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s|x)            # extionsion (optional)
(\d){2,5}))?                #extension number-part (optional)
)
''', re.VERBOSE)
# email addresses, 
emailRegex = re.compile(r'''
#some._+thing@something.com

[a-zA-Z0-9_.+]+          #name part
@                        #at symbol
[a-zA-Z0-9_.+]+         #domain name part
''', re.VERBOSE)

# get text off clipboard, 
text = pyperclip.paste()

# extract email/phone from text, 
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


first_elements = []
for tuple in extractedPhone:
    first_elements.append(tuple[0])
    
# print(f"The whole phone numbers are: {first_elements}")

# print(extractedEmail)


#copy extracted to clipboard
results = '\n'.join(first_elements) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)