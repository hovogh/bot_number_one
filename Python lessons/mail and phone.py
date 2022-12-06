mail = input('Mail: ')
phone = input('Phone: ')
if 0 < str.find(mail, '@') < str.find(mail, '.') and str.find(mail, '.') > 0: #str.find(mail, '@') > 0 and str.find(mail, '.') > 0 and str.find(mail, '@') < str.find(mail, '.') :
    print('Your mail is:', mail)
    gmail = str.title(mail[(str.find(mail, '@')) + 1:str.find(mail, '.')])
    print('Your mail website is:', gmail)
else:
    print('Incorrect mail.')
if len(phone) == 8 and str.isdigit(phone) > 0:
    print('Your phone number is:', '+374' + phone)
elif len(phone) == 9 and str.isdigit(phone) > 0 and phone[0] in '0':
    nphone = str.replace(phone, '0', '', 1)
    print('Your phone number is:', '+374' + nphone)
else:
    print('Incorrect phone number')

