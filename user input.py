
# Ask for Employee ID

employee_id = input("Enter Employee ID: ")

# Check Employee ID

if not employee_id.isdigit() or len(employee_id) > 7:
    print("Invalid Employee ID. Program terminated.")
    exit()


# Ask for Employee Name

employee_name = input("Enter Employee Name: ")

# Check Employee Name

bad_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')',
            '_', '=', '+', ',', '<', '>', '/', '?', ';', ':',
            '[', ']', '{', '}', '\\']

name_letters = 0
name_ok = True

for character in employee_name:
    if character.isalpha():
        name_letters += 1

    if character in bad_name:
        name_ok = False

if employee_name == "" or name_letters <= len(employee_name) / 2:
    name_ok = False

if name_ok == False:
    print("Invalid Employee Name. Program terminated.")
    exit()


# Ask for Employee Email Address

employee_email = input("Enter Employee Email Address: ")

# Check Employee Email Address

bad_email = ['!', '"', "'", '#', '$', '%', '^', '&', '*',
             '(', ')', '=', '+', ',', '<', '>', '/', '?',
             ';', ':', '[', ']', '{', '}', '\\']

email_letters = 0
email_ok = True

for character in employee_email:
    if character.isalnum():
        email_letters += 1

    if character in bad_email:
        email_ok = False

if employee_email == "" or email_letters <= len(employee_email) / 2:
    email_ok = False

if email_ok == False:
    print("Invalid Employee Email Address. Program terminated.")
    exit()


# Ask for Employee Address

employee_address = input("Enter Employee Address (optional): ")

# Check Employee Address

bad_address = ['!', '"', "'", '@', '$', '%', '^', '&',
               '*', '_', '=', '+', '<', '>', '?',
               ';', ':', '[', ']', '{', '}']

address_letters = 0
address_ok = True

for character in employee_address:
    if character.isalnum():
        address_letters += 1

    if character in bad_address:
        address_ok = False

if employee_address != "":
    if address_letters <= len(employee_address) / 2:
        address_ok = False

if address_ok == False:
    print("Invalid Employee Address. Program terminated.")
    exit()


# Display Employee Information

if employee_address != "":
    print("Hello, " + employee_name + ". Your Employee ID is " +
          employee_id + ", and your email address is " +
          employee_email + ". Your address is " + employee_address + ".")
else:
    print("Hello, " + employee_name + ". Your Employee ID is " +
          employee_id + ", and your email address is " +
          employee_email + ". You did not provide an address.")
