'''
Task 2 - ProDigy Infotech

Password Complexity Checker

Developed as part of my internship at Prodigy Infotech, this tool evaluates the strength of a password based on essential security criteria. 
It checks for length, uppercase and lowercase letters, numbers, and special characters to provide users with feedback on password strength. 

This project helped me understand Python's built-in functions like `any()`, string handling, and user input validation while reinforcing best security practices. 
By implementing real-time password analysis, I aimed to enhance security awareness and guide users in creating stronger passwords.

'''


def validate_pass(password):
    print("\n~\033[92mYou Entered the Password: \033[0m",password)
    #======== Function Code =======
    check_length = len(password) >= 8 #1st criteria ==== Lenght
    check_upper = any(upper.isupper() for upper in password)  #2st criteria ==== Upper Case Character
    check_lower = any(lower.islower() for lower in password)  #3st criteria ==== Lower Case Character
    check_digit = any(digit.isdigit() for digit in password)  #4st criteria ==== Digit
    check_special_character = any(special in string.punctuation for special in password)
    
    result = sum([check_length,check_upper,check_lower,check_digit,check_special_character])
    
    if not check_length:
        # Password Strength Logic
        print("\n~\033[91mYour Password is Weak \n~(Too Short - Minimum 8 Characters Required) \033[0m")
    elif check_length and result > 4:
        print("\n~\033[95mYour Password is Strong\033[0m\n~\033[96mExcellent! Your password is secure and best to Use..!\033[0m")
    elif check_length and result == 3 or result == 4:
        print("\n~\033[93mYour Password is Medium\033[0m\n~\033[96mYour password is decent, but it can be improved.\033[0m")
    else:
        print("\n~\033[91mYour Password is weak\033[0m\n~\033[96mYour password is too simple! Try adding uppercase letters, numbers, and special characters to make it stronger.\033[0m")
    
#============== Main Code =============

import string


print('''\033[32m
      
██╗      ██████╗  ██████╗██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
██║     ██║   ██║██║     █████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ 
██║     ██║   ██║██║     ██╔═██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
███████╗╚██████╔╝╚██████╗██║  ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
\033[0m
         \033[35m~~~~~ Developed by Aspiring Penster Mr. Izaz  ~~~~~ \033[0m 
         \033[93m~~~~~ Follow Here: GitHub.com/mizazhaider-ceh ~~~~~\033[0m

      ''')

print("            \033[96mWelcome to the  ~Lock-Check\033[0m                    ")
print("\033[91m-----------------------------------------------------------\033[0m")
print("\033[94mEnter a password, and Lock-Check Will analyze its strength\033[0m ")
print("          🔴 Weak | 🟡 Medium | 🟢 Strong                 ")
print("\033[91m-----------------------------------------------------------\033[0m")

password = input("\n~ \033[33mEnter your password: \033[0m")
validate_pass(password)