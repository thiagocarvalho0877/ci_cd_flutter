"""
author: @endormi
Automated Git commands
Automate the process of using commands such as clone, commit, branch, pull, merge, blame and stash
"""

import subprocess
#from pyfiglet import figlet_format
#from termcolor import cprint
import os

logo = 'Git-Commands'

def run(*args):
    return subprocess.check_call(['git'] + list(args))


def createPOCreateReviewBranch():
    branch = input("\nType in the name of the branch you want to make: ")
    br = 'PM--' + f'{branch}' 

    f= open("dumb file to hit the trigger","w+")

    run("checkout", "-b", br)

    print(f)

    print(br)

    run("add", ".")

    run("commit", "-am", "commit message")

    choice = input("\nDo you want to push the branch right now to GitHub? (y/n): ")
    choice = choice.lower()

    os.remove("dumb file to hit the trigger")

    if choice == "y":
        run("push", "--set-upstream", "origin", br)

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")

    run("push", "-d", "origin", br)

def main():
    createPOCreateReviewBranch()
  #  cprint(figlet_format(logo, font='slant'), 'green')
    # print(info + "\n")

    # choices = 'clone, commit, branch, createpocreatereviewbranch, pull, fetch, merge, reset, blame and stash'
    # print("Commands to use: " + choices)

    # choose_command = input("Type in the command you want to use: ")
    # choose_command = choose_command.lower()

    # if choose_command == "clone":
    #     clone()

    # elif choose_command == "commit":
    #     commit()

    # elif choose_command == "branch":
    #     branch()
    
    # elif choose_command == "createpocreatereviewbranch":
    #     createPOCreateReviewBranch()

    # elif choose_command == "pull":
    #     pull()

    # elif choose_command == "fetch":
    #     fetch()

    # elif choose_command == "merge":
    #     merge()

    # elif choose_command == "reset":
    #     reset()

    # elif choose_command == "blame":
    #     blame()

    # elif choose_command == "stash":
    #     stash()

    # else:
    #     print("\nNot a valid command!")
    #     print("\nUse " + choices)


if __name__ == '__main__':
    main()