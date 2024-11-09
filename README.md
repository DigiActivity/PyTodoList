# Projet Python : Gestionnaire de Tâches en POO

## Objectif :
L’objectif de cet exercice est de créer un gestionnaire de tâches en ligne de commande en utilisant la Programmation Orientée Objet (POO). Ce projet est découpé en plusieurs modules afin d’apprendre à structurer un projet Python. Vous allez :
- Créer des classes pour représenter les tâches et leur gestion.
- Organiser le code en plusieurs modules pour respecter une architecture de projet claire.
- Manipuler une interface utilisateur en ligne de commande pour interagir avec le programme.

---

## Étapes du projet :

### 1. Initialisation du projet
Commencez par créer une structure de fichiers pour votre projet :
```
projet_todo/
│
├── task.py          # Contient la classe Task
├── task_manager.py  # Contient la classe TaskManager
├── cli.py           # Gère l'interface utilisateur
├── main.py          # Point d’entrée du programme
└── README.md        # Fichier d'instructions (ce fichier)
```

Tout le code créé dans un fichier doit être importé dans un autre fichier pour être utilisé. Imaginons que la classe `Task` est définie dans `task.py`. Pour l'utiliser dans `main.py`, vous devez l'importer comme suit :
```python
from task import Task # task est le fichier task.py et Task est la classe
``` 


### 2. Créer la classe `Task`
Dans `task.py`, créez une classe `Task` qui représente une tâche.  
Chaque tâche doit avoir :
- Un titre.
- Un statut (complété ou non).

**Méthodes** à inclure :
- Un constructeur pour initialiser le titre de la tâche et son statut (par défaut, non complété).
- Une méthode pour marquer la tâche comme terminée.
- Une méthode pour formater l'affichage de la tâche (avec son statut).

### 3. Créer la classe `TaskManager`
Dans `task_manager.py`, créez une classe `TaskManager` pour gérer la liste des tâches.  
Elle doit permettre de :
- Ajouter une tâche.
- Lister toutes les tâches.
- Marquer une tâche comme terminée.
- Supprimer une tâche.

**Méthodes** à inclure :
- Ajouter une tâche avec un titre.
- Lister toutes les tâches en les numérotant.
- Marquer une tâche comme terminée via son numéro.
- Supprimer une tâche via son numéro.

### 4. Créer l’interface utilisateur
Dans `cli.py`, créez une classe `TaskCLI` qui sera utilisée pour interagir avec l’utilisateur via la ligne de commande.  
Elle doit permettre de :
- Afficher un menu avec différentes options (ajouter, lister, terminer, supprimer une tâche).
- Gérer les entrées de l’utilisateur.

**Étapes** :
- Afficher le menu avec les options.
- Récupérer le choix de l’utilisateur.
- Appeler la méthode appropriée du `TaskManager` selon le choix.
- Répéter l'affichage jusqu'à ce que l’utilisateur choisisse de quitter.

### 5. Faire fonctionner le programme
Dans `main.py`, liez toutes les parties ensemble pour exécuter le programme.  
L’application doit tourner en boucle jusqu’à ce que l’utilisateur décide de quitter le programme.

---

## Fonctionnalités supplémentaires (Bonus) :
1. **Persistance des données** : Sauvegardez les tâches dans un fichier (par exemple, au format JSON) afin que les tâches soient conservées entre les exécutions du programme.
2. **Gestion des erreurs** : Gérez les erreurs possibles (comme entrer un numéro de tâche invalide).
3. **Améliorations de l'interface** : Ajoutez plus de fonctionnalités à l'interface, comme la possibilité de modifier le titre d’une tâche.

---

## À la fin de ce projet, vous aurez appris à :
- Structurer un projet Python en modules.
- Travailler avec la Programmation Orientée Objet (POO).
- Créer une interface utilisateur en ligne de commande.
