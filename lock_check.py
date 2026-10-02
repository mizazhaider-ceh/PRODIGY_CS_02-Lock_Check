'''
Task 2 - ProDigy Infotech

Password Complexity Checker

Developed as part of my internship at Prodigy Infotech, this tool evaluates the strength of a password based on essential security criteria.
It checks for length, uppercase and lowercase letters, numbers, and special characters to provide users with feedback on password strength.

This project helped me understand Python's built-in functions like `any()`, string handling, and user input validation while reinforcing best security practices.
By implementing real-time password analysis, I aimed to enhance security awareness and guide users in creating stronger passwords.

'''

import getpass
import string

BANNER = '''\033[32m

██╗      ██████╗  ██████╗██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
██║     ██║   ██║██║     █████╔╝     ██║     ███████║█████╗  ██║     █████╔╝
██║     ██║   ██║██║     ██╔═██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗
███████╗╚██████╔╝╚██████╗██║  ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
\033[0m
         \033[35m~~~~~ Developed by Aspiring Pentester Mr. Izaz  ~~~~~ \033[0m
         \033[93m~~~~~ Follow Here: GitHub.com/mizazhaider-ceh ~~~~~\033[0m
   \033[94m~~~~~ Internship Task/Project Assigned by ProDigy Infotech ~~~~~\033[0m
   '''

# The five strength criteria, each a (label, check function) pair.
CRITERIA = [
    ("At least 8 characters", lambda p: len(p) >= 8),
    ("Uppercase letter (A-Z)", lambda p: any(c.isupper() for c in p)),
    ("Lowercase letter (a-z)", lambda p: any(c.islower() for c in p)),
    ("Digit (0-9)", lambda p: any(c.isdigit() for c in p)),
    ("Special character", lambda p: any(c in string.punctuation for c in p)),
]


def evaluate(password):
    """Check a password against every criterion.

    Returns (strength, results) where strength is one of
    "weak" / "medium" / "strong" and results is a list of
    (label, passed) tuples, one per criterion.
    """
    results = [(label, check(password)) for label, check in CRITERIA]
    score = sum(passed for _, passed in results)

    if not results[0][1]:
        strength = "weak"  # Too short, no matter what else passes
    elif score == 5:
        strength = "strong"
    elif score >= 3:
        strength = "medium"
    else:
        strength = "weak"
    return strength, results


def validate_pass(password):
    """Analyze a password and print the verdict. Never prints the password itself."""
    strength, results = evaluate(password)

    print("\n~\033[92mPassword received (%d characters, hidden for your safety)\033[0m" % len(password))
    for label, passed in results:
        mark = "\033[92mPASS\033[0m" if passed else "\033[91mFAIL\033[0m"
        print("  [%s] %s" % (mark, label))

    if strength == "weak" and not results[0][1]:
        print("\n~\033[91mYour Password is Weak \n~(Too Short - Minimum 8 Characters Required) \033[0m")
    elif strength == "strong":
        print("\n~\033[95mYour Password is Strong\033[0m\n~\033[96mExcellent! Your password is secure and best to Use..!\033[0m")
    elif strength == "medium":
        print("\n~\033[93mYour Password is Medium\033[0m\n~\033[96mYour password is decent, but it can be improved.\033[0m")
    else:
        print("\n~\033[91mYour Password is weak\033[0m\n~\033[96mYour password is too simple! Try adding uppercase letters, numbers, and special characters to make it stronger.\033[0m")


def main():
    print(BANNER)
    print("            \033[96mWelcome to the  ~Lock-Check\033[0m                    ")
    print("\033[91m-----------------------------------------------------------\033[0m")
    print("\033[94mEnter a password, and Lock-Check Will analyze its strength\033[0m ")
    print("          Weak | Medium | Strong                 ")
    print("\033[91m-----------------------------------------------------------\033[0m")

    try:
        # getpass hides the password while typing; fall back to plain input
        # on terminals that do not support it.
        password = getpass.getpass("\n~ \033[33mEnter your password (hidden): \033[0m")
    except (EOFError, OSError):
        password = input("\n~ \033[33mEnter your password: \033[0m")
    validate_pass(password)


if __name__ == "__main__":
    main()
