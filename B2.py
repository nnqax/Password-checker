import string #To have the wanted character without writing a long list
list_lowercase = list(string.ascii_lowercase) #To have the ability to take random characters easily
list_uppercase = list(string.ascii_uppercase) #To have the ability to take random characters easily
list_digits = list(string.digits) #To have the ability to take random characters easily
list_allowed_panctuation=['@','#','_','@','#','_','@','#','_','@','#','_',] #To have the ability to take random characters easily and to ensure we are using the allowed things according to the rules

password_letters_list=[]
password_letters_list +=list_lowercase 
password_letters_list +=list_uppercase
password_letters_list += list_digits 
password_letters_list += list_allowed_panctuation


def password_check():
  def ending():#the ending of the generator
       while True:
         print('do you want to check another password')
         desicions=input('write y if you want to ,and n if you dont')#asking the user if they want to make another password at the end
         if desicions.lower() =='y':#what will happen if they type y and this will ensure that even if the user types Y it will be y
           password_check()
         elif desicions == 'n':#what will happen if they type n and this will ensure that even if the user types N it will be n
           exit() #this function will exit the whole app
         else:
           print('invalid option try again')
  password=list(input('enter your password here:'))
  password_length=len(password)
  if 8 <= password_length <= 15:
      if ' ' in password:
         print('Non-compliant')
         print('password contains a space')
         ending()
      else:
         if any(i in list_lowercase for i in password):
            if any(i in list_uppercase for i in password):
               if any(i in list_allowed_panctuation for i in password):
                  if any(i in list_digits for i in password):
                    print('Compliant')
                    ending()
                  else:
                    print('Non-compliant')
                    print('password has no numbers')
                    ending()
               else:
                 print('Non-compliant')
                 print('password has no panctuation letters')
                 ending()
            else:
              print('Non-compliant')
              print('password has no uppercase letters')
              ending()
         else:
            print('Non-compliant')
            print('password has no lowercase letters')
            ending()
         ending()
  else:
      print('Non-compliant')
      print('password should be between or equal 8 to 15 characters')
      ending()

def rules():#for the user to know the rules from the rule.txt
    while True:
        question = input('Do you want to read the rules? (y/n): ')
        if question.lower() == 'y':
            print('1. Password length should at least be between eight and fifteen characters to avoid the employees forgetting about it ')
            print('2. Password must include at least one numberPassword should include at least one number')
            print('3. Password should consist of at least one lowercase letter')
            print('4. Password should consist of at least one uppercase letter')
            print('5. Password should consist of at least one punctuation from this list only {@ ,# ,_ }')
            print('6. password should not contain a space')
            while True:  
                examples = input('Do you want examples? (y/n): ')
                if examples.lower() == 'y':
                    print('Example 1: y#NIiOgjekV_')
                    print('Example 2: Mm@#@V@bYY5KLj')
                    break  # Exit examples loop
                elif examples.lower() == 'n':
                    password_check()
                    return  # Exit the entire rules function
                else:
                    print('Invalid option. Try again.')
        elif question.lower() == 'n':
            password_check()
            break  # Exit rules loop if the user doesn't want rules
        else:
            print('Invalid option. Try again.')

rules()