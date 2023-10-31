# First_name = 'Eli'
# Last_name = 'Averett'
# Email_address = 'ave21001@byui.edu'
# Phone_number = '(214) 945-6196'
# Job_title = 'Student'
# ID = '83-639-7542'

print('Please enter the following information:')

print()

first = input('First name')
last = input('Last name')
email = input('Email address')
phone = input ('Phone number:')
job_title = input('Job title:')
id_number = input('ID Number:')

print('\nThe ID Card is:')
print('------------------------------------------')
print(f"{last.upper() }, {first.capitalize() }")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print("-----------------------------------------------")