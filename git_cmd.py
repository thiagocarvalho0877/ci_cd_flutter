"""
author: @endormi
Automated Git commands
Automate the process of using commands such as clone, commit, branch, pull, merge, blame and stash
"""

import subprocess
#from pyfiglet import figlet_format
#from termcolor import cprint
import os
import uuid


logo = 'Git-Commands'

def run(*args):
    return subprocess.check_call(['git'] + list(args))

# Cria a branch com o Trigger para gerarmos a versão de teste da PO
def createPOCreateReviewBranch():
    branch = input("\nDigite o nome da branch que será criada para gerarmos o build :) : ")
    br = 'PO/' + f'{branch}' 

    _uuid = uuid.uuid4()

    print( _uuid.hex)
    
    # Criamos um arquivo dumb apenas para commitar e hitar o trigger
    f= open('_auxFile' + _uuid.hex,"w+")
    
    # Criamos a branch de teste ex: PO--feature/token-toro-aprova-ai-big
    run("checkout", "-b", br)
    
    # Adiciona o arquivo
    run("add", ".")

    # Pergunta se quer realmente subir para a pipeline
    choice = input("\nEnviar a branch para pipeline? (S) (N)")
    choice = choice.lower()
    
    # Fluxo de escolha
    if choice == "s":
         # Commita
        run("commit", "-am", "dumb commit message")
        run("push", "--set-upstream", "origin", br)

    elif choice == "n":
        print("\nObrigado!\n")
         

    else:
        print("\nComando inválido\n")
         # Remove o arquivo dumb

   
    run("push", "-d", "origin", br)

def main():
    createPOCreateReviewBranch()
    # Remove o arquivo dumb
    os.remove("_auxfile.txt")

if __name__ == '__main__':
    main()