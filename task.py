class Task:
    
    # Initialiser la tâche
    def __init__(self, title):
        self.title = title
        self.is_done = False

    # Pouvoir valider rapidement la tâche
    def validate(self):
        self.is_done = True

    # Formatter l'affichage
    def __str__(self):
        done_text = "Terminé" if self.is_done else "A Faire"
        return f"[Tâche] {self.title} ({done_text})"