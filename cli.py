import os
from task_manager import TaskManager

class TaskCLI:
    
    def __init__(self, task_manager):
        self.task_manager = task_manager
    
    def start(self):
        choice = None
        while (choice != "quit"):
            # vider tout le contenu de la console
            os.system('cls' if os.name=='nt' else 'clear')
            # un petit peu de déco
            print("[[ Mega TODO LIST 3000 ]]\n")
            print("-------------------------\n")
            # je print mes tâches
            print(self.task_manager)
            print("-------------------------\n")
            # menu et actions
            
            possible_choices = ["add", "remove", "done", "quit"]
            while (choice not in possible_choices):
                choice = input("Choisissez une action (add, remove, done, quit) : ")
            # je suis sûr à cette étape que choice est inclus dans le tableau




## TESTS ##

task_manager = TaskManager()
cli = TaskCLI(task_manager)

assert cli.task_manager == task_manager

cli.start()
