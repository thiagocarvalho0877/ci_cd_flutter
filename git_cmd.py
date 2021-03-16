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
    branch = input("\nDigite o nome da branch que será criada para gerarmos o build :) : ")
    br = 'PM--' + f'{branch}' 

    f= open("dumb file to hit the trigger","w+")

    run("checkout", "-b", br)

    run("add", ".")

    run("commit", "-am", "commit message")

    choice = input("\nEnviar a branch para pipeline? (S) (N)")
    choice = choice.lower()

    os.remove("dumb file to hit the trigger")

    if choice == "S":
        run("push", "--set-upstream", "origin", br)

    elif choice == "N":
        print("\nObrigado!\n")

    else:
        print("\nComando inválido\n")

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