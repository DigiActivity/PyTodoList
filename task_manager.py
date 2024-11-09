from task import Task

class TaskManager:

    # Démarrer la liste des tâches
    def __init__(self):
        self.tasks = []
    
    # ajouter une tâche
    def add_task(self, task):
        self.tasks.append(task)
    

    # Marquer une tâche comme terminée
    # si il y a les tâches 0 1 et 2, number sera 1 2 ou 3
    def validate_index(self, number):
        task = self.tasks[number - 1]
        task.validate()
    
    # Lister toutes les tâches en les numérotant
    def __str__(self):
        if len(self.tasks) == 0:
            return "Il n'y a pas de tâches."

        texte = "Toutes les tâches : \n"

        for i in range(len(self.tasks)):
            task = self.tasks[i]
            texte += f" {i+1}. {str(task)}"
            # si ce n'est pas la derniere ligne
            if i != len(self.tasks) - 1:
                texte += "\n"

        return texte


# TESTS

task_manager = TaskManager()

task = Task("Faire mes lacets")
task2 = Task("Faire mon sac")

# add_task

task_manager.add_task(task)
task_manager.add_task(task2)

# validate index

task_manager.validate_index(2)

print(task2.is_done) # True

# formattage

print(task_manager)